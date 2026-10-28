import math
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

def compute_combinations(n, k):
    """
    Tính số tổ hợp C(n, k) = n! / (k! * (n - k)!)
    """
    return math.comb(n, k)

def compute_grid_search_space(params_dict):
    """
    Tính kích thước không gian Grid Search bằng nguyên lý nhân
    """
    total = 1
    for param_values in params_dict.values():
        total *= len(param_values)
    return total

def run_pca_analysis(X_scaled, variance_threshold=0.80):
    """
    Thực hiện PCA trên dữ liệu đã chuẩn hóa.
    Báo cáo tỉ lệ phương sai tích lũy và chọn số component sao cho bảo toàn >= 80% phương sai.
    """
    pca_full = PCA()
    X_pca_full = pca_full.fit_transform(X_scaled)
    explained_variance_ratio = pca_full.explained_variance_ratio_
    cumulative_variance = np.cumsum(explained_variance_ratio)
    
    # Chọn số component đạt ít nhất variance_threshold (80%)
    n_components = np.argmax(cumulative_variance >= variance_threshold) + 1
    
    pca_selected = PCA(n_components=n_components)
    X_pca = pca_selected.fit_transform(X_scaled)
    
    # Trực quan hóa 2 component chính PC1 - PC2
    pca_2d = PCA(n_components=2)
    X_pca_2d = pca_2d.fit_transform(X_scaled)
    
    return {
        "pca_full": pca_full,
        "explained_variance_ratio": explained_variance_ratio,
        "cumulative_variance": cumulative_variance,
        "n_components_selected": n_components,
        "X_pca": X_pca,
        "X_pca_2d": X_pca_2d,
        "pca_2d_variance": pca_2d.explained_variance_ratio_
    }

def compare_models_before_after_pca(X_raw, X_pca, y, random_state=42):
    """
    Huấn luyện và so sánh mô hình DecisionTree trên tập dữ liệu gốc vs tập sau khi giảm chiều PCA.
    """
    # Split train/test
    X_train_raw, X_test_raw, y_train, y_test = train_test_split(
        X_raw, y, test_size=0.25, random_state=random_state, stratify=y
    )
    X_train_pca, X_test_pca, _, _ = train_test_split(
        X_pca, y, test_size=0.25, random_state=random_state, stratify=y
    )
    
    # Model 1: Train on Raw Features
    clf_raw = DecisionTreeClassifier(random_state=random_state, max_depth=4)
    clf_raw.fit(X_train_raw, y_train)
    y_pred_raw = clf_raw.predict(X_test_raw)
    
    # Model 2: Train on PCA Features
    clf_pca = DecisionTreeClassifier(random_state=random_state, max_depth=4)
    clf_pca.fit(X_train_pca, y_train)
    y_pred_pca = clf_pca.predict(X_test_pca)
    
    metrics = {
        "Raw_Features": {
            "Accuracy": accuracy_score(y_test, y_pred_raw),
            "Precision": precision_score(y_test, y_pred_raw, zero_division=0),
            "Recall": recall_score(y_test, y_pred_raw, zero_division=0),
            "F1_Score": f1_score(y_test, y_pred_raw, zero_division=0),
            "Confusion_Matrix": confusion_matrix(y_test, y_pred_raw)
        },
        "PCA_Features": {
            "Accuracy": accuracy_score(y_test, y_pred_pca),
            "Precision": precision_score(y_test, y_pred_pca, zero_division=0),
            "Recall": recall_score(y_test, y_pred_pca, zero_division=0),
            "F1_Score": f1_score(y_test, y_pred_pca, zero_division=0),
            "Confusion_Matrix": confusion_matrix(y_test, y_pred_pca)
        }
    }
    
    return metrics
