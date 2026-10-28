# TRƯỜNG CAO ĐẲNG FPT POLYTECHNIC
## KHOA CÔNG NGHỆ THÔNG TIN

---

# BÁO CÁO TỔNG KẾT TOÀN DIỆN DỰ ÁN SMARTEDU AI (GIAI ĐOẠN 1 & 2)
### HỆ THỐNG PHÂN TÍCH HỌC TẬP, DỰ BÁO SINH VIÊN NGUY CƠ RỦI RO VÀ TỐI ƯU HÓA CAN THIỆP GIÁO DỤC
**Nền tảng Toán học cho Học máy: Đại số tuyến tính, Tổ hợp, PCA, Xác suất Bayes, Entropy Shannon, Đồ thị, Chuỗi Markov & Quy hoạch tuyến tính**

| Thông tin đồ án | Chi tiết |
|:---|:---|
| **Tên đồ án / Dự án:** | SmartEdu AI — Hệ sinh thái Cảnh báo Nguy cơ & Hỗ trợ Cá nhân hóa (Toàn diện Giai đoạn 1 & 2) |
| **Môn học ứng dụng:** | ITA201 — Toán cho học máy (Mathematics for Machine Learning) |
| **Giảng viên hướng dẫn:** | Giảng viên Bộ môn CNTT — FPT Polytechnic |
| **Tập dữ liệu khảo sát:** | Kaggle Predict Students Dropout and Academic Success (4.424 sinh viên, 10 thuộc tính chuẩn hóa) |
| **Mạng lưới tương tác:** | 1.128 sinh viên, 1.500 liên kết tương tác học tập có hướng |
| **Đội ngũ Mentor hỗ trợ:** | 5 giảng viên/mentor chuyên môn, 4 hình thức can thiệp học tập |

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

# LỜI MỞ ĐẦU

Trong bối cảnh chuyển đổi số giáo dục đang diễn ra mạnh mẽ tại Việt Nam nói chung và tại Trường Cao đẳng FPT Polytechnic nói riêng, việc ứng dụng Trí tuệ nhân tạo (AI) và Khoa học dữ liệu (Data Science) vào công tác quản trị học tập không còn là xu hướng thử nghiệm mà đã trở thành yêu cầu cấp thiết. Hàng năm, một tỷ lệ không nhỏ sinh viên gặp khó khăn trong việc theo kịp tiến độ chương trình, dẫn đến kết quả học tập sa sút, trễ hạn nộp bài, vắng học và nghiêm trọng nhất là bỏ học giữa chừng.

Dự án **SmartEdu AI** được nhóm nghiên cứu hình thành và phát triển với mục tiêu giải quyết triệt để vấn đề trên. Không dừng lại ở việc áp dụng các mô hình học máy dạng "hộp đen" (black-box), SmartEdu AI được xây dựng dựa trên nền tảng toán học vững chắc xuyên suốt 5 phân hệ kiến thức cốt lõi của môn học **ITA201 - Toán cho học máy**:
1. **Phần A (Đại số tuyến tính & Tổ hợp):** Làm sạch dữ liệu, xây dựng ma trận đặc trưng $X$, vector nhãn $y$, tính toán điểm rủi ro tuyến tính $s = Xw$, chuẩn hóa vector $L_1/L_2$ và tổ hợp không gian tìm kiếm siêu tham số.
2. **Phần B (Phân tích thành phần chính PCA & Cây quyết định):** Phân tích ma trận tương quan, giảm số chiều đặc trưng từ 8 chiều xuống 4 chiều bảo toàn hơn $80\%$ lượng phương sai và so sánh hiệu năng mô hình phân loại.
3. **Phần C (Xác suất có điều kiện, Định lý Bayes & Entropy Shannon):** Đo lường xác suất rủi ro hai chiều, huấn luyện bộ phân loại Gaussian Naive Bayes và định lượng mức độ quan trọng của đặc trưng thông qua Information Gain.
4. **Phần D (Lý thuyết đồ thị & Chuỗi Markov):** Xây dựng mạng lưới xã hội học tập 1.128 sinh viên, duyệt BFS/DFS, khảo sát tính liên thông và mô hình hóa quá trình chuyển dịch trạng thái học tập qua Chuỗi Markov 20 bước với phân phối dừng dài hạn.
5. **Phần E (Tối ưu hóa phân bổ nguồn lực can thiệp):** Ứng dụng Quy hoạch số nguyên nhị phân (PuLP BIP) và Mạng luồng cực đại (Max-Flow Bipartite Matching) để tự động hóa việc ghép cặp sinh viên có nguy cơ cao với đội ngũ giảng viên/mentor phù hợp nhất.

Báo cáo này tổng kết toàn bộ quá trình nghiên cứu, thiết kế thuật toán, thực nghiệm mã nguồn và diễn giải toán học tính tay chi tiết của nhóm.

---

# MỤC LỤC TỔNG THỂ

* **CHƯƠNG 1. PHÂN TÍCH Ý TƯỞNG VÀ TỔNG QUAN DỰ ÁN SMARTEDU AI**
  * 1.1. Bối cảnh dự án SmartEdu AI
  * 1.2. Bài toán thực tiễn đặt ra trong môi trường giáo dục
  * 1.3. Phân tích mô hình SWOT của dự án
  * 1.4. Mục tiêu nghiên cứu tổng thể của Giai đoạn 1 & Giai đoạn 2
  * 1.5. Giới thiệu Dataset khảo sát và Ngăn xếp công nghệ triển khai
* **CHƯƠNG 2. XÂY DỰNG PIPELINE, TIỀN XỬ LÝ DỮ LIỆU VÀ XÂY DỰNG ĐẶC TRƯNG (PHẦN A.1)**
  * 2.1. Cấu trúc và quy trình chuyển đổi từ Kaggle Dataset (35 cột) sang SmartEdu Dataset (10 cột)
  * 2.2. Bảng mô tả chi tiết 10 đặc trưng dữ liệu học tập
  * 2.3. Quy trình làm sạch dữ liệu khuyết tật (Missing Values) bằng Trung vị (Median)
  * 2.4. Kỹ thuật mã hóa thứ bậc (Ordinal Encoding) cho đặc trưng định tính
* **CHƯƠNG 3. NỀN TẢNG TOÁN HỌC: ĐẠI SỐ TUYẾN TÍNH, CHUẨN KHOẢNG CÁCH VÀ TỔ HỢP (PHẦN A.2, A.3, A.4)**
  * 3.1. Thiết lập ma trận đặc trưng X và vector nhãn y
  * 3.2. Điểm rủi ro tuyến tính s = Xw và Phép nhân ma trận - vector
  * 3.3. Chuẩn hóa StandardScaler, Chuẩn Vector Norm L1, L2 và Khoảng cách hình học
  * 3.4. Lý thuyết tổ hợp C(n, k) và Không gian tìm kiếm tham số Grid Search
  * 3.5. Nhận xét nghiệm thu kỹ thuật Phần A
* **CHƯƠNG 4. PHÂN TÍCH THÀNH PHẦN CHÍNH (PCA) VÀ ĐÁNH GIÁ MÔ HÌNH PHÂN LOẠI (PHẦN B.1, B.2, B.3)**
  * 4.1. Ma trận tương quan Pearson (Heatmap) và hiện tượng đa cộng tuyến
  * 4.2. Cơ sở toán học của PCA: Ma trận hiệp phương sai, Trị riêng và Vector riêng
  * 4.3. Phân tích tỷ lệ phương sai giải thích và lựa chọn số lượng Principal Components
  * 4.4. Trực quan hóa không gian 2D (PC1 vs PC2) phân tách nhóm nguy cơ
  * 4.5. Huấn luyện và so sánh mô hình Decision Tree Trước vs Sau PCA
  * 4.6. Nhận xét nghiệm thu kỹ thuật Phần B
* **CHƯƠNG 5. MÔ HÌNH XÁC SUẤT, ĐỊNH LÝ BAYES VÀ LÝ THUYẾT THÔNG TIN (PHẦN C.1, C.2, C.3)**
  * 5.1. Bảng xác suất có điều kiện hai chiều và Kiểm chứng Định lý Bayes
  * 5.2. Huấn luyện Mô hình Gaussian Naive Bayes & Dự báo Xác suất
  * 5.3. Định lượng độ bất định qua Shannon Entropy & Độ tăng thông tin (Information Gain)
  * 5.4. Nhận xét nghiệm thu kỹ thuật Phần C
* **CHƯƠNG 6. LÝ THUYẾT ĐỒ THỊ MẠNG LƯỚI SINH VIÊN VÀ CHUỖI MARKOV DỰ BÁO HÀNH VI (PHẦN D.1, D.2, D.3)**
  * 6.1. Xây dựng Đồ thị có hướng quan hệ sinh viên & Biểu diễn ma trận kề
  * 6.2. Thuật toán duyệt BFS/DFS & Phân tích tính liên thông mạng lưới
  * 6.3. Mô hình Hóa Chuỗi Markov Dự báo Hành vi Học tập
  * 6.4. Nhận xét nghiệm thu kỹ thuật Phần D
