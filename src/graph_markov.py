import networkx as nx
import pandas as pd
import numpy as np

def build_interaction_graph(interactions_path):
    """
    Phần D.1: Xây dựng Đồ thị quan hệ sinh viên từ interactions.csv
    Sử dụng đồ thị có hướng (Directed Graph) vì quan hệ tương tác/hỏi bài có chiều.
    """
    df_inter = pd.read_csv(interactions_path)
    
    G = nx.DiGraph()
    for _, row in df_inter.iterrows():
        u = str(row["source_student"])
        v = str(row["target_student"])
        w = float(row["interaction_count"])
        rel = str(row["relation_type"])
        G.add_edge(u, v, weight=w, relation=rel)
        
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    
    # Lấy danh sách kề cho 5 đỉnh đầu tiên
    sample_nodes = list(G.nodes())[:5]
    adj_list_sample = {node: list(G.neighbors(node)) for node in sample_nodes}
    
    # Tạo đồ thị con 6 đỉnh để xuất ma trận kề
    sub_nodes = list(G.nodes())[:6]
    sub_G = G.subgraph(sub_nodes)
    adj_matrix_df = pd.DataFrame(
        nx.to_numpy_array(sub_G, nodelist=sub_nodes, weight=None, dtype=int),
        index=sub_nodes,
        columns=sub_nodes
    )
    
    return G, num_nodes, num_edges, adj_list_sample, adj_matrix_df

def traverse_bfs_dfs(G, start_node=None):
    """
    Phần D.2: Duyệt đồ thị BFS, DFS và kiểm tra tính liên thông
    """
    # Nếu start_node không được chỉ định hoặc không có cạnh ra, chọn đỉnh có bậc ra cao nhất
    if start_node is None or start_node not in G or G.out_degree(start_node) == 0:
        degrees = dict(G.out_degree())
        start_node = max(degrees, key=degrees.get)
        
    # Duyệt BFS
    bfs_nodes = list(nx.bfs_tree(G, source=start_node).nodes())
    
    # Duyệt DFS
    dfs_nodes = list(nx.dfs_tree(G, source=start_node).nodes())
    
    # Phân tích tính liên thông
    # Weakly connected components (WCC)
    wcc = list(nx.weakly_connected_components(G))
    num_wcc = len(wcc)
    largest_wcc = max(len(c) for c in wcc)
    
    # Strongly connected components (SCC)
    scc = list(nx.strongly_connected_components(G))
    num_scc = len(scc)
    largest_scc = max(len(c) for c in scc)
    
    connectivity_report = {
        "start_node": start_node,
        "bfs_order_sample": bfs_nodes[:10],
        "dfs_order_sample": dfs_nodes[:10],
        "total_visited_bfs": len(bfs_nodes),
        "total_visited_dfs": len(dfs_nodes),
        "num_wcc": num_wcc,
        "largest_wcc_size": largest_wcc,
        "num_scc": num_scc,
        "largest_scc_size": largest_scc
    }
    
    return connectivity_report

def simulate_markov_learning_behavior(num_steps=20):
    """
    Phần D.3: Ứng dụng chuỗi Markov mô hình hóa hành vi học tập
    3 trạng thái:
    - S1 (Học tích cực): Điểm tốt, nộp bài đúng hạn, chăm chỉ
    - S2 (Học cầm chừng): Điểm trung bình, thỉnh thoảng trễ hạn
    - S3 (Nguy cơ sa sút): Bỏ học phần, vắng nhiều, điểm liệt
    """
    states = ["Học tích cực (S1)", "Học cầm chừng (S2)", "Nguy cơ sa sút (S3)"]
    
    # 1. Ma trận xác suất chuyển trạng thái P (3x3)
    P = np.array([
        [0.75, 0.20, 0.05],  # Từ S1: 75% giữ tích cực, 20% tụt sang S2, 5% sang S3
        [0.20, 0.60, 0.20],  # Từ S2: 20% vươn lên S1, 60% ở lại S2, 20% rơi vào S3
        [0.05, 0.25, 0.70]   # Từ S3: 5% cải thiện lên S1, 25% lên S2, 70% tiếp tục nguy cơ
    ])
    
    # Chứng minh tổng mỗi dòng bằng 1.0
    row_sums = P.sum(axis=1)
    
    # 2. Phân phối xác suất ban đầu (đầu kỳ học)
    pi_0 = np.array([0.70, 0.25, 0.05])
    
    # 3. Tính phân phối sau 1 bước
    pi_1 = np.dot(pi_0, P)
    
    # 4. Mô phỏng qua các bước k = 1..num_steps
    history = [pi_0]
    pi_k = pi_0.copy()
    for _ in range(num_steps):
        pi_k = np.dot(pi_k, P)
        history.append(pi_k)
        
    df_history = pd.DataFrame(history, columns=states)
    df_history.index.name = "Bước (k)"
    
    # 5. Tìm phân phối dừng (Stationary Distribution) pi* thỏa: pi* P = pi* và sum(pi*) = 1
    # Giải hệ phương trình: (P^T - I) pi* = 0 với ràng buộc sum(pi*) = 1
    A = (P.T - np.eye(3))
    A[-1] = [1.0, 1.0, 1.0]
    b = np.array([0.0, 0.0, 1.0])
    pi_stationary = np.linalg.lstsq(A, b, rcond=None)[0]
    
    return states, P, row_sums, pi_0, pi_1, df_history, pi_stationary
