# # 热图（Heatmap）
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# # 读取Excel文件
# file_path = './all_log/profiler_result.xlsx'  # 替换为你的文件路径
# sheet_name = 'warp_execution_efficiency'
#
# # 读取数据
# df = pd.read_excel(file_path, sheet_name=sheet_name)
#
# # 设置Dataset为行索引
# df.set_index('Datasets', inplace=True)
#
# # 绘制热图
# plt.figure(figsize=(12, 8))
# sns.heatmap(df, annot=False, cmap='coolwarm', cbar_kws={'label': 'GLD Transactions per Request'}, linewidths=0.5)
#
# # cmap='coolwarm'：适合展示数值的对比，颜色从冷色到暖色逐渐变化。
# # cmap='viridis'：渐变的颜色方案，颜色从暗到亮变化，适合展示数据的渐变趋势。
# # cmap='magma'：色调从黑色到红色，可以较好地突出较大的数值差异。
# # cmap='cividis'：色盲友好的渐变色，可以确保对所有用户都具有可访问性。
# # cmap='inferno'：色调从黑色到黄色，非常适合显示高对比度的热图。
#
# # 添加标题
# plt.title('', fontsize=16)
# plt.xlabel('', fontsize=14)
# plt.ylabel('', fontsize=14)
#
# # 显示图形
# plt.tight_layout()
# plt.show()


# # 雷达图（Radar Chart）
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from math import pi
#
# # 读取Excel文件
# file_path = './all_log/profiler_result.xlsx'  # 替换为你的文件路径
# sheet_name = 'warp_execution_efficiency'
#
# # 读取数据
# df = pd.read_excel(file_path, sheet_name=sheet_name)
#
# # 设置Dataset为行索引
# df.set_index('Datasets', inplace=True)

# As-Caida
# P2p-Gnutella31
# Email-EuAll
# Soc-Slashdot0922
# Web-NotreDame
# Com-Dblp
# Amazon0601
# RoadNet-CA
# Wiki-Talk
# Web-BerkStan
# As-Skitter
# Cit-Patents
# Soc-Pokec
# Sx-Stackoverflow
# Com-Lj
# Soc-LiveJ
# Com-Orkut
# Twitter7
# Com-Friendster


# # 选择多个数据集进行比较（例如：'As-Caida', 'P2p-Gnutella31', 'Email-EuAll'）
# dataset_names = ['As-Caida', 'P2p-Gnutella31', 'Email-EuAll', 'Soc-Slashdot0922','Web-NotreDame', 'Com-Dblp', 'Amazon0601', 'RoadNet-CA', 'Wiki-Talk', 'Web-BerkStan', 'As-Skitter', 'Cit-Patents', 'Soc-Pokec', 'Sx-Stackoverflow', 'Com-Lj', 'Soc-LiveJ','Com-Orkut', 'Twitter7', 'Com-Friendster']  # 可以根据需要修改
#
# # 算法名称
# algorithms = df.columns
#
# # 计算雷达图的角度
# angles = np.linspace(0, 2 * np.pi, len(algorithms), endpoint=False).tolist()
#
# # 设置绘制每个数据集的雷达图
# fig, ax = plt.subplots(figsize=(10, 10), dpi=100, subplot_kw=dict(polar=True))
#
# # 为每个数据集绘制雷达图
# colors = ['skyblue', 'lightgreen', 'lightcoral', 'lightgoldenrodyellow', 'lightpink', 'lightsteelblue', 'lightyellow', 'lightseagreen', 'lightsalmon', 'lightskyblue', 'lightyellow', 'lightsteelblue', 'lightpink', 'lightgoldenrodyellow', 'lightcoral', 'lightgreen', 'skyblue', 'lightseagreen', 'lightsalmon']  # 为每个数据集选择不同的颜色
#
# for i, dataset_name in enumerate(dataset_names):
#     values = df.loc[dataset_name].values
#     values = np.concatenate((values, [values[0]]))  # 让雷达图闭合
#     angles_with_closure = np.concatenate((angles, [angles[0]]))  # 闭合角度
#
#     # 绘制每个数据集的雷达图
#     ax.fill(angles_with_closure, values, color=colors[i], alpha=0.25)
#     ax.plot(angles_with_closure, values, color=colors[i], linewidth=2, label=dataset_name)
#
# # 设置坐标轴标签
# ax.set_yticklabels([])  # 去掉径向刻度
# ax.set_xticks(angles)  # 设置x轴的刻度
# ax.set_xticklabels(algorithms, fontsize=12)  # 设置算法标签
#
# # 添加图例
# fig.legend(loc='upper left', bbox_to_anchor=(0.07, 0.95), fontsize=12)
#
#
# # 设置标题
# ax.set_title('Radar Chart for Multiple Datasets', size=16, color='darkblue', pad=20)
#
# # 显示雷达图
# plt.tight_layout()
# plt.show()


