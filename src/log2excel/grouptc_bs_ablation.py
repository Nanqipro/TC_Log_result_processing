# %%
import pandas as pd
import re

from basic import read_multiple_part_time_logs_to_df
from basic import log_base_path, excel_base_path

# 读取日志文件
log_file_path_prefix = log_base_path + "D01-10-grouptc-bs-ablation/"
log_file_path_suffix = "/time_output.txt"
output_excel_path = excel_base_path + "grouptc_bs_ablation_time.xlsx"


datasets_info = {
    "Web-NotreDame": "WN",
    "Com-Dblp": "CD",
    "Amazon0601": "AM",
    "RoadNet-CA": "RC",
    "Wiki-Talk": "WT",
    "Imdb-2021": "IM",
    "Web-BerkStan": "WB",
    "As-Skitter": "AS",
    "Cit-Patents": "CP",
    "Soc-Pokec": "SP",
    "Sx-Stackoverflow": "SX",
    "Com-Lj": "CL",
    "Soc-LiveJ": "SL",
    "k-mer-graph5": "K5",
    "Hollywood-2011": "HW",
    "Com-Orkut": "CO",
    "Enwiki-2024": "EN",
    "k-mer-graph4": "K4",
    "Twitter7": "TW",
    "Com-Friendster": "CF",
    "cluster2-s20-e2": "s20-e2",
    "cluster2-s20-e4": "s20-e4",
    "cluster2-s20-e8": "s20-e8",
    "cluster2-s20-e16": "s20-e16",
    "cluster2-s20-e32": "s20-e32",
    "cluster2-s20-e64": "s20-e64",
    "cluster2-s20-e128": "s20-e128",
    "cluster2-s20-e256": "s20-e256",
    "cluster4-s17-e32": "s17-e32",
    "cluster4-s18-e32": "s18-e32",
    "cluster4-s19-e32": "s19-e32",
    "cluster4-s20-e32": "s20-e32",
    "cluster4-s21-e32": "s21-e32",
    "cluster4-s22-e32": "s22-e32",
    "cluster4-s23-e32": "s23-e32",
    "cluster4-s24-e32": "s24-e32",
}

time_types = ["no optimization", "VP", "VP+EF", "VP+EF+RL"]

data = read_multiple_part_time_logs_to_df(
    log_file_path_prefix,
    log_file_path_suffix,
    "GroupTC-OPT",
    datasets_info,
    time_types,
)

data["baseline"] = [1] * len(data["Datasets"])

for time_type in time_types:
    if time_type != "no optimization":
        data[f"{time_type}_speedup"] = data["baseline"] / data[time_type]


print(data.to_string(index=True))
data.to_excel(output_excel_path, index=True)

# %%
