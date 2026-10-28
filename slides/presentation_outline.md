# SMARTEDU AI — BÀI THUYẾT TRÌNH BẢO VỆ ĐỒ ÁN TOÁN CHO HỌC MÁY (ITA201)
## HỆ THỐNG PHÂN TÍCH HỌC TẬP, DỰ BÁO NGUY CƠ RỦI RO & TỐI ƯU HÓA CAN THIỆP GIÁO DỤC
**Đơn vị đào tạo:** Trường Cao đẳng FPT Polytechnic — Khoa Công nghệ Thông tin  
**Nhóm thực hiện:**
- Trưởng nhóm: **Nguyễn Thanh Hoài (PS47905)** — Project Manager
- Thành viên: **Nguyễn Duy Liêm (PS47845)** — Data Engineer
- Thành viên: **Nguyễn Minh Khôi (PS48256)** — Data Analyst
- Thành viên: **Vũ Quang Khải (PS48224)** — AI / Machine Learning Researcher

---

## CẤU TRÚC SLIDE BẢO VỆ (12 SLIDES CHÍNH):

### SLIDE 1: TRANG BÌA & THÔNG TIN ĐỒ ÁN
- Tiêu đề: SMARTEDU AI — BÁO CÁO BẢO VỆ ĐỒ ÁN TOÁN CHO HỌC MÁY (ITA201)
- Đơn vị: Trường Cao đẳng FPT Polytechnic — Khoa CNTT
- Thông tin thành viên nhóm và giảng viên hướng dẫn

### SLIDE 2: BỐI CẢNH & BÀI TOÁN THỰC TIỄN TRONG QUẢN TRỊ ĐÀO TẠO
- Vấn đề thực tế: Học chế tín chỉ và Blended Learning khiến sinh viên dễ nợ môn, trượt đồ án nếu mất tập trung ban đầu.
- Hạn chế: Giảng viên chỉ có bảng điểm cuối kỳ; phân bổ phụ đạo dựa vào trực giác thiếu định lượng.
- Sứ mệnh SmartEdu AI: Cảnh báo sớm dựa trên dữ liệu nhật ký học tập và tự động phân bổ nguồn lực trợ giảng tối ưu.

### SLIDE 3: KIẾN TRÚC TỔNG THỂ 5 PHÂN HỆ TOÁN HỌC
- Phần A: Đại số tuyến tính, Chuẩn hóa StandardScaler, s = Xw, Khoảng cách L1/L2, Tổ hợp C(8, 3) = 56 và Grid Search 336 mô hình.
- Phần B: Phân tích tương quan Pearson, Giảm chiều dữ liệu PCA (4 PCs giữ 80.19% phương sai), Cây quyết định (F1 = 78.06%).
- Phần C: Xác suất có điều kiện hai chiều, Định lý Bayes (chuyên cần thấp -> 91.32% rớt môn), Gaussian Naive Bayes, Information Gain.
- Phần D: Lý thuyết Đồ thị mạng lưới 1.128 sinh viên, duyệt BFS/DFS, khảo sát WCC/SCC, Chuỗi Markov 20 bước với phân phối dừng.
- Phần E: Tối ưu hóa phân bổ mentor bằng PuLP BIP (Z* = 184.0) và Mạng luồng cực đại Bipartite Max-Flow ghép cặp hoàn hảo.

### SLIDE 4: PHẦN A — ĐẠI SỐ TUYẾN TÍNH, ĐIỂM RỦI RO s = Xw & KHOẢNG CÁCH L1/L2
- Ma trận đặc trưng X (4.424 x 8) và vector nhãn y (4.424). Làm sạch dữ liệu bằng Median và Ordinal Encoding.
- Tích ma trận - vector s = Xw:
  * SV0001: s1 = -1.4400 (Tính tay thay số chi tiết, khớp 100% kết quả phần mềm).
  * SV0002: s2 = -2.1500.
- Đo lường khoảng cách hình học giữa 2 sinh viên sau chuẩn hóa StandardScaler:
  * Khoảng cách Manhattan L1 = 7.6448.
  * Khoảng cách Euclidean L2 = 4.1856.

### SLIDE 5: PHẦN B — PHÂN TÍCH THÀNH PHẦN CHÍNH (PCA) & CÂY QUYẾT ĐỊNH
- Ma trận tương quan Pearson: Lab - Assignment r = 0.68, Attendance - Risk r = -0.58.
- Chọn 4 thành phần chính (PC1..PC4) giải thích 80.19% phương sai gốc.
- Đối chiếu Cây quyết định Trước vs Sau PCA:
  * Accuracy: 79.89% -> 77.97% (chỉ giảm nhẹ 1.92%).
  * F1-Score: 80.05% -> 78.06% (đạt tiêu chuẩn thực tế >= 75%).
  * Kích thước lưu trữ giảm 50% (từ 8 chiều xuống 4 chiều).

