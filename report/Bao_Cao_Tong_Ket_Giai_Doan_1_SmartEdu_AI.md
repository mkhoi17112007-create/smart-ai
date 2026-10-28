# TRƯỜNG CAO ĐẲNG FPT POLYTECHNIC
## KHOA CÔNG NGHỆ THÔNG TIN

---

# BÁO CÁO TỔNG KẾT GIAI ĐOẠN 1 DỰ ÁN SMARTEDU AI
### HỆ THỐNG PHÂN TÍCH HỌC TẬP VÀ DỰ BÁO SINH VIÊN NGUY CƠ RỦI RO
**Nền tảng Dữ liệu, Toán học cho Học máy và Phân tích Giảm chiều PCA**

| Thông tin đồ án | Chi tiết |
|:---|:---|
| **Tên đồ án / Dự án:** | SmartEdu AI — Hệ sinh thái Cảnh báo Nguy cơ & Hỗ trợ Cá nhân hóa (Giai đoạn 1) |
| **Môn học ứng dụng:** | ITA201 — Toán cho học máy (Mathematics for Machine Learning) |
| **Tập dữ liệu khảo sát:** | Kaggle Predict Students Dropout and Academic Success (4.424 sinh viên, 10 thuộc tính) |

**DANH SÁCH THÀNH VIÊN NHÓM THỰC HIỆN:**

| STT | Họ và tên sinh viên | Mã số sinh viên | Vai trò trong nhóm |
|:---:|:---|:---:|:---|
| 1 | **Nguyễn Thanh Hoài** | **PS47905** | **Trưởng nhóm / Project Manager** |
| 2 | Nguyễn Duy Liêm | PS47845 | Data Engineer |
| 3 | Nguyễn Minh Khôi | PS48256 | Data Analyst |
| 4 | Vũ Quang Khải | PS48224 | AI / Machine Learning Researcher |

**TP. HỒ CHÍ MINH — THÁNG 10/2026**

---

### NHẬN XÉT CỦA GIẢNG VIÊN HƯỚNG DẪN
.................................................................................................................................................................................
.................................................................................................................................................................................
.................................................................................................................................................................................
.................................................................................................................................................................................

**Giáo viên hướng dẫn ký, ghi rõ họ tên:** ___________________________

---

### NHẬN XÉT CỦA HỘI ĐỒNG PHẢN BIỆN
.................................................................................................................................................................................
.................................................................................................................................................................................
.................................................................................................................................................................................
.................................................................................................................................................................................

**HĐ phản biện ký, ghi rõ họ tên:** ___________________________

---

# MỤC LỤC TỔNG THỂ

* **CHƯƠNG 1. PHÂN TÍCH Ý TƯỞNG VÀ BÀI TOÁN NGHIÊN CỨU**
  * 1.1. Bối cảnh dự án SmartEdu AI
  * 1.2. Bài toán đặt ra trong môi trường giáo dục
  * 1.3. Phân tích mô hình SWOT
  * 1.4. Mục tiêu nghiên cứu của Giai đoạn 1
  * 1.5. Giới thiệu Dataset và Ngăn xếp công nghệ
* **CHƯƠNG 2. XÂY DỰNG PIPELINE VÀ TIỀN XỬ LÝ DỮ LIỆU**
  * 2.1. Dataset sử dụng (Kaggle 4.424 bản ghi)
  * 2.2. Cấu trúc thuộc tính và phân loại biến số
  * 2.3. Quy trình làm sạch dữ liệu khuyết thiếu bằng Median
  * 2.4. Mã hóa Ordinal Encoding
  * 2.5. Toàn bộ Pipeline 5 bước thực thi
* **CHƯƠNG 3. NỀN TẢNG DỮ LIỆU VÀ TOÁN HỌC (PHẦN A)**
  * 3.1. Khởi tạo Project và cấu trúc Repository
  * 3.2. Ma trận đặc trưng X và Vector nhãn y
  * 3.3. Áp dụng công thức tính tay phép nhân ma trận s = X * w
  * 3.4. Áp dụng công thức tính tay StandardScaler, chuẩn Norm L1, L2 và khoảng cách hình học
  * 3.5. Áp dụng công thức tính tay Đại số tổ hợp C(8, 3) và không gian Grid Search
  * 3.6. Tổng kết nghiệm thu kỹ thuật Phần A
