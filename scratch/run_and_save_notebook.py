import json
import nbformat
from nbclient import NotebookClient

nb_path = r'c:\HOC_HANH\Mon dang hoc\ITA201\smartedu-ai\notebooks\smartedu_assignment.ipynb'

with open(nb_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

# 1. Update Cell 8 code
cell8_code = """X, y, feature_cols = extract_features_and_labels(df_clean)
print(f"Kích thước Ma trận đặc trưng X: {X.shape}")
print(f"Kích thước Vector nhãn y: {y.shape}")

print("\\n--- MA TRẬN CON (SUB-MATRIX) 3 MẪU ĐẦU TIÊN ---")
display(pd.DataFrame(X[:3], columns=feature_cols, index=df_clean["student_id"][:3]))

# Tính điểm nguy cơ s = X * w
risk_scores, weights = compute_risk_scores(X, feature_cols)
df_clean["calculated_risk_score"] = risk_scores

print("\\n--- ĐIỂM NGUY CƠ TÍNH TỪ PHÉP NHÂN X * w (5 MẪU ĐẦU) ---")
display(df_clean[["student_id", "attendance_rate", "quiz_avg", "lab_avg", "calculated_risk_score", "risk_label"]].head())

# Kiểm chứng đối chiếu với kết quả tính tay:
s1_manual = np.dot(X[0], weights)
s2_manual = np.dot(X[1], weights)
print(f"\\n[ĐỐI CHIẾU TÍNH TAY] Điểm rủi ro SV0001 (Thay số tính tay): s1 = {s1_manual:.4f}")
print(f"[ĐỐI CHIẾU TÍNH TAY] Điểm rủi ro SV0002 (Thay số tính tay): s2 = {s2_manual:.4f}")
"""
nb['cells'][8]['source'] = cell8_code

# 2. Update Cell 11 code
cell11_code = """X_scaled, dist_l2, dist_l1, v1, v2 = compute_student_distances(X, feature_cols, idx1=0, idx2=1)

print(f"So sánh khoảng cách giữa sinh viên {df_clean['student_id'].iloc[0]} và {df_clean['student_id'].iloc[1]}:")
print(f"- Khoảng cách Euclidean (L2 Norm): {dist_l2:.4f}")
print(f"- Khoảng cách Manhattan (L1 Norm): {dist_l1:.4f}")

# Kiểm chứng đối chiếu với kết quả tính tay:
diff = v1 - v2
l1_check = np.sum(np.abs(diff))
l2_check = np.sqrt(np.sum(diff**2))
print(f"\\n[ĐỐI CHIẾU TÍNH TAY] Khoảng cách Manhattan D_L1 = sum(|v1 - v2|) = {l1_check:.4f}")
print(f"[ĐỐI CHIẾU TÍNH TAY] Khoảng cách Euclidean D_L2 = sqrt(sum((v1 - v2)^2)) = {l2_check:.4f}")
"""
nb['cells'][11]['source'] = cell11_code

# Execute notebook to update all cell outputs cleanly
client = NotebookClient(nb, timeout=600, kernel_name='python3')
client.execute()

with open(nb_path, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

print("Successfully executed notebook and updated all pre-rendered outputs!")
