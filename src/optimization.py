import pulp
import pandas as pd
import numpy as np
import networkx as nx

def solve_mentor_allocation_lp(df_clean, mentors_path, support_capacity_path, top_n_students=12, total_budget=24):
    """
    Phần E.1: Quy hoạch Tuyến tính Nguyên nhị phân (Binary Integer Programming) bằng PuLP
    Tối ưu hóa phân bổ hoạt động hỗ trợ cho sinh viên nguy cơ cao.
    """
    # 1. Đọc dữ liệu năng lực hỗ trợ
    df_cap = pd.read_csv(support_capacity_path)
    # Lấy top N sinh viên nguy cơ cao nhất dựa vào điểm lab_avg và assignment_score thấp nhất
    df_high_risk = df_clean[df_clean["risk_label"] == "high_risk"].sort_values(
        by=["lab_avg", "assignment_score", "attendance_rate"], ascending=True
    ).head(top_n_students).copy()
    
    student_list = df_high_risk["student_id"].tolist()
    support_types = df_cap["support_type"].tolist()
    
    costs = dict(zip(df_cap["support_type"], df_cap["cost_per_student"]))
    priorities = dict(zip(df_cap["support_type"], df_cap["priority_score"]))
    capacities = dict(zip(df_cap["support_type"], df_cap["capacity"]))
    
    # Tính điểm ưu tiên cá nhân dựa trên mức độ khó khăn (lab thấp được ưu tiên hơn)
    student_urgency = {}
    for _, row in df_high_risk.iterrows():
        sid = row["student_id"]
        # Thang điểm khẩn cấp từ 1.0 đến 2.0
        urgency = 1.0 + (10.0 - row["lab_avg"]) / 10.0
        student_urgency[sid] = round(urgency, 2)
        
    # 2. Khởi tạo bài toán quy hoạch nguyên nhị phân
    prob = pulp.LpProblem("Student_Support_Allocation", pulp.LpMaximize)
    
    # Biến quyết định: x[i, j] = 1 nếu sinh viên i nhận hình thức hỗ trợ j, ngược lại = 0
    x = {
        (i, j): pulp.LpVariable(f"assign_{i}_{j}".replace(" ", "_").replace("-", "_"), cat=pulp.LpBinary)
        for i in student_list for j in support_types
    }
    
    # Hàm mục tiêu: Tối đa hóa tổng điểm ưu tiên
    prob += pulp.lpSum(
        x[i, j] * priorities[j] * student_urgency[i]
        for i in student_list for j in support_types
    ), "Total_Priority_Score"
    
    # Ràng buộc 1: Mỗi sinh viên chỉ nhận tối đa 1 hình thức hỗ trợ
    for i in student_list:
        prob += pulp.lpSum(x[i, j] for j in support_types) <= 1, f"Max_One_Support_{i}"
        
    # Ràng buộc 2: Tổng ngân sách chi phí hỗ trợ <= total_budget
    prob += pulp.lpSum(
        x[i, j] * costs[j]
        for i in student_list for j in support_types
    ) <= total_budget, "Budget_Constraint"
    
    # Ràng buộc 3: Giới hạn năng lực tiếp nhận của từng hình thức hỗ trợ
    for j in support_types:
        prob += pulp.lpSum(x[i, j] for i in student_list) <= capacities[j], f"Capacity_Constraint_{j}"
        
    # Giải bài toán
    prob.solve(pulp.PULP_CBC_CMD(msg=False))
    
    status = pulp.LpStatus[prob.status]
    optimal_score = pulp.value(prob.objective)
    
    # Trích xuất kết quả phân bổ
    assignments = []
    total_cost_used = 0
    for i in student_list:
        assigned_type = "Không được hỗ trợ (vượt ngân sách)"
        cost = 0
        prio = 0
        for j in support_types:
            if pulp.value(x[i, j]) == 1:
                assigned_type = j
                cost = costs[j]
                prio = priorities[j]
                total_cost_used += cost
                break
        assignments.append({
            "student_id": i,
            "Mức độ khẩn cấp": student_urgency[i],
            "Hình thức hỗ trợ phân bổ": assigned_type,
            "Chi phí (giờ)": cost,
            "Điểm ưu tiên gốc": prio
        })
        
    df_alloc = pd.DataFrame(assignments)
    
    summary = {
        "Status": status,
        "Optimal_Score": round(optimal_score, 2),
        "Total_Budget": total_budget,
        "Total_Cost_Used": total_cost_used,
        "Students_Supported": sum(1 for a in assignments if a["Chi phí (giờ)"] > 0),
        "Total_Considered": len(student_list)
    }
    
    return summary, df_alloc

