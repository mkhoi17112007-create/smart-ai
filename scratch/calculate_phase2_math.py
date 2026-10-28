import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

import os
import pandas as pd
import numpy as np

sys.path.append(r'c:\HOC_HANH\Mon dang hoc\ITA201\smartedu-ai')
from src.data_processing import load_data, clean_students_data
from src.linear_algebra import extract_features_and_labels
from src.probability_entropy import compute_conditional_probabilities, train_gaussian_naive_bayes, compute_information_gain_ranking
from src.graph_markov import simulate_markov_learning_behavior
from src.optimization import solve_mentor_allocation_lp, solve_bipartite_max_flow

base_dir = r"c:\HOC_HANH\Mon dang hoc\ITA201\smartedu-ai"
data_dir = os.path.join(base_dir, "data")
students = load_data(data_dir)
df_clean = clean_students_data(students)
X, y, feature_cols = extract_features_and_labels(df_clean)

print("="*60)
print("1. CHI TIẾT TÍNH TAY BAYES & XÁC SUẤT CÓ ĐIỀU KIỆN (C.1, C.2)")
print("="*60)
# C.1 Conditional Probabilities
total_N = len(df_clean)
num_high = (df_clean["risk_label"] == "high_risk").sum()
num_low = (df_clean["risk_label"] == "low_risk").sum()
p_high = num_high / total_N
p_low = num_low / total_N

# Attendance bin
df_clean["att_bin"] = pd.cut(df_clean["attendance_rate"], bins=[-np.inf, 0.75, 0.90, np.inf], labels=["att_low", "att_med", "att_high"])
att_low_count = (df_clean["att_bin"] == "att_low").sum()
att_low_and_high_risk = ((df_clean["att_bin"] == "att_low") & (df_clean["risk_label"] == "high_risk")).sum()

p_att_low = att_low_count / total_N
p_att_low_given_high = att_low_and_high_risk / num_high
p_high_given_att_low = att_low_and_high_risk / att_low_count

print(f"Tổng mẫu N: {total_N}")
print(f"Số sinh viên high_risk: {num_high} -> P(high_risk) = {p_high:.4f}")
print(f"Số sinh viên low_risk: {num_low} -> P(low_risk) = {p_low:.4f}")
print(f"Số sinh viên att_low (attendance_rate <= 0.75): {att_low_count} -> P(att_low) = {p_att_low:.4f}")
print(f"Số sinh viên vừa att_low vừa high_risk: {att_low_and_high_risk}")
print(f"P(att_low | high_risk) = {att_low_and_high_risk} / {num_high} = {p_att_low_given_high:.4f} ({p_att_low_given_high*100:.2f}%)")
print(f"P(high_risk | att_low) = {att_low_and_high_risk} / {att_low_count} = {p_high_given_att_low:.4f} ({p_high_given_att_low*100:.2f}%)")
print(f"Kiểm chứng định lý Bayes:")
print(f"P(high_risk | att_low) = [P(att_low | high_risk) * P(high_risk)] / P(att_low)")
print(f"                       = [{p_att_low_given_high:.4f} * {p_high:.4f}] / {p_att_low:.4f}")
print(f"                       = {p_att_low_given_high * p_high / p_att_low:.4f}")

print("\n" + "="*60)
print("2. GAUSSIAN NAIVE BAYES PARAMETERS (C.2)")
print("="*60)
gnb, X_train, X_test, y_train, y_test, y_pred, y_proba, gnb_metrics = train_gaussian_naive_bayes(X, y)
print(f"GNB Priors: {gnb.class_prior_}")
print(f"Classes: {gnb.classes_}")
# Class 0: low_risk, Class 1: high_risk
print("Means theta_:")
for c_idx, c_name in enumerate(["low_risk (0)", "high_risk (1)"]):
    print(f"  Class {c_name}:")
    for f_idx, f_name in enumerate(feature_cols):
        print(f"    {f_name:<22}: mean = {gnb.theta_[c_idx][f_idx]:.4f}, var = {gnb.var_[c_idx][f_idx]:.4f}")

