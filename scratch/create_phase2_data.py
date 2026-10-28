import os
import pandas as pd
import numpy as np

base_dir = r"c:\HOC_HANH\Mon dang hoc\ITA201\smartedu-ai"
data_dir = os.path.join(base_dir, "data")

# 1. Load students.csv to get student IDs
df_students = pd.read_csv(os.path.join(data_dir, "students.csv"))
student_ids = df_students["student_id"].tolist()
print(f"Loaded {len(student_ids)} students from students.csv")

# 2. Generate data/interactions.csv
# Create ~1,500 realistic interaction edges among students
np.random.seed(42)
num_edges = 1500
relation_types = ["study_together", "discuss_assignment", "peer_support", "forum_reply"]

sources = []
targets = []
counts = []
relations = []

# Create dense clusters among first 100 students plus connections across the cohort
pool_dense = student_ids[:100]

edges_set = set()
while len(edges_set) < num_edges:
    if np.random.rand() < 0.6:
        # 60% interactions within dense cohort (first 100 students)
        u, v = np.random.choice(pool_dense, size=2, replace=False)
    else:
        # 40% interactions across the whole student body
        u = np.random.choice(student_ids)
        v = np.random.choice(student_ids)
        if u == v:
            continue
    
    if (u, v) not in edges_set:
        edges_set.add((u, v))
        sources.append(u)
        targets.append(v)
        counts.append(int(np.random.randint(1, 15)))
        relations.append(np.random.choice(relation_types, p=[0.35, 0.35, 0.20, 0.10]))

df_interactions = pd.DataFrame({
    "source_student": sources,
    "target_student": targets,
    "interaction_count": counts,
    "relation_type": relations
})

interactions_path = os.path.join(data_dir, "interactions.csv")
df_interactions.to_csv(interactions_path, index=False, encoding="utf-8-sig")
print(f"Generated {len(df_interactions)} interactions in {interactions_path}")

# 3. Generate data/mentors.csv (matches ASM1.pdf page 5)
df_mentors = pd.DataFrame({
    "mentor_id": ["M01", "M02", "M03", "M04", "M05"],
    "mentor_name": ["ThS. Trần Văn Hùng", "TS. Nguyễn Thị Mai", "ThS. Lê Hoàng Nam", "ThS. Phạm Thu Trang", "TS. Vũ Quốc Bảo"],
    "specialty": ["Python", "Data analysis", "Machine learning", "Mathematics for AI", "Database Systems"],
    "max_students": [5, 4, 3, 5, 4],
    "available_hours": [6, 5, 4, 6, 5]
})
mentors_path = os.path.join(data_dir, "mentors.csv")
df_mentors.to_csv(mentors_path, index=False, encoding="utf-8-sig")
print(f"Generated {len(df_mentors)} mentors in {mentors_path}")

# 4. Generate data/support_capacity.csv (matches ASM1.pdf page 5)
df_capacity = pd.DataFrame({
    "support_type": ["Online mentoring", "Lab tutoring", "One-to-one support", "Workshop review"],
    "capacity": [12, 8, 4, 20],
    "cost_per_student": [1, 2, 4, 1],
    "priority_score": [5, 8, 10, 6]
})
capacity_path = os.path.join(data_dir, "support_capacity.csv")
df_capacity.to_csv(capacity_path, index=False, encoding="utf-8-sig")
print(f"Generated {len(df_capacity)} support capacity types in {capacity_path}")