* **CHƯƠNG 7. TỐI ƯU HÓA PHÂN BỔ NGUỒN LỰC HỖ TRỢ VÀ TỔNG KẾT DỰ ÁN (PHẦN E.1, E.2)**
  * 7.1. Bài toán Quy hoạch số nguyên nhị phân (PuLP BIP) phân bổ mentor
  * 7.2. Mạng Luồng Cực Đại (Max-Flow) & Ghép cặp Đồ thị hai phía
  * 7.3. Nhận xét nghiệm thu kỹ thuật Phần E
  * 7.4. Kết luận toàn diện dự án SmartEdu AI, Bài học kinh nghiệm & Đề xuất mở rộng

---

# CHƯƠNG 1. PHÂN TÍCH Ý TƯỞNG VÀ TỔNG QUAN DỰ ÁN SMARTEDU AI

### 1.1. Bối cảnh dự án SmartEdu AI
Trong môi trường đào tạo theo hình thức Blended Learning và tín chỉ linh hoạt tại Cao đẳng FPT Polytechnic, sinh viên được tiếp cận với nguồn học liệu số phong phú trên hệ thống quản lý học tập (LMS). Tuy nhiên, khối lượng bài tập thực hành (Labs), bài tập đồ án (Assignments) và bài kiểm tra tiến độ (Quizzes) liên tục đòi hỏi sinh viên phải có kỹ năng tự học cao và sự kỷ luật nghiêm ngặt. Khi sinh viên gặp khó khăn ban đầu mà không có sự hỗ trợ kịp thời, tình trạng nợ môn, trượt môn và nguy cơ thôi học sẽ tích lũy theo hiệu ứng quả cầu tuyết.

Dự án **SmartEdu AI** ra đời nhằm hiện đại hóa quy trình giám sát học tập, biến đổi dữ liệu nhật ký học tập rời rạc thành các thông tin cảnh báo thông minh, giúp giảng viên và ban đào tạo can thiệp chính xác vào thời điểm vàng.

### 1.2. Bài toán thực tiễn đặt ra trong môi trường giáo dục
* **Đối với Sinh viên:** Thường không nhận thức được mức độ nghiêm trọng khi bắt đầu nghỉ học 1-2 buổi hoặc nộp bài trễ; thiếu định hướng khi gặp bài toán khó dẫn đến tâm lý chán nản.
* **Đối với Giảng viên:** Một lớp học có từ 30 đến 40 sinh viên, giảng viên dạy nhiều ca trong ngày nên khó có thể theo dõi sát sao từng cá nhân nếu chỉ nhìn vào sổ điểm cuối kỳ.
* **Đối với Nhà trường:** Nguồn lực trợ giảng (Mentors) và thời lượng phụ đạo có giới hạn, cần một cơ chế phân bổ khoa học, tối ưu thay vì hỗ trợ dàn trải hoặc cảm tính.

### 1.3. Phân tích mô hình SWOT của dự án
* **Điểm mạnh (Strengths):**
  * Nền tảng thuật toán hoàn chỉnh kết hợp giữa Đại số tuyến tính, Giảm chiều dữ liệu PCA, Xác suất Bayes, Lý thuyết đồ thị và Quy hoạch tuyến tính.
  * Tích hợp cơ chế giải thích rõ ràng (Explainable AI), cho phép giảng viên biết chính xác vì sao một sinh viên bị gán nhãn nguy cơ.
  * Dữ liệu khảo sát thực tế quy mô lớn ($4.424$ hồ sơ).
* **Điểm yếu (Weaknesses):**
  * Một số biến dữ liệu hành vi (như xem video, tương tác diễn đàn) phụ thuộc vào tính tự giác của sinh viên.
  * Cần đồng bộ liên tục với hệ thống cơ sở dữ liệu nhà trường để cập nhật thời gian thực.
* **Cơ hội (Opportunities):**
  * Triển khai mở rộng cho toàn bộ các cơ sở đào tạo FPT Polytechnic trên toàn quốc.
  * Tích hợp thêm các mô hình học sâu (Deep Learning) và hệ khuyến nghị tự động gợi ý tài liệu học tập theo năng lực.
* **Thách thức (Threats):**
  * Đảm bảo tính bảo mật và quyền riêng tư dữ liệu cá nhân của người học theo các quy định pháp luật.
  * Sự thay đổi trong cấu trúc chương trình học qua từng học kỳ đòi hỏi mô hình phải được tái huấn luyện định kỳ.

### 1.4. Mục tiêu nghiên cứu tổng thể của Giai đoạn 1 & Giai đoạn 2
* **Mục tiêu Giai đoạn 1:** Xây dựng quy trình xử lý dữ liệu chuẩn hóa, trích xuất ma trận đặc trưng $X$, vector nhãn $y$; áp dụng chuẩn $L_1/L_2$ so sánh học lực; phân tích tổ hợp $C(8, 3)$ tối ưu hóa không gian tìm kiếm; thực hiện PCA giảm số chiều dữ liệu xuống 4 chiều đạt $\ge 80\%$ phương sai và đánh giá Decision Tree trước/sau PCA.
* **Mục tiêu Giai đoạn 2:** Khai phá xác suất có điều kiện và kiểm chứng định lý Bayes; huấn luyện mô hình phân loại Gaussian Naive Bayes; định lượng thông tin bằng Entropy Shannon và Information Gain; xây dựng mạng lưới xã hội sinh viên, duyệt BFS/DFS, khảo sát liên thông; mô hình hóa chuyển dịch hành vi bằng Chuỗi Markov 20 bước với phân phối dừng dài hạn; giải bài toán tối ưu phân bổ mentor bằng PuLP BIP và mạng luồng cực đại Max-Flow.

### 1.5. Giới thiệu Dataset khảo sát và Ngăn xếp công nghệ triển khai
* **Dataset khảo sát:** Sử dụng bộ dữ liệu chuẩn hóa quốc tế *Predict Students Dropout and Academic Success* từ kho lưu trữ Kaggle, gồm $4.424$ hồ sơ sinh viên với các nhóm thuộc tính nhân khẩu học, quá trình học tập kỳ 1, kỳ 2 và kết quả cuối cùng.
* **Ngăn xếp công nghệ triển khai (Tech Stack):**
  * Ngôn ngữ lập trình: Python 3.10+
  * Xử lý dữ liệu & Tính toán số học: `numpy`, `pandas`
  * Máy học & Tiền xử lý: `scikit-learn` (`StandardScaler`, `PCA`, `DecisionTreeClassifier`, `GaussianNB`, `metrics`)
  * Trực quan hóa dữ liệu: `matplotlib`, `seaborn`
  * Mạng lưới & Đồ thị: `networkx`
  * Tối ưu hóa toán học: `pulp` (CBC Solver), `scipy.optimize`
  * Soạn thảo & Thực thi tài liệu: `jupyter`, `nbclient`, `python-docx`

---

# CHƯƠNG 2. XÂY DỰNG PIPELINE, TIỀN XỬ LÝ DỮ LIỆU VÀ XÂY DỰNG ĐẶC TRƯNG (PHẦN A.1)

### 2.1. Cấu trúc và quy trình chuyển đổi từ Kaggle Dataset (35 cột) sang SmartEdu Dataset (10 cột)
Bộ dữ liệu nguyên bản trên Kaggle chứa 35 cột bao gồm nhiều yếu tố bên ngoài như nghề nghiệp của bố mẹ, trình độ học vấn phụ huynh, tỷ lệ lạm phát kinh tế quốc gia... Nhằm tập trung vào bài toán giáo dục ứng dụng tại FPT Polytechnic, nhóm nghiên cứu đã xây dựng module tiền xử lý `process_kaggle_dataset.py` để trích xuất và biến đổi thành 10 đặc trưng trực tiếp liên quan đến hành vi học tập:

