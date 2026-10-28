import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

def create_deck():
    prs = Presentation()
    # Set slide dimensions to 16:9 widescreen (10 inches by 5.625 inches)
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    base_dir = r"c:\HOC_HANH\Mon dang hoc\ITA201\smartedu-ai"
    figures_dir = os.path.join(base_dir, "outputs", "figures")
    slides_dir = os.path.join(base_dir, "slides")
    os.makedirs(slides_dir, exist_ok=True)

    blank_layout = prs.slide_layouts[6] # Blank slide

    def add_header(slide, title_text, category="SMARTEDU AI - BÁO CÁO BẢO VỆ ĐỒ ÁN TOÁN HỌC CHO HỌC MÁY (ITA201)"):
        # Header category
        tb_cat = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.5), Inches(0.4))
        p_c = tb_cat.text_frame.paragraphs[0]
        p_c.text = category.upper()
        p_c.font.size = Pt(11)
        p_c.font.bold = True
        p_c.font.color.rgb = RGBColor(0x7F, 0x8C, 0x8D)

        # Header title
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.5), Inches(0.8))
        p = tb.text_frame.paragraphs[0]
        p.text = title_text
        p.font.size = Pt(24)
        p.font.bold = True
        p.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)

    # -------------------------------------------------------------
    # SLIDE 1: TITLE SLIDE
    # -------------------------------------------------------------
    s1 = prs.slides.add_slide(blank_layout)
    tb1 = s1.shapes.add_textbox(Inches(1.0), Inches(1.2), Inches(11.3), Inches(4.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p1 = tf1.paragraphs[0]
    p1.text = "TRƯỜNG CAO ĐẲNG FPT POLYTECHNIC — KHOA CNTT"
    p1.font.size = Pt(14)
    p1.font.bold = True
    p1.font.color.rgb = RGBColor(0xE6, 0x7E, 0x22)

    p2 = tf1.add_paragraph()
    p2.text = "SMARTEDU AI — BÁO CÁO TỔNG KẾT BẢO VỆ ĐỒ ÁN"
    p2.font.size = Pt(28)
    p2.font.bold = True
    p2.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
    p2.space_before = Pt(12)

    p3 = tf1.add_paragraph()
    p3.text = "Hệ thống Phân tích Học tập, Dự báo Sinh viên Nguy cơ & Tối ưu hóa Can thiệp Giáo dục\nNền tảng Toán học cho Học máy (ITA201 — Toàn diện Giai đoạn 1 & 2)"
    p3.font.size = Pt(16)
    p3.font.italic = True
    p3.font.color.rgb = RGBColor(0x34, 0x49, 0x5E)
    p3.space_before = Pt(8)

    p4 = tf1.add_paragraph()
    p4.text = "NHÓM THỰC HIỆN:\n• Trưởng nhóm: Nguyễn Thanh Hoài — PS47905\n• Thành viên: Nguyễn Duy Liêm (PS47845) | Nguyễn Minh Khôi (PS48256) | Vũ Quang Khải (PS48224)"
    p4.font.size = Pt(14)
    p4.font.bold = True
    p4.font.color.rgb = RGBColor(0x2C, 0x3E, 0x50)
    p4.space_before = Pt(24)

    # -------------------------------------------------------------
    # SLIDE 2: BỐI CẢNH & BÀI TOÁN
    # -------------------------------------------------------------
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "1. Bối cảnh & Bài toán Thực tiễn trong Quản trị Đào tạo")
    tb2 = s2.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.5), Inches(5.0))
    tf2 = tb2.text_frame
    tf2.word_wrap = True

    pts2 = [
        "Vấn đề đào tạo tín chỉ & Blended Learning: Tỷ lệ sinh viên nợ môn, trượt đồ án và bỏ học tích lũy âm thầm nếu không được phát hiện từ sớm.",
        "Hạn chế của phương pháp truyền thống: Giảng viên chỉ nắm điểm số vào cuối kỳ, thiếu công cụ định lượng nguy cơ và phân bổ phụ đạo dựa trên cảm tính.",
        "Giải pháp SmartEdu AI: Xây dựng hệ sinh thái khép kín từ Dữ liệu -> Toán học học máy -> Cảnh báo sớm -> Tối ưu hóa can thiệp.",
        "Quy mô khảo sát: 4.424 sinh viên chuẩn hóa từ Kaggle, 1.128 sinh viên trong mạng lưới tương tác xã hội học tập, 5 chuyên môn mentor phụ đạo.",
        "Mục tiêu cốt lõi: Kết hợp tính chính xác toán học (Explainable AI) với hiệu quả can thiệp thực tế tại FPT Polytechnic."
    ]
    for pt in pts2:
        p = tf2.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(15)
        p.space_after = Pt(14)

    # -------------------------------------------------------------
    # SLIDE 3: KIẾN TRÚC 5 PHÂN HỆ TOÁN HỌC
    # -------------------------------------------------------------
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "2. Kiến trúc Tổng thể 5 Phân hệ Toán học SmartEdu AI")
    tb3 = s3.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.5), Inches(5.0))
    tf3 = tb3.text_frame
    tf3.word_wrap = True

    pts3 = [
        "Phần A - Đại số tuyến tính & Tổ hợp: Làm sạch Median, chuẩn hóa StandardScaler, s = Xw, khoảng cách L1/L2, tổ hợp C(8, 3) = 56 và Grid Search 336 mô hình.",
        "Phần B - PCA & Cây quyết định: Ma trận tương quan Pearson, giảm chiều trực giao từ 8 xuống 4 thành phần chính (bảo toàn 80.19% phương sai), F1-Score đạt 78.06%.",
        "Phần C - Xác suất Bayes & Entropy: Xác suất có điều kiện hai chiều, kiểm chứng Bayes (vắng học -> 91.32% rớt môn), GaussianNB (Precision 86.38%), Information Gain chọn lọc đặc trưng.",
        "Phần D - Lý thuyết Đồ thị & Markov: Mạng lưới 1.128 đỉnh và 1.500 cạnh, duyệt BFS/DFS, khảo sát WCC/SCC, mô hình hóa chuyển dịch hành vi Markov qua 20 bước với phân phối dừng dài hạn.",
        "Phần E - Tối ưu hóa nguồn lực can thiệp: Quy hoạch số nguyên nhị phân PuLP BIP (Z* = 184.0, hỗ trợ 12/12 SV nguy cơ) và Mạng luồng cực đại Bipartite Max-Flow ghép cặp hoàn hảo."
    ]
    for pt in pts3:
        p = tf3.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(14.5)
        p.space_after = Pt(12)

    # -------------------------------------------------------------
    # SLIDE 4: PHẦN A - ĐẠI SỐ TUYẾN TÍNH & TÍNH TAY s = Xw
    # -------------------------------------------------------------
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "3. Phần A: Đại số tuyến tính, Điểm rủi ro s = Xw & Khoảng cách L1/L2")
    tb4 = s4.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.5), Inches(5.0))
    tf4 = tb4.text_frame
    tf4.word_wrap = True

    pts4 = [
        "Biểu diễn dữ liệu: Ma trận đặc trưng X (4.424 x 8) và vector nhãn y (4.424 x 1). Làm sạch missing bằng Median và Ordinal Encoding.",
        "Công thức điểm rủi ro tuyến tính: s = X * w (với w = [0.25, 0.30, 0.25, -0.20, -0.15, 0.40, -0.10, -0.30]^T).",
        "Đối chiếu tính tay cụ thể từng bước:",
        "  - Sinh viên SV0001: s1 = 0.5(0.25) + 2.0(0.30) + 0(0.25) + 0(-0.20) + 9.1(-0.15) + 0(0.40) + 5(-0.10) + 1(-0.30) = -1.4400 (Trùng khớp 100% code).",
        "  - Sinh viên SV0002: s2 = 0.6(0.25) + 2.0(0.30) + 7.0(0.25) + 6.8(-0.20) + 8.6(-0.15) + 0(0.40) + 17(-0.10) + 1(-0.30) = -2.1500.",
        "Chuẩn hóa StandardScaler và Đo khoảng cách hình học:",
        "  - Khoảng cách Manhattan (L1 norm): D_L1(z1, z2) = 7.6448 (Phản ánh tổng độ lệch tuyệt đối giữa 2 hồ sơ học tập).",
        "  - Khoảng cách Euclidean (L2 norm): D_L2(z1, z2) = 4.1856 (Khoảng cách không gian đa chiều, làm tiền đề phân cụm K-Means)."
    ]
    for pt in pts4:
        p = tf4.add_paragraph()
        p.text = pt
        p.font.size = Pt(13.5)
        p.space_after = Pt(6)

    # -------------------------------------------------------------
    # SLIDE 5: PHẦN B - PCA & HEATMAP TƯƠNG QUAN
    # -------------------------------------------------------------
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "4. Phần B: Phân tích Thành phần chính (PCA) & Giảm chiều dữ liệu")
    tb5 = s5.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(6.0), Inches(5.0))
    tf5 = tb5.text_frame
    tf5.word_wrap = True

    pts5 = [
        "Phát hiện Đa cộng tuyến: Cặp Lab - Assignment đạt r = 0.68, Chuyên cần - Nguy cơ r = -0.58. Dữ liệu chứa nhiều thông tin dư thừa tuyến tính.",
        "Thuật toán PCA: Giải bài toán trị riêng ma trận hiệp phương sai trực giao.",
        "Tỷ lệ phương sai tích lũy của các thành phần:",
        "  - PC1: 32.45% | PC2: 19.82% | PC3: 15.12% | PC4: 12.80%",
        "  - Tổng 4 PCs đầu: 80.19% (Đạt ngưỡng kỹ thuật >= 80%).",
        "Hiệu năng Cây quyết định Trước vs Sau PCA:",
        "  - Trước PCA (8 chiều): Accuracy 79.89%, F1-Score 80.05%.",
        "  - Sau PCA (4 chiều): Accuracy 77.97%, F1-Score 78.06%.",
        "Kết luận: Giảm 50% số chiều dữ liệu nhưng hiệu năng F1 chỉ suy giảm 1.99%, tối ưu hóa tốc độ huấn luyện và bộ nhớ."
    ]
    for pt in pts5:
        p = tf5.add_paragraph()
        p.text = pt
        p.font.size = Pt(12.5)
        p.space_after = Pt(6)

    # Add heatmap picture
    img_heatmap = os.path.join(figures_dir, "correlation_heatmap.png")
    if os.path.exists(img_heatmap):
        s5.shapes.add_picture(img_heatmap, Inches(7.2), Inches(1.6), width=Inches(5.3))

    # -------------------------------------------------------------
    # SLIDE 6: PHẦN C - XÁC SUẤT BAYES & GAUSSIAN NAIVE BAYES
    # -------------------------------------------------------------
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "5. Phần C: Xác suất có điều kiện, Định lý Bayes & Gaussian Naive Bayes")
    tb6 = s6.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(6.2), Inches(5.0))
    tf6 = tb6.text_frame
    tf6.word_wrap = True

    pts6 = [
        "Bảng xác suất có điều kiện hai chiều:",
        "  - P(high_risk | att_low) = 91.32% vs P(att_low | high_risk) = 56.98%.",
        "Kiểm chứng định lý Bayes tính tay:",
        "  P(high | att_low) = [P(att_low | high) * P(high)] / P(att_low)",
        "                    = [0.5698 * 0.5007] / 0.3124 = 91.32% (Trùng khớp tuyệt đối).",
        "  Ý nghĩa: Vắng học quá quy định đẩy nguy cơ rớt môn lên tới 91.32%!",
        "Mô hình phân loại Gaussian Naive Bayes:",
        "  - Accuracy: 74.69% | Precision: 86.38% | F1-Score: 69.89%.",
        "  - Dự báo SV0001: P(high_risk | X) ~ 1.0000 do điểm Lab = 0 và vắng học nhiều."
    ]
    for pt in pts6:
        p = tf6.add_paragraph()
        p.text = pt
        p.font.size = Pt(13)
        p.space_after = Pt(6)

    img_gnb = os.path.join(figures_dir, "gnb_confusion_matrix.png")
    if os.path.exists(img_gnb):
        s6.shapes.add_picture(img_gnb, Inches(7.3), Inches(1.6), width=Inches(5.2))

    # -------------------------------------------------------------
    # SLIDE 7: PHẦN C - SHANNON ENTROPY & INFORMATION GAIN
    # -------------------------------------------------------------
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "6. Phần C: Lý thuyết Thông tin — Shannon Entropy & Information Gain")
    tb7 = s7.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(6.2), Inches(5.0))
    tf7 = tb7.text_frame
    tf7.word_wrap = True

    pts7 = [
        "Đo lường độ bất định thông tin của nhãn rủi ro:",
        "  H(S) = - [0.4993 log2(0.4993) + 0.5007 log2(0.5007)] = 1.0000 bit (Bất định tối đa).",
        "Tính tay Entropy có điều kiện H(S | attendance_bin):",
        "  - Nhóm att_low: H(S1) = 0.4258 bit (tỷ trọng 0.3124).",
        "  - Nhóm att_med: H(S2) = 0.9627 bit (tỷ trọng 0.2098).",
        "  - Nhóm att_high: H(S3) = 0.6837 bit (tỷ trọng 0.4778).",
        "  -> H(S | attendance) = 0.6617 bit.",
        "Độ tăng thông tin: IG = 1.0000 - 0.6617 = 0.3383 bit (Đứng đầu bảng).",
        "Xếp hạng: attendance (0.3383) > assignment (0.1672) > lab (0.1203) > quiz (0.0057).",
        "Ý nghĩa: Giải thích toán học vì sao Cây quyết định luôn chọn tiêu chí chuyên cần làm gốc phân loại."
    ]
    for pt in pts7:
        p = tf7.add_paragraph()
        p.text = pt
        p.font.size = Pt(12.5)
        p.space_after = Pt(6)

    img_ig = os.path.join(figures_dir, "information_gain_ranking.png")
    if os.path.exists(img_ig):
        s7.shapes.add_picture(img_ig, Inches(7.3), Inches(1.6), width=Inches(5.2))

    # -------------------------------------------------------------
    # SLIDE 8: PHẦN D - MẠNG LƯỚI TƯƠNG TÁC SINH VIÊN (BFS/DFS)
    # -------------------------------------------------------------
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "7. Phần D: Lý thuyết Đồ thị — Mạng lưới Tương tác Sinh viên")
    tb8 = s8.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(6.2), Inches(5.0))
    tf8 = tb8.text_frame
    tf8.word_wrap = True

    pts8 = [
        "Mô hình hóa Đồ thị có hướng G = (V, E):",
        "  - Số đỉnh |V|: 1.128 sinh viên tham gia tương tác trao đổi bài.",
        "  - Số cạnh |E|: 1.500 mối liên kết có hướng (hỏi bài / làm việc nhóm).",
        "Thuật toán duyệt đồ thị BFS & DFS từ gốc SV0030:",
        "  - Cả 2 thuật toán đều tiếp cận được 113 sinh viên.",
        "  - BFS: Tìm đường truyền thông tin ngắn nhất qua Queue FIFO.",
        "  - DFS: Khám phá chu trình trao đổi sâu qua Stack/Đệ quy.",
        "Phân tích tính liên thông mạng lưới:",
        "  - 430 thành phần liên thông yếu (WCC) — Cụm lớn nhất 435 sinh viên.",
        "  - 1.029 thành phần liên thông mạnh (SCC) — Nhóm tương tác hai chiều lớn nhất 10 sinh viên.",
        "Cảnh báo sinh viên cô lập (Isolates): In-degree = Out-degree = 0, cần giảng viên chủ động kết nối vào nhóm."
    ]
    for pt in pts8:
        p = tf8.add_paragraph()
        p.text = pt
        p.font.size = Pt(12.5)
        p.space_after = Pt(6)

    img_graph = os.path.join(figures_dir, "student_interaction_graph.png")
    if os.path.exists(img_graph):
        s8.shapes.add_picture(img_graph, Inches(7.3), Inches(1.6), width=Inches(5.2))

    # -------------------------------------------------------------
    # SLIDE 9: PHẦN D - CHUỖI MARKOV DỰ BÁO HÀNH VI HỌC TẬP
    # -------------------------------------------------------------
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "8. Phần D: Chuỗi Markov — Mô hình Hóa Chuyển dịch Trạng thái Học tập")
    tb9 = s9.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(6.2), Inches(5.0))
    tf9 = tb9.text_frame
    tf9.word_wrap = True

    pts9 = [
        "Không gian 3 trạng thái: S = {Active, Moderate, At-risk}.",
        "Ma trận xác suất chuyển trạng thái P (3x3):",
        "  [[0.75, 0.20, 0.05], [0.20, 0.60, 0.20], [0.05, 0.25, 0.70]].",
        "Tính tay bước 1 phép nhân ma trận pi_1 = pi_0 * P (pi_0 = [0.70, 0.25, 0.05]):",
        "  - pi_1(Active) = 0.70(0.75) + 0.25(0.20) + 0.05(0.05) = 0.5775 (57.75%).",
        "  - pi_1(Moderate) = 0.70(0.20) + 0.25(0.60) + 0.05(0.25) = 0.3025 (30.25%).",
        "  - pi_1(At-risk) = 0.70(0.05) + 0.25(0.20) + 0.05(0.70) = 0.1200 (12.00%).",
        "  (Tổng xác suất = 1.0000, trùng khớp mô phỏng).",
        "Phân phối dừng dài hạn sau 20 bước (pi* P = pi*):",
        "  pi* = [34.57% Active, 35.80% Moderate, 29.63% At-risk].",
        "Kết luận: Nếu không can thiệp, gần 30% sinh viên sẽ trôi dạt vào vùng nguy cơ rớt môn thường trực!"
    ]
    for pt in pts9:
        p = tf9.add_paragraph()
        p.text = pt
        p.font.size = Pt(12)
        p.space_after = Pt(6)

    img_markov = os.path.join(figures_dir, "markov_convergence.png")
    if os.path.exists(img_markov):
        s9.shapes.add_picture(img_markov, Inches(7.3), Inches(1.6), width=Inches(5.2))

    # -------------------------------------------------------------
    # SLIDE 10: PHẦN E - TỐI ƯU HÓA PU-LP & MAX-FLOW
    # -------------------------------------------------------------
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "9. Phần E: Tối ưu hóa Can thiệp Giáo dục — PuLP BIP & Max-Flow")
    tb10 = s10.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.5), Inches(5.0))
    tf10 = tb10.text_frame
    tf10.word_wrap = True

    pts10 = [
        "1. Quy hoạch số nguyên nhị phân (PuLP BIP):",
        "  - Mục tiêu: Max Z = sum(c_ij * x_ij) với ràng buộc mỗi SV nhận tối đa 1 hỗ trợ và tổng ngân sách <= 24 giờ.",
        "  - Kết quả tối ưu: Z* = 184.0, sử dụng 23/24 giờ ngân sách, can thiệp trọn vẹn 12 / 12 sinh viên nguy cơ cao nhất.",
        "  - Phân bổ: 1 SV kèm 1-1 (One-to-one: 4h, điểm 20.0), 8 SV kèm Lab (Lab tutoring: 16h, điểm 128.0), 3 SV Workshop (3h, điểm 36.0).",
        "2. Mạng luồng cực đại (Max-Flow) & Ghép cặp Đồ thị hai phía:",
        "  - Xây dựng mạng luồng s -> 10 Sinh viên -> 5 Mentors -> t với dung lượng tương thích chuyên môn và sức chứa.",
        "  - Giá trị Max-Flow = 10 (Ghép cặp thành công 10 / 10 sinh viên, đạt hiệu suất 100%).",
        "  - Định lý Max-Flow Min-Cut: Phát hiện điểm nghẽn tại Mentor M03 (Thực hành đồ án) và M01 (Lập trình cơ bản), khuyến nghị nhà trường ưu tiên bổ sung trợ giảng vào các phân môn này."
    ]
    for pt in pts10:
        p = tf10.add_paragraph()
        p.text = pt
        p.font.size = Pt(13.5)
        p.space_after = Pt(8)

    # -------------------------------------------------------------
    # SLIDE 11: TỔNG KẾT ĐỒ ÁN & HƯỚNG PHÁT TRIỂN
    # -------------------------------------------------------------
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "10. Tổng kết Đồ án SmartEdu AI & Hướng Mở rộng")
    tb11 = s11.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.5), Inches(5.0))
    tf11 = tb11.text_frame
    tf11.word_wrap = True

    pts11 = [
        "Kết quả đạt được: Hoàn thành 100% tất cả các mục tiêu kỹ thuật và toán học của môn ITA201 qua 5 phân hệ A, B, C, D, E.",
        "Tính minh bạch toán học: Mọi công thức (s = Xw, khoảng cách L1/L2, tổ hợp C(8, 3), tỷ lệ phương sai PCA, định lý Bayes, Entropy Shannon, Markov chuyển bước, hàm mục tiêu LP) đều được giải thích rõ nguồn gốc tham số, thay số tính tay và đối chiếu trùng khớp hoàn hảo với mã nguồn.",
        "Giá trị thực tiễn: Đề xuất một giải pháp quản trị học tập thông minh hoàn chỉnh, sẵn sàng tích hợp với LMS của FPT Polytechnic.",
        "Hướng phát triển tiếp theo:",
        "  - Tích hợp hệ thống thông báo đẩy tự động qua Zalo OA / Email khi sinh viên chạm ngưỡng cảnh báo chuyên cần (attendance <= 0.75).",
        "  - Nghiên cứu mô hình học tăng cường (Reinforcement Learning) để tự động điều chỉnh lộ trình học tập cá nhân hóa."
    ]
    for pt in pts11:
        p = tf11.add_paragraph()
        p.text = pt
        p.font.size = Pt(14)
        p.space_after = Pt(10)

    # -------------------------------------------------------------
    # SLIDE 12: KẾT THÚC / Q&A
    # -------------------------------------------------------------
    s12 = prs.slides.add_slide(blank_layout)
    tb12 = s12.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(11.3), Inches(3.5))
    tf12 = tb12.text_frame
    tf12.word_wrap = True

    p_end = tf12.paragraphs[0]
    p_end.alignment = PP_ALIGN.CENTER
    p_end.text = "XIN TRÂN TRỌNG CẢM ƠN QUÝ THẦY CÔ\nVÀ HỘI ĐỒNG PHẢN BIỆN!"
    p_end.font.size = Pt(30)
    p_end.font.bold = True
    p_end.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)

    p_qa = tf12.add_paragraph()
    p_qa.alignment = PP_ALIGN.CENTER
    p_qa.text = "SMARTEDU AI — NHÓM THỰC HIỆN\nTrưởng nhóm: Nguyễn Thanh Hoài (PS47905)\nNguyễn Duy Liêm (PS47845) | Nguyễn Minh Khôi (PS48256) | Vũ Quang Khải (PS48224)\n\n--- SẴN SÀNG TIẾP NHẬN CÂU HỎI & GÓP Ý (Q&A) ---"
    p_qa.font.size = Pt(16)
    p_qa.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
    p_qa.space_before = Pt(20)

    out_pptx = os.path.join(slides_dir, "SmartEdu_AI_Defense_Presentation.pptx")
    prs.save(out_pptx)
    print(f"Successfully generated PowerPoint presentation deck at: {out_pptx}")

if __name__ == "__main__":
    create_deck()
