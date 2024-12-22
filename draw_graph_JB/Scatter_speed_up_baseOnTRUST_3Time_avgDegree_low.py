
# #%%
# # speed-up,speed-up_build,speed-up_search only scatter
# import pandas as pd
# import matplotlib.pyplot as plt

# # 读取Excel文件
# file_path = './TrustVSGroupTC/lowDegree-buildIndex.xlsx'  # 修改为实际的文件路径
# df = pd.read_excel(file_path)

# # 数据列名
# x = df['avg_degree']
# y = df['speed-up-all']
# y_search = df['speed-up_search']
# y_build = df['speed-up_build']

# # 筛选大于 10 的值
# condition = (y > 10) | (y_search > 10) | (y_build > 10)

# # 普通值
# x_normal = x[~condition]
# y_normal = y[~condition]
# y_search_normal = y_search[~condition]
# y_build_normal = y_build[~condition]

# # 特殊值
# x_special = x[condition]
# y_special = y[condition]
# y_search_special = y_search[condition]
# y_build_special = y_build[condition]

# # 创建主图
# fig, ax1 = plt.subplots(figsize=(30, 10))

# # 绘制普通值散点图
# ax1.scatter(x_normal, y_build_normal, marker='^', color='#E29135', alpha=1, s=200, linewidths=9, label='Hash Table Construction')
# ax1.scatter(x_normal, y_search_normal, marker='o', color='#94C6CD', alpha=1, s=200, linewidths=9, label='Hash Search')
# ax1.scatter(x_normal, y_normal, marker='*', color='#4A5F7E', alpha=1, s=200, linewidths=9, label='Total')

# # 添加基准线 y=1
# ax1.axhline(y=1, color='red', linestyle='-', linewidth=4, label='baseline')

# # 设置坐标轴标签
# ax1.set_xlabel('avg degree', fontsize=30, fontweight='bold')
# ax1.set_ylabel('Speedup', fontsize=30, fontweight='bold')


# # 设置刻度标签大小
# ax1.tick_params(axis='x', labelsize=25)
# ax1.tick_params(axis='y', labelsize=25)

# # 设置边框线宽
# ax = plt.gca()
# ax.spines['top'].set_linewidth(2)
# ax.spines['right'].set_linewidth(2)
# ax.spines['bottom'].set_linewidth(2)
# ax.spines['left'].set_linewidth(2)

# # 添加图例
# fig.legend(loc='upper left', bbox_to_anchor=(0.82, 0.95), ncol=1, fontsize=20, frameon=True, facecolor=(1, 1, 1, 0.6))

# # 添加小窗显示特殊值（右上角空白处）
# inset_ax = fig.add_axes([0.12, 0.8, 0.1, 0.15])  # 小窗位置：[左, 下, 宽, 高]
# inset_ax.scatter(x_special, y_build_special, marker='^', color='#E29135', alpha=1, s=100, linewidths=9)
# inset_ax.scatter(x_special, y_search_special, marker='o', color='#94C6CD', alpha=1, s=100, linewidths=9)
# inset_ax.scatter(x_special, y_special, marker='*', color='#4A5F7E', alpha=1, s=100, linewidths=9)

# # 小窗设置（风格一致）
# # inset_ax.set_xlabel('avg degree', fontsize=15, fontweight='bold')
# # inset_ax.set_ylabel('Speedup', fontsize=15, fontweight='bold')
# # inset_ax.tick_params(axis='both', labelsize=10)
# inset_ax.set_xlim(min(x_special) * 0.9, max(x_special) * 1.1)
# inset_ax.set_ylim(12, 16)
# inset_ax.grid(alpha=0.5)

# # 自动调整布局并保存
# plt.tight_layout(pad=1.0, h_pad=2.0, w_pad=1.0)
# plt.savefig(r'D:\\work\\Good Lab\\overleaf\\TC-Journal\\data\\pdf\\Scatter_speed_up_baseOnTRUST_3Time_avgDegree_special_v1.pdf', format='pdf')

# # 显示图像
# plt.show()


#%%
# speed-up,speed-up_build,speed-up_search  only scatter
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取Excel文件
file_path = './TrustVSGroupTC/lowDegree-buildIndex.xlsx'  # 修改为实际的文件路径
df = pd.read_excel(file_path)

# 检查数据结构，确保列名正确
# print(df.head())

# 假设 Excel 中列名分别是 'edge-count'、'speed-up'、'speed-up_search' 和 'speed-up_build'
x = df['avg_degree']
y = df['speed-up-all']
y_search = df['speed-up_search']
y_build = df['speed-up_build']

# 对数据进行对数变换，以e为底的对数
x_log = x

# 创建图形和子图
fig, ax1 = plt.subplots(figsize=(30, 10))


# 添加 speed-up_build 的散点图
ax1.scatter(x_log, y_build, marker='^', color='#E29135', alpha=1, s=200, linewidths=9, label='Hash Table Construction')
# 添加 speed-up_search 的散点图
ax1.scatter(x_log, y_search, marker='o', color='#94C6CD', alpha=1, s=200, linewidths=9, label='Hash Search')
# 创建原始的散点图
ax1.scatter(x_log, y, marker='*', color='#4A5F7E', alpha=1, s=200, linewidths=9, label='Total')

# # 添加 speed-up_build 的散点图
# ax1.scatter(x_log, y_build, marker='^', color='#89AA7B', alpha=1, s=50, linewidths=5, label='Hash Table Construction')
# # 添加 speed-up_search 的散点图
# ax1.scatter(x_log, y_search, marker='o', color='#9D9EA3', alpha=1, s=50, linewidths=5, label='Hash Search')
# # 创建原始的散点图
# ax1.scatter(x_log, y, marker='*', color='#9BBBE1', alpha=1, s=100, linewidths=5, label='Total')


# 添加基准线 y=1
ax1.axhline(y=1, color='red', linestyle='-', linewidth=4, label='baseline')

# 设置 X 轴为对数坐标
# ax1.set_xscale('log')

# 设置 y 轴为对数坐标（可以根据需要取消注释）
# ax1.set_yscale('log')

# 设置坐标轴标签
ax1.set_xlabel('avg degree', fontsize=30, fontweight='bold')
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

plt.savefig(r'D:\BaiduNetdiskDownload\Scatter_speed_up_baseOnTRUST_3Time_avgDegree_v2.pdf', format='pdf')

# 显示图像
plt.show()
# %%