1. **`student_id`:** Định danh duy nhất sinh viên theo định dạng `SV0001` đến `SV4424`.
2. **`attendance_rate`:** Tỷ lệ tham dự lớp học (từ 0.0 đến 1.0), biến đổi từ tỷ lệ số tín chỉ được công nhận trên số tín chỉ đăng ký học kỳ 1 (`Curricular units 1st sem (approved)` / `Curricular units 1st sem (enrolled)`).
3. **`quiz_avg`:** Điểm trung bình kiểm tra ngắn (thang 5), chuyển đổi tuyến tính từ số tín chỉ hoàn thành không cần thi lại.
4. **`lab_avg`:** Điểm trung bình thực hành Lab trên thang điểm 10, ánh xạ từ điểm trung bình học tập kỳ 1 (`Curricular units 1st sem (grade)`).
5. **`assignment_score`:** Điểm đánh giá bài tập lớn / đồ án trên thang điểm 10, ánh xạ từ điểm trung bình kỳ 2 (`Curricular units 2nd sem (grade)`).
6. **`self_study_hours`:** Số giờ tự học ước tính mỗi tuần (dao động quanh 8-14 giờ), ánh xạ từ độ tuổi sinh viên khi nhập học và tính chuyên cần.
7. **`late_submissions`:** Số lần nộp bài trễ hạn trong học kỳ, sinh ngẫu nhiên có kiểm soát dựa trên số môn nợ của học kỳ 1.
8. **`video_views`:** Số lượt xem video học liệu số trên cổng LMS (dao động 5-35 lượt), biểu diễn mức độ tương tác tài nguyên học tập.
9. **`participation_level`:** Mức độ tích cực tham gia trên lớp (Low, Medium, High), tổng hợp từ tình trạng học bổng, hoàn thành học phí và điểm số.
10. **`risk_label`:** Nhãn mục tiêu giám sát học tập, gồm 2 lớp: `low_risk` (sinh viên an toàn, tốt nghiệp đúng hạn) và `high_risk` (sinh viên có nguy cơ rớt môn hoặc thôi học), chuyển đổi từ cột `Target` (Dropout -> `high_risk`, Graduate/Enrolled -> `low_risk`).

### 2.2. Bảng mô tả chi tiết 10 đặc trưng dữ liệu học tập

| STT | Tên đặc trưng | Kiểu dữ liệu | Khoảng giá trị | Ý nghĩa thực tiễn trong quản trị học tập |
|:---:|:---|:---:|:---:|:---|
| 1 | `student_id` | String | `SV0001` - `SV4424` | Mã số sinh viên định danh quản lý |
| 2 | `attendance_rate` | Float | $0.00 - 1.00$ | Tỷ lệ đi học chuyên cần tại các buổi học trên lớp |
| 3 | `quiz_avg` | Float | $0.00 - 5.00$ | Điểm kiểm tra trắc nghiệm kiến thức định kỳ |
| 4 | `lab_avg` | Float | $0.00 - 10.00$ | Điểm đánh giá năng lực thực hành kỹ thuật tại phòng Lab |
| 5 | `assignment_score` | Float | $0.00 - 10.00$ | Điểm bài tập đồ án giai đoạn / Assignment môn học |
| 6 | `self_study_hours` | Float | $4.00 - 18.00$ | Số giờ tự nghiên cứu và làm bài tập tại nhà mỗi tuần |
| 7 | `late_submissions` | Integer | $0 - 5$ | Số lần nộp bài quá hạn hệ thống LMS |
| 8 | `video_views` | Integer | $3 - 40$ | Số lần truy cập và xem lại video bài giảng trực tuyến |
| 9 | `participation_level` | String | Low, Medium, High | Đánh giá mức độ tích cực trao đổi và xây dựng bài |
| 10 | `risk_label` | String | `low_risk`, `high_risk` | Nhãn mục tiêu phân loại rủi ro học tập của sinh viên |

### 2.3. Quy trình làm sạch dữ liệu khuyết tật (Missing Values) bằng Trung vị (Median)
Trong dữ liệu giáo dục thực tế, việc sinh viên bỏ trống bài kiểm tra hoặc lỗi ghi nhận đường truyền trên hệ thống dẫn đến các giá trị khuyết tật (NaN / Null). Để đảm bảo tính khách quan và không làm sai lệch phân phối dữ liệu:
* Nhóm sử dụng phương pháp điền giá trị khuyết tật bằng **Trung vị (Median)** của từng cột đặc trưng số (`attendance_rate`, `quiz_avg`, `lab_avg`, `assignment_score`, `self_study_hours`).
* **Lý do chọn Median thay vì Trung bình (Mean):** Trong phân phối điểm số học tập, các giá trị dị biệt (Outliers) như điểm 0 do bỏ thi sẽ kéo giá trị Mean xuống thấp một cách bất hợp lý. Median là đại lượng thống kê vững chắc (Robust Statistic), đại diện chính xác hơn cho phần đông sinh viên trong lớp.

### 2.4. Kỹ thuật mã hóa thứ bậc (Ordinal Encoding) cho đặc trưng định tính
Đặc trưng `participation_level` là một biến phân loại có thứ bậc tự nhiên về mức độ tích cực của người học. Nhóm áp dụng phương pháp mã hóa thứ bậc (Ordinal Encoding):
$$\text{Low} \to 0, \quad \text{Medium} \to 1, \quad \text{High} \to 2$$
Cách ánh xạ này bảo toàn được quan hệ thứ tự về mặt toán học: $\text{Low} < \text{Medium} < \text{High}$, cho phép các thuật toán tuyến tính và đo lường khoảng cách tận dụng được thông tin về độ tích cực của sinh viên.

---

# CHƯƠNG 3. NỀN TẢNG TOÁN HỌC: ĐẠI SỐ TUYẾN TÍNH, CHUẨN KHOẢNG CÁCH VÀ TỔ HỢP (PHẦN A.2, A.3, A.4)

### 3.1. Thiết lập ma trận đặc trưng $X$ và vector nhãn $y$
Sau khi làm sạch và mã hóa, tập dữ liệu $4.424$ sinh viên được cấu trúc thành:
* **Ma trận đặc trưng $X \in \mathbb{R}^{4424 \times 8}$:** Mỗi dòng đại diện cho một vector học tập của sinh viên $\mathbf{x}_i = [x_{i1}, x_{i2}, \dots, x_{i8}]$, với 8 cột đặc trưng tương ứng:
  1. `attendance_rate`
  2. `quiz_avg`
  3. `lab_avg`
  4. `assignment_score`
  5. `self_study_hours`
  6. `late_submissions`
  7. `video_views`
  8. `participation_encoded`
* **Vector nhãn $y \in \mathbb{R}^{4424}$:** Chứa nhãn phân loại nhị phân ($0 = \text{low\_risk}, 1 = \text{high\_risk}$). Số lượng mẫu phân bố cân bằng: $2.209$ sinh viên `low_risk` ($49.93\%$) và $2.215$ sinh viên `high_risk` ($50.07\%$).

### 3.2. Điểm rủi ro tuyến tính $s = Xw$ và Phép nhân ma trận - vector
Điểm rủi ro tổng hợp $s_i$ của mỗi sinh viên được xác định bằng tích vô hướng giữa vector đặc trưng $\mathbf{x}_i$ và vector trọng số nghiệp vụ $\mathbf{w} \in \mathbb{R}^8$:
$$s = X \cdot \mathbf{w} \implies s_i = \sum_{j=1}^8 X_{ij} w_j$$

> **HƯỚNG DẪN TÍNH TAY & THAY SỐ CÔNG THỨC $s = X \cdot w$ (MINH HỌA CHI TIẾT TỪNG THAM SỐ):**
>
> **1. Nguồn gốc từng tham số lấy ở đâu và bằng bao nhiêu:**
> * **Tham số $X_{ij}$ (Ma trận đặc trưng $X$):** Lấy trực tiếp từ file dữ liệu đã làm sạch `data/students.csv` tại dòng sinh viên thứ $i$ và cột đặc trưng thứ $j$:
>   * Sinh viên `SV0001` ($i=1$): $X_{1,1}=0.50$, $X_{1,2}=2.00$, $X_{1,3}=0.00$, $X_{1,4}=0.00$, $X_{1,5}=9.10$, $X_{1,6}=0$, $X_{1,7}=5$, $X_{1,8}=1$.
>   * Sinh viên `SV0002` ($i=2$): $X_{2,1}=0.60$, $X_{2,2}=2.00$, $X_{2,3}=7.00$, $X_{2,4}=6.80$, $X_{2,5}=8.60$, $X_{2,6}=0$, $X_{2,7}=17$, $X_{2,8}=1$.
> * **Tham số $\mathbf{w}$ (Vector trọng số nghiệp vụ $\mathbf{w} \in \mathbb{R}^8$):** Được định nghĩa dựa trên tầm quan trọng chuyên môn giáo dục trong `src/linear_algebra.py`:
>   $$\mathbf{w} = [0.25, 0.30, 0.25, -0.20, -0.15, 0.40, -0.10, -0.30]^T$$
>   Trong đó các yếu tố làm tăng nguy cơ mang dấu dương (vắng học, nộp trễ), các yếu tố học tốt mang dấu âm (điểm lab cao, tự học nhiều, tham gia tích cực).
>
> **2. Công thức sau khi đã thay số cụ thể từng bước:**
> * **Đối với sinh viên `SV0001`:**
>   $$s_1 = (0.50 \times 0.25) + (2.00 \times 0.30) + (0.00 \times 0.25) + (0.00 \times -0.20) + (9.10 \times -0.15) + (0 \times 0.40) + (5 \times -0.10) + (1 \times -0.30)$$
>   $$s_1 = 0.1250 + 0.6000 + 0.0000 + 0.0000 - 1.3650 + 0.0000 - 0.5000 - 0.3000 = -1.4400$$
> * **Đối với sinh viên `SV0002`:**
>   $$s_2 = (0.60 \times 0.25) + (2.00 \times 0.30) + (7.00 \times 0.25) + (6.80 \times -0.20) + (8.60 \times -0.15) + (0 \times 0.40) + (17 \times -0.10) + (1 \times -0.30)$$
>   $$s_2 = 0.1500 + 0.6000 + 1.7500 - 1.3600 - 1.2900 + 0.0000 - 1.7000 - 0.3000 = -2.1500$$
>
> **3. Nhận xét kết quả:**
> * Kết quả tính tay $s_1 = -1.4400$ và $s_2 = -2.1500$ trùng khớp $100\%$ với kết quả in ra từ chương trình máy tính.
> * Điểm $s_1 = -1.4400$ lớn hơn đáng kể so với $s_2 = -2.1500$ phản ánh đúng thực tế sinh viên `SV0001` có điểm thực hành Lab và Assignment đều bằng 0, rơi vào diện nguy cơ rất cao (`high_risk`).

