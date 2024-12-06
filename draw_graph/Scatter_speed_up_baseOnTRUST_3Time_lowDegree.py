# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
#
# # 读取Excel文件
# file_path = './TrustVSGroupTC/lowDegree-buildIndex.xlsx'  # 修改为实际的文件路径
# df = pd.read_excel(file_path)
#
# # 检查数据结构，确保列名正确
# print(df.head())
#
# # 假设 Excel 中列名分别是 'edge-count' 和 'speed-up'，如果不同请根据实际修改
# x = df['edge-count']
# y = df['speed-up']
#
# # 对数据进行对数变换，以e为底的对数
# x_log = np.log1p(x)
# # y_log = np.log1p(y)
#
# # 创建散点图
# plt.figure(figsize=(10, 6))
# plt.scatter(x_log, y, marker='o', color='blue', alpha=0.5)
#
# # 设置横纵坐标的刻度
# plt.xticks(np.arange(10, int(x_log.max()) + 1, 0.5))
# plt.yticks(np.arange(0, int(y.max())+0.5, 0.2))  # 每隔 0.5 进行刻度显示
#
# # 设置标题和标签
# # plt.title('Log Transformed Edge Count vs Speed-up', fontsize=14)
# plt.xlabel('Log(Edge Count)', fontsize=12)
# plt.ylabel('Log(Speed-up)', fontsize=12)
#
# # 显示网格
# plt.grid(False)
#
# # 显示图像
# plt.show()


# speed-up,speed-up_build,speed-up_search  only scatter
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取Excel文件
file_path = './TrustVSGroupTC/lowDegree-buildIndex.xlsx'  # 修改为实际的文件路径
df = pd.read_excel(file_path)

# 检查数据结构，确保列名正确
print(df.head())

# 假设 Excel 中列名分别是 'edge-count'、'speed-up'、'speed-up_search' 和 'speed-up_build'
x = df['edge-count']
y = df['speed-up']
y_search = df['speed-up_search']
y_build = df['speed-up_build']

# 对数据进行对数变换，以e为底的对数
x_log = x

# 创建图形和子图
fig, ax1 = plt.subplots(figsize=(30, 10))


# 添加 speed-up_build 的散点图
ax1.scatter(x_log, y_build, marker='^', color='#E29135', alpha=1, s=140, linewidths=9, label='Hash Table Construction')
# 添加 speed-up_search 的散点图
ax1.scatter(x_log, y_search, marker='o', color='#94C6CD', alpha=1, s=140, linewidths=9, label='Hash Search')
# 创建原始的散点图
ax1.scatter(x_log, y, marker='*', color='#4A5F7E', alpha=1, s=140, linewidths=9, label='Total')

# # 添加 speed-up_build 的散点图
# ax1.scatter(x_log, y_build, marker='^', color='#89AA7B', alpha=1, s=50, linewidths=5, label='Hash Table Construction')
# # 添加 speed-up_search 的散点图
# ax1.scatter(x_log, y_search, marker='o', color='#9D9EA3', alpha=1, s=50, linewidths=5, label='Hash Search')
# # 创建原始的散点图
# ax1.scatter(x_log, y, marker='*', color='#9BBBE1', alpha=1, s=100, linewidths=5, label='Total')


# 添加基准线 y=1
ax1.axhline(y=1, color='red', linestyle='-', linewidth=4, label='baseline')

# 设置 X 轴为对数坐标
ax1.set_xscale('log')

# 设置 y 轴为对数坐标（可以根据需要取消注释）
# ax1.set_yscale('log')

# 设置坐标轴标签
ax1.set_xlabel('Edge Count', fontsize=30, fontweight='bold')
ax1.set_ylabel('Speedup', fontsize=30, fontweight='bold')

# 设置 x 轴的刻度标签大小
ax1.tick_params(axis='x', labelsize=25)

# 设置 y 轴的刻度标签大小
ax1.tick_params(axis='y', labelsize=25)

# 设置边框线宽
ax = plt.gca()
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)

# 显示网格
ax1.grid(False)

# 添加图例
# ax1.legend(fontsize=20)
fig.legend(loc='upper left', bbox_to_anchor=(0.82, 0.95), ncol=1, fontsize=20, frameon=True, facecolor=(1, 1, 1, 0.6))


