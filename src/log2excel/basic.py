import pandas as pd
import re
import os

log_base_path = "../../log/"
excel_base_path = "../../excel/"
pdf_base_path = "../../pdf/"


def datasets_characteristics():
    data = {
        "Datasets": [
            "Web-NotreDame",
            "Com-Dblp",
            "Amazon0601",
            "RoadNet-CA",
            "Wiki-Talk",
            "Imdb-2021",
            "Web-BerkStan",
            "As-Skitter",
            "Cit-Patents",
            "Soc-Pokec",
            "Sx-Stackoverflow",
            "Com-Lj",
            "Soc-LiveJ",
            "k-mer-graph5",
            "Hollywood-2011",
            "Com-Orkut",
            "Enwiki-2024",
            "k-mer-graph4",
            "Twitter7",
            "Com-Friendster",
        ],
        "ABBR": [
            "WN",
            "CD",
            "AM",
            "RC",
            "WT",
            "IM",
            "WB",
            "AS",
            "CP",
            "SP",
            "SX",
            "CL",
            "SL",
            "K5",
            "HW",
            "CO",
            "EN",
            "K4",
            "TW",
            "CF",
        ],
        "vertex_count": [
            325729,
            317080,
            403394,
            1965206,
            2394385,
            1224346,
            685230,
            1696415,
            3774768,
            1632803,
            2601977,
            3997962,
            4847571,
            55042369,
            1985306,
            3072441,
            6783976,
            214005017,
            41652230,
            65608366,
        ],
        "edge_count": [
            1090108,
            1049866,
            2443408,
            2766607,
            4659565,
            5369472,
            6649470,
            11095298,
            16518947,
            22301964,
            28183518,
            34681189,
            42851237,
            58608800,
            114492816,
            117185083,
            157010940,
            232705452,
            1202513046,
            1806067135,
        ],
        "avg_degree": [
            6.69,
            6.62,
            12.11,
            2.82,
            3.89,
            8.77,
            19.41,
            13.08,
            8.75,
            27.32,
            21.66,
            17.35,
            17.68,
            2.13,
            115.34,
            76.28,
            46.29,
            2.17,
            57.74,
            55.06,
        ],
    }
    return pd.DataFrame(data)


def read_time_log(log_file_path, algorithm_key, algorithm_names, datasets_info):
    """
    读取时间日志并解析数据集名称和时间值。

    参数:
    log_file_path: 日志文件的路径
    algorithm_key: 算法的关键字
    algorithm_names: 算法名称的字典
    datasets_info: 数据集信息的字典

    返回:
    包含数据集名称和对应时间值的字典
    """
    # 解析日志
    data = {"Datasets": [], algorithm_names[algorithm_key]: []}
    with open(log_file_path, "r") as file:
        for line in file:
            match = re.search(
                r" " + algorithm_key + "\s+(.*?)\s+\d+\s+\d+\s+([\d.]+)", line
            )
            if match:
                dataset_name = match.group(1).split("/")[-1]  # 获取数据集名称
                time = float(match.group(2)) * 1000  # 获取时间值并乘以1000，单位为ms
                if dataset_name in datasets_info:  # 检查数据集是否在datasets_info中
                    data["Datasets"].append(datasets_info[dataset_name])
                    data[algorithm_names[algorithm_key]].append(time)
    return data


def read_time_logs_to_df(
    log_file_path_prefix,
    log_file_path_suffix,
    algorithms_info,
    datasets_info,
):
    """
    处理时间日志并将结果输出到Excel文件。

    参数:
    log_file_path_prefix: 日志文件路径前缀
    log_file_path_suffix: 日志文件路径后缀
    algorithms_info: 算法信息的字典
    datasets_info: 数据集信息的字典
    """
    all_data = pd.DataFrame()  # 创建一个空的DataFrame来存储所有数据

    # 修复：在创建字典之前，确保all_data已经包含数据集名称
    for algorithm_key in algorithms_info:
        log_file_path = log_file_path_prefix + algorithm_key + log_file_path_suffix
        data = read_time_log(
            log_file_path, algorithm_key, algorithms_info, datasets_info
        )

        # 如果all_data为空，初始化数据集名称
        if all_data.empty:
            all_data = pd.DataFrame(data)  # 初始化all_data

        for dataset, time in zip(
            data["Datasets"], data[algorithms_info[algorithm_key]]
        ):
            if dataset not in all_data["Datasets"].values:  # 确保数据集名称唯一
                all_data.loc[len(all_data)] = {"Datasets": dataset}  # 使用loc添加新行
            all_data.loc[
                all_data["Datasets"] == dataset, algorithms_info[algorithm_key]
            ] = time  # 更新时间值

    return all_data


def read_prof_log(prof_file, prof_metrics):
    """
    读取性能日志并解析数据集名称和性能指标值。

    参数:
    prof_file: 性能日志文件
    prof_metrics: 性能指标的列表

    返回:
    包含数据集名称和对应性能指标值的字典
    """
    ret_prof = {}
    dataset = "none"
    lines = prof_file.readlines()

    for line in lines:
        if "Profiling application" in line:
            dataset = line.split("-dataset=")[1].strip()
        if "Metric result" in line:
            i = lines.index(line) + 2
            metric_values = {}
            while i < len(lines) and len(lines[i].split(",")) > 5:
                matches = re.findall(r'"([^"]+)"|([-+]?\d*\.\d+|[-+]?\d+)', lines[i])
                for prof_metric in prof_metrics:
                    if len(matches) > 7 and matches[3][0] == prof_metric:
                        invocations = int(matches[2][1])
                        metric_avg = float(matches[7][1].strip("%"))
                        # 保存 metric_avg 和 metric_sum
                        metric_values[prof_metric] = {
                            "avg": metric_avg,
                            "sum": invocations * metric_avg,
                        }
                i += 1
            ret_prof[dataset] = metric_values
    return ret_prof


