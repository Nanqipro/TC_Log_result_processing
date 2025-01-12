# %%
import pandas as pd
import re

from basic import read_multiple_part_time_logs_to_df    
from basic import log_base_path, excel_base_path


# 读取日志文件
log_file_path_prefix = log_base_path + "D01-10-trust-partition/"
log_file_path_suffix = "/time_output.txt"
output_excel_path = excel_base_path + "trust_partition_time.xlsx"

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
}


data = read_multiple_part_time_logs_to_df(
    log_file_path_prefix,
    log_file_path_suffix,
    "TRUST",
    datasets_info,
    ["small degree vertex", "large degree vertex", "all vertex"],
)

print(data.to_string(index=True))
data.to_excel(output_excel_path, index=True)

# %%
