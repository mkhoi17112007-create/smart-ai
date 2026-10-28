import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Add project root to sys.path
sys.path.append(r'c:\HOC_HANH\Mon dang hoc\ITA201\smartedu-ai')
from src.data_processing import load_data, clean_students_data
from src.linear_algebra import extract_features_and_labels, compute_risk_scores, compute_student_distances

df_raw = load_data(r'c:\HOC_HANH\Mon dang hoc\ITA201\smartedu-ai\data')
df_clean = clean_students_data(df_raw)
X, y, feature_cols = extract_features_and_labels(df_clean)
risk_scores, weights = compute_risk_scores(X, feature_cols)
X_scaled, dist_l2, dist_l1, v1, v2 = compute_student_distances(X, feature_cols, 0, 1)

print("="*60)
print("1. CHI TIẾT TÍNH TAY: PHÉP NHÂN MA TRẬN - VECTOR s = X * w")
print("="*60)
print(f"Danh sách 8 đặc trưng: {feature_cols}")
print(f"Vector trọng số w (8 phần tử): {weights.tolist()}")
print("\nSinh viên SV0001 (Dòng 0):")
print(f"X[0] = {X[0].tolist()}")

terms_s1 = []
sum_check = 0.0
for j in range(8):
    val_x = X[0][j]
    val_w = weights[j]
    prod = val_x * val_w
    sum_check += prod
    terms_s1.append(f"({val_x} * {val_w}) = {prod:.4f}")
    print(f"  Feature {j+1} ({feature_cols[j]:<22}): X_1,{j+1} = {val_x:<5} | w_{j+1} = {val_w:<5} -> Tích = {prod:.4f}")

print(f"\nCông thức thay số cho SV0001:")
print("s_1 = " + " + ".join(terms_s1))
print(f"s_1 = {sum_check:.4f} (risk_scores[0] = {risk_scores[0]:.4f})")

print("\nSinh viên SV0002 (Dòng 1):")
print(f"X[1] = {X[1].tolist()}")
terms_s2 = []
sum_check2 = 0.0
for j in range(8):
    val_x = X[1][j]
    val_w = weights[j]
    prod = val_x * val_w
    sum_check2 += prod
    terms_s2.append(f"({val_x} * {val_w}) = {prod:.4f}")
    print(f"  Feature {j+1} ({feature_cols[j]:<22}): X_2,{j+1} = {val_x:<5} | w_{j+1} = {val_w:<5} -> Tích = {prod:.4f}")
print(f"s_2 = {sum_check2:.4f} (risk_scores[1] = {risk_scores[1]:.4f})")

print("\n" + "="*60)
print("2. CHI TIẾT TÍNH TAY: CHUẨN HÓA VÀ KHOẢNG CÁCH HÌNH HỌC L1, L2")
print("="*60)
scaler = StandardScaler()
scaler.fit(X)
means = scaler.mean_
stds = np.sqrt(scaler.var_)

print(f"{'Feature':<22} | {'Mean (mu)':<10} | {'Std (sigma)':<10} | {'SV0001 (gốc)':<12} | {'SV0001 (scaled)':<15} | {'SV0002 (gốc)':<12} | {'SV0002 (scaled)':<15}")
print("-" * 105)
for j in range(8):
    print(f"{feature_cols[j]:<22} | {means[j]:<10.4f} | {stds[j]:<10.4f} | {X[0][j]:<12.2f} | {v1[j]:<15.4f} | {X[1][j]:<12.2f} | {v2[j]:<15.4f}")

diff = v1 - v2
diff_abs = np.abs(diff)
diff_sq = diff ** 2

print("\nChi tiết độ lệch từng đặc trưng giữa SV0001 và SV0002:")
print(f"{'Feature':<22} | {'v1_j - v2_j':<15} | {'|v1_j - v2_j| (L1)':<20} | {'(v1_j - v2_j)^2 (L2)':<20}")
print("-" * 85)
for j in range(8):
    print(f"{feature_cols[j]:<22} | {diff[j]:<15.4f} | {diff_abs[j]:<20.4f} | {diff_sq[j]:<20.4f}")

print(f"\nTổng sai số tuyệt đối (L1 Norm): sum(|v1_j - v2_j|) = {np.sum(diff_abs):.4f}")
print(f"Khoảng cách Manhattan D_L1 = {dist_l1:.4f}")

print(f"\nTổng bình phương sai số: sum((v1_j - v2_j)^2) = {np.sum(diff_sq):.4f}")
print(f"Căn bậc hai (L2 Norm): sqrt({np.sum(diff_sq):.4f}) = {np.sqrt(np.sum(diff_sq)):.4f}")
print(f"Khoảng cách Euclidean D_L2 = {dist_l2:.4f}")
