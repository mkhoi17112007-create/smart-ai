import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
import os

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_table_borders(table, color="D3D3D3"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="single" w:sz="4" w:space="0" w:color="{color}"/>'
        f'  <w:bottom w:val="single" w:sz="6" w:space="0" w:color="1B365D"/>'
        f'  <w:left w:val="none"/>'
        f'  <w:right w:val="none"/>'
        f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="{color}"/>'
        f'  <w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def build_final_docx():
    doc = Document()
    base_dir = r"c:\HOC_HANH\Mon dang hoc\ITA201\smartedu-ai"
    figures_dir = os.path.join(base_dir, "outputs", "figures")
    
    # Page Margins (Standard A4: Top 2.5cm, Bottom 2.5cm, Left 3cm, Right 2cm)
    for section in doc.sections:
        section.top_margin = Inches(0.98)     # ~2.5 cm
        section.bottom_margin = Inches(0.98)  # ~2.5 cm
        section.left_margin = Inches(1.18)    # ~3.0 cm
        section.right_margin = Inches(0.79)   # ~2.0 cm

    # Base Normal Style
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(13)
    normal_style.font.color.rgb = RGBColor(0x22, 0x22, 0x22)
    normal_style.paragraph_format.line_spacing = 1.25
    normal_style.paragraph_format.space_after = Pt(4)

    # -------------------------------------------------------------
    # COVER PAGE / HEADER
    # -------------------------------------------------------------
    p_org = doc.add_paragraph()
    p_org.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_org = p_org.add_run("TRƯỜNG CAO ĐẲNG FPT POLYTECHNIC\nKHOA CÔNG NGHỆ THÔNG TIN")
    r_org.font.bold = True
    r_org.font.size = Pt(14)
    r_org.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)

    p_div = doc.add_paragraph()
    p_div.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_div.add_run("------------------***------------------").font.color.rgb = RGBColor(0x77, 0x77, 0x77)

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("BÁO CÁO TỔNG KẾT TOÀN DIỆN DỰ ÁN SMARTEDU AI\n(GIAI ĐOẠN 1 & GIAI ĐOẠN 2)\n")
    r_title.font.bold = True
    r_title.font.size = Pt(17)
    r_title.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)

    r_sub = p_title.add_run("HỆ THỐNG PHÂN TÍCH HỌC TẬP, DỰ BÁO SINH VIÊN NGUY CƠ RỦI RO\nVÀ TỐI ƯU HÓA CAN THIỆP GIÁO DỤC\nNền tảng Toán học cho Học máy (ITA201)")
    r_sub.font.bold = True
    r_sub.font.size = Pt(13)
    r_sub.font.italic = True
    r_sub.font.color.rgb = RGBColor(0x44, 0x44, 0x44)

    doc.add_paragraph().paragraph_format.space_after = Pt(14)

    # Info Table
    info_table = doc.add_table(rows=5, cols=2)
    info_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(info_table)
    
    info_data = [
        ("Tên đồ án / Dự án:", "SmartEdu AI — Hệ sinh thái Cảnh báo Nguy cơ & Hỗ trợ Cá nhân hóa"),
        ("Môn học ứng dụng:", "ITA201 — Toán cho học máy (Mathematics for Machine Learning)"),
        ("Tập dữ liệu khảo sát:", "Kaggle Predict Students Dropout and Academic Success (4.424 sinh viên, 10 thuộc tính)"),
        ("Mạng lưới tương tác:", "1.128 sinh viên, 1.500 liên kết tương tác học tập có hướng"),
        ("Đội ngũ Mentor hỗ trợ:", "5 giảng viên/mentor chuyên môn, 4 hình thức can thiệp học tập")
    ]
    for idx, (k, v) in enumerate(info_data):
        row = info_table.rows[idx]
        cell_k, cell_v = row.cells[0], row.cells[1]
        cell_k.width = Inches(2.2)
        cell_v.width = Inches(4.3)
        
        pk = cell_k.paragraphs[0]
        rk = pk.add_run(k)
        rk.bold = True
        rk.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
        
        pv = cell_v.paragraphs[0]
        pv.add_run(v)
        set_cell_background(cell_k, "F0F4F8")

    doc.add_paragraph().paragraph_format.space_after = Pt(14)

    # Member Table Title
    p_mem_t = doc.add_paragraph()
    r_mem_t = p_mem_t.add_run("DANH SÁCH THÀNH VIÊN NHÓM THỰC HIỆN:")
    r_mem_t.bold = True
    r_mem_t.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)

    mem_table = doc.add_table(rows=5, cols=4)
    mem_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(mem_table)

    headers = ["STT", "Họ và tên sinh viên", "Mã số SV", "Vai trò trong nhóm"]
    hdr_cells = mem_table.rows[0].cells
    for i, title in enumerate(headers):
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(title)
        r.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        set_cell_background(hdr_cells[i], "1B365D")

    members = [
        ("1", "Nguyễn Thanh Hoài", "PS47905", "Trưởng nhóm / Project Manager"),
        ("2", "Nguyễn Duy Liêm", "PS47845", "Data Engineer"),
        ("3", "Nguyễn Minh Khôi", "PS48256", "Data Analyst"),
        ("4", "Vũ Quang Khải", "PS48224", "AI / Machine Learning Researcher")
    ]
    for idx, (stt, name, mssv, role) in enumerate(members, start=1):
        row_cells = mem_table.rows[idx].cells
        vals = [stt, name, mssv, role]
        for c_idx, val in enumerate(vals):
            p = row_cells[c_idx].paragraphs[0]
            if c_idx in [0, 2]:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            if c_idx == 1:
                r.bold = True
        if idx % 2 == 1:
            for c_cell in row_cells:
                set_cell_background(c_cell, "F9FAFC")

    doc.add_paragraph().paragraph_format.space_after = Pt(16)

    p_loc = doc.add_paragraph()
    p_loc.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_loc = p_loc.add_run("TP. HỒ CHÍ MINH — THÁNG 10/2026")
    r_loc.font.bold = True
    r_loc.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

    doc.add_page_break()

    # -------------------------------------------------------------
    # NHẬN XÉT CỦA GIẢNG VIÊN & HỘI ĐỒNG PHẢN BIỆN
    # -------------------------------------------------------------
    def add_comment_box(title, signer):
        p_hdr = doc.add_paragraph()
        r_hdr = p_hdr.add_run(title)
        r_hdr.bold = True
        r_hdr.font.size = Pt(14)
        r_hdr.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
        
        p_box = doc.add_paragraph()
        p_box.paragraph_format.space_after = Pt(6)
        p_box.add_run(".................................................................................................................................................................................\n"
                       ".................................................................................................................................................................................\n"
                       ".................................................................................................................................................................................\n"
                       ".................................................................................................................................................................................").font.color.rgb = RGBColor(0xAA, 0xAA, 0xAA)
        
        p_sign = doc.add_paragraph()
        p_sign.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r_sign = p_sign.add_run(f"{signer} (Ký và ghi rõ họ tên):\n\n\n\n___________________________")
        r_sign.font.italic = True
        p_sign.paragraph_format.space_after = Pt(20)

    add_comment_box("NHẬN XÉT CỦA GIẢNG VIÊN HƯỚNG DẪN", "Giáo viên hướng dẫn")
    add_comment_box("NHẬN XÉT CỦA HỘI ĐỒNG PHẢN BIỆN", "HĐ phản biện")

    doc.add_page_break()

    # -------------------------------------------------------------
    # READ AND APPEND MARKDOWN REPORT CONTENT
    # -------------------------------------------------------------
    md_path = os.path.join(base_dir, "report", "Bao_Cao_Tong_Ket_SmartEdu_AI.md")
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    in_content = False
    in_table = False
    table_rows = []

    def flush_table():
        nonlocal in_table, table_rows
        if not table_rows:
            return
        
        header_cells_text = [c.strip() for c in table_rows[0].split('|')[1:-1]]
        num_cols = len(header_cells_text)
        
        valid_data_rows = []
        for r_str in table_rows:
            parts = [c.strip() for c in r_str.split('|')[1:-1]]
            if len(parts) == num_cols:
                if all(set(p).issubset({'-', ':', ' '}) for p in parts):
                    continue
                valid_data_rows.append(parts)

        if valid_data_rows:
            tbl = doc.add_table(rows=len(valid_data_rows), cols=num_cols)
            tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
            set_table_borders(tbl)
            
            for r_idx, row_parts in enumerate(valid_data_rows):
                row_cells = tbl.rows[r_idx].cells
                is_header = (r_idx == 0)
                for c_idx, text in enumerate(row_parts):
                    cell = row_cells[c_idx]
                    p = cell.paragraphs[0]
                    clean_txt = text.replace('**', '').replace('$', '')
                    if is_header:
                        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        r = p.add_run(clean_txt)
                        r.bold = True
                        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                        set_cell_background(cell, "1B365D")
                    else:
                        r = p.add_run(clean_txt)
                        if "**" in text or c_idx == 0 and ("CHƯƠNG" in text or "TỔNG" in text):
                            r.bold = True
                        if r_idx % 2 == 1:
                            set_cell_background(cell, "F9FAFC")
            doc.add_paragraph().paragraph_format.space_after = Pt(8)

        table_rows = []
        in_table = False

    def add_image_safely(img_path, caption):
        if os.path.exists(img_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            doc.add_paragraph().paragraph_format.space_before = Pt(6)
            run = p_img.add_run()
            run.add_picture(img_path, width=Inches(5.5))
            
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r_cap = p_cap.add_run(caption)
            r_cap.font.italic = True
            r_cap.font.size = Pt(11)
            r_cap.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
            p_cap.paragraph_format.space_after = Pt(10)

    for line in lines:
        raw_line = line.rstrip('\r\n')
        
        if "LỜI MỞ ĐẦU" in raw_line:
            in_content = True
        
        if not in_content:
            continue

        # Check for Markdown tables
        if raw_line.strip().startswith('|') and raw_line.strip().endswith('|'):
            in_table = True
            table_rows.append(raw_line.strip())
            continue
        elif in_table:
            flush_table()

        # Handle Headings
        if raw_line.startswith('# CHƯƠNG ') or raw_line.startswith('# LỜI MỞ ĐẦU') or raw_line.startswith('# MỤC LỤC TỔNG THỂ'):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(16)
            p.paragraph_format.space_after = Pt(8)
            title_text = raw_line.lstrip('#').strip()
            r = p.add_run(title_text)
            r.bold = True
            r.font.size = Pt(15.5)
            r.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
        elif raw_line.startswith('### '):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(4)
            sub_title = raw_line.lstrip('#').strip()
            r = p.add_run(sub_title)
            r.bold = True
            r.font.size = Pt(13.5)
            r.font.color.rgb = RGBColor(0x2B, 0x54, 0x8A)
            
            # Contextual image injections
            if "4.1." in sub_title:
                add_image_safely(os.path.join(figures_dir, "correlation_heatmap.png"), "Hình 4.1: Ma trận hệ số tương quan Pearson giữa các đặc trưng học tập")
            elif "4.4." in sub_title:
                add_image_safely(os.path.join(figures_dir, "pca_scatter_pc1_pc2.png"), "Hình 4.2: Phân bố dữ liệu trên không gian 2D tạo bởi PC1 và PC2")
            elif "5.2." in sub_title:
                add_image_safely(os.path.join(figures_dir, "gnb_confusion_matrix.png"), "Hình 5.1: Ma trận nhầm lẫn (Confusion Matrix) của mô hình Gaussian Naive Bayes")
            elif "5.3." in sub_title:
                add_image_safely(os.path.join(figures_dir, "information_gain_ranking.png"), "Hình 5.2: Biểu đồ xếp hạng Độ tăng thông tin (Information Gain) của các đặc trưng")
            elif "6.1." in sub_title:
                add_image_safely(os.path.join(figures_dir, "student_interaction_graph.png"), "Hình 6.1: Trực quan hóa mạng lưới tương tác sinh viên (Mạng con 25 đỉnh)")
            elif "6.3." in sub_title:
                add_image_safely(os.path.join(figures_dir, "markov_convergence.png"), "Hình 6.2: Đường cong hội tụ xác suất trạng thái Chuỗi Markov qua 20 bước")

        elif raw_line.startswith('---'):
            continue
        elif raw_line.startswith('> '):
            # Math blockquote
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.25)
            p.paragraph_format.space_after = Pt(3)
            quote_text = raw_line.lstrip('>').strip()
            parts = quote_text.split('**')
            for idx, part in enumerate(parts):
                r = p.add_run(part)
                if idx % 2 == 1:
                    r.bold = True
                r.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
                r.font.size = Pt(12)
        elif raw_line.startswith('* ') or raw_line.startswith('  * '):
            p = doc.add_paragraph(style='List Bullet')
            p.paragraph_format.space_after = Pt(2.5)
            bullet_text = raw_line.strip().lstrip('*').strip()
            parts = bullet_text.split('**')
            for idx, part in enumerate(parts):
                r = p.add_run(part)
                if idx % 2 == 1:
                    r.bold = True
        elif raw_line.strip():
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(5)
            parts = raw_line.strip().split('**')
            for idx, part in enumerate(parts):
                r = p.add_run(part)
                if idx % 2 == 1:
                    r.bold = True

    if in_table:
        flush_table()

    # Save final docx
    out_path = os.path.join(base_dir, "report", "Bao_Cao_Tong_Ket_SmartEdu_AI.docx")
    doc.save(out_path)
    print(f"Successfully generated final DOCX report at: {out_path}")

if __name__ == "__main__":
    build_final_docx()
