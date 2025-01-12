#%%

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取数据
file_path = '../../excel/real_world_graph_time.xlsx'  # 替换为实际文件路径
df = pd.read_excel(file_path)

# 提取数据用于绘图
datasets = df['Datasets']
Bisson = df['Bisson']
Fox = df['Fox']
Green = df['Green']
H_INDEX = df['H-INDEX']
Hu = df['Hu']
Polak = df['Polak']
TriCore = df['TriCore']
TRUST = df['TRUST']
# GroupTC_BS = df['GroupTC-BS']
# GroupTC_HS = df['GroupTC-HS']

avg_degree = df['avg_degree'] if 'avg_degree' in df.columns else None  # 如果有 'avg_degree' 列则使用

# 设置图形和坐标轴
fig, ax1 = plt.subplots(figsize=(30, 10))

# 设置柱状图的宽度
bar_width = 0.1

# 设置每组柱状图的位置，确保每组柱子紧密排列
spacing = 0.25  # 设置每组数据集之间的间隔

# 设置柱状图的x轴位置，使用arange并增加spacing来调整间隔
bar_positions = np.arange(len(datasets)) * (8 * bar_width + spacing)  # 使每组数据集之间有间隔

# 计算图表的最大值，用于设置虚线柱子的高度
max_value = max(df[['Bisson', 'Fox', 'Green', 'H-INDEX', 'Hu', 'Polak', 'TriCore', 'TRUST']].max())

# 标记缺失值的颜色
missing_color = '#D3D3D3'  # 灰色用于标记缺失值
dashed_line_style = '--'  # 虚线样式

# 绘制柱状图并设置不同的颜色
# def plot_bar_with_missing(ax, positions, data, label, color, missing_color, bar_width, max_value):
#     # 遍历数据，检查是否缺失
#     for i, value in enumerate(data):
#         if pd.isna(value):  # 如果数据缺失
#             ax.plot([positions[i], positions[i]], [0, max_value], linestyle=dashed_line_style, color='black', linewidth=2)  # 绘制虚线柱
#             # ax.text(positions[i], max_value * 0.05, '', ha='center', va='bottom', fontsize=10, color='black')  # 添加缺失标记
#         else:
#             ax.bar(positions[i], value, bar_width, color=color, edgecolor='black', linewidth=1)  # 绘制正常柱

# def plot_bar_with_missing(ax, positions, data, label, color, missing_color, bar_width, max_value):
#     # 遍历数据，检查是否缺失
#     for i, value in enumerate(data):
#         if pd.isna(value):  # 如果数据缺失
#             # 绘制透明的虚线柱子，可以调整透明度来模拟虚线效果
#             ax.bar(positions[i], max_value, bar_width, color=missing_color,linestyle= dashed_line_style, edgecolor='black', linewidth=1, alpha=0.3)  # 透明柱
#         else:
#             ax.bar(positions[i], value, bar_width, color=color, edgecolor='black', linewidth=1)  # 绘制正常柱

def plot_bar_with_missing(ax, positions, data, label, color, missing_color, bar_width, max_value):
    # 获取当前 y 轴的最大值
    y_max = 100000

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
plot_bar_with_missing(ax1, bar_positions - 3.5 * bar_width, Polak, 'Polak', '#f6c89a', missing_color, bar_width, max_value)
plot_bar_with_missing(ax1, bar_positions - 2.5 * bar_width, Green, 'Green', '#a5d4a1', missing_color, bar_width, max_value)
plot_bar_with_missing(ax1, bar_positions - 1.5 * bar_width, Bisson, 'Bisson', '#c1b3d5', missing_color, bar_width, max_value)
plot_bar_with_missing(ax1, bar_positions - 0.5 * bar_width, TriCore, 'TriCore', '#fefea9', missing_color, bar_width, max_value)
plot_bar_with_missing(ax1, bar_positions + 0.5 * bar_width, Fox, 'Fox', '#9fbaef', missing_color, bar_width, max_value)
plot_bar_with_missing(ax1, bar_positions + 1.5 * bar_width, Hu, 'Hu', '#f9bbf8', missing_color, bar_width, max_value)
plot_bar_with_missing(ax1, bar_positions + 2.5 * bar_width, H_INDEX, 'H-INDEX', '#b2b893', missing_color, bar_width, max_value)
plot_bar_with_missing(ax1, bar_positions + 3.5 * bar_width, TRUST, 'TRUST', '#bce2ea', missing_color, bar_width, max_value)