* **CHƯƠNG 4. PHÂN TÍCH NÂNG CAO VÀ MÔ HÌNH HÓA (PHẦN B)**
  * 4.1. Phân tích ma trận tương quan Heatmap và đa cộng tuyến
  * 4.2. Áp dụng công thức tính tay tỷ lệ phương sai và chọn Component PCA
  * 4.3. Trực quan hóa không gian 2D (PC1 vs PC2)
  * 4.4. Hệ số tải PCA Loadings và ý nghĩa nghiệp vụ
  * 4.5. Huấn luyện mô hình Decision Tree và đánh giá ma trận nhầm lẫn
  * 4.6. Phân tích đánh đổi thông tin (Trade-off)
* **CHƯƠNG 5. QUẢN TRỊ DỰ ÁN VÀ PHỐI HỢP NHÓM**
  * 5.1. Phân chia vai trò và nhiệm vụ (Team roles)
  * 5.2. Kế hoạch và tiến độ triển khai Agile/Scrum
  * 5.3. Quản lý mã nguồn trên Git/GitHub
  * 5.4. Quy tắc cộng tác và đạo đức nghề nghiệp
* **CHƯƠNG 6. TỔNG KẾT VÀ HƯỚNG PHÁT TRIỂN GIAI ĐOẠN 2**
  * 6.1. Những kết quả nổi bật nhóm đã đạt được
  * 6.2. Điểm mạnh và hạn chế còn tồn tại
  * 6.3. Bảng kiểm toán tiêu chí nghiệm thu Giai đoạn 1 (Checklist 11/11 PASS)
  * 6.4. Kế hoạch thực hiện Giai đoạn 2
* **PHỤ LỤC TỔNG HỢP**
  * Phụ lục A: Danh mục Deliverables và Output kỹ thuật
  * Phụ lục B: Bảng tra cứu các công thức toán học áp dụng

---

# CHƯƠNG 1. PHÂN TÍCH Ý TƯỞNG VÀ BÀI TOÁN NGHIÊN CỨU

### 1.1. Bối cảnh dự án SmartEdu AI
Trong thời đại chuyển đổi số giáo dục đại học và cao đẳng, việc theo dõi định lượng quá trình học tập của hàng ngàn sinh viên là thách thức lớn. Nếu chỉ căn cứ vào điểm thi kết thúc học phần, các can thiệp hỗ trợ sẽ quá muộn. Dự án SmartEdu AI được thiết kế nhằm xây dựng một hệ thống phân tích học tập (Learning Analytics) giúp phát hiện sớm các sinh viên có nguy cơ bỏ học hoặc rớt môn (`high_risk`), từ đó đưa ra cảnh báo kịp thời.

### 1.2. Bài toán đặt ra trong môi trường giáo dục
1. **Chuyển đổi dữ liệu học tập thô sang không gian số chuẩn:** Chuẩn hóa các biến điểm số, chuyên cần, hành vi tương tác trực tuyến LMS và nhân khẩu học.
2. **Định lượng hóa rủi ro học tập bằng toán học:** Ứng dụng các phép toán đại số tuyến tính (tích ma trận, vector trọng số, khoảng cách hình học $L_1, L_2$) để tính toán chỉ số rủi ro minh bạch.
3. **Giảm chiều dữ liệu và triệt tiêu đa cộng tuyến:** Sử dụng kỹ thuật Phân tích Thành phần chính (PCA) để nén không gian đặc trưng nhưng vẫn bảo toàn tối thiểu 80% phương sai thông tin.

### 1.3. Phân tích mô hình SWOT
* **Điểm mạnh (Strengths):** Sử dụng tập dữ liệu thực tế lớn từ Kaggle (4.424 sinh viên), thuật toán toán học minh bạch, có kiểm chứng tính tay step-by-step.
* **Điểm yếu (Weaknesses):** Chưa tích hợp dữ liệu chuỗi thời gian chi tiết theo từng tuần học; các thành phần chính PCA mang tính trừu tượng cần bảng loadings để giải thích.
* **Cơ hội (Opportunities):** Dễ dàng mở rộng sang các hệ thống LMS lớn như Moodle, Canvas; tạo tiền đề cho Giai đoạn 2 phát triển mạng lưới đồ thị và mô hình xác suất Naive Bayes.
* **Thách thức (Threats):** Xử lý sự mất cân bằng nhẹ của các trường hợp cá biệt và tối ưu hóa thời gian tính toán khi mở rộng sang hàng chục ngàn sinh viên.

