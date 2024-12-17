
# 折线图与百分比图复合图
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
# 读取第一个Excel文件的数据
file_path = './TRUST/highDegreeVSlowDegree.xlsx'
df1 = pd.read_excel(file_path)

# 提取数据列
datasets = df1['datasets'].tolist()

TRUST_low_percent = df1['percentage_low'].tolist()

TRUST_high_percent = df1['percentage_high'].tolist()



# 定义柱子的位置
x = np.arange(len(datasets))  # datasets 在横坐标上的位置
width = 0.5  # 每个柱子的宽度
spacing = 0.25  # 设置每组数据集之间的间隔
# 创建图形和双Y轴
fig, ax2 = plt.subplots(figsize=(30, 10))



# 绘制百分比的柱状图（左Y轴）
ax2.bar(x, TRUST_low_percent, width,  label='Low degree part', color='#6BAED6', edgecolor='black', linewidth=2)
ax2.bar(x, TRUST_high_percent, width, bottom=TRUST_low_percent,label='High degree part', color='#FED976', edgecolor='black', linewidth=2)

# 设置右边Y轴的标签和范围
ax2.set_ylabel('Percentage', fontsize=25, fontweight='bold')
ax2.set_ylim(0, 1)  # 百分比范围从0到1
# 使用FuncFormatter将Y轴格式化为百分比
ax2.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y*100:.0f}%'))

# 设置X轴
ax2.set_xlabel('', fontsize=30, fontweight='bold')
ax2.set_xticks(x)
ax2.set_xticklabels(datasets, rotation=0, ha='center', fontsize=25)



# 修改左右边Y轴刻度标签的字体大小
ax2.tick_params(axis='y', labelsize=25)  # 设置右边Y轴的字体大小

# 设置图例
fig.legend(loc='upper left', bbox_to_anchor=(0.82, 0.95), ncol=1, fontsize=25, frameon=True, facecolor=(1, 1, 1, 0.6), edgecolor='none')

# 设置 x 轴范围，左边界为负值，以缩短第一个刻度与原点的距离
ax2.set_xlim([-0.5, len(datasets) * (1 * width + spacing) +4.6])

# 显示图形
plt.tight_layout()

# 保存图形为 PDF 文件
plt.savefig(r'D:\BaiduNetdiskDownload\TRUST_percentage.pdf', format='pdf')

plt.show()
