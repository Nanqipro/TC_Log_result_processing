# %%
from basic import process_prof_logs_to_excel
from basic import log_base_path, excel_base_path

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
    "GroupTC-HASH-V2": "GroupTC-HS",
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
