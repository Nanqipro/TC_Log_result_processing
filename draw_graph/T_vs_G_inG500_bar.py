# # G500数据集上的折线图
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Load the data from the Excel file
# file_path = './TrustVSGroupTC/G500_TRUSTvsGroupTC_lowdegree_2.xlsx'  # 请修改为实际的文件路径
# df = pd.read_excel(file_path)
#
# # Extract data for plotting
# # edge_count = df['avg_degree'].astype(str)  # 将 Edge Count 转换为字符串以便作为标签
# datasets = df['datasets']
# speed_up_build = df['speed-up_build']
# speed_up_search = df['speed-up_search']
#
# # Set up the figure and axes for the speed-up plot
# fig, ax = plt.subplots(figsize=(15, 8))
#
# # Plotting the speed-up ratios as line plots
# ax.plot(datasets, speed_up_build, marker='o', markersize=7, linestyle='-', color='#66CC00', label='Speed-up_build', linewidth=3)
# ax.plot(datasets, speed_up_search, marker='s', markersize=7, linestyle='-', color='#A8D8EA', label='Speed-up Search', linewidth=3)
#
# # Set axis labels and title with bold font
# ax.set_xlabel('datasets', fontsize=18, fontweight='bold')
# ax.set_ylabel('Speedup', fontsize=18, fontweight='bold')
#
# # Set x-ticks evenly spaced
# num_ticks = len(datasets)
# ax.set_xticks(np.linspace(0, num_ticks - 1, num_ticks))  # 设置均匀分布的tick位置
# ax.set_xticklabels(datasets, rotation=20, ha='center', fontsize=20)
#
# # Add legend with specified font size
# ax.legend(fontsize=18)
#
# # Set y-axis tick label size
# ax.tick_params(axis='y', labelsize=18)
#
# # Set thicker border for the plot
# ax.spines['top'].set_linewidth(2)
# ax.spines['right'].set_linewidth(2)
# ax.spines['bottom'].set_linewidth(2)
# ax.spines['left'].set_linewidth(2)
#
# # Show the plot
# plt.tight_layout()
# plt.show()

# # percents
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
#
# # 读取数据
# file_path = './TrustVSGroupTC/G500_TRUSTvsGroupTC_lowdegree_1.xlsx'
# df = pd.read_excel(file_path)
#
# # 提取数据列
# datasets = df['datasets'].tolist()
# GroupTC_HASH_build_percent = df['GroupTC-HASH-bulid_percent'].tolist()
# TRUST_build_percent = df['TRUST-bulid_percent'].tolist()
# GroupTC_HASH_search_percent = df['GroupTC-HASH-search_percent'].tolist()
# TRUST_search_percent = df['TRUST-search_percent'].tolist()
#
# # 定义柱子的位置
# x = np.arange(len(datasets))  # datasets 在横坐标上的位置
# width = 0.2  # 每个柱子的宽度
#
# # 创建图形
# fig, ax = plt.subplots(figsize=(10, 6))
#
# # 绘制柱子
# ax.bar(x - width/2, GroupTC_HASH_build_percent, width, bottom=GroupTC_HASH_search_percent, label='GroupTC-HASH Build', color='#fefeb2',edgecolor='black',linewidth=1)
# ax.bar(x + width/2, TRUST_build_percent, width,bottom=TRUST_search_percent, label='TRUST Build', color='#9cd5fc',edgecolor='black',linewidth=1)
#
# ax.bar(x - width/2, GroupTC_HASH_search_percent, width, label='GroupTC-HASH Search', color='#f2e5c1',edgecolor='black',linewidth=1)
# ax.bar(x + width/2, TRUST_search_percent, width, label='TRUST Search', color='#bce2ea',edgecolor='black',linewidth=1)
#
# # 添加标签和标题
# ax.set_xlabel('Datasets')
# ax.set_ylabel('Percentage')
# ax.set_title('Comparison of GroupTC-HASH and TRUST Algorithms')
# ax.set_xticks(x)
# ax.set_xticklabels(datasets)
# ax.set_ylim(0, 1)  # 百分比范围从0到1
#
# # 显示图例
# ax.legend()
#
# # 显示图形
# plt.tight_layout()
# plt.show()