def solve_bipartite_max_flow(df_clean, mentors_path, num_students=10):
    """
    Phần E.2: Mở rộng bằng Mạng Luồng Cực đại (Max Flow) & Đồ thị Hai phía (Bipartite Graph)
    Ghép cặp sinh viên với Mentor phù hợp chuyên môn.
    Nguồn (s) -> Sinh viên -> Mentor -> Đích (t)
    """
    df_mentors = pd.read_csv(mentors_path)
    
    # Chọn ra 10 sinh viên nguy cơ cao nhất
    df_top_risk = df_clean[df_clean["risk_label"] == "high_risk"].head(num_students).copy()
    student_nodes = df_top_risk["student_id"].tolist()
    mentor_nodes = df_mentors["mentor_id"].tolist()
    
    # Xây dựng đồ thị luồng
    G_flow = nx.DiGraph()
    source = "Source_s"
    sink = "Sink_t"
    
    # 1. Cạnh từ Nguồn -> Sinh viên (dung lượng = 1)
    for sid in student_nodes:
        G_flow.add_edge(source, sid, capacity=1)
        
    # 2. Cạnh từ Sinh viên -> Mentor (nếu mentor có chuyên môn phù hợp)
    # Quy tắc nghiệp vụ:
    # M01 (Python) hỗ trợ SV có lab_avg < 4.0
    # M02 (Data analysis) hỗ trợ SV có quiz_avg < 3.0
    # M03 (Machine learning) hỗ trợ SV có assignment_score < 4.0
    # M04 (Mathematics for AI) hỗ trợ SV có attendance_rate < 0.70
    # M05 (Database Systems) hỗ trợ SV có video_views < 10
    mentor_specialties = dict(zip(df_mentors["mentor_id"], df_mentors["specialty"]))
    
    for _, row in df_top_risk.iterrows():
        sid = row["student_id"]
        # Kết nối theo nhu cầu cụ thể
        if row["lab_avg"] <= 5.0:
            G_flow.add_edge(sid, "M01", capacity=1)
        if row["quiz_avg"] <= 3.0:
            G_flow.add_edge(sid, "M02", capacity=1)
        if row["assignment_score"] <= 4.0:
            G_flow.add_edge(sid, "M03", capacity=1)
        if row["attendance_rate"] <= 0.80:
            G_flow.add_edge(sid, "M04", capacity=1)
        if row["video_views"] <= 15:
            G_flow.add_edge(sid, "M05", capacity=1)
            
    # 3. Cạnh từ Mentor -> Đích (dung lượng = max_students)
    mentor_caps = dict(zip(df_mentors["mentor_id"], df_mentors["max_students"]))
    for mid in mentor_nodes:
        G_flow.add_edge(mid, sink, capacity=mentor_caps[mid])
        
    # Tính luồng cực đại bằng thuật toán Edmonds-Karp / Preflow-push
    flow_value, flow_dict = nx.maximum_flow(G_flow, source, sink)
    
    # Trích xuất các cặp ghép thành công
    matched_pairs = []
    for sid in student_nodes:
        if sid in flow_dict:
            for mid, f_val in flow_dict[sid].items():
                if f_val > 0 and mid in mentor_nodes:
                    matched_pairs.append({
                        "student_id": sid,
                        "mentor_id": mid,
                        "specialty": mentor_specialties[mid]
                    })
                    
    df_matched = pd.DataFrame(matched_pairs)
    
    # Nhận diện nút thắt cổ chai Min-Cut
    # Sử dụng minimum_cut trong networkx
    cut_value, partition = nx.minimum_cut(G_flow, source, sink)
    reachable, non_reachable = partition
    
    bottleneck_edges = []
    for u in reachable:
        for v in non_reachable:
            if G_flow.has_edge(u, v):
                cap = G_flow[u][v]["capacity"]
                bottleneck_edges.append((u, v, cap))
                
    report_flow = {
        "Max_Flow_Value": flow_value,
        "Total_Students": num_students,
        "Successful_Matches": len(matched_pairs),
        "Min_Cut_Value": cut_value,
        "Bottleneck_Edges": bottleneck_edges
    }
    
    return report_flow, df_matched, G_flow
