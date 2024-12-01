# speed-up
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
ax1.scatter(x_log, y, marker='*', color='#666e9a', alpha=1, s=160, linewidths=7)

# 设置 X 轴为对数坐标
ax1.set_xscale('log')

# 设置 y 轴为对数坐标
# ax1.set_yscale('log')

# 设置坐标轴标签
ax1.set_xlabel('Edge Count', fontsize=22, fontweight='bold')
ax1.set_ylabel('Speedup', fontsize=22, fontweight='bold')
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

# 保存图形为 PDF 文件
plt.savefig(r'D:\BaiduNetdiskDownload\Scatter_speed_up_baseOnTRUST_allTime_lowDegree.pdf', format='pdf')

# 显示图像
plt.show()