### 3.3. Chuẩn hóa StandardScaler, Chuẩn Vector Norm $L_1, L_2$ và Khoảng cách hình học
Do các đặc trưng có thang đo rất khác nhau (tỷ lệ chuyên cần từ $0-1$, trong khi lượt xem video lên tới $40$), việc tính khoảng cách đòi hỏi phải chuẩn hóa ma trận bằng `StandardScaler`:
$$z_{ij} = \frac{X_{ij} - \mu_j}{\sigma_j}$$

Bảng tham số thống kê trên toàn bộ $4.424$ sinh viên:
* `attendance_rate`: $\mu_1 = 0.8146, \sigma_1 = 0.2019$
* `quiz_avg`: $\mu_2 = 2.5446, \sigma_2 = 1.5046$
* `lab_avg`: $\mu_3 = 5.3200, \sigma_3 = 2.4217$
* `assignment_score`: $\mu_4 = 5.1152, \sigma_4 = 2.6054$
* `self_study_hours`: $\mu_5 = 10.1443, \sigma_5 = 2.3453$
* `late_submissions`: $\mu_6 = 0.1377, \sigma_6 = 0.6908$
* `video_views`: $\mu_7 = 21.5981, \sigma_7 = 8.3573$
* `participation_encoded`: $\mu_8 = 0.8933, \sigma_8 = 0.7695$

> **HƯỚNG DẪN TÍNH TAY & THAY SỐ CÔNG THỨC KHOẢNG CÁCH $L_1, L_2$:**
>
> **1. Nguồn gốc từng tham số:**
> Vector sau chuẩn hóa của 2 sinh viên $\mathbf{z}_1$ (`SV0001`) và $\mathbf{z}_2$ (`SV0002`):
> * $\mathbf{z}_1 = [-1.5583, -0.3619, -2.1968, -1.9633, -0.4453, -0.1993, -1.9861, 0.1386]$
> * $\mathbf{z}_2 = [-1.0630, -0.3619, 0.6937, 0.6466, -0.6585, -0.1993, -0.5502, 0.1386]$
> * Vector chênh lệch $\mathbf{d} = \mathbf{z}_1 - \mathbf{z}_2$:
>   $$\mathbf{d} = [-0.4953, 0.0000, -2.8905, -2.6099, 0.2132, 0.0000, -1.4359, 0.0000]$$
>
> **2. Công thức sau khi đã thay số cụ thể:**
> * **Khoảng cách Manhattan ($L_1$ norm):**
>   $$D_{L1}(\mathbf{z}_1, \mathbf{z}_2) = \sum_{j=1}^8 |d_j| = |-0.4953| + 0 + |-2.8905| + |-2.6099| + |0.2132| + 0 + |-1.4359| + 0$$
>   $$D_{L1}(\mathbf{z}_1, \mathbf{z}_2) = 0.4953 + 2.8905 + 2.6099 + 0.2132 + 1.4359 = 7.6448$$
> * **Khoảng cách Euclidean ($L_2$ norm):**
>   $$D_{L2}(\mathbf{z}_1, \mathbf{z}_2) = \sqrt{\sum_{j=1}^8 d_j^2} = \sqrt{(-0.4953)^2 + 0^2 + (-2.8905)^2 + (-2.6099)^2 + (0.2132)^2 + 0^2 + (-1.4359)^2 + 0^2}$$
>   $$D_{L2}(\mathbf{z}_1, \mathbf{z}_2) = \sqrt{0.2453 + 8.3550 + 6.8116 + 0.0455 + 2.0618} = \sqrt{17.5192} = 4.1856$$
>
> **3. Nhận xét kết quả:**
> * Độ chênh lệch giữa hai sinh viên chủ yếu bắt nguồn từ 2 cột điểm thực hành Lab (chênh lệch chuẩn hóa $2.8905$) và Assignment ($2.6099$). Khoảng cách hình học $L_2 = 4.1856$ phản ánh khoảng cách thực tế trong không gian đa chiều, dùng làm đầu vào cho các thuật toán phân cụm K-Means hoặc K-NN.

### 3.4. Lý thuyết tổ hợp $C(n, k)$ và Không gian tìm kiếm tham số Grid Search
Khi xây dựng mô hình học máy tinh gọn, việc lựa chọn một tập con gồm $k = 3$ đặc trưng tốt nhất từ $n = 8$ đặc trưng được giải quyết bằng đại số tổ hợp:
$$C(n, k) = \frac{n!}{k!(n-k)!} \implies C(8, 3) = \frac{8!}{3!(8-3)!} = \frac{40.320}{6 \times 120} = 56 \text{ tổ hợp}$$

Khi thực hiện Grid Search kết hợp với việc tinh chỉnh siêu tham số mô hình:
* Số lượng tổ hợp đặc trưng: $56$ tổ hợp.
* Chiều sâu tối đa của cây (`max_depth` $\in \{3, 5, 7\}$): $3$ giá trị.
* Tiêu chí phân tách (`criterion` $\in \{\text{'gini'}, \text{'entropy'}\}$): $2$ giá trị.
* Áp dụng **Nguyên lý nhân (Multiplication Rule)** trong đại số tổ hợp, tổng số cấu hình thử nghiệm trong không gian tìm kiếm là:
  $$N_{\text{models}} = 56 \times 3 \times 2 = 336 \text{ cấu hình huấn luyện}$$

### 3.5. Nhận xét nghiệm thu kỹ thuật Phần A
Phần A đã hoàn thành trọn vẹn $100\%$ các mục tiêu kỹ thuật: dữ liệu được làm sạch triệt để, ma trận và vector được biểu diễn chuẩn xác, phép nhân tuyến tính $s = Xw$ và các chuẩn khoảng cách $L_1, L_2$ được kiểm chứng đối chiếu tính tay trùng khớp tuyệt đối, không gian tổ hợp $336$ mô hình được thiết lập chặt chẽ.

---

# CHƯƠNG 4. PHÂN TÍCH THÀNH PHẦN CHÍNH (PCA) VÀ ĐÁNH GIÁ MÔ HÌNH PHÂN LOẠI (PHẦN B.1, B.2, B.3)

### 4.1. Ma trận tương quan Pearson (Heatmap) và hiện tượng đa cộng tuyến
Hệ số tương quan tuyến tính Pearson giữa hai biến đặc trưng $X$ và $Y$ được tính bằng:
$$r_{XY} = \frac{\sum (X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum (X_i - \bar{X})^2 \sum (Y_i - \bar{Y})^2}}$$

Kết quả phân tích ma trận tương quan trên $4.424$ hồ sơ sinh viên cho thấy:
* Cặp đặc trưng có tương quan dương mạnh nhất: `lab_avg` và `assignment_score` đạt $r = 0.68$, cho thấy sinh viên làm tốt bài Lab thường hoàn thành xuất sắc đồ án Assignment.
* Cặp đặc trưng tương quan nghịch rõ rệt: `attendance_rate` và `risk_label` đạt $r = -0.58$, chứng minh chuyên cần là chỉ dấu trực tiếp bảo vệ sinh viên khỏi nguy cơ rớt môn.
* **Hiện tượng đa cộng tuyến (Multicollinearity):** Sự phụ thuộc tuyến tính cao giữa các biến điểm số gây nhiễu cho mô hình phân loại và làm lãng phí tài nguyên tính toán. Đây chính là lý do toán học thôi thúc nhóm áp dụng thuật toán Giảm chiều dữ liệu PCA.

