# %%
import pandas as pd
import re
from basic import read_time_log, read_time_logs_to_df
from basic import log_base_path, excel_base_path
from basic import real_world_datasets_characteristics

# 读取日志文件
log_file_path_prefix = log_base_path + "D01-10-all-time/"
log_file_path_suffix = "/time_output.txt"
output_excel_path = excel_base_path + "real_world_graph_time_PTGG.xlsx"

algorithms_info = {
    "Polak": "Polak",
    "TRUST": "TRUST",
    "GroupTC-OPT": "GroupTC-BS",
    "GroupTC-HASH-V2": "GroupTC-HS",
}

datasets_characteristics_df = real_world_datasets_characteristics()
datasets_info = datasets_characteristics_df.set_index("Datasets")["ABBR."].to_dict()


data = read_time_logs_to_df(
    log_file_path_prefix,
    log_file_path_suffix,
    algorithms_info,
    datasets_info,
)

data = pd.merge(
    data,
    datasets_characteristics_df,
    left_on="Datasets",
    right_on="ABBR.",
    how="left",
)
data.rename(columns={"Datasets_x": "Datasets"}, inplace=True)
data.drop(columns=["Datasets_y"], inplace=True)
data.drop(columns=["ABBR."], inplace=True)

print(data.to_string(index=True))
data.to_excel(output_excel_path, index=False)

# %%
