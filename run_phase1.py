import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure sys stdout handles utf-8 cleanly
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Add src to path
base_dir = r"c:\HOC_HANH\Mon dang hoc\ITA201\smartedu-ai"
src_dir = os.path.join(base_dir, "src")
data_dir = os.path.join(base_dir, "data")
outputs_dir = os.path.join(base_dir, "outputs")
figures_dir = os.path.join(outputs_dir, "figures")
tables_dir = os.path.join(outputs_dir, "tables")

sys.path.append(src_dir)

from data_processing import load_data, clean_students_data
from linear_algebra import extract_features_and_labels, compute_risk_scores, compute_student_distances
from pca_analysis import compute_combinations, compute_grid_search_space, run_pca_analysis, compare_models_before_after_pca

print("==========================================================")
print("     SMARTEDU AI - ASSIGNMENT PHASE 1 EVALUATION          ")
print("==========================================================")

# 1. Load & Clean Data
students = load_data(data_dir)
print(f"\n[PHẦN A.1] Dữ liệu ban đầu: {students.shape[0]} dòng, {students.shape[1]} cột.")
print(f"Số lượng giá trị missing ban đầu:\n{students.isnull().sum()[students.isnull().sum() > 0]}")

df_clean = clean_students_data(students)
print(f"Sau khi làm sạch & điền median, số giá trị thiếu: {df_clean.isnull().sum().sum()}")
print("Đã mã hóa participation_level (Thấp:0, Trung bình:1, Cao:2) & risk_label (high_risk:1, low_risk:0).")

# 2. Extract Features X and Labels y
X, y, feature_cols = extract_features_and_labels(df_clean)
print(f"\n[PHẦN A.2] Kích thước ma trận đặc trưng X: {X.shape} (m={X.shape[0]} sinh viên, n={X.shape[1]} đặc trưng).")
print(f"Kích thước vector nhãn y: {y.shape}")

print("\n--- Ma trận con (Sub-matrix) 3 mẫu đầu tiên ---")
df_sub = pd.DataFrame(X[:3], columns=feature_cols, index=df_clean["student_id"][:3])
print(df_sub)

# Matrix-Vector Multiplication: Risk Score
risk_scores, weights = compute_risk_scores(X, feature_cols)
df_clean["calculated_risk_score"] = risk_scores
print("\n--- Phép nhân Ma trận-Vector s = X * w (5 mẫu đầu) ---")
for i in range(5):
    print(f"Mã SV {df_clean['student_id'].iloc[i]}: Risk Score = {risk_scores[i]:.2f} | Nhãn thực tế = {df_clean['risk_label'].iloc[i]}")

# 3. Norms & Distances
X_scaled, dist_l2, dist_l1, v1, v2 = compute_student_distances(X, feature_cols, idx1=0, idx2=1)
sv1_id = df_clean['student_id'].iloc[0]
sv2_id = df_clean['student_id'].iloc[1]

print(f"\n[PHẦN A.3] So sánh 2 sinh viên cụ thể: {sv1_id} và {sv2_id}")
print(f"- Khoảng cách Euclidean (L2 Norm): {dist_l2:.4f}")
print(f"- Khoảng cách Manhattan (L1 Norm): {dist_l1:.4f}")

# 4. Combinatorics
total_features = len(feature_cols)
k_select = 3
c_val = compute_combinations(total_features, k_select)
print(f"\n[PHẦN A.4] Tổ hợp & Không gian tìm kiếm:")
print(f"- Số cách chọn {k_select} đặc trưng từ {total_features} đặc trưng: C({total_features}, {k_select}) = {c_val}")

grid_params = {"learning_rate": [0.01, 0.05, 0.1], "max_depth": [3, 5], "n_estimators": [50, 100]}
grid_size = compute_grid_search_space(grid_params)
print(f"- Kích thước không gian Grid Search với {grid_params}: {grid_size} cấu hình.")

# 5. Correlation & PCA
print(f"\n[PHẦN B.1 & B.2] Phân tích Tương quan & PCA")
corr_matrix = pd.DataFrame(X, columns=feature_cols).corr()

# Plot & Save Correlation Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
plt.title("Correlation Heatmap of Student Features")
plt.tight_layout()
heatmap_path = os.path.join(figures_dir, "correlation_heatmap.png")
plt.savefig(heatmap_path, dpi=300)
plt.close()
print(f"Đã lưu heatmap tương quan tại: {heatmap_path}")

# Run PCA
pca_res = run_pca_analysis(X_scaled, variance_threshold=0.80)
print(f"- Tỉ lệ phương sai từng Component: {np.round(pca_res['explained_variance_ratio'], 4)}")
print(f"- Tỉ lệ phương sai tích lũy: {np.round(pca_res['cumulative_variance'], 4)}")
print(f"- Số component được chọn (bảo toàn >= 80% phương sai): {pca_res['n_components_selected']} components")

# Plot & Save PC1 vs PC2 Scatter Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(
    x=pca_res['X_pca_2d'][:, 0],
    y=pca_res['X_pca_2d'][:, 1],
    hue=df_clean['risk_label'],
    palette={"high_risk": "red", "low_risk": "green"},
    style=df_clean['risk_label'],
    s=80
)
plt.xlabel("Principal Component 1 (PC1)")
plt.ylabel("Principal Component 2 (PC2)")
plt.title("Scatter Plot PC1 vs PC2 colored by Risk Label")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
pca_scatter_path = os.path.join(figures_dir, "pca_scatter_pc1_pc2.png")
plt.savefig(pca_scatter_path, dpi=300)
plt.close()
print(f"Đã lưu biểu đồ PCA Scatter tại: {pca_scatter_path}")

# 6. Model Comparison Before & After PCA
model_metrics = compare_models_before_after_pca(X_scaled, pca_res['X_pca'], y)
print("\n[PHẦN B.3] So sánh hiệu năng mô hình Decision Tree (Trước vs Sau PCA):")
df_comparison = pd.DataFrame(model_metrics).T[["Accuracy", "Precision", "Recall", "F1_Score"]]
print(df_comparison.to_string())

comparison_csv_path = os.path.join(tables_dir, "pca_model_comparison.csv")
df_comparison.to_csv(comparison_csv_path)
print(f"Đã xuất bảng đối chiếu mô hình tại: {comparison_csv_path}")

print("\n==========================================================")
print("    ĐÃ HOÀN THÀNH TOÀN BỘ CÁC BƯỚC THỰC HIỆN GIAI ĐOẠN 1   ")
print("==========================================================")
