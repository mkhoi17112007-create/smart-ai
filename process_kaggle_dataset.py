import os
import pandas as pd
import numpy as np

base_dir = r"c:\HOC_HANH\Mon dang hoc\ITA201\smartedu-ai"
data_dir = os.path.join(base_dir, "data")
raw_dataset_path = os.path.join(data_dir, "dataset.csv")

# 1. Read Kaggle raw dataset
df_raw = pd.read_csv(raw_dataset_path, encoding="utf-8-sig")
print(f"Loaded raw Kaggle dataset: {df_raw.shape[0]} rows, {df_raw.shape[1]} columns.")

# 2. Map features to SMARTEDU AI standard columns (Phase 1)
n_records = len(df_raw)
student_ids = [f"SV{i:04d}" for i in range(1, n_records + 1)]

# Compute attendance_rate (0.50 to 1.00)
enrolled_sem1 = np.maximum(df_raw["Curricular units 1st sem (enrolled)"], 1)
approved_ratio = df_raw["Curricular units 1st sem (approved)"] / enrolled_sem1
attendance = 0.4 * df_raw["Tuition fees up to date"] + 0.6 * approved_ratio
attendance = np.clip(attendance, 0.50, 1.00)

# Compute quiz_avg (0 to 10)
quiz = np.clip((df_raw["Previous qualification"] / 20.0) * 10, 2.0, 10.0)

# Compute lab_avg (0 to 10)
lab = np.clip(df_raw["Curricular units 1st sem (grade)"] / 2.0, 0.0, 10.0)

# Compute assignment_score (0 to 10)
assignment = np.clip(df_raw["Curricular units 2nd sem (grade)"] / 2.0, 0.0, 10.0)

# Compute self_study_hours (1.0 to 15.0)
self_study = np.clip(df_raw["Age at enrollment"] / 2.2, 1.0, 15.0)

# Compute late_submissions (0 to 10)
late = df_raw["Curricular units 1st sem (without evaluations)"].astype(int)

# Compute video_views (2 to 50)
video = (df_raw["Curricular units 1st sem (evaluations)"] * 2 + 5).astype(int)

# Compute participation_level
conditions = [
    df_raw["Scholarship holder"] == 1,
    df_raw["Displaced"] == 1
]
choices = ["Cao", "Trung bình"]
participation = np.select(conditions, choices, default="Thấp")

# Compute risk_label
risk_label = np.where(df_raw["Target"].isin(["Dropout", "Enrolled"]), "high_risk", "low_risk")

df_students = pd.DataFrame({
    "student_id": student_ids,
    "attendance_rate": np.round(attendance, 2),
    "quiz_avg": np.round(quiz, 1),
    "lab_avg": np.round(lab, 1),
    "assignment_score": np.round(assignment, 1),
    "self_study_hours": np.round(self_study, 1),
    "late_submissions": late,
    "video_views": video,
    "participation_level": participation,
    "risk_label": risk_label
})

# Introduce 20 missing values intentionally to demonstrate missing value handling in Phase A.1 (Trang 6 ASM1)
np.random.seed(42)
missing_indices_quiz = np.random.choice(n_records, size=20, replace=False)
missing_indices_study = np.random.choice(n_records, size=20, replace=False)

df_students.loc[missing_indices_quiz, "quiz_avg"] = np.nan
df_students.loc[missing_indices_study, "self_study_hours"] = np.nan

# Save students.csv
students_csv_path = os.path.join(data_dir, "students.csv")
df_students.to_csv(students_csv_path, index=False, encoding="utf-8-sig")
print(f"Created data/students.csv with {len(df_students)} rows successfully for Phase 1!")
