import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def extract_features_and_labels(df_clean):
    """
    Tách ma trận đặc trưng X và vector nhãn y
    Lưu ý: student_id chỉ dùng định danh, KHÔNG đưa vào X.
    """
    feature_cols = [
        "attendance_rate", "quiz_avg", "lab_avg", 
        "assignment_score", "self_study_hours", 
        "late_submissions", "video_views", "participation_encoded"
    ]
    
    X = df_clean[feature_cols].values
    y = df_clean["risk_encoded"].values
    
    return X, y, feature_cols

def compute_risk_scores(X, feature_cols, weights=None):
    """
    Phép nhân ma trận-vector s = X * w để tính điểm nguy cơ đơn giản.
    """
    if weights is None:
        # Trọng số giả định phù hợp với miền giá trị các feature:
        # [attendance(0-1), quiz(0-10), lab(0-10), assign(0-10), self_study(1-15), late(0-5), video(2-35), part(0-2)]
        weights = np.array([0.25, 0.30, 0.25, -0.20, -0.15, 0.40, -0.10, -0.30])
        
    # Phép nhân ma trận-vector (Matrix-Vector multiplication)
    risk_scores = np.dot(X, weights)
    return risk_scores, weights

def compute_student_distances(X, feature_cols, idx1=0, idx2=1):
    """
    Chuẩn hóa StandardScaler và tính khoảng cách L1 (Manhattan) và L2 (Euclidean) giữa 2 sinh viên.
    """
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    v1 = X_scaled[idx1]
    v2 = X_scaled[idx2]
    
    # Khoảng cách L2 (Euclidean distance)
    dist_l2 = np.sqrt(np.sum((v1 - v2) ** 2))
    
    # Khoảng cách L1 (Manhattan distance)
    dist_l1 = np.sum(np.abs(v1 - v2))
    
    return X_scaled, dist_l2, dist_l1, v1, v2
