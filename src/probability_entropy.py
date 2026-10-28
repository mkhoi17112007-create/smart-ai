import numpy as np
import pandas as pd
import math
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

def compute_conditional_probabilities(df_clean):
    """
    Phần C.1: Tính xác suất có điều kiện hai chiều
    P(Nhãn | Feature) vs P(Feature | Nhãn)
    """
    df = df_clean.copy()
    
    # 1. Rời rạc hóa các thuộc tính liên tục
    df["attendance_group"] = np.where(df["attendance_rate"] < 0.80, "att_low", "att_high")
    df["late_sub_group"] = np.where(df["late_submissions"] > 0, "late_yes", "late_no")
    df["self_study_group"] = np.where(df["self_study_hours"] < 8.0, "study_low", "study_high")
    
    total_samples = len(df)
    n_high = (df["risk_label"] == "high_risk").sum()
    n_low = (df["risk_label"] == "low_risk").sum()
    
    results = []
    
    pairs = [
        ("attendance_group", "att_low", "Chuyên cần thấp (<80%)"),
        ("attendance_group", "att_high", "Chuyên cần cao (>=80%)"),
        ("late_sub_group", "late_yes", "Có nộp bài muộn (>0 lần)"),
        ("late_sub_group", "late_no", "Không nộp bài muộn (0 lần)"),
        ("participation_level", "Thấp", "Mức độ tham gia: Thấp"),
        ("participation_level", "Trung bình", "Mức độ tham gia: Trung bình"),
        ("participation_level", "Cao", "Mức độ tham gia: Cao"),
        ("self_study_group", "study_low", "Tự học ít (<8h/tuần)"),
        ("self_study_group", "study_high", "Tự học nhiều (>=8h/tuần)")
    ]
    
    for col, val, desc in pairs:
        subset = df[df[col] == val]
        count_feature = len(subset)
        if count_feature == 0:
            continue
            
        count_both = (subset["risk_label"] == "high_risk").sum()
        
        # P(high_risk | Feature) = Count(Feature & high_risk) / Count(Feature)
        p_risk_given_feat = count_both / count_feature
        
        # P(Feature | high_risk) = Count(Feature & high_risk) / Count(high_risk)
        p_feat_given_risk = count_both / n_high if n_high > 0 else 0
        
        results.append({
            "Thuộc tính": col,
            "Giá trị / Nhóm": desc,
            "Số mẫu có Feature": count_feature,
            "Số mẫu High Risk": count_both,
            "P(high_risk | Feature)": round(p_risk_given_feat, 4),
            "P(Feature | high_risk)": round(p_feat_given_risk, 4)
        })
        
    df_prob = pd.DataFrame(results)
    return df_prob

def train_gaussian_naive_bayes(X, y, test_size=0.2, random_state=42):
    """
    Phần C.2: Phân loại nhãn bằng Gaussian Naive Bayes
    Đánh giá mô hình trên tập Test và diễn giải các thành phần Bayes
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    gnb = GaussianNB()
    gnb.fit(X_train, y_train)
    
    y_pred = gnb.predict(X_test)
    y_proba = gnb.predict_proba(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, zero_division=0)
    rec = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)
    cm = confusion_matrix(y_test, y_pred)
    
    # Prior probabilities
    class_priors = gnb.class_prior_
    
    metrics = {
        "Accuracy": acc,
        "Precision": prec,
        "Recall": rec,
        "F1-Score": f1,
        "Confusion_Matrix": cm,
        "Priors": class_priors,
        "Classes": gnb.classes_
    }
    
    return gnb, X_train, X_test, y_train, y_test, y_pred, y_proba, metrics

def calculate_shannon_entropy(labels):
    """
    Tính Shannon Entropy H(S) của danh sách nhãn:
    H(S) = - sum(p_i * log2(p_i))
    """
    total = len(labels)
    if total == 0:
        return 0.0
    counts = pd.Series(labels).value_counts()
    entropy = 0.0
    for count in counts:
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return entropy

def compute_information_gain_ranking(df_clean):
    """
    Phần C.3: Tính Shannon Entropy ban đầu và Information Gain của các đặc trưng
    """
    df = df_clean.copy()
    
    # 1. Entropy ban đầu của tập dữ liệu
    target_col = "risk_label"
    H_parent = calculate_shannon_entropy(df[target_col])
    
    # 2. Rời rạc hóa các thuộc tính bằng pd.cut với ngưỡng miền giá trị cụ thể
    df["attendance_bin"] = pd.cut(df["attendance_rate"], bins=[-np.inf, 0.75, 0.90, np.inf], labels=["Thấp", "TB", "Cao"])
    df["quiz_bin"] = pd.cut(df["quiz_avg"], bins=[-np.inf, 2.0, 4.0, np.inf], labels=["Thấp", "TB", "Cao"])
    df["lab_bin"] = pd.cut(df["lab_avg"], bins=[-np.inf, 4.0, 7.0, np.inf], labels=["Thấp", "TB", "Cao"])
    df["assignment_bin"] = pd.cut(df["assignment_score"], bins=[-np.inf, 4.0, 7.0, np.inf], labels=["Thấp", "TB", "Cao"])
    df["late_sub_bin"] = np.where(df["late_submissions"] > 0, "Có muộn", "Không muộn")
    
    feature_list = ["attendance_bin", "quiz_bin", "lab_bin", "assignment_bin", "late_sub_bin", "participation_level"]
    
    ig_results = []
    total_len = len(df)
    
    for feat in feature_list:
        # Entropy có điều kiện H(S|A)
        H_children = 0.0
        val_counts = df[feat].value_counts()
        for val, count in val_counts.items():
            sub_labels = df[df[feat] == val][target_col]
            weight = count / total_len
            H_children += weight * calculate_shannon_entropy(sub_labels)
            
        ig = H_parent - H_children
        ig_results.append({
            "Feature": feat,
            "Entropy_Parent": round(H_parent, 4),
            "Conditional_Entropy": round(H_children, 4),
            "Information_Gain": round(ig, 4)
        })
        
    df_ig = pd.DataFrame(ig_results).sort_values(by="Information_Gain", ascending=False).reset_index(drop=True)
    return H_parent, df_ig
