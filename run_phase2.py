import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx

# Ensure sys stdout handles utf-8 cleanly
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"c:\HOC_HANH\Mon dang hoc\ITA201\smartedu-ai"
src_dir = os.path.join(base_dir, "src")
data_dir = os.path.join(base_dir, "data")
outputs_dir = os.path.join(base_dir, "outputs")
figures_dir = os.path.join(outputs_dir, "figures")
tables_dir = os.path.join(outputs_dir, "tables")

os.makedirs(figures_dir, exist_ok=True)
os.makedirs(tables_dir, exist_ok=True)

sys.path.append(src_dir)

from data_processing import load_data, clean_students_data
from linear_algebra import extract_features_and_labels
from probability_entropy import compute_conditional_probabilities, train_gaussian_naive_bayes, compute_information_gain_ranking
from graph_markov import build_interaction_graph, traverse_bfs_dfs, simulate_markov_learning_behavior
from optimization import solve_mentor_allocation_lp, solve_bipartite_max_flow

print("==========================================================")
print("     SMARTEDU AI - ASSIGNMENT PHASE 2 EVALUATION          ")
print("==========================================================")

# 1. Load Data
students = load_data(data_dir)
df_clean = clean_students_data(students)
X, y, feature_cols = extract_features_and_labels(df_clean)

# ==========================================================
# PHẦN C. XÁC SUẤT, BAYES VÀ LÝ THUYẾT THÔNG TIN
# ==========================================================
print("\n--- PHẦN C.1: XÁC SUẤT CÓ ĐIỀU KIỆN HAI CHIỀU ---")
df_prob = compute_conditional_probabilities(df_clean)
print(df_prob.to_string(index=False))
prob_csv = os.path.join(tables_dir, "conditional_probabilities.csv")
df_prob.to_csv(prob_csv, index=False, encoding="utf-8-sig")
print(f"-> Đã lưu bảng xác suất tại: {prob_csv}")

print("\n--- PHẦN C.2: PHÂN LOẠI GAUSSIAN NAIVE BAYES ---")
gnb, X_train, X_test, y_train, y_test, y_pred, y_proba, gnb_metrics = train_gaussian_naive_bayes(X, y)
print(f"- Accuracy:  {gnb_metrics['Accuracy']*100:.2f}%")
print(f"- Precision: {gnb_metrics['Precision']*100:.2f}%")
print(f"- Recall:    {gnb_metrics['Recall']*100:.2f}%")
print(f"- F1-Score:  {gnb_metrics['F1-Score']*100:.2f}%")
print(f"- Prior Probabilities: P(low_risk)={gnb_metrics['Priors'][0]:.4f}, P(high_risk)={gnb_metrics['Priors'][1]:.4f}")

# Dự báo cho 1 sinh viên kiểm thử cụ thể
sample_idx = 0
sample_id = df_clean.iloc[sample_idx]["student_id"]
sample_feat = X[sample_idx].reshape(1, -1)
sample_proba = gnb.predict_proba(sample_feat)[0]
sample_pred = gnb.predict(sample_feat)[0]
label_map = {0: "low_risk", 1: "high_risk"}
print(f"- Dự báo cho sinh viên {sample_id}:")
print(f"  P(low_risk | X) = {sample_proba[0]:.4f} | P(high_risk | X) = {sample_proba[1]:.4f}")
print(f"  => Dự đoán: {label_map[sample_pred]} (Nhãn thực tế: {df_clean.iloc[sample_idx]['risk_label']})")

# Vẽ và lưu biểu đồ Confusion Matrix cho Gaussian Naive Bayes
plt.figure(figsize=(6, 5))
sns.heatmap(gnb_metrics["Confusion_Matrix"], annot=True, fmt="d", cmap="Blues",
            xticklabels=["low_risk (0)", "high_risk (1)"],
            yticklabels=["low_risk (0)", "high_risk (1)"])
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Gaussian Naive Bayes Confusion Matrix")
plt.tight_layout()
cm_path = os.path.join(figures_dir, "gnb_confusion_matrix.png")
plt.savefig(cm_path, dpi=300)
plt.close()
print(f"-> Đã lưu biểu đồ Confusion Matrix tại: {cm_path}")

print("\n--- PHẦN C.3: SHANNON ENTROPY VÀ INFORMATION GAIN ---")
H_parent, df_ig = compute_information_gain_ranking(df_clean)
print(f"- Entropy ban đầu của nhãn H(risk_label): {H_parent:.4f} bits")
print("- Bảng xếp hạng đặc trưng theo Information Gain:")
print(df_ig.to_string(index=False))
ig_csv = os.path.join(tables_dir, "information_gain_ranking.csv")
df_ig.to_csv(ig_csv, index=False, encoding="utf-8-sig")
print(f"-> Đã lưu bảng xếp hạng Information Gain tại: {ig_csv}")

