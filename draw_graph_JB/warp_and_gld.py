import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import seaborn as sns

# 设置全局字体大小
plt.rcParams.update({'font.size':20})

# 定义颜色列表
colors = ['#f6c89a', '#a5d4a1', '#c1b3d5', '#fefea9', '#9fbaef',
          '#f9bbf8', '#b2b893', '#bce2ea', '#91d0fc', '#f2e5c1']

# 确保颜色列表足够长
def extend_colors(base_colors, required_length):
    if len(base_colors) < required_length:
        extended = (base_colors * (required_length // len(base_colors) + 1))[:required_length]
        return extended
    return base_colors

# 创建子图，1行2列
fig, axes = plt.subplots(1, 2, figsize=(32, 12))

# ---------------------- 第一个子图：warp_execution_efficiency ---------------------- #
# 从 Excel 文件中加载数据
df_efficiency = pd.read_excel('./all_log/profiler_result.xlsx', sheet_name='warp_execution_efficiency')

# 提取数据集名称和算法名称
datasets_eff = df_efficiency['Datasets']
algorithms_eff = df_efficiency.columns[1:]

# 指定要绘制的算法名称
selected_algorithms = ['Polak', 'Green', 'Bisson', 'TriCore', 'Fox',
                       'Hu', 'H-INDEX', 'TRUST', 'GroupTC-BS', 'GroupTC-HS']

# 确保选中的算法在数据列中
selected_algorithms_eff = [algo for algo in selected_algorithms if algo in algorithms_eff]

# 数据清洗和提取有效数据，确保所有数据都是数值类型并除以100
boxplot_data_eff = []
for algorithm in selected_algorithms_eff:
    cleaned_data = pd.to_numeric(df_efficiency[algorithm], errors='coerce').dropna().values / 100
    boxplot_data_eff.append(cleaned_data)

# 扩展颜色列表
colors_eff = extend_colors(colors, len(selected_algorithms_eff))

# 创建箱线图
box_eff = axes[0].boxplot(boxplot_data_eff, patch_artist=True,
                          boxprops=dict(color='black'),
                          whiskerprops=dict(color='black'),
                          capprops=dict(color='black'),
                          medianprops=dict(color='black'))

# 为每个箱线图单独设置颜色
for i, patch in enumerate(box_eff['boxes']):
    patch.set_facecolor(colors_eff[i])

# 设置X轴标签和其它图形样式
axes[0].set_xticks(range(1, len(selected_algorithms_eff) + 1))
axes[0].set_xticklabels(selected_algorithms_eff, rotation=30, fontsize=40)
axes[0].set_ylabel('warp_execution_efficiency', fontsize=40, fontweight='bold')
axes[0].tick_params(axis='x', labelsize=40)
axes[0].tick_params(axis='y', labelsize=40)

# 设置百分比格式
axes[0].yaxis.set_major_formatter(PercentFormatter(1.0))

# 可选：设置y轴的范围
# axes[0].set_ylim(0, 1)

# ---------------------- 第二个子图：gld_transactions_per_request ---------------------- #
# 从 Excel 文件中加载数据
df_transactions = pd.read_excel('./all_log/profiler_result.xlsx', sheet_name='gld_transactions_per_request')

# 提取数据集名称和算法名称
datasets_trans = df_transactions['Datasets']
algorithms_trans = df_transactions.columns[1:]

# 指定要绘制的算法名称
selected_algorithms_trans = [algo for algo in selected_algorithms if algo in algorithms_trans]

# 数据清洗和提取有效数据，确保所有数据都是数值类型
boxplot_data_trans = []
for algorithm in selected_algorithms_trans:
    cleaned_data = pd.to_numeric(df_transactions[algorithm], errors='coerce').dropna().values
    boxplot_data_trans.append(cleaned_data)

# 扩展颜色列表
colors_trans = extend_colors(colors, len(selected_algorithms_trans))

# 创建箱线图
box_trans = axes[1].boxplot(boxplot_data_trans, patch_artist=True,
                            boxprops=dict(color='black'),
                            whiskerprops=dict(color='black'),
                            capprops=dict(color='black'),
                            medianprops=dict(color='black'))

# 为每个箱线图单独设置颜色
for i, patch in enumerate(box_trans['boxes']):
    patch.set_facecolor(colors_trans[i])

# 设置X轴标签和其它图形样式
axes[1].set_xticks(range(1, len(selected_algorithms_trans) + 1))
axes[1].set_xticklabels(selected_algorithms_trans, rotation=30, fontsize=40)
axes[1].set_ylabel('gld_transactions_per_request', fontsize=40, fontweight='bold')
axes[1].tick_params(axis='x', labelsize=40)
axes[1].tick_params(axis='y', labelsize=40)

# 设置Y轴为数值型，并设置最大值
axes[1].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0f}'))
axes[1].set_ylim(0, 14)

# 调整布局
plt.tight_layout()

# 保存图形为 PDF 文件
plt.savefig(r'D:\BaiduNetdiskDownload\combined_efficiency_transactions.pdf', format='pdf')

# 显示图形
plt.show()