### SLIDE 6: PHẦN C — XÁC SUẤT CÓ ĐIỀU KIỆN & ĐỊNH LÝ BAYES
- Xác suất hai chiều: P(high_risk | att_low) = 91.32% vs P(att_low | high_risk) = 56.98%.
- Thay số định lý Bayes:
  $$P(\text{high\_risk} | \text{att\_low}) = \frac{0.5698 \times 0.5007}{0.3124} = 91.32\%$$
- Mô hình Gaussian Naive Bayes:
  * Accuracy 74.69%, Precision 86.38%, Recall 58.69%, F1 69.89%.
  * Dự báo chính xác cho SV0001 với P(high_risk | X) ~ 1.0000.

### SLIDE 7: PHẦN C — LÝ THUYẾT THÔNG TIN: ENTROPY & INFORMATION GAIN
- Độ bất định của nhãn: H(S) = 1.0000 bit.
- Entropy có điều kiện H(S | attendance_bin) = 0.6617 bit.
- Information Gain: IG = 1.0000 - 0.6617 = 0.3383 bit.
- Xếp hạng đặc trưng: attendance (0.3383) > assignment (0.1672) > lab (0.1203) > participation (0.0729) > quiz (0.0057) > late_submissions (0.0053).
- Chứng minh toán học tiêu chí phân loại quan trọng nhất trong việc cảnh báo học tập.

### SLIDE 8: PHẦN D — MẠNG LƯỚI TƯƠNG TÁC HỌC TẬP & DUYỆT BFS/DFS
- Đồ thị có hướng G = (V, E) với 1.128 sinh viên và 1.500 liên kết tương tác.
- Duyệt từ SV0030: cả BFS và DFS đều tiếp cận được 113 sinh viên trong mạng thành phần.
- Phân tích tính liên thông:
  * 430 thành phần liên thông yếu (WCC) — Cụm lớn nhất 435 sinh viên.
  * 1.029 thành phần liên thông mạnh (SCC) — Tương tác hai chiều lớn nhất 10 sinh viên.
- Nhận diện các sinh viên cô lập (Isolates) cần can thiệp kết nối.

### SLIDE 9: PHẦN D — CHUỖI MARKOV DỰ BÁO HÀNH VI HỌC TẬP
- Không gian 3 trạng thái: S = {Active, Moderate, At-risk}.
- Ma trận chuyển trạng thái P (3x3).
- Thay số tính tay bước 1: pi_1 = pi_0 * P = [0.5775, 0.3025, 0.1200] (tổng bằng 1.0).
- Phân phối dừng dài hạn sau 20 bước:
  $$\pi^* = [34.57\% \text{ Active}, 35.80\% \text{ Moderate}, 29.63\% \text{ At-risk}]$$
- Cảnh báo: Gần 30% sinh viên rơi vào vùng nguy cơ nếu không có hành động can thiệp kịp thời.

### SLIDE 10: PHẦN E — TỐI ƯU HÓA PU-LP BIP & MẠNG LUỒNG CỰC ĐẠI MAX-FLOW
- Quy hoạch số nguyên nhị phân (PuLP BIP):
  * Hàm mục tiêu Max Z = 184.0, sử dụng 23/24 giờ ngân sách.
  * Can thiệp thành công trọn vẹn 12 / 12 sinh viên nguy cơ cao nhất.
- Ghép cặp Bipartite Max-Flow:
  * Max Flow = 10, ghép cặp hoàn hảo 10 / 10 sinh viên với đúng chuyên môn của mentor.
  * Phát hiện điểm nghẽn Min-Cut tại Mentor M03 (Thực hành đồ án) và M01 (Lập trình cơ bản).

### SLIDE 11: TỔNG KẾT ĐỒ ÁN VÀ ĐỀ XUẤT PHÁT TRIỂN
- Hoàn thành toàn diện 100% mục tiêu Giai đoạn 1 & Giai đoạn 2 của môn học ITA201.
- Mọi công thức toán đều có nguồn gốc tham số, số liệu thay thế cụ thể và kiểm chứng tính tay độc lập.
- Hướng mở rộng: Tích hợp API gửi thông báo Zalo tự động và xây dựng hệ thống khuyến nghị học tập cá nhân hóa.

### SLIDE 12: KẾT THÚC & TIẾP NHẬN Ý KIẾN PHẢN BIỆN (Q&A)
- Lời cảm ơn Quý Thầy Cô và Hội đồng đánh giá môn học ITA201.
- Sẵn sàng giải đáp câu hỏi và tiếp thu ý kiến đóng góp.
