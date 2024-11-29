# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Load the data from the Excel file
# file_path = './all_log/time_all.xlsx'
# df = pd.read_excel(file_path)
#
# # Extract data for plotting
# datasets = df['Datasets']
# polak = df['Polak']
# groupTC_BS = df['GroupTC-BS']
# trust = df['TRUST']
# groupTC_HS = df['GroupTC-HS']
# avg_degree = df['avg_degree'] if 'avg_degree' in df.columns else None  # Optional avg_degree column
#
# # Set up the figure and axes
# fig, ax1 = plt.subplots(figsize=(30, 10))
#
# # Set width of bar
# bar_width = 0.2
#
# # Set positions for each bar group
# bar_positions = np.arange(len(datasets))
#
# # Plotting the bar chart with edgecolor
# ax1.bar(bar_positions - 1.5 * bar_width, polak, bar_width, label='Polak', color='#f6c89a', edgecolor='black', linewidth=1)
# ax1.bar(bar_positions - 0.5 * bar_width, trust, bar_width, label='TRUST', color='#bce2ea', edgecolor='black', linewidth=1)
# ax1.bar(bar_positions + 0.5 * bar_width, groupTC_HS, bar_width, label='GroupTC-BS', color='#91d0fc', edgecolor='black', linewidth=1)
# ax1.bar(bar_positions + 1.5 * bar_width, groupTC_BS, bar_width, label='GroupTC-HS', color='#f2e5c1', edgecolor='black', linewidth=1)
#
# # Add avg_degree as a secondary line plot if available
# if avg_degree is not None:
#     ax2 = ax1.twinx()
#     ax2.plot(bar_positions, avg_degree, 'k-', marker='s', label='avg degree', linewidth=2)
#     ax2.set_ylabel('avg degree', fontsize=25, fontweight='bold')
#     ax2.set_ylim(0, 100)
#     ax2.tick_params(axis='both', labelsize=20)  # 设置 y 轴和 x 轴刻度标签字体大小为 20
#
# # Set axis labels and title
# ax1.set_xlabel('', fontsize=25, fontweight='bold')
# ax1.set_ylabel('Time (ms)', fontsize=25, fontweight='bold')
# ax1.set_yscale('log')
# # ax1.set_title('Running times of different algorithms under various datasets', fontsize=16)
#
# # Set y-axis tick label size for the main axis
# ax1.tick_params(axis='y', labelsize=20)
#
# # Set x-ticks
# ax1.set_xticks(bar_positions)
# ax1.set_xticklabels(datasets, fontsize=20, rotation=20, ha='center')
#
# # 添加图例
# # fig.legend(loc='upper left', bbox_to_anchor=(0.07, 0.95), fontsize=20)
# fig.legend(loc='upper center', bbox_to_anchor=(0.3, 0.95), ncol=5, fontsize=20)
# # Set thicker border for the plot
# ax = plt.gca()
# ax.spines['top'].set_linewidth(2)
# ax.spines['right'].set_linewidth(2)
# ax.spines['bottom'].set_linewidth(2)
# ax.spines['left'].set_linewidth(2)
#
# # Show the plot
# plt.tight_layout()
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from the Excel file
file_path = './G500_log/G500_log1.xlsx'
df = pd.read_excel(file_path)

# Extract data for plotting
datasets = df['Datasets']
Polak = df['Polak']
GroupTC_BS = df['GroupTC-BS']
TRUST = df['TRUST']
GroupTC_HS = df['GroupTC-HS']
avg_degree = df['avg_degree'] if 'avg_degree' in df.columns else None  # Optional avg_degree column

# Set up the figure and axes
fig, ax1 = plt.subplots(figsize=(15, 8))

# Set width of bar
bar_width = 0.1
# 设置每组柱状图的位置，确保每组柱子紧密排列
spacing = 0.25  # 设置每组数据集之间的间隔

# Set positions for each bar group
# bar_positions = np.arange(len(datasets))

# 设置柱状图的x轴位置，使用arange并增加spacing来调整间隔
bar_positions = np.arange(len(datasets)) * (4 * bar_width + spacing)  # 使每组数据集之间有间隔