def read_prof_logs(
    log_file_path_prefix, log_file_path_suffix, algorithms_info, metrics
):
    """
    读取多个性能日志并解析数据集名称和性能指标值。

    参数:
    log_file_path_prefix: 日志文件路径前缀
    log_file_path_suffix: 日志文件路径后缀
    algorithms_info: 算法信息的字典
    metrics: 性能指标的列表

    返回:
    包含数据集名称和对应性能指标值的字典
    """
    datas = {}
    for algorithm_key in algorithms_info:
        log_file_path = log_file_path_prefix + algorithm_key + log_file_path_suffix
        with open(log_file_path) as file:
            data = read_prof_log(file, metrics)
            datas[algorithm_key] = data
    return datas


def process_prof_metric_data(
    datas, datasets_info, algorithms_info, metrics, metrics_type
):
    """
    处理性能指标数据并输出到Excel文件。

    参数:
    datas: 包含性能指标数据的字典
    datasets_info: 数据集信息的字典
    algorithms_info: 算法信息的字典
    metrics: 性能指标的列表
    metrics_type: 性能指标类型的列表
    """
    all_prof_metric_data = {}
    for metric, metric_type in zip(metrics, metrics_type):
        prof_metric_data = {}
        for algorithm_key, datasets in datas.items():
            for dataset, metric_values in datasets.items():
                metric_value = metric_values.get(metric, {}).get(metric_type, 0)
                algorithm_name = algorithms_info[algorithm_key]
                if algorithm_name not in prof_metric_data:
                    prof_metric_data[algorithm_name] = {}
                prof_metric_data[algorithm_name][datasets_info[dataset]] = metric_value

        # 将数据转换为 DataFrame
        df = pd.DataFrame(prof_metric_data)
        all_prof_metric_data[metric] = df
    return all_prof_metric_data


def write_prof_metrics_to_excel(all_prof_metric_data, output_excel_path):
    """
    将多个DataFrame写入Excel文件。

    参数:
    all_prof_metric_data: 包含多个DataFrame的字典
    output_excel_path: 输出Excel文件的路径
    """
    with pd.ExcelWriter(
        output_excel_path
    ) as writer:  # 使用 ExcelWriter 以便导出多个 sheet
        for metric, df in all_prof_metric_data.items():
            df.to_excel(
                writer, index=False, sheet_name=metric
            )  # 将 DataFrame 导出到指定的 sheet


def process_prof_logs_to_excel(
    log_file_path_prefix,
    log_file_path_suffix,
    output_excel_path,
    datasets_info,
    algorithms_info,
    metrics,
    metrics_type,
):
    """
    处理性能日志并将结果输出到Excel文件。

    参数:
    log_file_path_prefix: 日志文件路径前缀
    log_file_path_suffix: 日志文件路径后缀
    output_excel_path: 输出Excel文件的路径
    datasets_info: 数据集信息的字典
    algorithms_info: 算法信息的字典
    metrics: 性能指标的列表
    metrics_type: 性能指标类型的列表
    """
    # 读取数据
    datas = read_prof_logs(
        log_file_path_prefix, log_file_path_suffix, algorithms_info, metrics
    )

    # 处理为 key-value 对。 key 为 metric，value 为 DataFrame
    all_prof_metric_data = process_prof_metric_data(
        datas, datasets_info, algorithms_info, metrics, metrics_type
    )

    for metric, df in all_prof_metric_data.items():
        print(metric)
        print(df.to_string(index=True))
        print()

    # 写入 Excel
    write_prof_metrics_to_excel(all_prof_metric_data, output_excel_path)


def read_multiple_part_time_logs_to_df(
    log_file_path_prefix,
    log_file_path_suffix,
    algorithm_key,
    datasets_info,
    time_types,
):
    """
    读取多个时间日志并解析数据集名称和时间值。

    参数:
    log_file_path_prefix: 日志文件路径前缀
    log_file_path_suffix: 日志文件路径后缀
    algorithm_key: 算法的关键字
    datasets_info: 数据集信息的字典
    time_types: 时间类型的列表
    """
    current_time_type = ""

    # 解析日志
    data = {
        "Datasets": [],
    }
    time_type_index = -1

    with open(log_file_path_prefix + algorithm_key + log_file_path_suffix, "r") as file:
        for line in file:
            if line == "\n":
                continue
            if line.strip() in time_types:
                time_type_index += 1
                current_time_type = line.strip()
                data[current_time_type] = []
                continue

            match = re.search(
                r" " + algorithm_key + "\s+(.*?)\s+\d+\s+\d+\s+([\d.]+)", line
            )
            if match:
                dataset_name = match.group(1).split("/")[-1]  # 获取数据集名称
                time = float(match.group(2)) * 1000  # 获取时间值并乘以1000，单位为ms
                if dataset_name in datasets_info:  # 检查数据集是否在datasets_info中
                    data[current_time_type].append(time)  # 添加时间值
                if time_type_index == 0:
                    data["Datasets"].append(datasets_info[dataset_name])
    df = pd.DataFrame(data)
    return df