### 1.4. Mục tiêu nghiên cứu của Giai đoạn 1
* Làm sạch và chuẩn hóa toàn bộ 4.424 bản ghi của tập dữ liệu Kaggle.
* Hiện thực hóa trọn vẹn các phép toán Đại số tuyến tính cơ sở (Phần A).
* Triển khai thuật toán PCA giảm 50% số chiều và so sánh mô hình Decision Tree trước vs sau PCA (Phần B).
* Đảm bảo 100% các tiêu chí kỹ thuật trong bảng kiểm nghiệm thu (11/11 PASS).

---

# CHƯƠNG 2. XÂY DỰNG PIPELINE VÀ TIỀN XỬ LÝ DỮ LIỆU

### 2.1. Dataset sử dụng
Dự án sử dụng bộ dữ liệu chuẩn quốc tế từ Kaggle: `Predict Students Dropout and Academic Success` (gốc gồm 4.424 bản ghi và 35 thuộc tính). Dữ liệu được trích xuất và chuẩn hóa thành tệp `data/students.csv` gồm 10 thuộc tính cốt lõi.

### 2.2. Cấu trúc thuộc tính và phân loại biến số
| STT | Tên cột đặc trưng | Kiểu dữ liệu | Miền giá trị | Ý nghĩa thực tế trong SmartEdu AI |
|:---:|:---|:---:|:---:|:---|
| 1 | `student_id` | Chuỗi | `SV0001` - `SV4424` | Mã định danh duy nhất của sinh viên |
| 2 | `attendance_rate` | Số thực | [0.50, 1.00] | Tỷ lệ chuyên cần học tập trên lớp |
| 3 | `quiz_avg` | Số thực | [0.0, 10.0] | Điểm kiểm tra trắc nghiệm định kỳ |
| 4 | `lab_avg` | Số thực | [0.0, 10.0] | Điểm thực hành thí nghiệm HK1 |
| 5 | `assignment_score` | Số thực | [0.0, 10.0] | Điểm bài tập lớn/tiểu luận HK2 |
| 6 | `self_study_hours` | Số thực | [1.0, 15.0] | Số giờ tự học mỗi tuần |
| 7 | `late_submissions` | Số nguyên | [0, 10] | Số lần nộp bài trễ hạn quy định |
| 8 | `video_views` | Số nguyên | [2, 50] | Số lượt tương tác bài giảng trên LMS |
| 9 | `participation_level`| Phân loại | Thấp, TB, Cao | Mức độ tích cực tham gia hoạt động |
| 10 | `risk_label` | Nhãn mục tiêu | low / high_risk | Nhãn phân loại nguy cơ học tập |

### 2.3. Quy trình làm sạch dữ liệu missing bằng Median
Nhóm phát hiện 40 giá trị khuyết thiếu (20 ở `quiz_avg`, 20 ở `self_study_hours`). Nhóm áp dụng phương pháp điền Trung vị (Median Imputation) vì trung vị có tính kháng nhiễu cực tốt trước các giá trị ngoại lai (outliers):
$$\text{quiz\_avg}_{\text{median}} = 2.00, \quad \text{self\_study\_hours}_{\text{median}} = 9.10$$
Sau bước xử lý, toàn bộ 4.424 dòng đều đạt trạng thái sạch hoàn hảo (0 missing values).

### 2.4. Mã hóa Ordinal Encoding
* `participation_level`: Thấp $\to 0$, Trung bình $\to 1$, Cao $\to 2$.
* `risk_label`: low_risk $\to 0$, high_risk $\to 1$.

---

# CHƯƠNG 3. NỀN TẢNG DỮ LIỆU VÀ TOÁN HỌC (PHẦN A)

### 3.1. Khởi tạo Project và cấu trúc Repository
Dự án được cấu trúc module hóa chuyên nghiệp:
* `data/`: Lưu trữ dataset thô và dataset sạch.
* `src/`: Các module mã nguồn xử lý độc lập (`data_processing.py`, `linear_algebra.py`, `pca_analysis.py`).
* `notebooks/`: Sổ tay thực nghiệm `smartedu_assignment.ipynb`.
* `outputs/`: Lưu trữ bảng số liệu CSV và đồ thị PNG.

### 3.2. Ma trận đặc trưng X và Vector nhãn y
Tách 8 thuộc tính số vào Ma trận đặc trưng $X \in \mathbb{R}^{4424 \times 8}$ và Vector nhãn $y \in \mathbb{R}^{4424}$. Cột `student_id` được tách riêng làm khóa định danh, không đưa vào ma trận tính toán để tránh thiên lệch giả tạo.

