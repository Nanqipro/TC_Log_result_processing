# %%
import pandas as pd
import re

from basic import read_multiple_part_time_logs_to_df, real_world_datasets_characteristics
from basic import log_base_path, excel_base_path


# 读取日志文件
log_file_path_prefix = log_base_path + "D01-10-trust-partition/"
log_file_path_suffix = "/time_output.txt"
output_excel_path = excel_base_path + "trust_partition_time.xlsx"

datasets_characteristics_df = real_world_datasets_characteristics()
datasets_info = datasets_characteristics_df.set_index("Datasets")["ABBR."].to_dict()


data = read_multiple_part_time_logs_to_df(
    log_file_path_prefix,
    log_file_path_suffix,
    "TRUST",
    datasets_info,
    ["small degree vertex", "large degree vertex", "all vertex"],
)

data["all vertex"] = data["small degree vertex"] + data["large degree vertex"]
data["low degree part"] = data["small degree vertex"] / data["all vertex"]
data["high degree part"] = data["large degree vertex"] / data["all vertex"]


print(data.to_string(index=True))
data.to_excel(output_excel_path, index=False)

# %%
