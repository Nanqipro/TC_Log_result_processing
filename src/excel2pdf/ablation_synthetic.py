import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from the Excel file
file_path = '../../excel/grouptc_bs_ablation_time.xlsx'
df = pd.read_excel(file_path)

# Extract data for plotting
datasets = df['Datasets'][20:37]
o1 = df['VP_speedup'][20:37]
o1o2 = df['VP+EF_speedup'][20:37]
o1o2o3 = df['VP+EF+RL_speedup'][20:37]
# avg_degree = df['avg_degree'] if 'avg_degree' in df.columns else None  # Optional avg_degree column

# Set up the figure and axes
fig, ax1 = plt.subplots(figsize=(30, 10))

# Set width of bar
bar_width = 0.2
# 设置每组柱状图的位置，确保每组柱子紧密排列
spacing = 0.25  # 设置每组数据集之间的间隔
# Set positions for each bar group
# bar_positions = np.arange(len(datasets))
# 设置柱状图的x轴位置，使用arange并增加spacing来调整间隔
bar_positions = np.arange(len(datasets)) * (3 * bar_width + spacing)  # 使每组数据集之间有间隔

# Plotting the bar chart with edgecolor
ax1.bar(bar_positions - 1 * bar_width, o1, bar_width, label='VP', color='#9ccffa', edgecolor='black', linewidth=1)
ax1.bar(bar_positions + 0 * bar_width, o1o2, bar_width, label='VP+EF', color='#577d97', edgecolor='black', linewidth=1)
ax1.bar(bar_positions + 1 * bar_width, o1o2o3, bar_width, label='VP+EF+RL', color='#f0c99e', edgecolor='black', linewidth=1)

# Add avg_degree as a secondary line plot if available
# if avg_degree is not None:
#     ax2 = ax1.twinx()
#     ax2.plot(bar_positions, avg_degree, 'k-', marker='s', label='ave degree', linewidth=2)
#     ax2.set_ylabel('Speedup', fontsize=50, fontweight='bold')
#     ax2.set_ylim(0, 100)
#     ax2.tick_params(axis='both', labelsize=50)  # 设置 y 轴和 x 轴刻度标签字体大小为 20
# 添加基准线 y=1
ax1.axhline(y=1, color='red', linestyle='-', linewidth=4, label='baseline')
# Set axis labels and title
ax1.set_xlabel('', fontsize=50, fontweight='bold')
ax1.set_ylabel('Speedup', fontsize=50, fontweight='bold')
# ax1.set_yscale('log')
# ax1.set_title('Running times of different algorithms under various datasets', fontsize=16)

# Set y-axis tick label size for the main axis
ax1.tick_params(axis='y', labelsize=50)

# Set x-ticks
ax1.set_xticks(bar_positions)
ax1.set_xticklabels(datasets, fontsize=45, rotation=0, ha='center')

# 添加图例
# fig.legend(loc='upper left', bbox_to_anchor=(0.07, 0.95), fontsize=20)
fig.legend(loc='upper right', bbox_to_anchor=(0.98, 1), ncol=4, fontsize=45)

# 设置 x 轴范围，左边界为负值，以缩短第一个刻度与原点的距离
ax1.set_xlim([-0.38, len(datasets) * (3 * bar_width + spacing) -0.52])


# Set thicker border for the plot
ax = plt.gca()
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)


plt.tight_layout(pad=1.0, h_pad=2.0, w_pad=1.0)

# Show the plot
plt.tight_layout()

# 保存图形为 PDF 文件
plt.savefig('../../pdf/grouptc_bs_ablation_synthetic_v1.pdf', format='pdf')

plt.show()