---

### 3.3. Áp dụng công thức tính tay phép nhân ma trận $s = X \cdot w$

#### 1. Công thức toán học tổng quát:
$$s_i = \sum_{j=1}^8 X_{ij} w_j$$

#### 2. Nguồn gốc từng tham số lấy ở đâu và bằng bao nhiêu:
* **Tham số $X_{ij}$ (Ma trận đặc trưng $X$):** Lấy trực tiếp từ bảng dữ liệu sạch `data/students.csv` tại dòng sinh viên thứ $i$ và cột đặc trưng thứ $j$:
  * **Sinh viên `SV0001` ($i=1$):**
    $X_{1,1} = 0.50$ (`attendance_rate`) | $X_{1,2} = 2.00$ (`quiz_avg`) | $X_{1,3} = 0.00$ (`lab_avg`) | $X_{1,4} = 0.00$ (`assignment_score`)
    $X_{1,5} = 9.10$ (`self_study_hours`) | $X_{1,6} = 0$ (`late_submissions`) | $X_{1,7} = 5$ (`video_views`) | $X_{1,8} = 1$ (`participation_encoded`: mức Trung bình)
  * **Sinh viên `SV0002` ($i=2$):**
    $X_{2,1} = 0.60$ (`attendance_rate`) | $X_{2,2} = 2.00$ (`quiz_avg`) | $X_{2,3} = 7.00$ (`lab_avg`) | $X_{2,4} = 6.80$ (`assignment_score`)
    $X_{2,5} = 8.60$ (`self_study_hours`) | $X_{2,6} = 0$ (`late_submissions`) | $X_{2,7} = 17$ (`video_views`) | $X_{2,8} = 1$ (`participation_encoded`: mức Trung bình)
* **Tham số $w$ (Vector trọng số $w \in \mathbb{R}^8$):** Lấy từ quy định nghiệp vụ trong module `src/linear_algebra.py`:
  $$w = [0.25, 0.30, 0.25, -0.20, -0.15, 0.40, -0.10, -0.30]^T$$
  Trong đó: $w_1 = 0.25, w_2 = 0.30, w_3 = 0.25, w_4 = -0.20, w_5 = -0.15, w_6 = 0.40, w_7 = -0.10, w_8 = -0.30$.

#### 3. Công thức sau khi đã thay số cụ thể từng bước (Step-by-step Substitution):
* **Tính điểm rủi ro $s_1$ cho sinh viên `SV0001`:**
  $$s_1 = X_{1,1} w_1 + X_{1,2} w_2 + X_{1,3} w_3 + X_{1,4} w_4 + X_{1,5} w_5 + X_{1,6} w_6 + X_{1,7} w_7 + X_{1,8} w_8$$
  $$s_1 = (0.50 \times 0.25) + (2.00 \times 0.30) + (0.00 \times 0.25) + (0.00 \times -0.20) + (9.10 \times -0.15) + (0 \times 0.40) + (5 \times -0.10) + (1 \times -0.30)$$
  $$s_1 = 0.1250 + 0.6000 + 0.0000 + 0.0000 - 1.3650 + 0.0000 - 0.5000 - 0.3000 = -1.4400$$

* **Tính điểm rủi ro $s_2$ cho sinh viên `SV0002`:**
  $$s_2 = X_{2,1} w_1 + X_{2,2} w_2 + X_{2,3} w_3 + X_{2,4} w_4 + X_{2,5} w_5 + X_{2,6} w_6 + X_{2,7} w_7 + X_{2,8} w_8$$
  $$s_2 = (0.60 \times 0.25) + (2.00 \times 0.30) + (7.00 \times 0.25) + (6.80 \times -0.20) + (8.60 \times -0.15) + (0 \times 0.40) + (17 \times -0.10) + (1 \times -0.30)$$
  $$s_2 = 0.1500 + 0.6000 + 1.7500 - 1.3600 - 1.2900 + 0.0000 - 1.7000 - 0.3000 = -2.1500$$

* **Nhận xét & Đối chiếu:** Kết quả tính tay $s_1 = -1.4400$ và $s_2 = -2.1500$ trùng khớp $100\%$ với kết quả in ra từ mô hình. Sinh viên `SV0001` có điểm rủi ro $-1.440$ cao hơn $-2.150$ của `SV0002` vì có điểm thực hành Lab và Assignment đều bằng 0 (chưa qua môn, thuộc nhóm `high_risk`).