# SV0001
sample_0 = X[0]
print(f"\nSV0001 Features: {sample_0}")
for f_idx in [0, 2]: # attendance_rate and lab_avg
    f_name = feature_cols[f_idx]
    x_val = sample_0[f_idx]
    # For high risk (1)
    mu_1 = gnb.theta_[1][f_idx]
    var_1 = gnb.var_[1][f_idx]
    p_x_1 = (1.0 / np.sqrt(2 * np.pi * var_1)) * np.exp(-((x_val - mu_1)**2) / (2 * var_1))
    # For low risk (0)
    mu_0 = gnb.theta_[0][f_idx]
    var_0 = gnb.var_[0][f_idx]
    p_x_0 = (1.0 / np.sqrt(2 * np.pi * var_0)) * np.exp(-((x_val - mu_0)**2) / (2 * var_0))
    print(f"  Feature {f_name} (x = {x_val}):")
    print(f"    high_risk: mu = {mu_1:.4f}, var = {var_1:.4f} -> P(x|high_risk) = {p_x_1:.6f}")
    print(f"    low_risk:  mu = {mu_0:.4f}, var = {var_0:.4f} -> P(x|low_risk)  = {p_x_0:.6f}")

print("\n" + "="*60)
print("3. SHANNON ENTROPY VÀ INFORMATION GAIN (C.3)")
print("="*60)
H_parent, df_ig = compute_information_gain_ranking(df_clean)
print(f"H(S) = {H_parent:.4f}")
print(df_ig)

# Detail calculation for attendance_bin:
att_counts = df_clean["att_bin"].value_counts()
print("\nAttendance bin counts:")
for cat in ["att_low", "att_med", "att_high"]:
    sub = df_clean[df_clean["att_bin"] == cat]
    sub_n = len(sub)
    sub_high = (sub["risk_label"] == "high_risk").sum()
    sub_low = (sub["risk_label"] == "low_risk").sum()
    p_h = sub_high / sub_n if sub_n > 0 else 0
    p_l = sub_low / sub_n if sub_n > 0 else 0
    h_v = 0.0
    if p_h > 0: h_v -= p_h * np.log2(p_h)
    if p_l > 0: h_v -= p_l * np.log2(p_l)
    print(f"  Group {cat:<8}: N = {sub_n} ({sub_n/total_N:.4f}), high = {sub_high}, low = {sub_low} -> H(S_v) = {h_v:.4f}")

print("\n" + "="*60)
print("4. CHUỖI MARKOV (D.3)")
print("="*60)
states, P, row_sums, pi_0, pi_1, df_markov_hist, pi_stat = simulate_markov_learning_behavior()
print("P matrix:")
print(P)
print(f"pi_0 = {pi_0}")
print(f"pi_1 = {pi_1}")
print(f"pi_stat = {pi_stat}")

print("\n" + "="*60)
print("5. PU-LP BIP (E.1) & MAX-FLOW (E.2)")
print("="*60)
mentors_file = os.path.join(data_dir, "mentors.csv")
capacity_file = os.path.join(data_dir, "support_capacity.csv")
lp_summary, df_lp_alloc = solve_mentor_allocation_lp(df_clean, mentors_file, capacity_file, top_n_students=12, total_budget=24)
print(f"LP Status: {lp_summary['Status']}, Z* = {lp_summary['Optimal_Score']}, Hours: {lp_summary['Total_Cost_Used']}/24")
print(df_lp_alloc[["student_id", "Mức độ khẩn cấp", "Hình thức hỗ trợ phân bổ", "Chi phí (giờ)"]])

mf_summary, df_matched, G_flow = solve_bipartite_max_flow(df_clean, mentors_file, num_students=10)
print(f"Max Flow: {mf_summary['Max_Flow_Value']}, Matched: {mf_summary['Successful_Matches']}/{mf_summary['Total_Students']}")