# 显示图形
plt.tight_layout(pad=1.0, h_pad=2.0, w_pad=1.0)

plt.savefig(r'D:\BaiduNetdiskDownload\Scatter_speed_up_baseOnTRUST_3Time_lowDegree.pdf', format='pdf')

# 显示图像
plt.show()

# # speed-up,speed-up_build,speed-up_search
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.ticker import FuncFormatter
#
# # 读取Excel文件
# file_path = './TrustVSGroupTC/lowDegree-buildIndex.xlsx'  # 修改为实际的文件路径
# df = pd.read_excel(file_path)
#
# # 检查数据结构，确保列名正确
# print(df.head())
#
# # 假设 Excel 中列名分别是 'edge-count'、'speed-up'、'speed-up_search' 和 'speed-up_build'
# x = df['edge-count']
# y = df['speed-up']
# y_search = df['speed-up_search']
# y_build = df['speed-up_build']
# y2_percentage_TRUST = df['TRUST-percent-search']
# y2_percentage_GroupTC_HS = df['GroupTC-HS-percent-search']
# # 对数据进行对数变换，以e为底的对数
# x_log = x
#
# # 创建图形和子图
# fig, ax1 = plt.subplots(figsize=(15, 8))
#
#
# # 添加 speed-up_build 的散点图
# ax1.scatter(x_log, y_build, marker='^', color='#88dae1', alpha=1, s=50, linewidths=5, label='Hash Table Construction')
#
# # 添加 speed-up_search 的散点图
# ax1.scatter(x_log, y_search, marker='o', color='#69a5a2', alpha=1, s=50, linewidths=5, label='Hash Search')
#
# # 创建原始的散点图
# ax1.scatter(x_log, y, marker='*', color='#666e9a', alpha=1, s=100, linewidths=5, label='Total')
# # 添加基准线 y=1
# ax1.axhline(y=1, color='red', linestyle='-.', linewidth=2, label='Baseline')
#
# # 设置 X 轴为对数坐标
# ax1.set_xscale('log')
#
# # 设置 y 轴为对数坐标（可以根据需要取消注释）
# # ax1.set_yscale('log')
#
# # 设置坐标轴标签
# ax1.set_xlabel('Edge Count', fontsize=22, fontweight='bold')
# ax1.set_ylabel('Speedup', fontsize=22, fontweight='bold')
#
# # 设置 x 轴的刻度标签大小
# ax1.tick_params(axis='x', labelsize=20)
#
# # 设置 y 轴的刻度标签大小
# ax1.tick_params(axis='y', labelsize=20)
#
# # 设置边框线宽
# ax = plt.gca()
# ax.spines['top'].set_linewidth(2)
# ax.spines['right'].set_linewidth(2)
# ax.spines['bottom'].set_linewidth(2)
# ax.spines['left'].set_linewidth(2)
#
# # 创建第二个Y轴
# ax2 = ax1.twinx()
#
# # 绘制百分比数据的折线图
# ax2.plot(x_log, y2_percentage_TRUST, color='#f56c5e', marker='o', linestyle='-', linewidth=3, label='TRUST-percent-search')
# ax2.plot(x_log, y2_percentage_GroupTC_HS, color='#61b8d2', marker='^', linestyle='-', linewidth=3, label='GroupTC-HS-percent-search')
#
# ax2.set_ylim(0, 1)  # 百分比范围从0到1
# # 使用FuncFormatter将Y轴格式化为百分比
# ax2.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y*100:.0f}%'))
#
# # 设置第二个y轴的刻度标签大小
# ax2.tick_params(axis='y', labelsize=20)
#
# # 显示网格
# ax1.grid(False)
#
# # 添加图例
# ax1.legend(fontsize=20)
#
# # 显示图形
# plt.tight_layout(pad=1.0, h_pad=2.0, w_pad=1.0)
#
# plt.savefig(r'D:\BaiduNetdiskDownload\Scatter_speed_up_baseOnTRUST_3Time_lowDegree.pdf', format='pdf')
#
# # 显示图像
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.ticker import FuncFormatter
#
# # 读取Excel文件
# file_path = './TrustVSGroupTC/lowDegree-buildIndex.xlsx'  # 修改为实际的文件路径
# df = pd.read_excel(file_path)
#
# # 检查数据结构，确保列名正确
# print(df.head())
#
# # 假设 Excel 中列名分别是 'edge-count'、'speed-up'、'speed-up_search' 和 'speed-up_build'
# x = df['edge-count']
# y = df['speed-up']
# y_search = df['speed-up_search']
# y_build = df['speed-up_build']
# y2_percentage_TRUST = df['TRUST-percent-search']
# y2_percentage_GroupTC_HS = df['GroupTC-HS-percent-search']
#
# # 对数据进行排序，确保按 'edge-count' 从小到大排序
# df_sorted = df.sort_values(by='edge-count')
#
# # 提取排序后的数据
# x_sorted = df_sorted['edge-count']
# y_sorted = df_sorted['speed-up']
# y_search_sorted = df_sorted['speed-up_search']
# y_build_sorted = df_sorted['speed-up_build']
# y2_percentage_TRUST_sorted = df_sorted['TRUST-percent-search']
# y2_percentage_GroupTC_HS_sorted = df_sorted['GroupTC-HS-percent-search']
#
# # # 对数据进行对数变换，以e为底的对数
# x_log = np.log(x_sorted)
# # 对数据进行对数变换，以e为底的对数
# # x_log = x
# # 创建图形和子图
# fig, ax1 = plt.subplots(figsize=(15, 8))
#
# # 添加 speed-up_build 的散点图
# ax1.scatter(x_log, y_build_sorted, marker='^', color='#88dae1', alpha=1, s=50, linewidths=5, label='Hash Table Construction')
#
# # 添加 speed-up_search 的散点图
# ax1.scatter(x_log, y_search_sorted, marker='o', color='#69a5a2', alpha=1, s=50, linewidths=5, label='Hash Search')
#
# # 创建原始的散点图
# ax1.scatter(x_log, y_sorted, marker='*', color='#666e9a', alpha=1, s=100, linewidths=5, label='Total')
#
# # 添加基准线 y=1
# ax1.axhline(y=1, color='red', linestyle='-.', linewidth=2, label='Baseline')
#
# # 设置 X 轴为对数坐标
# ax1.set_xscale('log')
#
# # 设置坐标轴标签
# ax1.set_xlabel('Edge Count', fontsize=22, fontweight='bold')
# ax1.set_ylabel('Speedup', fontsize=22, fontweight='bold')
#
# # 设置 x 轴的刻度标签大小
# ax1.tick_params(axis='x', labelsize=20)
#
# # 设置 y 轴的刻度标签大小
# ax1.tick_params(axis='y', labelsize=20)
#
# # 设置边框线宽
# ax = plt.gca()
# ax.spines['top'].set_linewidth(2)
# ax.spines['right'].set_linewidth(2)
# ax.spines['bottom'].set_linewidth(2)
# ax.spines['left'].set_linewidth(2)
#
# # 创建第二个Y轴
# ax2 = ax1.twinx()
#
# # 绘制百分比数据的折线图
# ax2.plot(x_log, y2_percentage_TRUST_sorted, color='#f56c5e', marker='^', linestyle='-', linewidth=3, label='TRUST Hash search')
# ax2.plot(x_log, y2_percentage_GroupTC_HS_sorted, color='#61b8d2', marker='o', linestyle='-', linewidth=3, label='GroupTC HS Hash search')
#
# ax2.set_ylim(0, 1)  # 百分比范围从0到1
# # 使用FuncFormatter将Y轴格式化为百分比
# ax2.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y*100:.0f}%'))
#
# # 设置第二个y轴的刻度标签大小
# ax2.tick_params(axis='y', labelsize=20)
#
# # 显示网格
# ax1.grid(False)
#
# # 添加图例
# fig.legend(loc='upper left', bbox_to_anchor=(0.50, 0.85), ncol=1, fontsize=20, frameon=True, facecolor=(1, 1, 1, 0.6), edgecolor='none')
#
#
# # 显示图形
# plt.tight_layout(pad=1.0, h_pad=2.0, w_pad=1.0)
#
# # 保存图像
# plt.savefig(r'D:\BaiduNetdiskDownload\Scatter_speed_up_baseOnTRUST_3Time_lowDegree.pdf', format='pdf')
#
# # 显示图像
# plt.show()