### 4.2. Cơ sở toán học của PCA: Ma trận hiệp phương sai, Trị riêng và Vector riêng
Thuật toán Phân tích thành phần chính (PCA) tìm kiếm một hệ cơ sở trực giao mới sao cho phương sai của dữ liệu chiếu lên các trục mới là lớn nhất:
1. Tính ma trận hiệp phương sai mẫu: $\Sigma = \frac{1}{N-1} X^T X \in \mathbb{R}^{8 \times 8}$.
2. Giải phương trình đặc trưng tìm các trị riêng $\lambda_i$ và vector riêng $\mathbf{v}_i$:
   $$\Sigma \mathbf{v}_i = \lambda_i \mathbf{v}_i$$
3. Các vector riêng $\mathbf{v}_i$ trực giao đôi một biểu diễn hướng phân tán chính của dữ liệu, và trị riêng $\lambda_i$ tương ứng chính là độ lớn phương sai trên trục đó.

### 4.3. Phân tích tỷ lệ phương sai giải thích và lựa chọn số lượng Principal Components
Tỷ lệ phương sai giải thích bởi thành phần chính thứ $k$ là:
$$\text{EVR}_k = \frac{\lambda_k}{\sum_{j=1}^8 \lambda_j}$$

Bảng kết quả phương sai tích lũy của 8 thành phần chính:

| Component | Tỷ lệ phương sai riêng lẻ | Phương sai tích lũy | Quyết định lựa chọn |
|:---:|:---:|:---:|:---|
| $PC_1$ | $32.45\%$ | $32.45\%$ | Chọn (Trục học lực tổng hợp) |
| $PC_2$ | $19.82\%$ | $52.27\%$ | Chọn (Trục tương tác & nỗ lực tự học) |
| $PC_3$ | $15.12\%$ | $67.39\%$ | Chọn (Trục chuyên cần & nộp bài đúng hạn) |
| $PC_4$ | $12.80\%$ | **$80.19\%$** | **Điểm dừng kỹ thuật ($\ge 80.0\%$)** |
| $PC_5$ | $8.45\%$ | $88.64\%$ | Loại bỏ (Nhiễu thứ yếu) |
| $PC_6$ | $5.12\%$ | $93.76\%$ | Loại bỏ |
| $PC_7$ | $3.89\%$ | $97.65\%$ | Loại bỏ |
| $PC_8$ | $2.35\%$ | $100.00\%$ | Loại bỏ |

Nhóm quyết định chọn **$k = 4$ thành phần chính**, giúp giảm một nửa số chiều của dữ liệu ($8 \to 4$) trong khi vẫn lưu giữ được **$80.19\%$** lượng thông tin và phương sai gốc của toàn bộ tập dữ liệu.

### 4.4. Trực quan hóa không gian 2D ($PC_1$ vs $PC_2$) phân tách nhóm nguy cơ
Khi chiếu dữ liệu lên mặt phẳng 2 chiều được tạo bởi 2 thành phần chính đầu tiên ($PC_1$ giải thích $32.45\%$ và $PC_2$ giải thích $19.82\%$, tổng cộng $52.27\%$ thông tin):
* Các điểm dữ liệu `low_risk` (màu xanh lá) tập trung dày đặc ở nửa bên phải đồ thị (giá trị $PC_1 > 0$), tương ứng với sinh viên có điểm Lab và Assignment cao.
* Các điểm dữ liệu `high_risk` (màu đỏ) phân bố dồn về nửa bên trái ($PC_1 < 0$), tương ứng với các sinh viên học lực yếu và vắng học nhiều.
* Mặt phẳng 2D này minh chứng dữ liệu có ranh giới phân tách tự nhiên rõ rệt, là tiền đề thuận lợi cho các thuật toán phân lớp.

### 4.5. Huấn luyện và so sánh mô hình Decision Tree Trước vs Sau PCA
Nhóm tiến hành phân chia tập dữ liệu theo tỷ lệ $80\%$ Train - $20\%$ Test (ngẫu nhiên có cố định `random_state=42`) và huấn luyện mô hình Cây quyết định (Decision Tree):

| Chỉ số đánh giá | Trước PCA (8 đặc trưng gốc) | Sau PCA (4 Principal Components) | Nhận xét đối chiếu |
|:---|:---:|:---:|:---|
| **Độ chính xác (Accuracy)** | $79.89\%$ | $77.97\%$ | Chỉ giảm nhẹ $1.92\%$ |
| **Precision (Độ chuẩn xác)** | $79.35\%$ | $77.62\%$ | Giữ mức tương đương |
| **Recall (Độ nhạy)** | $80.77\%$ | $78.51\%$ | Duy trì khả năng bắt trúng nguy cơ |
| **F1-Score (Trung bình điều hòa)** | **$80.05\%$** | **$78.06\%$** | **Đạt tiêu chuẩn thực tế ($\ge 75\%$)** |
| **Kích thước không gian dữ liệu** | $4.424 \times 8$ ($35.392$ giá trị) | $4.424 \times 4$ ($17.696$ giá trị) | **Giảm $50\%$ dung lượng lưu trữ** |

### 4.6. Nhận xét nghiệm thu kỹ thuật Phần B
Mô hình sau PCA đạt hiệu năng phân loại rất ấn tượng ($F1 = 78.06\%$), chứng minh phương pháp biến đổi trực giao của PCA đã loại bỏ hiệu quả các thành phần dư thừa và đa cộng tuyến, giúp mô hình huấn luyện nhanh hơn, tiết kiệm $50\%$ bộ nhớ mà không làm suy giảm chất lượng cảnh báo sinh viên nguy cơ.

---

# CHƯƠNG 5. MÔ HÌNH XÁC SUẤT, ĐỊNH LÝ BAYES VÀ LÝ THUYẾT THÔNG TIN (PHẦN C.1, C.2, C.3)

### 5.1. Bảng xác suất có điều kiện hai chiều và Kiểm chứng Định lý Bayes
Để hiểu sâu mối quan hệ nhân - quả giữa các biểu hiện học tập rời rạc hóa và nguy cơ rớt môn, nhóm khảo sát bảng xác suất có điều kiện hai chiều:
* Chiều 1: $P(\text{high\_risk} | \text{feature})$ — Cho biết nếu sinh viên có biểu hiện đó thì xác suất rớt môn là bao nhiêu.
* Chiều 2: $P(\text{feature} | \text{high\_risk})$ — Cho biết trong số những sinh viên rớt môn, có bao nhiêu phần trăm có biểu hiện đó.

Bảng kết quả xác suất có điều kiện thực nghiệm trên $4.424$ hồ sơ:

| Đặc trưng quan sát ($A$) | Số lượng sinh viên ($N_A$) | $P(A)$ | $P(\text{high\_risk} \cap A)$ | $P(\text{high\_risk} | A)$ | $P(A | \text{high\_risk})$ |
|:---|:---:|:---:|:---:|:---:|:---:|
| `att_low` (Chuyên cần $\le 0.75$) | $1.382$ | $31.24\%$ | $1.262$ | **$91.32\%$** | **$56.98\%$** |
| `att_med` (Chuyên cần $0.75 - 0.90$) | $928$ | $20.98\%$ | $569$ | $61.31\%$ | $25.69\%$ |
| `att_high` (Chuyên cần $> 0.90$) | $2.114$ | $47.78\%$ | $384$ | $18.16\%$ | $17.34\%$ |
| `lab_low` (Điểm Lab $\le 4.0$) | $1.520$ | $34.36\%$ | $1.230$ | **$80.92\%$** | $55.53\%$ |
| `assignment_low` (Assignment $\le 4.0$) | $1.610$ | $36.39\%$ | $1.345$ | **$83.54\%$** | $60.72\%$ |
| `part_low` (Tích cực: Low) | $1.450$ | $32.78\%$ | $1.080$ | $74.48\%$ | $48.76\%$ |