# 计算图表的最大值，用于设置虚线柱子的高度
max_value = max(df[['Polak', 'TRUST', 'GroupTC-BS', 'GroupTC-HS']].max())
# 标记缺失值的颜色
missing_color = '#D3D3D3'  # 灰色用于标记缺失值
dashed_line_style = '--'  # 虚线样式

def plot_bar_with_missing(ax, positions, data, label, color, missing_color, bar_width, max_value):
    # 获取当前 y 轴的最大值
    y_max = 100

    # 遍历数据，检查是否缺失
    for i, value in enumerate(data):
        if pd.isna(value):  # 如果数据缺失
            # 绘制透明的虚线柱子，顶格至 y_max
            ax.bar(positions[i], y_max, bar_width, color=missing_color, linestyle=dashed_line_style, edgecolor='black', linewidth=1, alpha=0.3)  # 透明柱

            # 在柱子顶部添加红色叉号标记
            ax.text(positions[i], max_value-20, '×', ha='center', va='bottom', fontsize=16, color='red')  # 红色叉号标记
        else:
            ax.bar(positions[i], value, bar_width, color=color, edgecolor='black', linewidth=1)  # 绘制正常柱

# 绘制柱状图，去掉 `label` 参数来避免重复
plot_bar_with_missing(ax1, bar_positions - 1.5 * bar_width, Polak, 'Polak', '#f6c89a', missing_color, bar_width, max_value)
plot_bar_with_missing(ax1, bar_positions - 0.5 * bar_width, TRUST, 'TRUST', '#bce2ea', missing_color, bar_width, max_value)
plot_bar_with_missing(ax1, bar_positions + 0.5 * bar_width, GroupTC_BS, 'GroupTC_BS', '#91d0fc', missing_color, bar_width, max_value)
plot_bar_with_missing(ax1, bar_positions + 1.5 * bar_width, GroupTC_HS, 'GroupTC_HS', '#f2e5c1', missing_color, bar_width, max_value)

# Add avg_degree as a secondary line plot if available
if avg_degree is not None:
    ax2 = ax1.twinx()
    ax2.plot(bar_positions, avg_degree, 'k-', marker='s', label='avg degree', linewidth=2)
    ax2.set_ylabel('Avg Degree', fontsize=25, fontweight='bold')
    ax2.set_ylim(0, 80)
    ax2.tick_params(axis='both', labelsize=20)  # 设置 y 轴和 x 轴刻度标签字体大小为 20

# Set axis labels and title
ax1.set_xlabel('', fontsize=28, fontweight='bold')
ax1.set_ylabel('Time (ms)', fontsize=28, fontweight='bold')
ax1.set_yscale('log')
# ax1.set_title('Running times of different algorithms under various datasets', fontsize=16)

ax1.set_xlim([-0.25, len(datasets) * (4 * bar_width+spacing) -0.4])


# Set y-axis tick label size for the main axis
ax1.tick_params(axis='y', labelsize=24)


# Set x-ticks
ax1.set_xticks(bar_positions)
ax1.set_xticklabels(datasets, fontsize=24, rotation=20, ha='center')

# 添加图例：手动添加一次图例项
ax1.bar(bar_positions[0], 0, bar_width, label='Polak', color='#f6c89a', edgecolor='black', linewidth=1)  # 假的柱子只为图例显示
ax1.bar(bar_positions[1], 0, bar_width, label='TRUST', color='#bce2ea', edgecolor='black', linewidth=1)  # 假的柱子只为图例显示
ax1.bar(bar_positions[2], 0, bar_width, label='GroupTC_BS', color='#91d0fc', edgecolor='black', linewidth=1)  # 假的柱子只为图例显示
ax1.bar(bar_positions[3], 0, bar_width, label='GroupTC_HS', color='#f2e5c1', edgecolor='black', linewidth=1)  # 假的柱子只为图例显示

# 添加图例
# fig.legend(loc='upper left', bbox_to_anchor=(0.07, 0.95), fontsize=20)
fig.legend(loc='upper center', bbox_to_anchor=(0.44, 0.95), ncol=4, fontsize=20)
# Set thicker border for the plot
ax = plt.gca()
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)

# Show the plot
plt.tight_layout()
plt.show()


