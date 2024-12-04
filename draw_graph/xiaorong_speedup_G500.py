import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from the Excel file
file_path = './xiaorong_for_GroupTC-BS/GroupTC-BS-xiaorong-G500.xlsx'  # 请确保文件路径正确
df_speedup = pd.read_excel(file_path, sheet_name='all')

# 确保不对数据进行排序，直接按原始顺序提取数据
datasets = df_speedup['datasets']
speedup1 = df_speedup['speedup-opt1']
speedup2 = df_speedup['speedup-opt12']
speedup3 = df_speedup['speedup-opt123']
baseline = df_speedup['baseline']

# # 按照 'datasets' 列排序
# df_speedup_sorted = df_speedup.sort_values(by='datasets')
#
# # Extract sorted data for plotting
# datasets = df_speedup_sorted['datasets']
# speedup1 = df_speedup_sorted['speedup-opt1']
# speedup2 = df_speedup_sorted['speedup-opt12']
# speedup3 = df_speedup_sorted['speedup-opt123']
# baseline = df_speedup_sorted['baseline']

# 使用数据框的索引作为 x 轴
x = np.arange(len(datasets))

# 设置图形和坐标轴
fig, ax = plt.subplots(figsize=(30, 10))

# 绘制线条，使用索引作为 x 值
ax.plot(x, speedup1, marker='s', markersize=15, linestyle='-', alpha=1, color='#77E4C8', label='o1', linewidth=5)
ax.plot(x, speedup2, marker='o', markersize=15, linestyle='-', alpha=1, color='#577d97', label='o1+o2', linewidth=5)
ax.plot(x, speedup3, marker='^', markersize=15, linestyle='-', alpha=1, color='#c2b79a', label='o1+o2+o3', linewidth=5)
ax.plot(x, baseline, marker='*', markersize=15, linestyle='-.', alpha=1, color='red', label='baseline', linewidth=5)

# 设置 y 轴标签
ax.set_ylabel('Speedup', fontsize=25, fontweight='bold')

# 设置 x 轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(datasets, rotation=20, ha='center', fontsize=20)

# 添加图例
ax.legend(fontsize=20)

# 设置坐标轴刻度参数
ax.tick_params(axis='x', labelsize=22, width=4)
ax.tick_params(axis='y', labelsize=20, width=4)

# 设置图形边框线宽
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)

# 调整布局
plt.tight_layout()

# 保存图形为 PDF 文件
plt.savefig(r'D:\BaiduNetdiskDownload\xiaorong_speedup_G500Datasets.pdf', format='pdf')

# 显示图形
plt.show()