# # 箱线图 可选颜色
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# # 从 Excel 文件中加载数据
# df = pd.read_excel('./all_log/profiler_result.xlsx', sheet_name='warp_execution_efficiency')
#
# # 提取数据集名称（第一列）和算法名称（列头）
# datasets = df['Datasets']
# algorithms = df.columns[1:]  # 假设第一列是 Dataset，其他是算法名称
#
# # 假设数据已经加载到df中
# # 数据清洗和提取有效数据
# boxplot_data = []
# for algorithm in algorithms:
#     # 删除空值（NaN），只使用有效的数据
#     cleaned_data = df[algorithm].dropna().values
#     boxplot_data.append(cleaned_data)
#
# # 自定义颜色，定义为一个列表，每个颜色对应一个算法
# colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2', '#DC143C', '#00CED1', '#FF4500', '#2E8B57', '#D2691E', '#87CEFA']
#
# # 创建箱线图
# plt.figure(figsize=(12, 10))
# plt.boxplot(boxplot_data, patch_artist=True,
#             boxprops=dict(facecolor=colors[10], color='black'),
#             whiskerprops=dict(color='black'),
#             capprops=dict(color='black'),
#             medianprops=dict(color='black'))
#
# # 设置标题和标签
# # plt.title('Boxplot of Algorithm Performance Across Datasets')
# plt.xticks(range(1, len(algorithms) + 1), algorithms, rotation=20, fontsize=25)
# plt.ylabel('Warp Execution Efficiency', fontsize=25, fontweight='bold')
# # 调整纵坐标刻度的字体大小
# plt.tick_params(axis='y', labelsize=25)  # 设置纵坐标刻度标签的字体大小为18
# # 显示图形
# plt.tight_layout()
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import PercentFormatter

# 从 Excel 文件中加载数据
df = pd.read_excel('./all_log/profiler_result.xlsx', sheet_name='warp_execution_efficiency')

# 提取数据集名称（第一列）和算法名称（列头）
datasets = df['Datasets']
algorithms = df.columns[1:]  # 假设第一列是 Dataset，其他是算法名称

# 假设数据已经加载到df中
# 数据清洗和提取有效数据，确保所有数据都是数值类型
boxplot_data = []
for algorithm in algorithms:
    # 尝试将数据转换为数值类型，无法转换的值将被设置为 NaN
    cleaned_data = pd.to_numeric(df[algorithm], errors='coerce').dropna().values
    boxplot_data.append(cleaned_data)

# 自定义颜色，定义为一个列表，每个颜色对应一个算法
colors = ['#f6c89a', '#a5d4a1', '#c1b3d5', '#fefea9', '#9fbaef', '#f9bbf8', '#b2b893', '#bce2ea', '#91d0fc', '#f2e5c1']

# 检查颜色列表是否足够，如果不够，可以循环使用或扩展颜色列表
if len(colors) < len(algorithms):
    # 循环使用颜色
    colors = (colors * (len(algorithms) // len(colors) + 1))[:len(algorithms)]

# 创建箱线图
plt.figure(figsize=(12, 10))
box = plt.boxplot(boxplot_data, patch_artist=True,
                  boxprops=dict(color='black'),
                  whiskerprops=dict(color='black'),
                  capprops=dict(color='black'),
                  medianprops=dict(color='black'))

# 为每个箱线图单独设置颜色
for i, patch in enumerate(box['boxes']):
    patch.set_facecolor(colors[i])  # 设置每个箱体的颜色

# 设置X轴标签和其它图形样式
plt.xticks(range(1, len(algorithms) + 1), algorithms, rotation=20, fontsize=30)
plt.ylabel('warp_execution_efficiency', fontsize=30, fontweight='bold')
plt.tick_params(axis='x', labelsize=25)  # 设置纵坐标刻度标签的字体大小为25
# 调整纵坐标刻度的字体大小
plt.tick_params(axis='y', labelsize=25)  # 设置纵坐标刻度标签的字体大小为25

# 如果数据范围在0到1之间，设置百分比格式
plt.gca().yaxis.set_major_formatter(PercentFormatter(1.0))

# 如果数据范围在0到100之间，设置百分比格式
# plt.gca().yaxis.set_major_formatter(PercentFormatter(100))

# 可选：设置y轴的范围（根据数据情况调整）
# plt.ylim(0, 1)  # 如果数据范围在0到1之间
# 或
# plt.ylim(0, 100)  # 如果数据范围在0到100之间

# 显示图形
plt.tight_layout()

# 保存图形为 PDF 文件
plt.savefig(r'D:\BaiduNetdiskDownload\warp_execution_efficiency_v4.pdf', format='pdf')

plt.show()


