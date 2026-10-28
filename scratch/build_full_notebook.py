import json
import os
import sys

nb_path = r"c:\HOC_HANH\Mon dang hoc\ITA201\smartedu-ai\notebooks\smartedu_assignment.ipynb"
with open(nb_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

# Keep Phase 1 cells (cells 0 to 29)
# Check if cell 29 is the closing divider
cells_phase1 = nb["cells"][:30]

# Now let's define Phase 2 cells
cells_phase2 = [
    # -------------------------------------------------------------
    # SECTION 5: PHẦN C
    # -------------------------------------------------------------
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 5. PHẦN C: XÁC SUẤT, BAYES VÀ LÝ THUYẾT THÔNG TIN\n",
            "\n",
            "Mục tiêu của Phần C là khai phá các quy luật xác suất và độ bất định thông tin trong dữ liệu học tập:\n",
            "1. Phân tích xác suất có điều kiện hai chiều $P(\\text{high\\_risk} | \\text{feature})$ và $P(\\text{feature} | \\text{high\\_risk})$.\n",
            "2. Xây dựng mô hình phân loại xác suất Gaussian Naive Bayes, tính toán hàm mật độ xác suất và ma trận nhầm lẫn.\n",
            "3. Ứng dụng Entropy Shannon và Độ tăng thông tin (Information Gain) để định lượng mức độ quan trọng của các đặc trưng phục vụ lựa chọn thuộc tính phân loại."
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 5.1. C.1 - Xác suất có điều kiện hai chiều & Kiểm chứng Định lý Bayes\n",
            "\n",
            "* Công thức định lý Bayes:\n",
            "$$P(\\text{high\\_risk} | A) = \\frac{P(A | \\text{high\\_risk}) \\cdot P(\\text{high\\_risk})}{P(A)}$$\n",
            "\n",
            "> **HƯỚNG DẪN TÍNH TAY & THAY SỐ CÔNG THỨC BAYES (MINH HỌA CHI TIẾT TỪNG THAM SỐ):**\n",
            ">\n",
            "> **1. Nguồn gốc từng tham số lấy ở đâu và bằng bao nhiêu:**\n",
            "> * **Tổng số sinh viên khảo sát ($N$):** $N = 4.424$ dòng dữ liệu từ `data/students.csv`.\n",
            "> * **Tham số $P(\\text{high\\_risk})$ (Xác suất tiên nghiệm sinh viên nguy cơ):**\n",
            ">   * Lấy từ số sinh viên có nhãn `high_risk` trong tập dữ liệu: $N_{\\text{high}} = 2.215$ sinh viên.\n",
            ">   * $P(\\text{high\\_risk}) = \\frac{2.215}{4.424} = 0.5007$ ($50.07\\%$).\n",
            "> * **Tham số $P(A)$ với biến cố $A = \\text{att\\_low}$ (Điểm chuyên cần thấp $\\le 0.75$):**\n",
            ">   * Đếm tổng số sinh viên có `attendance_rate` $\\le 0.75$ trong toàn bộ mẫu: $N_{\\text{att\\_low}} = 1.382$ sinh viên.\n",
            ">   * $P(\\text{att\\_low}) = \\frac{1.382}{4.424} = 0.3124$ ($31.24\\%$).\n",
            "> * **Tham số $P(\\text{att\\_low} | \\text{high\\_risk})$ (Độ hợp lý Likelihood):**\n",
            ">   * Trong số $2.215$ sinh viên nguy cơ cao, có $1.262$ sinh viên có điểm chuyên cần thấp.\n",
            ">   * $P(\\text{att\\_low} | \\text{high\\_risk}) = \\frac{1.262}{2.215} = 0.5698$ ($56.98\\%$).\n",
            ">\n",
            "> **2. Công thức sau khi đã thay số cụ thể từng bước:**\n",
            "> $$P(\\text{high\\_risk} | \\text{att\\_low}) = \\frac{P(\\text{att\\_low} | \\text{high\\_risk}) \\times P(\\text{high\\_risk})}{P(\\text{att\\_low})}$$\n",
            "> $$P(\\text{high\\_risk} | \\text{att\\_low}) = \\frac{0.5698 \\times 0.5007}{0.3124} = \\frac{0.2853}{0.3124} = 0.9132 \\quad (91.32\\%)$$\n",
            ">\n",
            "> **3. Nhận xét kết quả:**\n",
            "> * Giá trị tính tay $91.32\\%$ hoàn toàn trùng khớp với tỷ lệ đếm trực tiếp $\\frac{1.262}{1.382} = 0.9132$ và kết quả từ code `compute_conditional_probabilities`.\n",
            "> * **Ý nghĩa thực tiễn:** Nếu một sinh viên có chuyên cần thấp ($A = \\text{att\\_low}$), xác suất sinh viên đó thuộc diện nguy cơ rớt môn lên tới **$91.32\\%$**. Đây là chỉ số cảnh báo sớm cực kỳ tin cậy để hệ thống SmartEdu AI kích hoạt hỗ trợ ngay lập tức."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "df_prob = compute_conditional_probabilities(df_clean)\n",
            "print(\"BẢNG XÁC SUẤT CÓ ĐIỀU KIỆN HAI CHIỀU:\")\n",
            "print(df_prob.to_string(index=False))\n",
            "\n",
            "# Lưu bảng xác suất\n",
            "prob_csv = os.path.join(tables_dir, \"conditional_probabilities.csv\")\n",
            "df_prob.to_csv(prob_csv, index=False, encoding=\"utf-8-sig\")\n",
            "print(f\"\\n-> Bảng kết quả đã được lưu tại: {prob_csv}\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 5.2. C.2 - Huấn luyện Mô hình Gaussian Naive Bayes & Dự báo Xác suất\n",
            "\n",
            "* Mô hình Gaussian Naive Bayes giả định các đặc trưng tuân theo phân phối chuẩn với hàm mật độ:\n",
            "$$P(x_i | C_k) = \\frac{1}{\\sqrt{2\\pi \\sigma_{k,i}^2}} \\exp\\left( -\\frac{(x_i - \\mu_{k,i})^2}{2\\sigma_{k,i}^2} \\right)$$\n",
            "* Xác suất hậu nghiệm tỷ lệ với tích xác suất tiên nghiệm và các hàm hợp lý:\n",
            "$$P(C_k | X) \\propto P(C_k) \\prod_{i=1}^n P(x_i | C_k)$$\n",
            "\n",
            "> **HƯỚNG DẪN TÍNH TAY & THAY SỐ CÔNG THỨC GAUSSIAN NAIVE BAYES (MINH HỌA CHO SINH VIÊN `SV0001`):**\n",
            ">\n",
            "> **1. Nguồn gốc từng tham số lấy ở đâu và bằng bao nhiêu:**\n",
            "> * **Tham số tiên nghiệm:** $P(C_0) = P(\\text{low\\_risk}) = 0.4993$, $P(C_1) = P(\\text{high\\_risk}) = 0.5007$.\n",
            "> * **Tham số thống kê lớp $\\text{high\\_risk}$ ($C_1$):** Lấy từ thuộc tính `gnb.theta_[1]` (trung bình $\\mu$) và `gnb.var_[1]` (phương sai $\\sigma^2$):\n",
            ">   * Đặc trưng `attendance_rate`: $\\mu_{1,1} = 0.6879, \\sigma_{1,1}^2 = 0.0369$\n",
            ">   * Đặc trưng `lab_avg`: $\\mu_{1,3} = 4.3317, \\sigma_{1,3}^2 = 7.8416$\n",
            "> * **Tham số thống kê lớp $\\text{low\\_risk}$ ($C_0$):** Lấy từ thuộc tính `gnb.theta_[0]` và `gnb.var_[0]`:\n",
            ">   * Đặc trưng `attendance_rate`: $\\mu_{0,1} = 0.9429, \\sigma_{0,1}^2 = 0.0119$\n",
            ">   * Đặc trưng `lab_avg`: $\\mu_{0,3} = 6.3465, \\sigma_{0,3}^2 = 1.7256$\n",
            "> * **Giá trị quan sát của sinh viên `SV0001`:** $x_1 = 0.50$ (`attendance_rate`), $x_3 = 0.00$ (`lab_avg`).\n",
            ">\n",
            "> **2. Công thức sau khi đã thay số cụ thể từng bước:**\n",
            "> * **Hàm mật độ đặc trưng Chuyên cần ($x_1 = 0.50$):**\n",
            ">   * Đối với lớp nguy cơ cao ($C_1$):\n",
            ">     $$P(x_1 | C_1) = \\frac{1}{\\sqrt{2\\pi \\times 0.0369}} \\exp\\left( -\\frac{(0.50 - 0.6879)^2}{2 \\times 0.0369} \\right) = \\frac{1}{0.4815} \\exp(-0.4784) = 2.0768 \\times 0.6198 = 1.2871$$\n",
            ">   * Đối với lớp an toàn ($C_0$):\n",
            ">     $$P(x_1 | C_0) = \\frac{1}{\\sqrt{2\\pi \\times 0.0119}} \\exp\\left( -\\frac{(0.50 - 0.9429)^2}{2 \\times 0.0119} \\right) = \\frac{1}{0.2735} \\exp(-8.2430) = 3.6563 \\times 0.000263 = 0.000974$$\n",
            "> * **Hàm mật độ đặc trưng Điểm thực hành ($x_3 = 0.00$):**\n",
            ">   * Đối với lớp nguy cơ cao ($C_1$):\n",
            ">     $$P(x_3 | C_1) = \\frac{1}{\\sqrt{2\\pi \\times 7.8416}} \\exp\\left( -\\frac{(0.00 - 4.3317)^2}{2 \\times 7.8416} \\right) = \\frac{1}{7.0191} \\exp(-1.1964) = 0.1425 \\times 0.3023 = 0.0431$$\n",
            ">   * Đối với lớp an toàn ($C_0$):\n",
            ">     $$P(x_3 | C_0) = \\frac{1}{\\sqrt{2\\pi \\times 1.7256}} \\exp\\left( -\\frac{(0.00 - 6.3465)^2}{2 \\times 1.7256} \\right) = \\frac{1}{3.2928} \\exp(-11.6702) = 0.3037 \\times 0.0000085 = 0.000003$$\n",
            ">\n",
            "> **3. Nhận xét kết quả:**\n",
            "> * Khi nhân tích các hàm mật độ, khả năng sinh viên `SV0001` rơi vào lớp $C_1$ cao gấp hàng triệu lần so với lớp $C_0$.\n",
            "> * Mô hình dự báo xác suất $P(\\text{high\\_risk} | X) \\approx 1.0000$ ($100\\%$), khớp hoàn toàn với thực tế sinh viên `SV0001` bỏ bê học tập và nhận nhãn nguy cơ cao."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "gnb, X_train, X_test, y_train, y_test, y_pred, y_proba, gnb_metrics = train_gaussian_naive_bayes(X, y)\n",
            "\n",
            "print(\"KẾT QUẢ ĐÁNH GIÁ MÔ HÌNH GAUSSIAN NAIVE BAYES:\")\n",
            "print(f\"- Độ chính xác (Accuracy):  {gnb_metrics['Accuracy']*100:.2f}%\")\n",
            "print(f\"- Precision:               {gnb_metrics['Precision']*100:.2f}%\")\n",
            "print(f\"- Recall (Độ nhạy):        {gnb_metrics['Recall']*100:.2f}%\")\n",
            "print(f\"- F1-Score:                {gnb_metrics['F1-Score']*100:.2f}%\")\n",
            "\n",
            "# Dự báo cho sinh viên SV0001\n",
            "sv1_proba = gnb.predict_proba(X[0].reshape(1, -1))[0]\n",
            "sv1_pred = gnb.predict(X[0].reshape(1, -1))[0]\n",
            "print(f\"\\n- Dự báo cho SV0001: P(low_risk)={sv1_proba[0]:.6f}, P(high_risk)={sv1_proba[1]:.6f} => Phân loại: {['low_risk', 'high_risk'][sv1_pred]}\")\n",
            "\n",
            "# Trực quan hóa ma trận nhầm lẫn Confusion Matrix\n",
            "plt.figure(figsize=(6, 5))\n",
            "sns.heatmap(gnb_metrics[\"Confusion_Matrix\"], annot=True, fmt=\"d\", cmap=\"Blues\",\n",
            "            xticklabels=[\"low_risk (0)\", \"high_risk (1)\"],\n",
            "            yticklabels=[\"low_risk (0)\", \"high_risk (1)\"])\n",
            "plt.xlabel(\"Nhãn dự đoán\")\n",
            "plt.ylabel(\"Nhãn thực tế\")\n",
            "plt.title(\"Ma trận nhầm lẫn (Confusion Matrix) - Gaussian Naive Bayes\")\n",
            "plt.tight_layout()\n",
            "plt.show()"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 5.3. C.3 - Shannon Entropy & Độ tăng thông tin (Information Gain)\n",
            "\n",
            "* Công thức Entropy Shannon của tập dữ liệu $S$:\n",
            "$$H(S) = -\\sum_{i=1}^c p_i \\log_2(p_i)$$\n",
            "* Entropy có điều kiện khi phân tách theo đặc trưng $X$:\n",
            "$$H(S | X) = \\sum_{v \\in \\text{Values}(X)} \\frac{|S_v|}{|S|} H(S_v)$$\n",
            "* Độ tăng thông tin (Information Gain):\n",
            "$$IG(S, X) = H(S) - H(S | X)$$\n",
            "\n",
            "> **HƯỚNG DẪN TÍNH TAY & THAY SỐ CÔNG THỨC SHANNON ENTROPY VÀ INFORMATION GAIN:**\n",
            ">\n",
            "> **1. Nguồn gốc từng tham số lấy ở đâu và bằng bao nhiêu:**\n",
            "> * **Tập dữ liệu gốc $S$ ($N = 4.424$):** Gồm $2.209$ mẫu `low_risk` ($p_0 = 0.4993$) và $2.215$ mẫu `high_risk` ($p_1 = 0.5007$).\n",
            "> * **Phân nhánh của đặc trưng `attendance_bin`:**\n",
            ">   * Nhóm `att_low` ($N_1 = 1.382$, tỷ trọng $\\frac{1.382}{4.424} = 0.3124$): gồm $1.262$ high_risk ($p_{11} = 0.9132$) và $120$ low_risk ($p_{10} = 0.0868$).\n",
            ">   * Nhóm `att_med` ($N_2 = 928$, tỷ trọng $\\frac{928}{4.424} = 0.2098$): gồm $569$ high_risk ($p_{21} = 0.6131$) và $359$ low_risk ($p_{20} = 0.3869$).\n",
            ">   * Nhóm `att_high` ($N_3 = 2.114$, tỷ trọng $\\frac{2.114}{4.424} = 0.4778$): gồm $384$ high_risk ($p_{31} = 0.1816$) và $1.730$ low_risk ($p_{30} = 0.8184$).\n",
            ">\n",
            "> **2. Công thức sau khi đã thay số cụ thể từng bước:**\n",
            "> * **Entropy gốc $H(S)$:**\n",
            ">   $$H(S) = - [0.4993 \\log_2(0.4993) + 0.5007 \\log_2(0.5007)] = - [0.4993 \\times (-1.0020) + 0.5007 \\times (-0.9980)] = 1.0000 \\text{ bit}$$\n",
            "> * **Entropy của từng nhóm con:**\n",
            ">   * Nhóm `att_low`: $H(S_1) = - [0.9132 \\log_2(0.9132) + 0.0868 \\log_2(0.0868)] = - [-0.1197 - 0.3061] = 0.4258 \\text{ bit}$\n",
            ">   * Nhóm `att_med`: $H(S_2) = - [0.6131 \\log_2(0.6131) + 0.3869 \\log_2(0.3869)] = - [-0.4328 - 0.5299] = 0.9627 \\text{ bit}$\n",
            ">   * Nhóm `att_high`: $H(S_3) = - [0.1816 \\log_2(0.1816) + 0.8184 \\log_2(0.8184)] = - [-0.4470 - 0.2367] = 0.6837 \\text{ bit}$\n",
            "> * **Entropy có điều kiện $H(S | \\text{attendance\\_bin})$:**\n",
            ">   $$H(S | \\text{attendance\\_bin}) = (0.3124 \\times 0.4258) + (0.2098 \\times 0.9627) + (0.4778 \\times 0.6837)$$\n",
            ">   $$H(S | \\text{attendance\\_bin}) = 0.1330 + 0.2020 + 0.3267 = 0.6617 \\text{ bit}$$\n",
            "> * **Độ tăng thông tin $IG(S, \\text{attendance\\_bin})$:**\n",
            ">   $$IG(S, \\text{attendance\\_bin}) = H(S) - H(S | \\text{attendance\\_bin}) = 1.0000 - 0.6617 = 0.3383 \\text{ bit}$$\n",
            ">\n",
            "> **3. Nhận xét kết quả:**\n",
            "> * Phép tính tay ra chính xác $IG = 0.3383$ bit. Trong tất cả các đặc trưng, `attendance_bin` đạt Information Gain cao nhất ($0.3383$ bit), tiếp theo là `assignment_bin` ($0.1672$ bit) và `lab_bin` ($0.1203$ bit).\n",
            "> * Điều này chứng minh toán học rằng việc theo dõi chuyên cần giúp loại bỏ độ bất định về nguy cơ học tập nhiều nhất, giải thích tại sao cây quyết định luôn chọn tiêu chí điểm danh làm nhánh phân tách gốc."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "H_parent, df_ig = compute_information_gain_ranking(df_clean)\n",
            "print(f\"Entropy ban đầu của nhãn H(risk_label): {H_parent:.4f} bits\\n\")\n",
            "print(\"BẢNG XẾP HẠNG ĐẶC TRƯNG THEO INFORMATION GAIN:\")\n",
            "print(df_ig.to_string(index=False))\n",
            "\n",
            "# Lưu bảng\n",
            "ig_csv = os.path.join(tables_dir, \"information_gain_ranking.csv\")\n",
            "df_ig.to_csv(ig_csv, index=False, encoding=\"utf-8-sig\")\n",
            "\n",
            "# Vẽ biểu đồ cột xếp hạng Information Gain\n",
            "plt.figure(figsize=(8, 4.5))\n",
            "sns.barplot(data=df_ig, x=\"Information_Gain\", y=\"Feature\", palette=\"viridis\")\n",
            "plt.title(\"Xếp hạng Độ tăng thông tin (Information Gain) của các đặc trưng\")\n",
            "plt.xlabel(\"Information Gain (bits)\")\n",
            "plt.ylabel(\"Đặc trưng\")\n",
            "plt.tight_layout()\n",
            "plt.show()"
        ]
    },

    # -------------------------------------------------------------
    # SECTION 6: PHẦN D
    # -------------------------------------------------------------
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 6. PHẦN D: LÝ THUYẾT ĐỒ THỊ VÀ CHUỖI MARKOV\n",
            "\n",
            "Mục tiêu của Phần D là phân tích mạng lưới tương tác xã hội - học tập và mô hình hóa quá trình chuyển dịch trạng thái học tập theo thời gian:\n",
            "1. Xây dựng đồ thị có hướng $G=(V, E)$ biểu diễn mạng lưới hỗ trợ/trao đổi giữa các sinh viên.\n",
            "2. Khảo sát thuật toán duyệt đồ thị BFS và DFS, đánh giá các thành phần liên thông yếu (WCC) và liên thông mạnh (SCC).\n",
            "3. Xây dựng Chuỗi Markov với 3 trạng thái học tập, tính toán xác suất chuyển trạng thái, mô phỏng qua 20 bước và tìm phân phối dừng dài hạn."
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 6.1. D.1 - Xây dựng Đồ thị có hướng quan hệ sinh viên & Biểu diễn ma trận kề\n",
            "\n",
            "* Đồ thị có hướng $G = (V, E)$ với tập đỉnh $V$ là các sinh viên và tập cạnh có hướng $E$ biểu diễn hành động trao đổi học tập (sinh viên $u$ tương tác/hỏi bài sinh viên $v$).\n",
            "* Biểu diễn cấu trúc đồ thị thông qua Danh sách kề (Adjacency List) và Ma trận kề (Adjacency Matrix):\n",
            "$$A_{ij} = \\begin{cases} 1 & \\text{nếu có cạnh } (u_i \\to u_j) \\in E \\\\ 0 & \\text{ngược lại} \\end{cases}$$\n",
            "* Phân tích bậc vào (`in-degree`: số lần được bạn bè hỏi) và bậc ra (`out-degree`: số lần chủ động đi hỏi bài).\n",
            "\n",
            "> **HƯỚNG DẪN TÍNH TAY & ĐẶC TRƯNG CỦA ĐỒ THỊ MẠNG LƯỚI:**\n",
            ">\n",
            "> **1. Nguồn gốc dữ liệu:** File `data/interactions.csv` chứa $1.500$ lượt tương tác giữa $1.128$ sinh viên.\n",
            "> **2. Phân tích bậc:**\n",
            "> * Những sinh viên có `in-degree` cao đóng vai trò là \"hạt nhân tri thức\" (Hubs/KOLs học tập), có thể tận dụng làm trợ giảng hoặc trưởng nhóm học tập.\n",
            "> * Những sinh viên có cả `in-degree = 0` và `out-degree = 0` hoặc rất thấp là các sinh viên cô lập (Isolated), có nguy cơ chán nản và bỏ học cao nhất."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "interactions_file = os.path.join(data_dir, \"interactions.csv\")\n",
            "G, num_nodes, num_edges, adj_list_sample, adj_matrix_sub = build_interaction_graph(interactions_file)\n",
            "\n",
            "print(f\"TỔNG QUAN ĐỒ THỊ TƯƠNG TÁC SINH VIÊN:\")\n",
            "print(f\"- Số lượng đỉnh |V|: {num_nodes} sinh viên\")\n",
            "print(f\"- Số lượng cạnh có hướng |E|: {num_edges} mối tương tác\")\n",
            "\n",
            "print(\"\\n- Danh sách kề (Adjacency List) mẫu cho 5 sinh viên đầu:\")\n",
            "for k, v in adj_list_sample.items():\n",
            "    print(f\"  {k} -> {v}\")\n",
            "\n",
            "print(\"\\n- Ma trận kề (Adjacency Matrix) đồ thị con 6 đỉnh:\")\n",
            "print(adj_matrix_sub)\n",
            "\n",
            "# Vẽ trực quan một mạng con tiêu biểu (25 sinh viên)\n",
            "sub_nodes_viz = list(G.nodes())[:25]\n",
            "sub_G_viz = G.subgraph(sub_nodes_viz)\n",
            "plt.figure(figsize=(8.5, 6))\n",
            "pos = nx.spring_layout(sub_G_viz, seed=42)\n",
            "nx.draw_networkx_nodes(sub_G_viz, pos, node_size=450, node_color=\"#3498db\", alpha=0.9)\n",
            "nx.draw_networkx_edges(sub_G_viz, pos, arrowstyle=\"->\", arrowsize=14, edge_color=\"#7f8c8d\", alpha=0.7)\n",
            "nx.draw_networkx_labels(sub_G_viz, pos, font_size=8.5, font_family=\"sans-serif\", font_color=\"white\")\n",
            "plt.title(\"Mạng lưới tương tác học tập sinh viên (Trích xuất phân lớp 25 đỉnh)\")\n",
            "plt.axis(\"off\")\n",
            "plt.tight_layout()\n",
            "plt.show()"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 6.2. D.2 - Thuật toán duyệt BFS/DFS & Phân tích tính liên thông\n",
            "\n",
            "* **BFS (Breadth-First Search - Duyệt theo chiều rộng):** Sử dụng hàng đợi FIFO (Queue), duyệt qua toàn bộ các bạn học cùng tầng trước khi lan sang các bạn của bạn. Rất phù hợp để tìm khoảng cách ngắn nhất trong mạng lưới trao đổi học tập.\n",
            "* **DFS (Depth-First Search - Duyệt theo chiều sâu):** Sử dụng ngăn xếp LIFO (Stack) hoặc đệ quy, đi sâu theo một chuỗi học tập đến khi chạm ngõ cụt thì quay lui. Phù hợp để phát hiện chu trình trao đổi khép kín và liên thông mạnh.\n",
            "* **Thành phần liên thông:**\n",
            "  * Weakly Connected Components (WCC): Bỏ qua chiều mũi tên cạnh, phản ánh các cụm sinh viên có bất kỳ liên hệ gián tiếp nào với nhau.\n",
            "  * Strongly Connected Components (SCC): Xét đúng chiều mũi tên, phản ánh các nhóm học tập có tương tác hai chiều (mọi sinh viên trong nhóm đều có thể gửi và nhận thông tin từ nhau)."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "conn_report = traverse_bfs_dfs(G)\n",
            "print(\"KẾT QUẢ DUYỆT ĐỒ THỊ VÀ KHẢO SÁT LIÊN THÔNG:\")\n",
            "print(f\"- Đỉnh gốc xuất phát: {conn_report['start_node']}\")\n",
            "print(f\"- Thứ tự duyệt BFS (10 đỉnh đầu): {conn_report['bfs_order_sample']}\")\n",
            "print(f\"- Thứ tự duyệt DFS (10 đỉnh đầu): {conn_report['dfs_order_sample']}\")\n",
            "print(f\"- Tổng số sinh viên có thể tiếp cận được từ gốc: {conn_report['total_visited_bfs']} sinh viên\")\n",
            "print(f\"- Số thành phần liên thông yếu (WCC): {conn_report['num_wcc']} (Nhóm lớn nhất gồm: {conn_report['largest_wcc_size']} sinh viên)\")\n",
            "print(f\"- Số thành phần liên thông mạnh (SCC): {conn_report['num_scc']} (Nhóm tương tác hai chiều lớn nhất: {conn_report['largest_scc_size']} sinh viên)\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 6.3. D.3 - Mô hình Hóa Chuỗi Markov Dự báo Hành vi Học tập\n",
            "\n",
            "* Không gian trạng thái $S = \\{\\text{Active}, \\text{Moderate}, \\text{At-risk}\\}$.\n",
            "* Ma trận xác suất chuyển trạng thái $P \\in \\mathbb{R}^{3 \\times 3}$ thỏa mãn $P_{ij} \\ge 0$ và $\\sum_j P_{ij} = 1$:\n",
            "$$P = \\begin{bmatrix} 0.75 & 0.20 & 0.05 \\\\ 0.20 & 0.60 & 0.20 \\\\ 0.05 & 0.25 & 0.70 \\end{bmatrix}$$\n",
            "* Quy luật chuyển dịch trạng thái qua từng bước:\n",
            "$$\\pi_{t+1} = \\pi_t \\cdot P$$\n",
            "* Phân phối dừng dài hạn $\\pi^*$ thỏa mãn hệ phương trình:\n",
            "$$\\pi^* P = \\pi^* \\quad \\text{và} \\quad \\sum_{i=1}^3 \\pi_i^* = 1$$\n",
            "\n",
            "> **HƯỚNG DẪN TÍNH TAY & THAY SỐ BƯỚC 1 PHÉP NHÂN MA TRẬN $\\pi_1 = \\pi_0 P$:**\n",
            ">\n",
            "> **1. Nguồn gốc từng tham số lấy ở đâu và bằng bao nhiêu:**\n",
            "> * **Phân phối ban đầu $\\pi_0$:** Khảo sát đầu kỳ gồm $70\\%$ sinh viên Tích cực, $25\\%$ Trung bình, $5\\%$ Nguy cơ $\\Rightarrow \\pi_0 = [0.70, 0.25, 0.05]$.\n",
            "> * **Ma trận chuyển trạng thái $P$:** Lấy từ bảng quan sát hành vi chuyển trạng thái tuần qua tuần của sinh viên.\n",
            ">\n",
            "> **2. Công thức sau khi đã thay số cụ thể từng bước:**\n",
            "> * Xác suất trạng thái Tích cực (Active) tại bước 1:\n",
            ">   $$\\pi_{1, 1} = (0.70 \\times 0.75) + (0.25 \\times 0.20) + (0.05 \\times 0.05) = 0.5250 + 0.0500 + 0.0025 = 0.5775 \\quad (57.75\\%)$$\n",
            "> * Xác suất trạng thái Trung bình (Moderate) tại bước 1:\n",
            ">   $$\\pi_{1, 2} = (0.70 \\times 0.20) + (0.25 \\times 0.60) + (0.05 \\times 0.25) = 0.1400 + 0.1500 + 0.0125 = 0.3025 \\quad (30.25\\%)$$\n",
            "> * Xác suất trạng thái Nguy cơ (At-risk) tại bước 1:\n",
            ">   $$\\pi_{1, 3} = (0.70 \\times 0.05) + (0.25 \\times 0.20) + (0.05 \\times 0.70) = 0.0350 + 0.0500 + 0.0350 = 0.1200 \\quad (12.00\\%)$$\n",
            "> * **Kiểm tra tổng xác suất:** $0.5775 + 0.3025 + 0.1200 = 1.0000$ ($100\\%$).\n",
            ">\n",
            "> **3. Nhận xét kết quả & Phân phối dừng:**\n",
            "> * Phép tính tay cho ra kết quả $\\pi_1 = [0.5775, 0.3025, 0.1200]$ khớp chính xác tuyệt đối với kết quả in ra từ chương trình mô phỏng.\n",
            "> * Qua 20 bước lặp, phân phối xác suất nhanh chóng hội tụ về phân phối dừng độc lập với trạng thái khởi đầu: $\\pi^* = [34.57\\%, 35.80\\%, 29.63\\%]$.\n",
            "> * **Ý nghĩa cảnh báo:** Nếu nhà trường không có biện pháp can thiệp can thiệp sớm, về lâu dài sẽ có tới **$29.63\\%$** sinh viên rơi vào trạng thái nguy cơ rớt môn thường trực."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "states, P, row_sums, pi_0, pi_1, df_markov_hist, pi_stat = simulate_markov_learning_behavior(num_steps=20)\n",
            "\n",
            "print(\"KẾT QUẢ MÔ HÌNH HÓA CHUỖI MARKOV:\")\n",
            "print(f\"- Ma trận chuyển trạng thái P:\\n{P}\")\n",
            "print(f\"- Kiểm tra tổng từng hàng: {row_sums}\")\n",
            "print(f\"- Phân phối ban đầu pi_0: {pi_0}\")\n",
            "print(f\"- Phân phối bước 1 pi_1:  {np.round(pi_1, 4)}\")\n",
            "print(f\"- Phân phối dừng dài hạn pi*: {np.round(pi_stat, 4)}\")\n",
            "for i, s in enumerate(states):\n",
            "    print(f\"  + Trạng thái '{s}': {pi_stat[i]*100:.2f}%\")\n",
            "\n",
            "# Lưu lịch sử mô phỏng\n",
            "markov_csv = os.path.join(tables_dir, \"markov_simulation.csv\")\n",
            "df_markov_hist.to_csv(markov_csv, encoding=\"utf-8-sig\")\n",
            "\n",
            "# Trực quan hóa đường cong hội tụ xác suất trạng thái\n",
            "plt.figure(figsize=(8, 4.5))\n",
            "for col in df_markov_hist.columns:\n",
            "    plt.plot(df_markov_hist.index, df_markov_hist[col], marker=\"o\", label=col)\n",
            "plt.axhline(y=pi_stat[0], color=\"blue\", linestyle=\"--\", alpha=0.4, label=\"Hội tụ Active\")\n",
            "plt.axhline(y=pi_stat[1], color=\"orange\", linestyle=\"--\", alpha=0.4, label=\"Hội tụ Moderate\")\n",
            "plt.axhline(y=pi_stat[2], color=\"green\", linestyle=\"--\", alpha=0.4, label=\"Hội tụ At-risk\")\n",
            "plt.title(\"Đồ thị hội tụ xác suất trạng thái Chuỗi Markov qua 20 bước\")\n",
            "plt.xlabel(\"Bước mô phỏng (Tuần k)\")\n",
            "plt.ylabel(\"Xác suất trạng thái\")\n",
            "plt.grid(True, linestyle=\":\", alpha=0.6)\n",
            "plt.legend()\n",
            "plt.tight_layout()\n",
            "plt.show()"
        ]
    },

    # -------------------------------------------------------------
    # SECTION 7: PHẦN E
    # -------------------------------------------------------------
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 7. PHẦN E: TỐI ƯU HÓA PHÂN BỔ NGUỒN LỰC HỖ TRỢ HỌC TẬP\n",
            "\n",
            "Mục tiêu của Phần E là vận dụng các công cụ toán tối ưu hóa vào bài toán phân bổ nguồn lực trợ giảng/mentor một cách khoa học:\n",
            "1. Bài toán Quy hoạch số nguyên nhị phân (Binary Integer Programming - BIP) giải bằng thư viện PuLP nhằm tối đa hóa điểm cải thiện học tập dưới ràng buộc ngân sách thời gian.\n",
            "2. Mô hình Luồng cực đại (Max-Flow) trên Đồ thị hai phía (Bipartite Matching) giải bằng thuật toán Edmonds-Karp nhằm tìm phương án ghép cặp sinh viên - mentor tối ưu và phát hiện nút cổ chai (Min-Cut)."
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 7.1. E.1 - Quy hoạch tuyến tính số nguyên nhị phân (BIP - PuLP)\n",
            "\n",
            "* Biến quyết định nhị phân:\n",
            "$$x_{ij} \\in \\{0, 1\\} = \\begin{cases} 1 & \\text{nếu sinh viên } i \\text{ được phân bổ hình thức hỗ trợ } j \\\\ 0 & \\text{ngược lại} \\end{cases}$$\n",
            "* Hàm mục tiêu: Tối đa hóa tổng điểm hiệu quả can thiệp:\n",
            "$$\\max Z = \\sum_{i=1}^M \\sum_{j=1}^K c_{ij} x_{ij}$$\n",
            "Trong đó hệ số hiệu quả $c_{ij} = \\text{Urgency}_i \\times \\text{Effectiveness}_j$.\n",
            "* Các ràng buộc kỹ thuật:\n",
            "  1. Mỗi sinh viên nhận tối đa 1 hình thức hỗ trợ: $\\sum_{j=1}^K x_{ij} \\le 1, \\quad \\forall i$.\n",
            "  2. Tổng ngân sách thời gian không vượt quá giới hạn cho phép: $\\sum_{i=1}^M \\sum_{j=1}^K h_j x_{ij} \\le B$.\n",
            "\n",
            "> **HƯỚNG DẪN TÍNH TAY & THAY SỐ KIỂM TRA ĐIỂM TỐI ƯU $Z^*$:**\n",
            ">\n",
            "> **1. Nguồn gốc từng tham số lấy ở đâu và bằng bao nhiêu:**\n",
            "> * **Tập sinh viên:** Chọn $12$ sinh viên có điểm nguy cơ cao nhất từ `df_clean` (đều có mức khẩn cấp $\\text{Urgency} = 2.0$).\n",
            "> * **Hình thức hỗ trợ & chi phí:**\n",
            ">   * `One-to-one support`: Điểm hiệu quả $e_1 = 10$, chi phí $h_1 = 4$ giờ.\n",
            ">   * `Lab tutoring`: Điểm hiệu quả $e_2 = 8$, chi phí $h_2 = 2$ giờ.\n",
            ">   * `Workshop review`: Điểm hiệu quả $e_3 = 6$, chi phí $h_3 = 1$ giờ.\n",
            ">   * `Online mentoring`: Điểm hiệu quả $e_4 = 4$, chi phí $h_4 = 1$ giờ.\n",
            "> * **Ngân sách tối đa:** $B = 24$ giờ mentor.\n",
            ">\n",
            "> **2. Công thức sau khi đã thay số theo phương án tối ưu:**\n",
            "> * Phân bổ nghiệm tối ưu tìm được bởi PuLP Solver:\n",
            ">   * $1$ sinh viên được hỗ trợ kèm 1-1 (`One-to-one`): đóng góp điểm $1 \\times (2.0 \\times 10) = 20.0$, chi phí $1 \\times 4 = 4$ giờ.\n",
            ">   * $8$ sinh viên được phụ đạo thực hành (`Lab tutoring`): đóng góp điểm $8 \\times (2.0 \\times 8) = 128.0$, chi phí $8 \\times 2 = 16$ giờ.\n",
            ">   * $3$ sinh viên được phụ đạo ôn tập (`Workshop review`): đóng góp điểm $3 \\times (2.0 \\times 6) = 36.0$, chi phí $3 \\times 1 = 3$ giờ.\n",
            "> * **Tổng ngân sách thời gian sử dụng:**\n",
            ">   $$\\sum h_j x_{ij} = 4 + 16 + 3 = 23 \\text{ giờ} \\le 24 \\text{ giờ (Thỏa mãn ràng buộc)}$$\n",
            "> * **Tổng điểm cải thiện cực đại $Z^*$:**\n",
            ">   $$Z^* = 20.0 + 128.0 + 36.0 = 184.0$$\n",
            ">\n",
            "> **3. Nhận xét kết quả:**\n",
            "> * Giá trị tính tay $Z^* = 184.0$ trùng khớp $100\\%$ với hàm mục tiêu tối ưu mà Solver CBC của PuLP tìm được.\n",
            "> * Toàn bộ **$12 / 12$ sinh viên nguy cơ cao** đều được hỗ trợ can thiệp, tiết kiệm được $1$ giờ ngân sách dự phòng ($23 / 24$ giờ)."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "mentors_file = os.path.join(data_dir, \"mentors.csv\")\n",
            "capacity_file = os.path.join(data_dir, \"support_capacity.csv\")\n",
            "lp_summary, df_lp_alloc = solve_mentor_allocation_lp(df_clean, mentors_file, capacity_file, top_n_students=12, total_budget=24)\n",
            "\n",
            "print(\"KẾT QUẢ TỐI ƯU HÓA QUY HOẠCH SỐ NGUYÊN (PuLP BIP):\")\n",
            "print(f\"- Trạng thái giải tối ưu: {lp_summary['Status']}\")\n",
            "print(f\"- Tổng điểm cải thiện kỳ vọng cực đại (Optimal Z*): {lp_summary['Optimal_Score']}\")\n",
            "print(f\"- Thời lượng mentor sử dụng: {lp_summary['Total_Cost_Used']} / {lp_summary['Total_Budget']} giờ\")\n",
            "print(f\"- Số sinh viên nhận hỗ trợ: {lp_summary['Students_Supported']} / {lp_summary['Total_Considered']} sinh viên\")\n",
            "\n",
            "print(\"\\nDANH SÁCH PHÂN BỔ CHI TIẾT TỪNG SINH VIÊN:\")\n",
            "print(df_lp_alloc[[\"student_id\", \"Mức độ khẩn cấp\", \"Hình thức hỗ trợ phân bổ\", \"Chi phí (giờ)\"]].to_string(index=False))\n",
            "\n",
            "# Lưu kết quả\n",
            "lp_csv = os.path.join(tables_dir, \"mentor_allocation_lp.csv\")\n",
            "df_lp_alloc.to_csv(lp_csv, index=False, encoding=\"utf-8-sig\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 7.2. E.2 - Mạng Luồng Cực Đại (Max-Flow) & Ghép cặp Đồ thị Hai phía\n",
            "\n",
            "* Biến đổi bài toán ghép cặp sinh viên - mentor thành mạng luồng có hướng $G' = (V', E')$:\n",
            "  * Đỉnh phát nguồn $s$ kết nối đến từng sinh viên cần hỗ trợ với dung lượng $c(s, u_i) = 1$.\n",
            "  * Sinh viên $u_i$ kết nối đến mentor $m_j$ tương thích môn học với dung lượng $c(u_i, m_j) = 1$.\n",
            "  * Mỗi mentor $m_j$ kết nối đến đỉnh đích $t$ với dung lượng $c(m_j, t) = \\text{Capacity}_j$ (số lượng sinh viên tối đa mentor có thể nhận).\n",
            "* Áp dụng định lý Lát cắt hẹp nhất - Luồng cực đại (Max-Flow Min-Cut Theorem):\n",
            "$$\\text{Max Flow} = \\text{Min Cut Capacity}$$\n",
            "* Nhận diện nút cổ chai (Bottleneck): Các cạnh đạt trạng thái bão hòa dung lượng ($f(e) = c(e)$) là giới hạn năng lực tiếp nhận của hệ thống trợ giảng."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "mf_summary, df_matched, G_flow = solve_bipartite_max_flow(df_clean, mentors_file, num_students=10)\n",
            "\n",
            "print(\"KẾT QUẢ GIẢI BÀI TOÁN LUỒNG CỰC ĐẠI GHÉP CẶP MENTOR:\")\n",
            "print(f\"- Giá trị Luồng cực đại (Max Flow): {mf_summary['Max_Flow_Value']}\")\n",
            "print(f\"- Số sinh viên ghép cặp thành công: {mf_summary['Successful_Matches']} / {mf_summary['Total_Students']}\")\n",
            "print(f\"- Dung lượng lát cắt nhỏ nhất (Min-Cut): {mf_summary['Min_Cut_Value']}\")\n",
            "\n",
            "print(\"\\nDANH SÁCH GHÉP CẶP SINH VIÊN - MENTOR:\")\n",
            "print(df_matched.to_string(index=False))\n",
            "\n",
            "print(\"\\nCÁC CẠNH BỊ BÃO HÒA DUNG LƯỢNG (BOTTLE-NECK / MIN-CUT):\\n\")\n",
            "for u, v, cap in mf_summary[\"Bottleneck_Edges\"]:\n",
            "    print(f\"  * Cạnh {u} -> {v}: Dung lượng bão hòa = {cap}\")\n",
            "\n",
            "# Lưu kết quả bảng ghép cặp\n",
            "flow_csv = os.path.join(tables_dir, \"bipartite_max_flow.csv\")\n",
            "df_matched.to_csv(flow_csv, index=False, encoding=\"utf-8-sig\")"
        ]
    },

    # -------------------------------------------------------------
    # SECTION 8: TỔNG KẾT TOÀN DỰ ÁN
    # -------------------------------------------------------------
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 8. TỔNG KẾT DỰ ÁN SMARTEDU AI (GIAI ĐOẠN 1 & GIAI ĐOẠN 2)\n",
            "\n",
            "Dự án SmartEdu AI đã hoàn thành toàn diện $100\\%$ tất cả các yêu cầu toán học và công nghệ của đồ án ITA201:\n",
            "\n",
            "1. **Giai đoạn 1 (Nền tảng Đại số tuyến tính, Tổ hợp & PCA):**\n",
            "   * Tiền xử lý dữ liệu chuẩn hóa từ $4.424$ hồ sơ sinh viên, làm sạch missing bằng trung vị, mã hóa thứ bậc.\n",
            "   * Thiết lập ma trận đặc trưng $X$, vector nhãn $y$, tính toán điểm rủi ro qua tích vô hướng $s = Xw$ và so sánh chuẩn khoảng cách $L_1, L_2$.\n",
            "   * Áp dụng đại số tổ hợp $C(8, 3) = 56$ tổ hợp để Grid Search bộ 3 đặc trưng tối ưu; phân tích tương quan và giảm chiều dữ liệu bằng PCA (giữ lại 4 PCs giải thích $80.19\\%$ phương sai), chứng minh mô hình Decision Tree sau PCA duy trì hiệu năng cao ($F1 = 78.43\\%$) trong khi giảm một nửa số chiều.\n",
            "\n",
            "2. **Giai đoạn 2 (Xác suất, Đồ thị & Tối ưu hóa can thiệp):**\n",
            "   * Phân tích xác suất có điều kiện hai chiều, kiểm chứng định lý Bayes và huấn luyện mô hình Gaussian Naive Bayes đạt F1-Score $69.89\\%$.\n",
            "   * Định lượng độ bất định thông tin qua Shannon Entropy và Information Gain, xác định `attendance_bin` ($IG = 0.3383$ bit) là đặc trưng phân loại mang tính quyết định.\n",
            "   * Xây dựng mạng lưới quan hệ sinh viên với $1.128$ đỉnh, $1.500$ cạnh, phân tích liên thông qua BFS/DFS và mô hình hóa quá trình chuyển dịch trạng thái học tập qua Chuỗi Markov 20 bước với phân phối dừng $\\pi^* = [34.57\\%, 35.80\\%, 29.63\\%]$.\n",
            "   * Ứng dụng thành công Quy hoạch số nguyên nhị phân PuLP phân bổ mentor đạt điểm tối ưu $Z^* = 184.0$ (hỗ trợ $12/12$ sinh viên) và thuật toán Max-Flow ghép cặp hoàn hảo $10/10$ sinh viên vào đúng chuyên môn của mentor.\n",
            "\n",
            "Toàn bộ mã nguồn, dữ liệu, bảng số liệu và báo cáo chi tiết đã được đồng bộ hóa hoàn chỉnh trong hệ sinh thái SmartEdu AI."
        ]
    }
]

# Combine Phase 1 + Phase 2
nb["cells"] = cells_phase1 + cells_phase2

# Save updated notebook
with open(nb_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, ensure_ascii=False, indent=2)

print(f"Updated notebook successfully! Total cells now: {len(nb['cells'])}")
