import json
import os
import sys
import nbformat
from nbclient import NotebookClient

nb_path = r"c:\HOC_HANH\Mon dang hoc\ITA201\smartedu-ai\notebooks\smartedu_assignment.ipynb"

with open(nb_path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# Update cell 2 with Phase 2 imports
cell2_source = """import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx

base_dir = r"c:\\HOC_HANH\\Mon dang hoc\\ITA201\\smartedu-ai"
src_dir = os.path.join(base_dir, "src")
data_dir = os.path.join(base_dir, "data")
figures_dir = os.path.join(base_dir, "outputs", "figures")
tables_dir = os.path.join(base_dir, "outputs", "tables")

sys.path.append(src_dir)

from data_processing import load_data, clean_students_data
from linear_algebra import extract_features_and_labels, compute_risk_scores, compute_student_distances
from pca_analysis import compute_combinations, compute_grid_search_space, run_pca_analysis, compare_models_before_after_pca
from probability_entropy import compute_conditional_probabilities, train_gaussian_naive_bayes, compute_information_gain_ranking
from graph_markov import build_interaction_graph, traverse_bfs_dfs, simulate_markov_learning_behavior
from optimization import solve_mentor_allocation_lp, solve_bipartite_max_flow

print("Khởi tạo môi trường SmartEdu AI thành công (Toàn bộ Giai đoạn 1 và Giai đoạn 2)!")
"""
nb["cells"][2]["source"] = cell2_source

print("Starting notebook execution with nbclient...")
client = NotebookClient(nb, timeout=600, kernel_name='python3')
client.execute()

with open(nb_path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print(f"Successfully executed all {len(nb['cells'])} cells and saved notebook with pre-rendered outputs!")
