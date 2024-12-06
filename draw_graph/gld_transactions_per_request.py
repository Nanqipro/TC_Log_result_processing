# # 热图（Heatmap）
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# # 读取Excel文件
# file_path = './all_log/profiler_result.xlsx'  # 替换为你的文件路径
# sheet_name = 'gld_transactions_per_request'
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
# sheet_name = 'gld_transactions_per_request'
#
# # 读取数据
# df = pd.read_excel(file_path, sheet_name=sheet_name)
#
# # 设置Dataset为行索引
# df.set_index('Datasets', inplace=True)
#
# # As-Caida
# # P2p-Gnutella31
# # Email-EuAll
# # Soc-Slashdot0922
# # Web-NotreDame
# # Com-Dblp
# # Amazon0601
# # RoadNet-CA
# # Wiki-Talk
# # Web-BerkStan
# # As-Skitter
# # Cit-Patents
# # Soc-Pokec
# # Sx-Stackoverflow
# # Com-Lj
# # Soc-LiveJ
# # Com-Orkut
# # Twitter7
# # Com-Friendster
#
#
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


# 箱线图 统一色
# import pandas as pd
# import matplotlib.pyplot as plt
#
# # 从 Excel 文件中加载数据
# df = pd.read_excel('./all_log/profiler_result.xlsx', sheet_name='gld_transactions_per_request')
#
# # 提取数据集名称（第一列）和算法名称（列头）
# datasets = df['Datasets']
# algorithms = df.columns[1:]  # 假设第一列是 Dataset，其他是算法名称
#
# # 数据准备：重塑数据为适合绘制箱线图的格式
# boxplot_data = []
#
# overall_color = '#87CEFA'  # 你可以改变为任何你喜欢的颜色
#
# # 遍历每个算法，提取每个算法在所有数据集下的值，去除NaN值
# for algorithm in algorithms:
#     # 删除空值（NaN），只使用有效的数据
#     cleaned_data = df[algorithm].dropna().values
#     boxplot_data.append(cleaned_data)
#
# # 创建箱线图
# plt.figure(figsize=(12, 8))
#
# # 绘制箱线图
# # plt.boxplot(boxplot_data, labels=algorithms, patch_artist=True)
# plt.boxplot(boxplot_data, patch_artist=True,
#             boxprops=dict(facecolor=overall_color, color='black'),
#             whiskerprops=dict(color='black'),
#             capprops=dict(color='black'),
#             medianprops=dict(color='black'))
# # 设置标题和标签
# # plt.title('Boxplot of GLD Transactions per Request for Different Algorithms', size=16)
# # plt.xlabel('Algorithms', size=14)
# # plt.ylabel('GLD Transactions per Request', size=14)
#
# # 设置标题和标签
# # plt.title('Boxplot of Algorithm Performance Across Datasets')
# plt.xticks(range(1, len(algorithms) + 1), algorithms, rotation=20, fontsize=18)
# plt.ylabel('GLD Transactions per Request', fontsize=18, fontweight='bold')
#
# # 显示图形
# plt.tight_layout()
# plt.show()

# # 箱线图 可选颜色
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# # 从 Excel 文件中加载数据
# df = pd.read_excel('./all_log/profiler_result.xlsx', sheet_name='gld_transactions_per_request')
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
# plt.ylabel('GLD Transactions per Request', fontsize=25, fontweight='bold')
#
# # 调整纵坐标刻度的字体大小
# plt.tick_params(axis='y', labelsize=25)  # 设置纵坐标刻度标签的字体大小为18
#
# # 显示图形
# plt.tight_layout()
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 从 Excel 文件中加载数据
df = pd.read_excel('./all_log/profiler_result.xlsx', sheet_name='gld_transactions_per_request')

# 提取数据集名称（第一列）和算法名称（列头）
datasets = df['Datasets']
algorithms = df.columns[1:]  # 假设第一列是 Dataset，其他是算法名称

# 假设数据已经加载到df中
# 数据清洗和提取有效数据
boxplot_data = []
for algorithm in algorithms:
    # 删除空值（NaN），只使用有效的数据
    cleaned_data = df[algorithm].dropna().values
    boxplot_data.append(cleaned_data)

# 自定义颜色，定义为一个列表，每个颜色对应一个算法
colors = ['#f6c89a', '#a5d4a1', '#c1b3d5', '#fefea9', '#9fbaef', '#f9bbf8', '#b2b893', '#bce2ea', '#91d0fc', '#f2e5c1']

# 创建箱线图
plt.figure(figsize=(16, 10))
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
plt.ylabel('gld_transactions_per_request', fontsize=30, fontweight='bold')
# 调整纵坐标刻度的字体大小
plt.tick_params(axis='x', labelsize=25)  # 设置纵坐标刻度标签的字体大小为25
# 调整纵坐标刻度的字体大小
plt.tick_params(axis='y', labelsize=25)  # 设置纵坐标刻度标签的字体大小为25

# 显示图形
plt.tight_layout()

plt.savefig(r'D:\BaiduNetdiskDownload\gld_transactions_per_request_v4.pdf', format='pdf')

plt.show()