> **HƯỚNG DẪN TÍNH TAY & THAY SỐ CÔNG THỨC ĐỊNH LÝ BAYES:**
>
> **1. Nguồn gốc từng tham số lấy ở đâu và bằng bao nhiêu:**
> * **Tổng số sinh viên:** $N = 4.424$.
> * **Xác suất tiên nghiệm sinh viên nguy cơ cao $P(\text{high\_risk})$:** Lấy từ số dòng có nhãn `high_risk` chia cho tổng mẫu:
>   $$P(\text{high\_risk}) = \frac{2.215}{4.424} = 0.5007 \quad (50.07\%)$$
> * **Xác suất tiên nghiệm biến cố chuyên cần thấp $P(\text{att\_low})$:** Đếm tổng số sinh viên có `attendance_rate` $\le 0.75$:
>   $$P(\text{att\_low}) = \frac{1.382}{4.424} = 0.3124 \quad (31.24\%)$$
> * **Độ hợp lý (Likelihood) $P(\text{att\_low} | \text{high\_risk})$:** Trong $2.215$ sinh viên nguy cơ cao, có $1.262$ sinh viên vắng học nhiều:
>   $$P(\text{att\_low} | \text{high\_risk}) = \frac{1.262}{2.215} = 0.5698 \quad (56.98\%)$$
>
> **2. Công thức sau khi đã thay số cụ thể từng bước:**
> $$P(\text{high\_risk} | \text{att\_low}) = \frac{P(\text{att\_low} | \text{high\_risk}) \times P(\text{high\_risk})}{P(\text{att\_low})}$$
> $$P(\text{high\_risk} | \text{att\_low}) = \frac{0.5698 \times 0.5007}{0.3124} = \frac{0.2853}{0.3124} = 0.9132 \quad (91.32\%)$$
>
> **3. Nhận xét kết quả:**
> * Công thức Bayes tính tay cho ra kết quả $91.32\%$, trùng khớp hoàn toàn với phép đếm trực tiếp $\frac{1.262}{1.382} = 0.9132$.
> * **Ý nghĩa thực tiễn:** Một sinh viên khi đã vắng học vượt ngưỡng quy định ($A = \text{att\_low}$) thì xác suất rớt môn lên tới **$91.32\%$**. Đây là quy luật xác suất quan trọng nhất chứng minh chuyên cần là lá chắn bảo vệ thành tích học tập.

### 5.2. Huấn luyện Mô hình Gaussian Naive Bayes & Dự báo Xác suất
Mô hình Gaussian Naive Bayes giả định các đặc trưng liên tục tuân theo phân phối chuẩn với hàm mật độ:
$$P(x_i | C_k) = \frac{1}{\sqrt{2\pi \sigma_{k,i}^2}} \exp\left( -\frac{(x_i - \mu_{k,i})^2}{2\sigma_{k,i}^2} \right)$$

Bảng tham số phân phối chuẩn của các đặc trưng chính theo từng lớp:
* Lớp An toàn ($C_0 = \text{low\_risk}$):
  * `attendance_rate`: $\mu_{0,1} = 0.9429, \sigma_{0,1}^2 = 0.0119$
  * `lab_avg`: $\mu_{0,3} = 6.3465, \sigma_{0,3}^2 = 1.7256$
* Lớp Nguy cơ ($C_1 = \text{high\_risk}$):
  * `attendance_rate`: $\mu_{1,1} = 0.6879, \sigma_{1,1}^2 = 0.0369$
  * `lab_avg`: $\mu_{1,3} = 4.3317, \sigma_{1,3}^2 = 7.8416$

> **HƯỚNG DẪN TÍNH TAY & THAY SỐ GAUSSIAN NAIVE BAYES CHO SINH VIÊN `SV0001`:**
>
> **1. Nguồn gốc tham số:**
> Sinh viên `SV0001` có $x_1 = 0.50$ (`attendance_rate`) và $x_3 = 0.00$ (`lab_avg`).
>
> **2. Thay số tính toán hàm mật độ xác suất:**
> * Đối với đặc trưng Chuyên cần ($x_1 = 0.50$):
>   * $P(x_1 | C_1) = \frac{1}{\sqrt{2\pi \times 0.0369}} \exp\left(-\frac{(0.50 - 0.6879)^2}{2 \times 0.0369}\right) = \frac{1}{0.4815} \exp(-0.4784) = 2.0768 \times 0.6198 = 1.2871$
>   * $P(x_1 | C_0) = \frac{1}{\sqrt{2\pi \times 0.0119}} \exp\left(-\frac{(0.50 - 0.9429)^2}{2 \times 0.0119}\right) = \frac{1}{0.2735} \exp(-8.2430) = 3.6563 \times 0.000263 = 0.000974$
> * Đối với đặc trưng Điểm thực hành Lab ($x_3 = 0.00$):
>   * $P(x_3 | C_1) = \frac{1}{\sqrt{2\pi \times 7.8416}} \exp\left(-\frac{(0.00 - 4.3317)^2}{2 \times 7.8416}\right) = \frac{1}{7.0191} \exp(-1.1964) = 0.1425 \times 0.3023 = 0.0431$
>   * $P(x_3 | C_0) = \frac{1}{\sqrt{2\pi \times 1.7256}} \exp\left(-\frac{(0.00 - 6.3465)^2}{2 \times 1.7256}\right) = \frac{1}{3.2928} \exp(-11.6702) = 0.3037 \times 0.0000085 = 0.000003$
>
> **3. Nhận xét kết quả:**
> Khi nhân tích các hàm mật độ với xác suất tiên nghiệm, xác suất không chuẩn hóa của lớp $C_1$ vượt trội hơn lớp $C_0$ hàng triệu lần. Sau khi chuẩn hóa Softmax, mô hình đưa ra dự báo xác suất $P(\text{high\_risk} | X) \approx 1.0000$ ($100\%$), dự đoán chính xác tuyệt đối nhãn nguy cơ của sinh viên `SV0001`.

Kết quả đánh giá mô hình Gaussian Naive Bayes trên tập kiểm thử:
* **Accuracy:** $74.69\%$
* **Precision:** $86.38\%$ (Rất cao, hầu như không báo động giả)
* **Recall:** $58.69\%$
* **F1-Score:** $69.89\%$

### 5.3. Định lượng độ bất định qua Shannon Entropy & Độ tăng thông tin (Information Gain)
Lý thuyết thông tin của Claude Shannon định lượng độ hỗn loạn của tập nhãn $S$:
$$H(S) = -\sum_{i=1}^c p_i \log_2(p_i)$$
Entropy có điều kiện khi phân tách dữ liệu theo đặc trưng $X$:
$$H(S | X) = \sum_{v \in \text{Values}(X)} \frac{|S_v|}{|S|} H(S_v)$$
Độ tăng thông tin (Information Gain):
$$IG(S, X) = H(S) - H(S | X)$$

> **HƯỚNG DẪN TÍNH TAY & THAY SỐ CHI TIẾT INFORMATION GAIN:**
>
> **1. Nguồn gốc từng tham số:**
> * Tập dữ liệu gốc $S$ gồm $2.209$ mẫu `low_risk` ($p_0 = 0.4993$) và $2.215$ mẫu `high_risk` ($p_1 = 0.5007$).
> * Phân nhánh đặc trưng `attendance_bin`:
>   * Nhóm `att_low`: $N_1 = 1.382$ (tỷ trọng $0.3124$), $1.262$ high ($91.32\%$), $120$ low ($8.68\%$).
>   * Nhóm `att_med`: $N_2 = 928$ (tỷ trọng $0.2098$), $569$ high ($61.31\%$), $359$ low ($38.69\%$).
>   * Nhóm `att_high`: $N_3 = 2.114$ (tỷ trọng $0.4778$), $384$ high ($18.16\%$), $1.730$ low ($81.84\%$).
>
> **2. Thay số tính toán từng bước:**
> * **Entropy gốc $H(S)$:**
>   $$H(S) = - [0.4993 \log_2(0.4993) + 0.5007 \log_2(0.5007)] = - [-0.5003 - 0.4997] = 1.0000 \text{ bit}$$
> * **Entropy của từng nhóm con:**
>   * $H(S_1) = - [0.9132 \log_2(0.9132) + 0.0868 \log_2(0.0868)] = 0.4258 \text{ bit}$
>   * $H(S_2) = - [0.6131 \log_2(0.6131) + 0.3869 \log_2(0.3869)] = 0.9627 \text{ bit}$
>   * $H(S_3) = - [0.1816 \log_2(0.1816) + 0.8184 \log_2(0.8184)] = 0.6837 \text{ bit}$
> * **Entropy có điều kiện:**
>   $$H(S | \text{attendance\_bin}) = (0.3124 \times 0.4258) + (0.2098 \times 0.9627) + (0.4778 \times 0.6837) = 0.6617 \text{ bit}$$
> * **Độ tăng thông tin:**
>   $$IG(S, \text{attendance\_bin}) = 1.0000 - 0.6617 = 0.3383 \text{ bit}$$

Bảng xếp hạng Information Gain của các đặc trưng:

| Thứ hạng | Đặc trưng | Entropy gốc $H(S)$ | Entropy có điều kiện $H(S|X)$ | Information Gain (bits) |
|:---:|:---|:---:|:---:|:---:|
| 1 | `attendance_bin` | $1.0000$ | $0.6617$ | **$0.3383$** |
| 2 | `assignment_bin` | $1.0000$ | $0.8328$ | **$0.1672$** |
| 3 | `lab_bin` | $1.0000$ | $0.8797$ | **$0.1203$** |
| 4 | `participation_level` | $1.0000$ | $0.9271$ | **$0.0729$** |
| 5 | `quiz_bin` | $1.0000$ | $0.9943$ | **$0.0057$** |
| 6 | `late_sub_bin` | $1.0000$ | $0.9947$ | **$0.0053$** |

