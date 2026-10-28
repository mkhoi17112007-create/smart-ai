import os
import pandas as pd
import numpy as np

def load_data(data_dir):
    """
    Đọc file dữ liệu sinh viên students.csv từ thư mục data/ cho Giai đoạn 1
    """
    students_path = os.path.join(data_dir, "students.csv")
    students = pd.read_csv(students_path)
    return students

def clean_students_data(df):
    """
    Làm sạch dữ liệu sinh viên cho Giai đoạn 1:
    - Xử lý giá trị thiếu (Missing Values) bằng phương pháp điền trung vị (median)
    - Mã hóa đặc trưng phân loại (participation_level: Thấp->0, Trung bình->1, Cao->2)
    - Mã hóa nhãn nguy cơ (risk_label: high_risk->1, low_risk->0)
    - Tách riêng student_id
    """
    df_clean = df.copy()
    
    # 1. Điền giá trị thiếu (Missing Values) bằng median
    num_cols = ["attendance_rate", "quiz_avg", "lab_avg", "assignment_score", "self_study_hours", "late_submissions", "video_views"]
    for col in num_cols:
        if df_clean[col].isnull().sum() > 0:
            median_val = df_clean[col].median()
            df_clean[col] = df_clean[col].fillna(median_val)
            
    # 2. Mã hóa đặc trưng phân loại participation_level
    mapping = {"Thấp": 0, "Trung bình": 1, "Cao": 2}
    df_clean["participation_encoded"] = df_clean["participation_level"].map(mapping)
    
    # 3. Mã hóa nhãn nguy cơ risk_label: high_risk -> 1, low_risk -> 0
    df_clean["risk_encoded"] = df_clean["risk_label"].map({"high_risk": 1, "low_risk": 0})
    
    return df_clean