# 如果存在 avg_degree 列，则绘制折线图
if avg_degree is not None:
    ax2 = ax1.twinx()  # 创建一个新的 y 轴
    ax2.plot(bar_positions, avg_degree, 'k-', marker='s', label='avg degree', linewidth=2)
    ax2.set_ylabel('avg degree', fontsize=30, fontweight='bold')
    ax2.set_ylim(0, 140)
    # 修改坐标轴刻度字体大小
    ax2.tick_params(axis='both', labelsize=25)  # 设置 y 轴和 x 轴刻度标签字体大小为 20

# 设置坐标轴标签和标题
# ax1.set_xlabel('Datasets', fontsize=18, fontweight='bold')
ax1.set_ylabel('Time (ms)', fontsize=30, fontweight='bold')
ax1.set_yscale('log')  # 设置 y 轴为对数坐标
# 设置 x 轴范围，左边界为负值，以缩短第一个刻度与原点的距离
ax1.set_xlim([-0.5, len(datasets) * (8 * bar_width + spacing) -0.61])

# 设置 y 轴的刻度标签大小
ax1.tick_params(axis='y', labelsize=25)

# 设置 x 轴刻度标签
ax1.set_xticks(bar_positions)
ax1.set_xticklabels(datasets, fontsize=25, rotation=0, ha='center')



# 添加图例：手动添加一次图例项
ax1.bar(bar_positions[0], 0, bar_width, label='Polak', color='#f6c89a', edgecolor='black', linewidth=1)  # 假的柱子只为图例显示
ax1.bar(bar_positions[1], 0, bar_width, label='Green', color='#a5d4a1', edgecolor='black', linewidth=1)  # 假的柱子只为图例显示
ax1.bar(bar_positions[2], 0, bar_width, label='Bisson', color='#c1b3d5', edgecolor='black', linewidth=1)  # 假的柱子只为图例显示
ax1.bar(bar_positions[3], 0, bar_width, label='TriCore', color='#fefea9', edgecolor='black', linewidth=1)  # 假的柱子只为图例显示
ax1.bar(bar_positions[4], 0, bar_width, label='Fox', color='#9fbaef', edgecolor='black', linewidth=1)  # 假的柱子只为图例显示
ax1.bar(bar_positions[5], 0, bar_width, label='Hu', color='#f9bbf8', edgecolor='black', linewidth=1)  # 假的柱子只为图例显示
ax1.bar(bar_positions[6], 0, bar_width, label='H-INDEX', color='#b2b893', edgecolor='black', linewidth=1)  # 假的柱子只为图例显示
ax1.bar(bar_positions[7], 0, bar_width, label='TRUST', color='#bce2ea', edgecolor='black', linewidth=1)  # 假的柱子只为图例显示

# 添加图例
# fig.legend(loc='upper left', bbox_to_anchor=(0.07, 0.95), fontsize=20)
fig.legend(loc='upper center', bbox_to_anchor=(0.41, 0.95), ncol=10, fontsize=20)

# 设置边框线宽
ax = plt.gca()
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)

# 显示图形
plt.tight_layout(pad=1.0, h_pad=2.0, w_pad=1.0)

# 保存图形为 PDF 文件
plt.savefig(r'../../pdf/time_output_v5.pdf', format='pdf')

plt.show()

# %%
