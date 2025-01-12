# %%
from basic import read_time_logs_to_df
from basic import log_base_path, excel_base_path

# 读取日志文件
log_file_path_prefix = log_base_path + "D01-10-all-time/"
log_file_path_suffix = "/time_output.txt"
output_excel_path = excel_base_path + "synthetic_ef_up_graph_time_PTGG.xlsx"

algorithms_info = {
    "Polak": "Polak",
    "TRUST": "TRUST",
    "GroupTC-OPT": "GroupTC-BS",
    "GroupTC-HASH-V2": "GroupTC-HS",
}

datasets_info = {
    "cluster2-s20-e2": "s20-e2",
    "cluster2-s20-e4": "s20-e4",
    "cluster2-s20-e8": "s20-e8",
    "cluster2-s20-e16": "s20-e16",
    "cluster2-s20-e32": "s20-e32",
    "cluster2-s20-e64": "s20-e64",
    "cluster2-s20-e128": "s20-e128",
    "cluster2-s20-e256": "s20-e256",
}

data = read_time_logs_to_df(
    log_file_path_prefix,
    log_file_path_suffix,
    algorithms_info,
    datasets_info,
)

for algorithm in algorithms_info.values():
    data[f"{algorithm}_speedup"] = data["Polak"] / data[algorithm]

print(data.to_string(index=True))

data.to_excel(output_excel_path, index=True)

# %%