# # bar Graph
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.ticker import FuncFormatter
#
# # 读取数据
# file_path = './TrustVSGroupTC/G500_TRUSTvsGroupTC_lowdegree_1.xlsx'
# df = pd.read_excel(file_path)
#
# # 提取数据列
# datasets = df['datasets'].tolist()
# GroupTC_HASH_build = df['GroupTC-HASH'].tolist()
# TRUST_build = df['TRUST'].tolist()
# GroupTC_HASH_search = df['GroupTC-HASH-search-time'].tolist()
# TRUST_search = df['TRUST-search-time'].tolist()
#
# # 定义柱子的位置
# x = np.arange(len(datasets))  # datasets 在横坐标上的位置
# width = 0.2  # 每个柱子的宽度
#
# # 创建图形
# fig, ax = plt.subplots(figsize=(10, 6))
#
# # 绘制堆叠柱子
# ax.bar(x - width/2, GroupTC_HASH_search, width, label='GroupTC-HASH Search', color='#f2e5c1', linewidth=1)
# ax.bar(x - width/2, GroupTC_HASH_build, width, bottom=GroupTC_HASH_search, label='GroupTC-HASH Build', color='#c2b79a', linewidth=1)
# ax.bar(x + width/2, TRUST_search, width, label='TRUST Search', color='#bce2ea', linewidth=1)
# ax.bar(x + width/2, TRUST_build, width, bottom=TRUST_search, label='TRUST Build', color='#96b5bb', linewidth=1)
#
# # 设置刻度格式为科学记数法（10的n次方）
# ax.set_ylabel('Time (ms)', fontsize=24, fontweight='bold')
# ax.set_yscale('log')  # 设置 y 轴为对数坐标
# ax.tick_params(axis='y', labelsize=20)
# # 添加标签和标题
# # ax.set_xlabel('Datasets')
# # ax.set_title('Comparison of GroupTC-HASH and TRUST Algorithms')
# ax.set_xticks(x)
# ax.set_xticklabels(datasets)
#
# # 显示图例
# ax.legend()
#
# # 显示图形
# plt.tight_layout()
# plt.show()



# 折线图与百分比图复合图
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
# 读取第一个Excel文件的数据
file_path = './TrustVSGroupTC/G500_TRUSTvsGroupTC_lowdegree_1.xlsx'
df1 = pd.read_excel(file_path)

# 提取数据列
datasets = df1['datasets'].tolist()
GroupTC_HASH_build_percent = df1['GroupTC-HASH-bulid_percent'].tolist()
TRUST_build_percent = df1['TRUST-bulid_percent'].tolist()
GroupTC_HASH_search_percent = df1['GroupTC-HASH-search_percent'].tolist()
TRUST_search_percent = df1['TRUST-search_percent'].tolist()

# 提取数据列
speed_up_build = df1['speed-up_build'].tolist()
speed_up_search = df1['speed-up_search'].tolist()

# 定义柱子的位置
x = np.arange(len(datasets))  # datasets 在横坐标上的位置
width = 0.2  # 每个柱子的宽度

# 创建图形和双Y轴
fig, ax1 = plt.subplots(figsize=(15, 8))

# 创建右边的Y轴（speed-up的折线图）
ax2 = ax1.twinx()

# 绘制百分比的柱状图（左Y轴）
ax2.bar(x - width/2, TRUST_build_percent, width, bottom=TRUST_search_percent, label='TRUST Hash Table Construction', color='#9cd5fc', edgecolor='black', linewidth=1)
ax2.bar(x + width/2, GroupTC_HASH_build_percent, width, bottom=GroupTC_HASH_search_percent, label='GroupTC-HS Hash Table Construction', color='#fefeb2', edgecolor='black', linewidth=1)
ax2.bar(x - width/2, TRUST_search_percent, width, label='TRUST Hash Search', color='#bce2ea', edgecolor='black', linewidth=1)
ax2.bar(x + width/2, GroupTC_HASH_search_percent, width, label='GroupTC-HS Hash Search', color='#f2e5c1', edgecolor='black', linewidth=1)

# 设置右边Y轴的标签和范围
ax2.set_ylabel('Percentage', fontsize=25, fontweight='bold')
ax2.set_ylim(0, 1)  # 百分比范围从0到1
# 使用FuncFormatter将Y轴格式化为百分比
ax2.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y*100:.0f}%'))
# 绘制折线图
ax1.plot(datasets, speed_up_build, marker='o', markersize=12, linestyle='-', color='#344C64', label='Hash Table Construction', linewidth=4)
ax1.plot(datasets, speed_up_search, marker='^', markersize=12, linestyle='-', color='#57A6A1', label='Hash Search', linewidth=4)

# 设置X轴
ax1.set_xlabel('', fontsize=25, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(datasets, rotation=20, ha='center', fontsize=20)

# 设置左右边Y轴的标签和范围
ax1.set_ylabel('Speedup', fontsize=25, fontweight='bold')

# 修改左右边Y轴刻度标签的字体大小
ax1.tick_params(axis='y', labelsize=20)  # 设置左边Y轴的字体大小
ax2.tick_params(axis='y', labelsize=20)  # 设置右边Y轴的字体大小

# 设置图例
fig.legend(loc='upper left', bbox_to_anchor=(0.47, 0.95), ncol=1, fontsize=20, frameon=True, facecolor=(1, 1, 1, 0.6), edgecolor='none')

# 调整图层顺序，确保折线图在上面
ax1.set_zorder(5)
ax2.set_zorder(2)
ax1.patch.set_visible(False)  # 去掉ax2的背景

# 显示图形
plt.tight_layout()

# 保存图形为 PDF 文件
plt.savefig(r'D:\BaiduNetdiskDownload\percentage_change_E.pdf', format='pdf')

plt.show()