---

### 3.4. Áp dụng công thức tính tay StandardScaler, chuẩn Norm L1, L2 và khoảng cách hình học

#### 1. Công thức toán học tổng quát:
* Chuẩn hóa Z-Score:
$$z_{ij} = \frac{X_{ij} - \mu_j}{\sigma_j}$$
* Khoảng cách Manhattan ($L_1$ Norm):
$$D_{L1}(v_1, v_2) = \sum_{j=1}^8 |v_{1,j} - v_{2,j}|$$
* Khoảng cách Euclidean ($L_2$ Norm):
$$D_{L2}(v_1, v_2) = \sqrt{\sum_{j=1}^8 (v_{1,j} - v_{2,j})^2}$$

#### 2. Nguồn gốc từng tham số lấy ở đâu và bằng bao nhiêu:
* **Tham số thống kê $\mu_j$ (Trung bình) và $\sigma_j$ (Độ lệch chuẩn):** Tính trên toàn bộ $4.424$ sinh viên thông qua `StandardScaler`:
  * `attendance_rate`: $\mu_1 = 0.8146, \sigma_1 = 0.2019$
  * `quiz_avg`: $\mu_2 = 2.5446, \sigma_2 = 1.5046$
  * `lab_avg`: $\mu_3 = 5.3200, \sigma_3 = 2.4217$
  * `assignment_score`: $\mu_4 = 5.1152, \sigma_4 = 2.6054$
  * `self_study_hours`: $\mu_5 = 10.1443, \sigma_5 = 2.3453$
  * `late_submissions`: $\mu_6 = 0.1377, \sigma_6 = 0.6908$
  * `video_views`: $\mu_7 = 21.5981, \sigma_7 = 8.3573$
  * `participation_encoded`: $\mu_8 = 0.8933, \sigma_8 = 0.7695$
* **Tọa độ vector sau chuẩn hóa:**
  * Vector `SV0001` ($v_1$): $[-1.5579, -0.3620, -2.1969, -1.9633, -0.4453, -0.1993, -1.9861, 0.1386]$
  * Vector `SV0002` ($v_2$): $[-1.0627, -0.3620, 0.6937, 0.6467, -0.6585, -0.1993, -0.5502, 0.1386]$
* **Hiệu số từng chiều $d_j = v_{1,j} - v_{2,j}$:**
  * $d_1 = -1.5579 - (-1.0627) = -0.4952 \implies |d_1| = 0.4952, d_1^2 = 0.2452$
  * $d_2 = -0.3620 - (-0.3620) = 0.0000 \implies |d_2| = 0.0000, d_2^2 = 0.0000$
  * $d_3 = -2.1969 - 0.6937 = -2.8906 \implies |d_3| = 2.8906, d_3^2 = 8.3554$
  * $d_4 = -1.9633 - 0.6467 = -2.6100 \implies |d_4| = 2.6100, d_4^2 = 6.8121$
  * $d_5 = -0.4453 - (-0.6585) = 0.2132 \implies |d_5| = 0.2132, d_5^2 = 0.0455$
  * $d_6 = -0.1993 - (-0.1993) = 0.0000 \implies |d_6| = 0.0000, d_6^2 = 0.0000$
  * $d_7 = -1.9861 - (-0.5502) = -1.4359 \implies |d_7| = 1.4359, d_7^2 = 2.0617$
  * $d_8 = 0.1386 - 0.1386 = 0.0000 \implies |d_8| = 0.0000, d_8^2 = 0.0000$

#### 3. Công thức sau khi đã thay số tính khoảng cách chi tiết:
* **Khoảng cách Manhattan ($L_1$ Norm):**
  $$D_{L1}(v_1, v_2) = 0.4952 + 0.0000 + 2.8906 + 2.6100 + 0.2132 + 0.0000 + 1.4359 + 0.0000 = 7.6449$$
* **Khoảng cách Euclidean ($L_2$ Norm):**
  $$D_{L2}(v_1, v_2) = \sqrt{0.2452 + 0.0000 + 8.3554 + 6.8121 + 0.0455 + 0.0000 + 2.0617 + 0.0000}$$
  $$D_{L2}(v_1, v_2) = \sqrt{17.5200} = 4.1857$$

* **Nhận xét:** Kết quả tính tay trùng khớp $100\%$ với code tự động ($D_{L1} = 7.6449, D_{L2} = 4.1857$). Sự khác biệt lớn nhất đến từ 2 môn học cốt lõi: Thực hành Lab ($d_3^2 = 8.3554$) và Bài tập lớn ($d_4^2 = 6.8121$).

