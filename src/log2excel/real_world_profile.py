# %%
from basic import process_prof_logs_to_excel
from basic import log_base_path, excel_base_path
from basic import real_world_datasets_characteristics

# 读取日志文件
log_file_path_prefix = log_base_path + "D01-10-profile/"
log_file_path_suffix = "/prof_output.txt"
output_excel_path = excel_base_path + "real_world_graph_profile.xlsx"

algorithms_info = {
    "Polak": "Polak",
    "Bisson": "Bisson",
    "Green": "Green",
    "TriCore": "TriCore",
    "Fox": "Fox",
    "Hu": "Hu",
    "H-INDEX": "H-INDEX",
    "TRUST": "TRUST",
    "GroupTC-OPT": "GroupTC-BS",
    "GroupTC-Cuckoo": "GroupTC-HS",
}

datasets_characteristics_df = real_world_datasets_characteristics()
datasets_info = datasets_characteristics_df.set_index("Datasets")["ABBR."].to_dict()

metrics = [
    "warp_execution_efficiency",
    "global_load_requests",
    "gld_transactions_per_request",
    "gld_efficiency",
]

metrics_type = ["avg", "sum", "avg", "avg"]


process_prof_logs_to_excel(
    log_file_path_prefix,
    log_file_path_suffix,
    output_excel_path,
    datasets_info,
    algorithms_info,
    metrics,
    metrics_type,
)

# %%
