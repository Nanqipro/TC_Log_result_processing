# %%
import pandas as pd
import re
from basic import read_time_log, read_time_logs_to_df
from basic import log_base_path, excel_base_path
from basic import datasets_characteristics

# 读取日志文件
log_file_path_prefix = log_base_path + "D01-10-all-time/"
log_file_path_suffix = "/time_output.txt"
output_excel_path = excel_base_path + "real_world_graph_time.xlsx"

algorithms_info = {
    "Polak": "Polak",
    "Bisson": "Bisson",
    "Green": "Green",
    "TriCore": "TriCore",
    "Fox": "Fox",
    "Hu": "Hu",
    "H-INDEX": "H-INDEX",
    "TRUST": "TRUST",
}

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

data = read_time_logs_to_df(
    log_file_path_prefix,
    log_file_path_suffix,
    algorithms_info,
    datasets_info,
)

datasets_characteristics_df = datasets_characteristics()
data = pd.merge(
    data,
    datasets_characteristics_df,
    left_on="Datasets",
    right_on="ABBR",
    how="left",
)
data.rename(columns={"Datasets_x": "Datasets"}, inplace=True)
data.drop(columns=["Datasets_y"], inplace=True)
data.drop(columns=["ABBR"], inplace=True)

print(data.to_string(index=True))
data.to_excel(output_excel_path, index=False)

# %%