---

### 3.5. Áp dụng công thức tính tay Đại số tổ hợp $C(8, 3)$ và không gian Grid Search

#### 1. Bài toán chọn 3 đặc trưng:
* Tham số: $n=8$ (8 đặc trưng gốc), $k=3$ (chọn 3 đặc trưng con).
* Công thức thay số chi tiết:
  $$C(8, 3) = \frac{8!}{3!(8-3)!} = \frac{8 \times 7 \times 6 \times 5!}{(3 \times 2 \times 1) \times 5!} = \frac{336}{6} = 56 \text{ tập đặc trưng}$$

#### 2. Bài toán không gian siêu tham số Grid Search:
* Tham số: $|learning\_rate| = 3$ ($[0.01, 0.05, 0.1]$), $|max\_depth| = 2$ ($[3, 5]$), $|n\_estimators| = 2$ ($[50, 100]$).
* Công thức thay số theo Nguyên lý nhân:
  $$N_{\text{Grid}} = 3 \times 2 \times 2 = 12 \text{ cấu hình thử nghiệm}$$

---

# CHƯƠNG 4. PHÂN TÍCH NÂNG CAO VÀ MÔ HÌNH HÓA (PHẦN B)

### 4.1. Phân tích ma trận tương quan Heatmap và đa cộng tuyến
Khảo sát ma trận tương quan Pearson giữa 8 đặc trưng phát hiện:
* `lab_avg` và `assignment_score` có tương quan rất cao ($r = 0.84$).
* Hiện tượng đa cộng tuyến này làm cho mô hình tuyến tính bị bất ổn định và lãng phí tài nguyên tính toán. Đây là cơ sở khoa học để áp dụng PCA.

### 4.2. Áp dụng công thức tính tay tỷ lệ phương sai và chọn Component PCA
* Tổng phương sai của 8 biến chuẩn hóa: $\sum_{j=1}^8 \lambda_j = 8.0000$.
* Giá trị 4 trị riêng lớn nhất: $\lambda_1 = 2.8569, \lambda_2 = 1.6258, \lambda_3 = 1.0673, \lambda_4 = 0.8655$.
* Thay số tính tỷ lệ phương sai:
  * $\text{Ratio}_1 = 2.8569 / 8.0 = 35.71\%$
  * $\text{Ratio}_2 = 1.6258 / 8.0 = 20.32\%$
  * $\text{Ratio}_3 = 1.0673 / 8.0 = 13.34\%$
  * $\text{Ratio}_4 = 0.8655 / 8.0 = 10.82\%$
* Thay số tính phương sai tích lũy 4 PCs:
  $$\text{Cumulative Variance}_4 = 35.71\% + 20.32\% + 13.34\% + 10.82\% = 80.19\% \ge 80.0\%$$
* Nhóm quyết định chọn giữ lại đúng $k=4$ thành phần chính (nén 50% số chiều nhưng giữ lại 80.19% thông tin).

### 4.3. Hệ số tải PCA Loadings và ý nghĩa nghiệp vụ
* **PC1 (35.71% phương sai):** Đóng vai trò là "Trục Năng lực Học thuật Tổng hợp" vì có hệ số tải dương rất mạnh ở `lab_avg` (+0.54), `assignment_score` (+0.53) và `attendance_rate` (+0.46).
* **PC2 (20.32% phương sai):** Đóng vai trò là "Trục Tự học và Tương tác số" vì có hệ số tải dương lớn ở `video_views` (+0.61) và `self_study_hours` (+0.58).

### 4.4. Huấn luyện mô hình Decision Tree và đánh giá ma trận nhầm lẫn
* Phân chia tập Train/Test theo tỷ lệ 80/20 (3.539 mẫu Train, 885 mẫu Test).
* Kết quả ma trận nhầm lẫn trên 4 thành phần PCA: $TP = 320, TN = 377, FP = 71, FN = 117$.
* Công thức thay số tính các chỉ số hiệu năng:
  * $\text{Accuracy} = \frac{320 + 377}{885} = \frac{697}{885} \approx 78.75\%$
  * $\text{Precision} = \frac{320}{320 + 71} = \frac{320}{391} \approx 81.84\%$
  * $\text{Recall} = \frac{320}{320 + 117} = \frac{320}{437} \approx 73.23\%$
  * $\text{F1-Score} = 2 \times \frac{0.8184 \times 0.7323}{0.8184 + 0.7323} \approx 77.29\%$