# Vẽ biểu đồ Bar Chart Information Gain
plt.figure(figsize=(8, 5))
sns.barplot(data=df_ig, x="Information_Gain", y="Feature", palette="viridis")
plt.title("Information Gain Ranking for Student Risk Classification")
plt.xlabel("Information Gain (bits)")
plt.ylabel("Feature")
plt.tight_layout()
ig_fig_path = os.path.join(figures_dir, "information_gain_ranking.png")
plt.savefig(ig_fig_path, dpi=300)
plt.close()
print(f"-> Đã lưu biểu đồ Information Gain tại: {ig_fig_path}")

# ==========================================================
# PHẦN D. ĐỒ THỊ, BFS/DFS VÀ CHUỖI MARKOV
# ==========================================================
print("\n--- PHẦN D.1: XÂY DỰNG ĐỒ THỊ QUAN HỆ SINH VIÊN ---")
interactions_file = os.path.join(data_dir, "interactions.csv")
G, num_nodes, num_edges, adj_list_sample, adj_matrix_sub = build_interaction_graph(interactions_file)
print(f"- Tổng số đỉnh |V|: {num_nodes} sinh viên")
print(f"- Tổng số cạnh |E|: {num_edges} liên kết tương tác có hướng")
print("\n- Danh sách kề (Adjacency List) mẫu cho 5 đỉnh:")
for k, v in adj_list_sample.items():
    print(f"  {k} -> {v}")
print("\n- Ma trận kề (Adjacency Matrix) đồ thị con 6 đỉnh:")
print(adj_matrix_sub)

print("\n--- PHẦN D.2: DUYỆT ĐỒ THỊ BFS/DFS VÀ TÍNH LIÊN THÔNG ---")
conn_report = traverse_bfs_dfs(G)
print(f"- Đỉnh xuất phát: {conn_report['start_node']}")
print(f"- Thứ tự duyệt BFS (10 đỉnh đầu): {conn_report['bfs_order_sample']}")
print(f"- Thứ tự duyệt DFS (10 đỉnh đầu): {conn_report['dfs_order_sample']}")
print(f"- Tổng đỉnh đến được qua BFS: {conn_report['total_visited_bfs']} / DFS: {conn_report['total_visited_dfs']}")
print(f"- Số thành phần liên thông yếu (WCC): {conn_report['num_wcc']} (Thành phần lớn nhất: {conn_report['largest_wcc_size']} đỉnh)")
print(f"- Số thành phần liên thông mạnh (SCC): {conn_report['num_scc']} (Thành phần lớn nhất: {conn_report['largest_scc_size']} đỉnh)")

# Vẽ đồ thị con trực quan
sub_nodes_viz = list(G.nodes())[:25]
sub_G_viz = G.subgraph(sub_nodes_viz)
plt.figure(figsize=(9, 7))
pos = nx.spring_layout(sub_G_viz, seed=42)
nx.draw_networkx_nodes(sub_G_viz, pos, node_size=500, node_color="#3498db", alpha=0.9)
nx.draw_networkx_edges(sub_G_viz, pos, arrowstyle="->", arrowsize=15, edge_color="#7f8c8d", alpha=0.7)
nx.draw_networkx_labels(sub_G_viz, pos, font_size=9, font_family="sans-serif", font_color="white")
plt.title("Student Interaction Network Subgraph (Sample 25 Students)")
plt.axis("off")
plt.tight_layout()
graph_fig_path = os.path.join(figures_dir, "student_interaction_graph.png")
plt.savefig(graph_fig_path, dpi=300)
plt.close()
print(f"-> Đã lưu hình đồ thị mạng lưới tại: {graph_fig_path}")

print("\n--- PHẦN D.3: MÔ HÌNH HÓA CHUỖI MARKOV ---")
states, P, row_sums, pi_0, pi_1, df_markov_hist, pi_stat = simulate_markov_learning_behavior(num_steps=20)
print(f"- Ma trận chuyển trạng thái P (3x3):\n{P}")
print(f"- Kiểm tra tổng từng hàng trong P: {row_sums} (Đều bằng 1.0)")
print(f"- Phân phối ban đầu pi_0: {pi_0}")
print(f"- Phân phối sau 1 bước pi_1: {np.round(pi_1, 4)}")
print(f"- Phân phối dừng lý thuyết pi*: {np.round(pi_stat, 4)}")
print(f"  -> {states[0]}: {pi_stat[0]*100:.2f}%")
print(f"  -> {states[1]}: {pi_stat[1]*100:.2f}%")
print(f"  -> {states[2]}: {pi_stat[2]*100:.2f}%")

