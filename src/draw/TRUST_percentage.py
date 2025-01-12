#%%
# 折线图与百分比图复合图
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# 读取第一个Excel文件的数据
file_path = '../../excel/trust_partition_time.xlsx'
df1 = pd.read_excel(file_path)

# 提取数据列
datasets = df1['Datasets'].tolist()
TRUST_low_percent = df1['low degree part'].tolist()
TRUST_high_percent = df1['high degree part'].tolist()

# 定义柱子的位置
x = np.arange(len(datasets))  # datasets 在横坐标上的位置
width = 0.5  # 每个柱子的宽度

# 创建图形和双Y轴
fig, ax2 = plt.subplots(figsize=(30, 10))

# 绘制百分比的柱状图（左Y轴）
ax2.bar(x, TRUST_low_percent, width, label='Low degree part', color='#6BAED6', edgecolor='black', linewidth=3)
ax2.bar(x, TRUST_high_percent, width, bottom=TRUST_low_percent, label='High degree part', color='#FED976', edgecolor='black', linewidth=3)

# 设置右边Y轴的标签和范围
ax2.set_ylabel('Percentage', fontsize=50, fontweight='bold')
ax2.set_ylim(0, 1)  # 百分比范围从0到1

# 使用FuncFormatter将Y轴格式化为百分比
ax2.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y*100:.0f}%'))

# 设置X轴
ax2.set_xlabel('', fontsize=50, fontweight='bold')
ax2.set_xticks(x)
ax2.set_xticklabels(datasets, rotation=0, ha='center', fontsize=50)

# 修改左右边Y轴刻度标签的字体大小
ax2.tick_params(axis='y', labelsize=50)  # 设置右边Y轴的字体大小

# 设置图例在图形的上方中央
fig.legend(loc='upper center', bbox_to_anchor=(0.383, 1.01), ncol=2, fontsize=50, frameon=True,
           facecolor=(1, 1, 1, 0.6), edgecolor='none')

# 调整 x 轴范围，确保图例不会覆盖柱状图
ax2.set_xlim([-0.35, len(datasets) * (width + 0.1) + 7.3])

# 调整布局以为图例腾出空间
plt.tight_layout()
plt.subplots_adjust(top=0.85)  # 根据图例位置调整 top 参数

# 保存图形为 PDF 文件
plt.savefig('../../pdf/TRUST_percentage_v5.pdf', format='pdf')

# 显示图形
plt.show()
# %%