---

# CHƯƠNG 5. QUẢN TRỊ DỰ ÁN VÀ PHỐI HỢP NHÓM

### 5.1. Phân chia vai trò và nhiệm vụ (Team Roles & Responsibilities)
* **Nguyễn Thanh Hoài (Trưởng nhóm / Project Manager):** Điều phối tiến độ, lập kế hoạch Sprint, phụ trách toán học $s = Xw$, chuẩn hóa khoảng cách $L_1/L_2$, thuật toán PCA và viết báo cáo chính thức.
* **Nguyễn Duy Liêm (Data Engineer):** Chịu trách nhiệm toàn diện về Data Pipeline: chuyển đổi Kaggle dataset, xử lý Missing Value bằng Median, mã hóa Ordinal Encoding.
* **Nguyễn Minh Khôi (Data Analyst):** Thực hiện phân tích khám phá EDA, vẽ biểu đồ nhiệt Heatmap, biểu đồ phân tán PCA Scatter 2D và trích xuất bảng Loadings.
* **Vũ Quang Khải (AI/ML Researcher):** Huấn luyện mô hình Decision Tree trước vs sau PCA, tính toán Confusion Matrix và đo lường các chỉ số hiệu năng.

### 5.2. Kế hoạch và tiến độ triển khai Agile/Scrum
* **Sprint 1 (Tuần 1-2):** Khảo sát dữ liệu Kaggle, tiền xử lý, làm sạch và xây dựng pipeline $X, y$.
* **Sprint 2 (Tuần 3):** Hiện thực hóa đại số tuyến tính: $s = Xw$, chuẩn hóa StandardScaler, khoảng cách $L_1, L_2$, khảo sát tổ hợp $C(8, 3)$.
* **Sprint 3 (Tuần 4):** Triển khai PCA, trích xuất 4 PCs, vẽ biểu đồ Scatter và huấn luyện Decision Tree so sánh hiệu năng.
* **Sprint 4 (Tuần 5):** Hoàn thiện Jupyter Notebook pre-rendered, viết báo cáo tổng kết 7 chương và kiểm thử 11 tiêu chí nghiệm thu.

### 5.3. Quản lý mã nguồn trên Git/GitHub
* Nhánh `main`: Lưu trữ bản phát hành ổn định nhất.
* Nhánh tính năng: `feature/data-pipeline`, `feature/linear-algebra`, `feature/pca-evaluation`.
* Quy tắc Pull Request: Phải có ít nhất 1 thành viên review và kiểm thử trước khi merge vào main.

### 5.4. Đạo đức nghề nghiệp
* Cam kết số liệu thực nghiệm trung thực, trích xuất trực tiếp từ mã nguồn thực thi.
* Tôn trọng bảo mật dữ liệu sinh viên thông qua việc ẩn danh hóa bằng mã `SV0001` - `SV4424`.

---

# CHƯƠNG 6. TỔNG KẾT VÀ HƯỚNG PHÁT TRIỂN GIAI ĐOẠN 2

### 6.1. Những kết quả nổi bật nhóm đã đạt được
1. Xử lý thành công toàn bộ 4.424 bản ghi dữ liệu Kaggle thực tế, điền 40 giá trị khuyết thiếu bằng Median.
2. Xây dựng chỉ số rủi ro $s = Xw$ và đo lường khoảng cách hình học chuẩn xác với đầy đủ công thức tính tay thay số.
3. Giảm 50% số chiều không gian (từ 8 xuống 4 PCs) bằng PCA nhưng vẫn bảo toàn 80.19% phương sai.
4. Mô hình Decision Tree trên tập PCA đạt độ chuẩn xác Precision lên tới 81.84%, giúp nhà trường cảnh báo đúng đối tượng cần can thiệp.

### 6.2. Bảng kiểm toán tiêu chí nghiệm thu Giai đoạn 1 (Checklist 11/11 PASS)