### 5.4. Nhận xét nghiệm thu kỹ thuật Phần C
Kết quả chứng minh về mặt toán học rằng đặc trưng Chuyên cần (`attendance_bin`) mang lượng thông tin giảm bất định lớn nhất ($0.3383$ bit), vượt xa các cột điểm thi định kỳ. Điều này hoàn toàn trùng khớp với việc Cây quyết định luôn chọn điểm danh làm gốc phân nhánh đầu tiên.

---

# CHƯƠNG 6. LÝ THUYẾT ĐỒ THỊ MẠNG LƯỚI SINH VIÊN VÀ CHUỖI MARKOV DỰ BÁO HÀNH VI (PHẦN D.1, D.2, D.3)

### 6.1. Xây dựng Đồ thị có hướng quan hệ sinh viên & Biểu diễn ma trận kề
Trong môi trường học tập, sinh viên không học tập cô lập mà luôn có sự tương tác, trao đổi bài vở và làm việc nhóm. Mạng lưới này được mô hình hóa bằng đồ thị có hướng $G = (V, E)$:
* Tập đỉnh $V$: gồm $|V| = 1.128$ sinh viên tham gia tương tác.
* Tập cạnh $E$: gồm $|E| = 1.500$ liên kết có hướng (sinh viên $u$ chủ động nhắn tin / hỏi bài sinh viên $v$).

Cấu trúc đồ thị được biểu diễn bằng Danh sách kề và Ma trận kề:
* **Bậc vào (`in-degree`):** Số lượng bạn học chủ động tìm đến sinh viên đó để hỏi bài. Những sinh viên có `in-degree` cao đóng vai trò là "Hub tri thức", có học lực giỏi và tinh thần hỗ trợ cao.
* **Bậc ra (`out-degree`):** Số lần sinh viên chủ động đi tìm người giúp đỡ.
* **Sinh viên cô lập (Isolates):** Những sinh viên có cả bậc vào và bậc ra đều bằng 0, hoàn toàn tách biệt khỏi tập thể lớp, là nhóm có nguy cơ trầm cảm và bỏ học cao nhất.

### 6.2. Thuật toán duyệt BFS/DFS & Phân tích tính liên thông mạng lưới
Nhóm áp dụng hai thuật toán duyệt kinh điển từ đỉnh xuất phát `SV0030`:
* **BFS (Breadth-First Search):** Sử dụng hàng đợi FIFO (Queue), duyệt mở rộng theo từng tầng khoảng cách. Rất hiệu quả để tìm lộ trình truyền tải hỗ trợ ngắn nhất từ giảng viên tới sinh viên.
* **DFS (Depth-First Search):** Sử dụng ngăn xếp LIFO (Stack) hoặc đệ quy, duyệt sâu theo một nhánh quan hệ đến tận cùng rồi mới quay lui. Hiệu quả để tìm các chu trình học tập khép kín.

Kết quả thực nghiệm duyệt đồ thị:
* Cả BFS và DFS đều tiếp cận được **$113$ sinh viên** từ nút gốc `SV0030`, minh chứng tính nhất quán về tập đỉnh đến được trong đồ thị.
* **Thành phần liên thông yếu (WCC):** Có **$430$ thành phần** (thành phần lớn nhất chứa $435$ sinh viên). Điều này phản ánh mạng lưới sinh viên tồn tại một cộng đồng trung tâm rất lớn và nhiều nhóm nhỏ rời rạc.
* **Thành phần liên thông mạnh (SCC):** Có **$1.029$ thành phần** (thành phần tương tác hai chiều lớn nhất chỉ có $10$ sinh viên). Điều này chỉ ra rằng các nhóm học tập có tương tác hai chiều chặt chẽ thường chỉ diễn ra trong các nhóm làm đồ án nhỏ (3-5 bạn).

### 6.3. Mô hình Hóa Chuỗi Markov Dự báo Hành vi Học tập
Trạng thái học tập của sinh viên qua các tuần được mô hình hóa bằng Chuỗi Markov rời rạc thời gian với không gian 3 trạng thái:
$$S = \{S_1: \text{Active (Tích cực)}, \quad S_2: \text{Moderate (Trung bình)}, \quad S_3: \text{At-risk (Nguy cơ)}\}$$

Ma trận xác suất chuyển trạng thái $P \in \mathbb{R}^{3 \times 3}$:
$$P = \begin{bmatrix} 0.75 & 0.20 & 0.05 \\ 0.20 & 0.60 & 0.20 \\ 0.05 & 0.25 & 0.70 \end{bmatrix}$$
Tổng mỗi dòng trong ma trận $P$ đều thỏa mãn điều kiện tiên quyết: $\sum_j P_{ij} = 1.0$.

> **HƯỚNG DẪN TÍNH TAY & THAY SỐ PHÉP NHÂN MA TRẬN $\pi_1 = \pi_0 P$:**
>
> **1. Nguồn gốc từng tham số:**
> * Phân phối ban đầu tại tuần khai giảng: $\pi_0 = [0.70, 0.25, 0.05]$ ($70\%$ tích cực, $25\%$ trung bình, $5\%$ nguy cơ).
> * Ma trận $P$ phản ánh xác suất giữ nguyên hoặc chuyển đổi trạng thái sau 1 tuần.
>
> **2. Thay số tính toán bước 1:**
> * Xác suất trạng thái Tích cực (Active):
>   $$\pi_{1, 1} = (0.70 \times 0.75) + (0.25 \times 0.20) + (0.05 \times 0.05) = 0.5250 + 0.0500 + 0.0025 = 0.5775 \quad (57.75\%)$$
> * Xác suất trạng thái Trung bình (Moderate):
>   $$\pi_{1, 2} = (0.70 \times 0.20) + (0.25 \times 0.60) + (0.05 \times 0.25) = 0.1400 + 0.1500 + 0.0125 = 0.3025 \quad (30.25\%)$$
> * Xác suất trạng thái Nguy cơ (At-risk):
>   $$\pi_{1, 3} = (0.70 \times 0.05) + (0.25 \times 0.20) + (0.05 \times 0.70) = 0.0350 + 0.0500 + 0.0350 = 0.1200 \quad (12.00\%)$$
> * Tổng kiểm tra xác suất: $0.5775 + 0.3025 + 0.1200 = 1.0000$ ($100\%$).

**Phân phối dừng dài hạn $\pi^*$:**
Giải hệ phương trình $\pi^* P = \pi^*$ kết hợp điều kiện chuẩn hóa $\sum \pi_i^* = 1$, ta tìm được phân phối dừng:
$$\pi^* = [0.3457, 0.3580, 0.2963]$$
* Trạng thái Tích cực (Active): **$34.57\%$**
* Trạng thái Trung bình (Moderate): **$35.80\%$**
* Trạng thái Nguy cơ (At-risk): **$29.63\%$**

### 6.4. Nhận xét nghiệm thu kỹ thuật Phần D
Mô hình Chuỗi Markov đưa ra một cảnh báo định lượng sâu sắc: Nếu không có sự can thiệp từ giảng viên, sau khoảng 10-15 tuần học, hệ thống sẽ rơi vào trạng thái dừng với gần **$30\%$ sinh viên nằm trong nhóm nguy cơ rớt môn**. Đây chính là động lực thôi thúc cần có Phần E - Tối ưu hóa phân bổ can thiệp học tập.

---

# CHƯƠNG 7. TỐI ƯU HÓA PHÂN BỔ NGUỒN LỰC HỖ TRỢ VÀ TỔNG KẾT DỰ ÁN (PHẦN E.1, E.2)

### 7.1. Bài toán Quy hoạch số nguyên nhị phân (PuLP BIP) phân bổ mentor
Để giải quyết bài toán can thiệp cho $12$ sinh viên có điểm nguy cơ cao nhất dưới giới hạn ngân sách thời gian $B = 24$ giờ làm việc của đội ngũ mentor, nhóm xây dựng mô hình Quy hoạch số nguyên nhị phân (Binary Integer Programming):
* Biến quyết định nhị phân: $x_{ij} \in \{0, 1\}$ ($1$ nếu sinh viên $i$ được nhận hỗ trợ $j$, $0$ nếu không).
* Hàm mục tiêu: Tối đa hóa tổng điểm cải thiện hiệu quả:
  $$\max Z = \sum_{i=1}^{12} \sum_{j=1}^4 c_{ij} x_{ij}$$
  Trong đó $c_{ij} = \text{Urgency}_i \times \text{Effectiveness}_j$.
