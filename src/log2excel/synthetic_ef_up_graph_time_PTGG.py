# %%
from basic import read_time_logs_to_df, synthetic_datasets_characteristics
from basic import log_base_path, excel_base_path

# 读取日志文件
log_file_path_prefix = log_base_path + "D01-10-all-time/"
log_file_path_suffix = "/time_output.txt"
output_excel_path = excel_base_path + "synthetic_ef_up_graph_time_PTGG.xlsx"

algorithms_info = {
    "Polak": "Polak",
    "TRUST": "TRUST",
    "GroupTC-OPT": "GroupTC-BS",
    "GroupTC-Cuckoo": "GroupTC-HS",
}

datasets_characteristics_df = synthetic_datasets_characteristics()
datasets_characteristics_df = datasets_characteristics_df[
    datasets_characteristics_df["Datasets"].str.contains(r"cluster2", regex=True)
]
datasets_info = datasets_characteristics_df.set_index("Datasets")["ABBR."].to_dict()


data = read_time_logs_to_df(
    log_file_path_prefix,
    log_file_path_suffix,
    algorithms_info,
    datasets_info,
)

for algorithm in algorithms_info.values():
    data[f"{algorithm}_speedup"] = data["Polak"] / data[algorithm]

print(data.to_string(index=True))

data.to_excel(output_excel_path, index=False)

# %%
