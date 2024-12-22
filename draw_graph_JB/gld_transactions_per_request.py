#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 从 Excel 文件中加载数据
df = pd.read_excel('./all_log/profiler_result.xlsx', sheet_name='gld_transactions_per_request')

# 提取数据集名称（第一列）和算法名称（列头）
datasets = df['Datasets']
algorithms = df.columns[1:]  # 假设第一列是 Dataset，其他是算法名称

# 指定要绘制的算法名称（可以替换为你感兴趣的算法列表）
# selected_algorithms = ['Bisson', 'Fox', 'Green', 'H-INDEX', 'Hu', 'Polak', 'TriCore', 'TRUST', 'GroupTC-BS', 'GroupTC-HS']
selected_algorithms = ['Polak', 'Green', 'Bisson', 'TriCore', 'Fox', 'Hu', 'H-INDEX', 'TRUST', 'GroupTC-BS', 'GroupTC-HS']


# 确保选中的算法在数据列中
selected_algorithms = [algo for algo in selected_algorithms if algo in algorithms]

# 数据清洗和提取有效数据，确保所有数据都是数值类型
boxplot_data = []
for algorithm in selected_algorithms:
    # 尝试将数据转换为数值类型，无法转换的值将被设置为 NaN
    cleaned_data = pd.to_numeric(df[algorithm], errors='coerce').dropna().values  # 除以100进行比例缩放
    boxplot_data.append(cleaned_data)

# 自定义颜色，定义为一个列表，每个颜色对应一个算法
colors = ['#f6c89a', '#a5d4a1', '#c1b3d5', '#fefea9', '#9fbaef', '#f9bbf8', '#b2b893', '#bce2ea', '#91d0fc', '#f2e5c1']

# 检查颜色列表是否足够，如果不够，可以循环使用或扩展颜色列表
if len(colors) < len(selected_algorithms):
    # 循环使用颜色
    colors = (colors * (len(selected_algorithms) // len(colors) + 1))[:len(selected_algorithms)]

# 创建箱线图
plt.figure(figsize=(16, 10))
box = plt.boxplot(boxplot_data, patch_artist=True,
                  boxprops=dict(color='black'),
                  whiskerprops=dict(color='black'),
                  capprops=dict(color='black'),
                  medianprops=dict(color='black'))

# 为每个箱线图单独设置颜色
for i, patch in enumerate(box['boxes']):
    patch.set_facecolor(colors[i])  # 设置每个箱体的颜色

# 设置X轴标签和其它图形样式

# 设置X轴标签和其它图形样式
plt.xticks(range(1, len(selected_algorithms) + 1), selected_algorithms, rotation=20, fontsize=30)
plt.ylabel('gld_transactions_per_request', fontsize=30, fontweight='bold')
plt.tick_params(axis='x', labelsize=25)  # 设置纵坐标刻度标签的字体大小为25
plt.tick_params(axis='y', labelsize=25)  # 设置纵坐标刻度标签的字体大小为25

# 设置Y轴为数值型，并设置最大值
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0f}'))  # 显示数值
plt.ylim(0, 14)  # 设置Y轴的最大值为300，您可以根据需要调整

# 显示图形
plt.tight_layout()

# 保存图形为 PDF 文件
plt.savefig(r'D:\BaiduNetdiskDownload\gld_transactions_per_request_v5.pdf', format='pdf')

plt.show()

# %%