* Các ràng buộc kỹ thuật:
  1. Mỗi sinh viên chỉ nhận tối đa 1 hỗ trợ: $\sum_{j=1}^4 x_{ij} \le 1, \quad \forall i$.
  2. Tổng ngân sách thời gian không vượt quá 24 giờ: $\sum_{i,j} h_j x_{ij} \le 24$.

> **HƯỚNG DẪN TÍNH TAY & THAY SỐ KIỂM TRA ĐIỂM TỐI ƯU $Z^*$:**
>
> **1. Nguồn gốc tham số:**
> * Cả 12 sinh viên đều có mức độ khẩn cấp $\text{Urgency} = 2.0$.
> * Các hình thức hỗ trợ:
>   * `One-to-one support`: Hiệu quả $e=10$, chi phí $h=4$ giờ.
>   * `Lab tutoring`: Hiệu quả $e=8$, chi phí $h=2$ giờ.
>   * `Workshop review`: Hiệu quả $e=6$, chi phí $h=1$ giờ.
>
> **2. Thay số theo phương án tối ưu tìm được:**
> * Phân bổ $1$ suất kèm 1-1: Điểm $= 1 \times (2.0 \times 10) = 20.0$, chi phí $= 1 \times 4 = 4$ giờ.
> * Phân bổ $8$ suất phụ đạo thực hành Lab: Điểm $= 8 \times (2.0 \times 8) = 128.0$, chi phí $= 8 \times 2 = 16$ giờ.
> * Phân bổ $3$ suất ôn tập Workshop: Điểm $= 3 \times (2.0 \times 6) = 36.0$, chi phí $= 3 \times 1 = 3$ giờ.
> * **Tổng ngân sách thời gian:** $4 + 16 + 3 = 23 \text{ giờ} \le 24 \text{ giờ (Thỏa mãn ràng buộc)}$.
> * **Tổng điểm tối ưu cực đại:** $Z^* = 20.0 + 128.0 + 36.0 = 184.0$.
>
> **3. Nhận xét kết quả:**
> * Toàn bộ **$12 / 12$ sinh viên nguy cơ cao** đều được nhận hỗ trợ phù hợp.
> * Giá trị tính tay $Z^* = 184.0$ trùng khớp $100\%$ với kết quả của Solver CBC trong thư viện PuLP.

Bảng kết quả phân bổ hỗ trợ chi tiết:

| Mã sinh viên | Mức khẩn cấp | Hình thức hỗ trợ phân bổ | Chi phí thời gian | Đóng góp điểm mục tiêu |
|:---:|:---:|:---|:---:|:---:|
| `SV0001` | 2.0 | One-to-one support | 4 giờ | 20.0 |
| `SV0003` | 2.0 | Lab tutoring | 2 giờ | 16.0 |
| `SV0008` | 2.0 | Lab tutoring | 2 giờ | 16.0 |
| `SV0013` | 2.0 | Workshop review | 1 giờ | 12.0 |
| `SV0037` | 2.0 | Lab tutoring | 2 giờ | 16.0 |
| `SV0045` | 2.0 | Lab tutoring | 2 giờ | 16.0 |
| `SV0057` | 2.0 | Workshop review | 1 giờ | 12.0 |
| `SV0060` | 2.0 | Lab tutoring | 2 giờ | 16.0 |
| `SV0063` | 2.0 | Lab tutoring | 2 giờ | 16.0 |
| `SV0065` | 2.0 | Workshop review | 1 giờ | 12.0 |
| `SV0071` | 2.0 | Lab tutoring | 2 giờ | 16.0 |
| `SV0073` | 2.0 | Lab tutoring | 2 giờ | 16.0 |
| **TỔNG CỘNG** | — | **12 sinh viên được hỗ trợ** | **23 / 24 giờ** | **$Z^* = 184.0$** |

### 7.2. Mạng Luồng Cực Đại (Max-Flow) & Ghép cặp Đồ thị hai phía
Khi phân bổ sinh viên vào từng mentor cụ thể, mỗi mentor có giới hạn tiếp nhận sinh viên (`capacity`) và chuyên môn riêng. Nhóm chuyển đổi bài toán ghép cặp hai phía thành mạng luồng cực đại $G' = (V', E')$:
* Đỉnh phát nguồn $s$ kết nối đến $10$ sinh viên cần hỗ trợ (dung lượng $c = 1$).
* Mỗi sinh viên kết nối đến mentor tương thích chuyên môn (dung lượng $c = 1$).
* Mỗi mentor $m_j$ kết nối đến đỉnh đích $t$ với dung lượng bằng sức chứa tối đa của mentor đó.

Kết quả giải bằng thuật toán Edmonds-Karp / Dinic:
* **Giá trị Luồng cực đại (Max Flow):** **$10$** (Ghép cặp thành công $10 / 10$ sinh viên, đạt hiệu suất $100\%$).
* **Lát cắt hẹp nhất (Min-Cut):** Theo định lý Max-Flow Min-Cut, dung lượng lát cắt cực tiểu bằng đúng $10$.
* **Phát hiện nút cổ chai (Bottlenecks):** Các cạnh từ mentor về đỉnh đích bị bão hòa dung lượng gồm:
  * Mentor `M01` (Chuyên môn Lập trình/Lab): Đạt tối đa $2/2$ sinh viên.
  * Mentor `M02` (Toán/Lý thuyết): Đạt tối đa $2/2$ sinh viên.
  * Mentor `M03` (Thực hành dự án): Đạt tối đa $3/3$ sinh viên.
  * Mentor `M04` (Cố vấn học tập): Đạt tối đa $2/2$ sinh viên.
  * Mentor `M05` (Ôn tập tổng hợp): Đạt tối đa $1/1$ sinh viên.
* **Khuyến nghị:** Nhà trường cần bổ sung thêm trợ giảng cho môn thực hành đồ án (tương ứng nhánh của `M03`) vì đây là khu vực bão hòa đầu tiên khi số lượng sinh viên gặp khó khăn gia tăng.

### 7.3. Nhận xét nghiệm thu kỹ thuật Phần E
Phần E đã chứng minh tính ứng dụng thực tiễn cao của toán học tối ưu hóa: thay vì phân bổ cảm tính, hệ thống đã tự động đưa ra phương án can thiệp tối đa hóa chất lượng giáo dục, tận dụng $23/24$ giờ ngân sách và giải quyết trọn vẹn $100\%$ các trường hợp khẩn cấp.

### 7.4. Kết luận toàn diện dự án SmartEdu AI, Bài học kinh nghiệm & Đề xuất mở rộng
* **Kết luận chung:** Dự án SmartEdu AI đã hoàn thành xuất sắc toàn bộ các mục tiêu đặt ra cho cả hai giai đoạn:
  1. Giai đoạn 1 thiết lập nền tảng dữ liệu vững chắc, chuẩn hóa $L_1/L_2$, tối ưu tổ hợp $C(8, 3)$ và giảm chiều PCA thành công giữ vững $80.19\%$ thông tin.
  2. Giai đoạn 2 khai phá xác suất Bayes ($91.32\%$ nguy cơ khi vắng học), phân loại Naive Bayes ($F1 = 69.89\%$), định lượng Entropy Information Gain, mô hình hóa mạng lưới tương tác $1.128$ sinh viên, dự báo hội tụ Markov ($29.63\%$ dừng) và tối ưu hóa phân bổ nguồn lực đạt $Z^* = 184.0$.
* **Bài học kinh nghiệm:** Việc kết hợp chặt chẽ giữa toán học lý thuyết và lập trình thực nghiệm giúp sinh viên hiểu rõ bản chất "dưới nắp ca-pô" của các thuật toán AI, tránh việc sử dụng thư viện như một hộp đen không kiểm soát.
* **Đề xuất phát triển:** Trong tương lai, hệ sinh thái SmartEdu AI có thể tích hợp trực tiếp API với hệ thống cổng thông tin đào tạo (AP/LMS) để phát thông báo đẩy (Push Notifications) tự động qua Zalo/Email cho sinh viên ngay khi chỉ số chuyên cần chạm ngưỡng cảnh báo $0.75$.

---

**DANH MỤC TÀI LIỆU THAM KHẢO:**
1. Giáo trình *Toán cho học máy (Mathematics for Machine Learning)* — FPT Polytechnic.
2. Marc Peter Deisenroth, A. Aldo Faisal, Cheng Soon Ong (2020), *Mathematics for Machine Learning*, Cambridge University Press.
3. Christopher M. Bishop (2006), *Pattern Recognition and Machine Learning*, Springer.
4. Dataset *Predict Students Dropout and Academic Success*, Kaggle Open Datasets Repository.
5. Thư viện mã nguồn mở: Scikit-learn, NetworkX, PuLP Optimization Suite Documentation.
