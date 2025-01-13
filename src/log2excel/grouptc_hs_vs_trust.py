# %%
import pandas as pd
import re

from basic import read_multiple_part_time_logs_to_df, all_datasets_characteristics
from basic import log_base_path, excel_base_path

# 读取日志文件
log_file_path_prefix = log_base_path + "D01-10-grouptc-hs-vs-trust/"
log_file_path_suffix = "/time_output.txt"
output_excel_path = excel_base_path + "grouptc_hs_vs_trust_time.xlsx"

datasets_characteristics_df = all_datasets_characteristics()
datasets_info = datasets_characteristics_df.set_index("Datasets")["ABBR."].to_dict()

log_time_types = [
    "small degree vertex total time",
    "small degree vertex hash table construction time",
    "large degree vertex total time",
    "large degree vertex hash table construction time",
]

grouptc_hs_data = read_multiple_part_time_logs_to_df(
    log_file_path_prefix,
    log_file_path_suffix,
    "GroupTC-Cuckoo",
    datasets_info,
    log_time_types,
)

print(grouptc_hs_data.to_string(index=True))

grouptc_hs_data["small degree vertex hash search time"] = (
    grouptc_hs_data["small degree vertex total time"]
    - grouptc_hs_data["small degree vertex hash table construction time"]
)
grouptc_hs_data["large degree vertex hash search time"] = (
    grouptc_hs_data["large degree vertex total time"]
    - grouptc_hs_data["large degree vertex hash table construction time"]
)

grouptc_hs_data = grouptc_hs_data.rename(
    columns=lambda x: f"grouptc_hs_{x}" if x != "Datasets" else x
)


trust_data = read_multiple_part_time_logs_to_df(
    log_file_path_prefix,
    log_file_path_suffix,
    "TRUST",
    datasets_info,
    log_time_types,
)
trust_data["small degree vertex hash search time"] = (
    trust_data["small degree vertex total time"]
    - trust_data["small degree vertex hash table construction time"]
)
trust_data["large degree vertex hash search time"] = (
    trust_data["large degree vertex total time"]
    - trust_data["large degree vertex hash table construction time"]
)
trust_data = trust_data.rename(columns=lambda x: f"trust_{x}" if x != "Datasets" else x)

data = pd.merge(grouptc_hs_data, trust_data, on="Datasets", how="left")

data["baseline"] = [1] * len(data["Datasets"])

all_time_types = [
    "small degree vertex total time",
    "small degree vertex hash table construction time",
    "small degree vertex hash search time",
    "large degree vertex total time",
    "large degree vertex hash table construction time",
    "large degree vertex hash search time",
]

for time_type in all_time_types:
    data[f"{time_type}_speedup"] = (
        data[f"trust_{time_type}"] / data[f"grouptc_hs_{time_type}"]
    )

data = data.merge(
    datasets_characteristics_df, left_on="Datasets", right_on="ABBR.", how="left"
)
data["large degree vertex avg degree"] = (
    data["small degree first edge"] * 2 / data["small degree first vertex"]
)

data.rename(columns={"Datasets_x": "Datasets"}, inplace=True)
data.drop(columns=["Datasets_y"], inplace=True)
data.drop(columns=["ABBR."], inplace=True)

print(data.to_string(index=True))

data.to_excel(output_excel_path, index=False)


# %%