| STT | Hạng mục Yêu cầu (ASM1.pdf) | Trạng thái | Ghi chú Kết quả Thực nghiệm |
|:---:|:---|:---:|:---|
| 1 | **Tên đề tài & Thành viên** | **PASS** | Nhóm 4 thành viên (Trưởng nhóm: Nguyễn Thanh Hoài). |
| 2 | **Mô tả bài toán** | **PASS** | Dự báo rủi ro sinh viên (`high_risk` vs `low_risk`). |
| 3 | **Nguồn dữ liệu Kaggle** | **PASS** | Bộ data Kaggle thực tế $4.424$ bản ghi sinh viên. |
| 4 | **Data Dictionary** | **PASS** | Bảng từ điển dữ liệu 10 thuộc tính chuẩn hóa. |
| 5 | **Làm sạch & Điền Missing** | **PASS** | Xử lý 40 missing values bằng phương pháp Median. |
| 6 | **Ma trận $X$ & Vector $y$** | **PASS** | Ma trận $X \in \mathbb{R}^{4424 \\times 8}$, Vector $y \in \mathbb{R}^{4424}$. |
| 7 | **Phép nhân $s = X \cdot w$** | **PASS** | Có hướng dẫn tính tay và thay số chi tiết từng bước. |
| 8 | **Chuẩn hóa & Norms $L_1/L_2$**| **PASS** | Có bảng thông số $\mu, \sigma$ và thay số tính $D_{L1}, D_{L2}$. |
| 9 | **Lý thuyết Tổ hợp $C(n,k)$** | **PASS** | Tính $C(8,3) = 56$ tập feature, Grid Search = 12 cấu hình. |
| 10 | **PCA & Biểu đồ $PC_1-PC_2$** | **PASS** | Chọn 4 PCs giải thích $80.19\%$ phương sai tích lũy. |
| 11 | **So sánh Mô hình PCA** | **PASS** | So sánh Decision Tree trước vs sau PCA (Precision $81.84\%$). |

### 6.3. Kế hoạch thực hiện Giai đoạn 2
* Xây dựng cấu trúc mạng lưới đồ thị tương tác sinh viên (Graph Analytics) với thuật toán BFS/DFS và thuật toán Google PageRank.
* Triển khai mô hình phân loại xác suất Naive Bayes kèm kỹ thuật làm mượt Laplace.
* Ứng dụng quy hoạch tuyến tính (Linear Programming) để phân bổ cố vấn học tập tối ưu cho các sinh viên nguy cơ cao.

---

# PHỤ LỤC TỔNG HỢP

### Phụ lục A: Danh mục Deliverables và Output Kỹ thuật
* `data/dataset.csv`: Dataset gốc Kaggle (4.424 dòng x 35 cột).
* `data/students.csv`: Dataset sạch (4.424 dòng x 10 cột).
* `notebooks/smartedu_assignment.ipynb`: Notebook thực nghiệm pre-rendered có đầy đủ công thức tính tay và nhận xét.
* `outputs/figures/correlation_heatmap.png`: Biểu đồ nhiệt tương quan 8 đặc trưng.
* `outputs/figures/pca_scatter_pc1_pc2.png`: Biểu đồ phân tán 2D PC1 vs PC2.
* `outputs/tables/pca_model_comparison.csv`: Bảng so sánh hiệu năng mô hình trước và sau PCA.
* `report/Bao_Cao_Tong_Ket_Giai_Doan_1_SmartEdu_AI.docx`: Tệp báo cáo Word chính thức nộp bài.

### Phụ lục B: Bảng tra cứu các công thức toán học áp dụng
| Tên giải thuật / Khái niệm | Công thức toán học | Ứng dụng trong dự án SmartEdu AI |
|:---|:---|:---|
| **Phép nhân ma trận-vector** | $s_i = \sum_{j=1}^p X_{ij} w_j$ | Tính điểm rủi ro tuyến tính ban đầu |
| **Chuẩn hóa Z-Score** | $z_{ij} = (X_{ij} - \mu_j) / \sigma_j$ | Đưa 8 đặc trưng về cùng phân phối $N(0, 1)$ |
| **Khoảng cách Manhattan ($L_1$)** | $D_{L1} = \sum \|x_j - z_j\|$ | Đo tổng độ lệch tuyệt đối giữa 2 sinh viên |
| **Khoảng cách Euclidean ($L_2$)** | $D_{L2} = \sqrt{\sum (x_j - z_j)^2}$ | Đo khoảng cách đường chim bay, tìm Top-k láng giềng |
| **Đại số tổ hợp** | $C(n, k) = \frac{n!}{k!(n-k)!}$ | Đếm số lượng tập con đặc trưng con |
| **Phương sai tích lũy PCA** | $\sum_{i=1}^k \lambda_i / \sum \lambda_j$ | Chọn lọc số chiều nén bảo toàn $\ge 80\%$ thông tin |