markov_csv = os.path.join(tables_dir, "markov_simulation.csv")
df_markov_hist.to_csv(markov_csv, encoding="utf-8-sig")
print(f"-> Đã lưu lịch sử mô phỏng Markov tại: {markov_csv}")

# Vẽ đồ thị hội tụ chuỗi Markov
plt.figure(figsize=(8, 5))
for col in df_markov_hist.columns:
    plt.plot(df_markov_hist.index, df_markov_hist[col], marker="o", label=col)
plt.axhline(y=pi_stat[0], color="blue", linestyle="--", alpha=0.4)
plt.axhline(y=pi_stat[1], color="orange", linestyle="--", alpha=0.4)
plt.axhline(y=pi_stat[2], color="green", linestyle="--", alpha=0.4)
plt.title("Markov Chain State Probability Convergence over 20 Steps")
plt.xlabel("Step (k)")
plt.ylabel("Probability")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()
plt.tight_layout()
markov_fig_path = os.path.join(figures_dir, "markov_convergence.png")
plt.savefig(markov_fig_path, dpi=300)
plt.close()
print(f"-> Đã lưu biểu đồ hội tụ Markov tại: {markov_fig_path}")

# ==========================================================
# PHẦN E. TỐI ƯU HÓA HỖ TRỢ SINH VIÊN
# ==========================================================
print("\n--- PHẦN E.1: QUY HOẠCH TUYẾN TÍNH NGUYÊN NHỊ PHÂN (PuLP) ---")
mentors_file = os.path.join(data_dir, "mentors.csv")
capacity_file = os.path.join(data_dir, "support_capacity.csv")
lp_summary, df_lp_alloc = solve_mentor_allocation_lp(df_clean, mentors_file, capacity_file, top_n_students=12, total_budget=24)
print(f"- Trạng thái giải: {lp_summary['Status']}")
print(f"- Điểm ưu tiên tối đa đạt được (Optimal Z*): {lp_summary['Optimal_Score']}")
print(f"- Ngân sách sử dụng: {lp_summary['Total_Cost_Used']} / {lp_summary['Total_Budget']} giờ")
print(f"- Số sinh viên được hỗ trợ: {lp_summary['Students_Supported']} / {lp_summary['Total_Considered']} sinh viên")
print("\nDanh sách phân bổ hỗ trợ cụ thể:")
print(df_lp_alloc[["student_id", "Mức độ khẩn cấp", "Hình thức hỗ trợ phân bổ", "Chi phí (giờ)"]].to_string(index=False))

lp_csv = os.path.join(tables_dir, "mentor_allocation_lp.csv")
df_lp_alloc.to_csv(lp_csv, index=False, encoding="utf-8-sig")
print(f"-> Đã lưu kết quả quy hoạch tuyến tính tại: {lp_csv}")

print("\n--- PHẦN E.2: MẠNG LUỒNG CỰC ĐẠI VÀ ĐỒ THỊ HAI PHÍA (MAX FLOW) ---")
mf_summary, df_matched, G_flow = solve_bipartite_max_flow(df_clean, mentors_file, num_students=10)
print(f"- Giá trị Luồng cực đại Max Flow: {mf_summary['Max_Flow_Value']}")
print(f"- Tổng số sinh viên cần ghép cặp: {mf_summary['Total_Students']}")
print(f"- Số cặp ghép thành công: {mf_summary['Successful_Matches']}")
print(f"- Dung lượng lát cắt hẹp nhất Min-Cut: {mf_summary['Min_Cut_Value']}")
print("\nDanh sách cặp ghép (Sinh viên -> Mentor):")
print(df_matched.to_string(index=False))
print("\nCác liên kết điểm nghẽn (Bottleneck / Min-Cut):")
for u, v, cap in mf_summary["Bottleneck_Edges"]:
    print(f"  -> Liên kết {u} -> {v} (Dung lượng bão hòa: {cap})")

flow_csv = os.path.join(tables_dir, "bipartite_max_flow.csv")
df_matched.to_csv(flow_csv, index=False, encoding="utf-8-sig")
print(f"-> Đã lưu kết quả ghép cặp Max Flow tại: {flow_csv}")

print("\n==========================================================")
print("    ĐÃ HOÀN THÀNH TOÀN BỘ CÁC BƯỚC THỰC HIỆN GIAI ĐOẠN 2   ")
print("==========================================================")
