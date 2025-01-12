# %%
import pandas as pd
import re

from basic import read_multiple_part_time_logs_to_df, all_datasets_characteristics
from basic import log_base_path, excel_base_path

# 读取日志文件
log_file_path_prefix = log_base_path + "D01-10-grouptc-bs-ablation/"
log_file_path_suffix = "/time_output.txt"
output_excel_path = excel_base_path + "grouptc_bs_ablation_time.xlsx"


datasets_characteristics_df = all_datasets_characteristics()
datasets_info = datasets_characteristics_df.set_index("Datasets")["ABBR."].to_dict()

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
        data[f"{time_type}_speedup"] = data["no optimization"] / data[time_type]


print(data.to_string(index=True))
data.to_excel(output_excel_path, index=False)

# %%
