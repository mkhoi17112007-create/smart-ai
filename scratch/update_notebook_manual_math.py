import json
import sys

def update_notebook():
    nb_path = r'c:\HOC_HANH\Mon dang hoc\ITA201\smartedu-ai\notebooks\smartedu_assignment.ipynb'
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    # 1. Update Cell 7 (Section 3.3 - s = X * w)
    nb['cells'][7]['source'] = [
        "### 3.3. A.2 - Biểu diễn Ma trận đặc trưng $X$, Vector nhãn $y$ và Phép nhân Ma trận $s = X \\cdot w$\n",
        "* Biểu diễn $4.424$ sinh viên thành Ma trận đặc trưng $X \\in \\mathbb{R}^{4424 \\times 8}$ và Vector nhãn $y \\in \\mathbb{R}^{4424}$.\n",
        "* Phép nhân ma trận-vector $s = X \\cdot w$ thể hiện tổ hợp tuyến tính các đặc trưng với vector trọng số giả định $w$:\n",
        "$$s_i = \\sum_{j=1}^8 X_{ij} w_j$$\n",
        "\n",
        "> **HƯỚNG DẪN TÍNH TAY & THAY SỐ CÔNG THỨC $s = X \\cdot w$ (MINH HỌA CHI TIẾT TỪNG THAM SỐ):**\n",
        ">\n",
        "> **1. Nguồn gốc từng tham số lấy ở đâu và bằng bao nhiêu:**\n",
        "> * **Tham số $X_{ij}$ (Ma trận đặc trưng $X$):** Lấy trực tiếp từ file dữ liệu đã làm sạch `data/students.csv` tại dòng sinh viên thứ $i$ và cột đặc trưng thứ $j$.\n",
        ">   * Với sinh viên `SV0001` ($i=1$): $X_{1,1}=0.50$ (`attendance_rate`), $X_{1,2}=2.00$ (`quiz_avg`), $X_{1,3}=0.00$ (`lab_avg`), $X_{1,4}=0.00$ (`assignment_score`), $X_{1,5}=9.10$ (`self_study_hours`), $X_{1,6}=0$ (`late_submissions`), $X_{1,7}=5$ (`video_views`), $X_{1,8}=1$ (`participation_encoded`: mức Trung bình).\n",
        ">   * Với sinh viên `SV0002` ($i=2$): $X_{2,1}=0.60$, $X_{2,2}=2.00$, $X_{2,3}=7.00$, $X_{2,4}=6.80$, $X_{2,5}=8.60$, $X_{2,6}=0$, $X_{2,7}=17$, $X_{2,8}=1$.\n",
        "> * **Tham số $w$ (Vector trọng số $w \\in \\mathbb{R}^8$):** Lấy từ quy định nghiệp vụ trong module `src/linear_algebra.py`:\n",
        ">   $$w = [0.25, 0.30, 0.25, -0.20, -0.15, 0.40, -0.10, -0.30]^T$$\n",
        ">   Trong đó: $w_1=0.25, w_2=0.30, w_3=0.25, w_4=-0.20, w_5=-0.15, w_6=0.40, w_7=-0.10, w_8=-0.30$.\n",
        ">\n",
        "> **2. Công thức sau khi đã thay số cụ thể từng bước:**\n",
        "> * **Đối với sinh viên `SV0001`:**\n",
        ">   $$s_1 = \\sum_{j=1}^8 X_{1,j} w_j = (0.50 \\times 0.25) + (2.00 \\times 0.30) + (0.00 \\times 0.25) + (0.00 \\times -0.20) + (9.10 \\times -0.15) + (0 \\times 0.40) + (5 \\times -0.10) + (1 \\times -0.30)$$\n",
        ">   $$s_1 = 0.1250 + 0.6000 + 0.0000 + 0.0000 - 1.3650 + 0.0000 - 0.5000 - 0.3000 = -1.4400$$\n",
        "> * **Đối với sinh viên `SV0002`:**\n",
        ">   $$s_2 = \\sum_{j=1}^8 X_{2,j} w_j = (0.60 \\times 0.25) + (2.00 \\times 0.30) + (7.00 \\times 0.25) + (6.80 \\times -0.20) + (8.60 \\times -0.15) + (0 \\times 0.40) + (17 \\times -0.10) + (1 \\times -0.30)$$\n",
        ">   $$s_2 = 0.1500 + 0.6000 + 1.7500 - 1.3600 - 1.2900 + 0.0000 - 1.7000 - 0.3000 = -2.1500$$\n",
        ">\n",
        "> **3. Nhận xét kết quả:** Giá trị tính tay ra $s_1 = -1.4400$ và $s_2 = -2.1500$ trùng khớp hoàn toàn $100\\%$ với kết quả ma trận $s = Xw$ in ra từ code máy tính bên dưới. Sinh viên `SV0001` có điểm nguy cơ $-1.440$ cao hơn $-2.150$ của `SV0002` vì có điểm thực hành Lab và Assignment đều bằng 0 (thuộc nhóm `high_risk`).\n"
    ]

    # 2. Update Cell 10 (Section 3.4 - StandardScaler, L1, L2)
    nb['cells'][10]['source'] = [
        "### 3.4. A.3 - Chuẩn hóa StandardScaler, chuẩn Vector Norm $L_1/L_2$ và Khoảng cách hình học\n",
        "* Chuẩn hóa ma trận đặc trưng bằng `StandardScaler` (mean=0, std=1):\n",
        "$$z_{ij} = \\frac{X_{ij} - \\mu_j}{\\sigma_j}$$\n",
        "* Công thức khoảng cách Euclidean ($L_2$ norm):\n",
        "$$D_{L2}(x, z) = \\sqrt{\\sum_{j=1}^n (x_j - z_j)^2}$$\n",
        "* Công thức khoảng cách Manhattan ($L_1$ norm):\n",
        "$$D_{L1}(x, z) = \\sum_{j=1}^n |x_j - z_j|$$\n",
        "* So sánh khoảng cách giữa 2 sinh viên cụ thể: `SV0001` và `SV0002`.\n",
        "\n",
        "> **HƯỚNG DẪN TÍNH TAY & THAY SỐ CÔNG THỨC KHOẢNG CÁCH $L_1, L_2$ (MINH HỌA CHI TIẾT TỪNG THAM SỐ):**\n",
        ">\n",
        "> **1. Nguồn gốc từng tham số lấy ở đâu và bằng bao nhiêu:**\n",
        "> * **Tham số thống kê $\\mu_j$ (Trung bình) và $\\sigma_j$ (Độ lệch chuẩn):** Được tính trên toàn bộ $4.424$ dòng dữ liệu thông qua `StandardScaler`:\n",
        ">   * `attendance_rate`: $\\mu_1 = 0.8146, \\sigma_1 = 0.2019$\n",
        ">   * `quiz_avg`: $\\mu_2 = 2.5446, \\sigma_2 = 1.5046$\n",
        ">   * `lab_avg`: $\\mu_3 = 5.3200, \\sigma_3 = 2.4217$\n",
        ">   * `assignment_score`: $\\mu_4 = 5.1152, \\sigma_4 = 2.6054$\n",
        ">   * `self_study_hours`: $\\mu_5 = 10.1443, \\sigma_5 = 2.3453$\n",
        ">   * `late_submissions`: $\\mu_6 = 0.1377, \\sigma_6 = 0.6908$\n",
        ">   * `video_views`: $\\mu_7 = 21.5981, \\sigma_7 = 8.3573$\n",
        ">   * `participation_encoded`: $\\mu_8 = 0.8933, \\sigma_8 = 0.7695$\n",
        "> * **Tọa độ vector sau khi chuẩn hóa $z = \\frac{X - \\mu}{\\sigma}$:**\n",
        ">   * Vector `SV0001` ($v_1$): $[-1.5579, -0.3620, -2.1969, -1.9633, -0.4453, -0.1993, -1.9861, 0.1386]$\n",
        ">   * Vector `SV0002` ($v_2$): $[-1.0627, -0.3620, 0.6937, 0.6467, -0.6585, -0.1993, -0.5502, 0.1386]$\n",
        "> * **Hiệu số từng chiều $d_j = v_{1,j} - v_{2,j}$:**\n",
        ">   * $d_1 = -1.5579 - (-1.0627) = -0.4952 \\implies |d_1| = 0.4952, d_1^2 = 0.2452$\n",
        ">   * $d_2 = -0.3620 - (-0.3620) = 0.0000 \\implies |d_2| = 0.0000, d_2^2 = 0.0000$\n",
        ">   * $d_3 = -2.1969 - 0.6937 = -2.8906 \\implies |d_3| = 2.8906, d_3^2 = 8.3554$\n",
        ">   * $d_4 = -1.9633 - 0.6467 = -2.6100 \\implies |d_4| = 2.6100, d_4^2 = 6.8121$\n",
        ">   * $d_5 = -0.4453 - (-0.6585) = 0.2132 \\implies |d_5| = 0.2132, d_5^2 = 0.0455$\n",
        ">   * $d_6 = -0.1993 - (-0.1993) = 0.0000 \\implies |d_6| = 0.0000, d_6^2 = 0.0000$\n",
        ">   * $d_7 = -1.9861 - (-0.5502) = -1.4359 \\implies |d_7| = 1.4359, d_7^2 = 2.0617$\n",
        ">   * $d_8 = 0.1386 - 0.1386 = 0.0000 \\implies |d_8| = 0.0000, d_8^2 = 0.0000$\n",
        ">\n",
        "> **2. Công thức sau khi đã thay số tính khoảng cách:**\n",
        "> * **Khoảng cách Manhattan ($L_1$ Norm):**\n",
        ">   $$D_{L1}(v_1, v_2) = \\sum_{j=1}^8 |v_{1,j} - v_{2,j}| = 0.4952 + 0.0000 + 2.8906 + 2.6100 + 0.2132 + 0.0000 + 1.4359 + 0.0000 = 7.6449$$\n",
        "> * **Khoảng cách Euclidean ($L_2$ Norm):**\n",
        ">   $$D_{L2}(v_1, v_2) = \\sqrt{\\sum_{j=1}^8 (v_{1,j} - v_{2,j})^2} = \\sqrt{0.2452 + 0.0000 + 8.3554 + 6.8121 + 0.0455 + 0.0000 + 2.0617 + 0.0000}$$\n",
        ">   $$D_{L2}(v_1, v_2) = \\sqrt{17.5200} = 4.1857$$\n",
        ">\n",
        "> **3. Nhận xét kết quả:** Kết quả tính tay ra $D_{L1} = 7.6449$ và $D_{L2} = 4.1857$ trùng khớp chính xác $100\\%$ với kết quả chạy tự động bên dưới. Khoảng cách lớn chủ yếu xuất phát từ sự chênh lệch vượt bậc ở điểm môn Thực hành ($d_3^2 = 8.3554$) và Bài tập lớn ($d_4^2 = 6.8121$).\n"
    ]

    # 3. Update Cell 13 (Section 3.5 - Combinatorics & Grid Search)
    nb['cells'][13]['source'] = [
        "### 3.5. A.4 - Đại số tổ hợp $C(n, k)$, Nguyên lý nhân và Lọc đặc trưng\n",
        "* Tính số tập hợp chọn $k=3$ đặc trưng từ $n=8$ đặc trưng:\n",
        "$$C(n, k) = \\frac{n!}{k!(n-k)!}$$\n",
        "* Kích thước không gian siêu tham số Grid Search theo nguyên lý nhân:\n",
        "$$N_{\\text{Grid}} = |P_1| \\times |P_2| \\times \\dots \\times |P_m|$$\n",
        "\n",
        "> **HƯỚNG DẪN TÍNH TAY & THAY SỐ CÔNG THỨC TỔ HỢP VÀ GRID SEARCH:**\n",
        ">\n",
        "> **1. Nguồn gốc tham số lấy ở đâu và bằng bao nhiêu:**\n",
        "> * **Bài toán chọn đặc trưng:**\n",
        ">   * $n = 8$: Tổng số 8 đặc trưng số học trong ma trận $X$.\n",
        ">   * $k = 3$: Kích thước tập đặc trưng con cần khảo sát theo đề bài.\n",
        "> * **Bài toán Grid Search:**\n",
        ">   * $|learning\\_rate| = 3$ giá trị thử nghiệm: $[0.01, 0.05, 0.1]$\n",
        ">   * $|max\\_depth| = 2$ giá trị thử nghiệm: $[3, 5]$\n",
        ">   * $|n\\_estimators| = 2$ giá trị thử nghiệm: $[50, 100]$\n",
        ">\n",
        "> **2. Công thức sau khi đã thay số cụ thể:**\n",
        "> * **Số tập hợp con 3 đặc trưng:**\n",
        ">   $$C(8, 3) = \\frac{8!}{3!(8-3)!} = \\frac{8 \\times 7 \\times 6 \\times 5!}{(3 \\times 2 \\times 1) \\times 5!} = \\frac{336}{6} = 56 \\text{ tập đặc trưng}$$\n",
        "> * **Số lượng cấu hình Grid Search:**\n",
        ">   $$N_{\\text{Grid}} = 3 \\times 2 \\times 2 = 12 \\text{ cấu hình thử nghiệm}$$\n",
        ">\n",
        "> **3. Nhận xét:** Kết quả tính tay $C(8, 3) = 56$ và $N_{\\text{Grid}} = 12$ hoàn toàn trùng khớp với kết quả thực thi code Python.\n"
    ]

    # 4. Update Cell 20 (Section 4.2 - PCA Variance & Components)
    nb['cells'][20]['source'] = [
        "### 4.2. B.2 - Thực hiện Thuật toán PCA và Lựa chọn số lượng Component tối ưu ($\\ge 80\\%$)\n",
        "* Thuật toán PCA tìm các **Vector riêng (Eigenvectors)** chỉ hướng biến thiên lớn nhất và **Trị riêng (Eigenvalues)** $\\lambda_j$ đo độ rộng phương sai.\n",
        "* Tỷ lệ phương sai giải thích từng Component:\n",
        "$$\\text{Ratio}_k = \\frac{\\lambda_k}{\\sum_{j=1}^p \\lambda_j}$$\n",
        "* Phương sai tích lũy của $k$ thành phần chính:\n",
        "$$\\text{Cumulative Variance}_k = \\sum_{i=1}^k \\text{Ratio}_i$$\n",
        "\n",
        "> **HƯỚNG DẪN TÍNH TAY & THAY SỐ CÔNG THỨC PHƯƠNG SAI TÍCH LŨY PCA:**\n",
        ">\n",
        "> **1. Nguồn gốc tham số lấy ở đâu và bằng bao nhiêu:**\n",
        "> * **Tổng phương sai:** Vì ma trận dữ liệu đã chuẩn hóa `StandardScaler` trên $8$ đặc trưng số, tổng phương sai (tổng các trị riêng) bằng chính số đặc trưng: $\\sum_{j=1}^8 \\lambda_j = 8.0000$.\n",
        "> * **Trị riêng của 4 thành phần chính đầu tiên:** Lấy từ phân rã ma trận hiệp phương sai:\n",
        ">   * $\\lambda_1 = 2.8569$ (PC1) | $\\lambda_2 = 1.6258$ (PC2) | $\\lambda_3 = 1.0673$ (PC3) | $\\lambda_4 = 0.8655$ (PC4)\n",
        ">\n",
        "> **2. Công thức sau khi đã thay số tính tỷ lệ phương sai:**\n",
        "> * $\\text{Ratio}_1 = \\frac{2.8569}{8.0000} = 0.3571 \\implies 35.71\\%$\n",
        "> * $\\text{Ratio}_2 = \\frac{1.6258}{8.0000} = 0.2032 \\implies 20.32\\%$\n",
        "> * $\\text{Ratio}_3 = \\frac{1.0673}{8.0000} = 0.1334 \\implies 13.34\\%$\n",
        "> * $\\text{Ratio}_4 = \\frac{0.8655}{8.0000} = 0.1082 \\implies 10.82\\%$\n",
        ">\n",
        "> **3. Công thức tính phương sai tích lũy 4 Components ($k=4$):**\n",
        "> $$\\text{Cumulative Variance}_4 = 35.71\\% + 20.32\\% + 13.34\\% + 10.82\\% = 80.19\\%$$\n",
        "> Vì $80.19\\% \\ge 80.0\\%$, việc giữ lại đúng $4$ thành phần chính vừa thỏa mãn chuẩn đề bài, vừa nén thành công $50\\%$ số chiều dữ liệu (từ 8 chiều xuống 4 chiều).\n"
    ]

    with open(nb_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)

    print("Successfully updated notebook with detailed step-by-step manual calculation breakdowns!")

if __name__ == '__main__':
    update_notebook()
