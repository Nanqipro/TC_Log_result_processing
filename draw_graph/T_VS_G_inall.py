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

#speed-up
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取Excel文件
file_path = './TrustVSGroupTC/lowDegree-buildIndex.xlsx'  # 修改为实际的文件路径
df = pd.read_excel(file_path)

# 检查数据结构，确保列名正确
print(df.head())

# 假设 Excel 中列名分别是 'edge-count' 和 'speed-up'
x = df['edge-count']
y = df['speed-up']

# 对数据进行对数变换，以e为底的对数
x_log = x

# 创建图形和子图
fig, ax1 = plt.subplots(figsize=(15, 8))

# 创建散点图
ax1.scatter(x_log, y, marker='x', color='blue', alpha=0.6, s=80, linewidths=4)

# 设置 X 轴为对数坐标
ax1.set_xscale('log')

# 设置 y 轴为对数坐标
# ax1.set_yscale('log')

# 设置坐标轴标签
ax1.set_xlabel('Edge Count', fontsize=20, fontweight='bold')
ax1.set_ylabel('Speed-up', fontsize=20, fontweight='bold')
# 设置 x 轴的刻度标签大小
ax1.tick_params(axis='x', labelsize=20)
# 设置 y 轴的刻度标签大小
ax1.tick_params(axis='y', labelsize=20)
# 设置边框线宽
ax = plt.gca()
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)

# 显示网格
ax1.grid(False)
# 显示图形
plt.tight_layout(pad=1.0, h_pad=2.0, w_pad=1.0)
# 显示图像
plt.show()


# # speed-up,speed-up_build,speed-up_search
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
# # 假设 Excel 中列名分别是 'edge-count'、'speed-up'、'speed-up_search' 和 'speed-up_build'
# x = df['edge-count']
# y = df['speed-up']
# y_search = df['speed-up_search']
# y_build = df['speed-up_build']
#
# # 对数据进行对数变换，以e为底的对数
# x_log = x
#
# # 创建图形和子图
# fig, ax1 = plt.subplots(figsize=(10, 6))
#
# # 创建原始的散点图
# ax1.scatter(x_log, y, marker='x', color='#000B58', alpha=0.6, s=80, linewidths=4, label='Speed-up')
#
# # 添加 speed-up_search 的散点图
# ax1.scatter(x_log, y_search, marker='o', color='#006A67', alpha=0.6, s=20, linewidths=4, label='Speed-up Search')
#
# # 添加 speed-up_build 的散点图
# ax1.scatter(x_log, y_build, marker='^', color='#36C2CE', alpha=0.6, s=20, linewidths=4, label='Speed-up Build')
#
# # 设置 X 轴为对数坐标
# ax1.set_xscale('log')
#
# # 设置 y 轴为对数坐标（可以根据需要取消注释）
# # ax1.set_yscale('log')
#
# # 设置坐标轴标签
# ax1.set_ylabel('Speed-up', fontsize=20, fontweight='bold')
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
# # 显示网格
# ax1.grid(False)
#
# # 添加图例
# ax1.legend(fontsize=14)
#
# # 显示图形
# plt.tight_layout(pad=1.0, h_pad=2.0, w_pad=1.0)
# # 显示图像
# plt.show()

