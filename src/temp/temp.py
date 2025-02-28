#%%
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
import pandas as pd

# 读取Excel文件中的数据
file_path = "Table1_uniform.xlsx"
data = pd.read_excel(file_path)

def get_result(data, type, metrics):
    result = data[(data["Metrics"] == metrics) | data[type].str.contains("M")][
        ["Tree size", type, type + ".1", type + ".2", type + ".3"]
    ]

    result.columns = result.iloc[0]  # 将第0行的值设为列名
    result = result.drop(index=0)  # 删除第0行
    result = result.reset_index(drop=True)
    return result

basic_result = get_result(data, "Basic", "Compute (SM) Throughput [%]")
grouping_result = get_result(data, "Grouping", "Compute (SM) Throughput [%]")

# 打印数据验证
print(basic_result)

# x轴为配置项（如 5M, 10M 等）
x_labels = basic_result.columns[1:].values
# 提取"Tree size"列作为 y 轴
y_labels = basic_result['Tree size'].values
# 提取计算吞吐量值，忽略第0列（'Tree size'）进行 Z 轴的计算
z_values_basic = basic_result.iloc[:, 1:].values
z_values_grouping = grouping_result.iloc[:, 1:].values

print(x_labels)
print(y_labels)
print(z_values_basic)
print(z_values_grouping)
#输出如下
# ['5 million' '10 million' '100 million']
# ['5M' ' 10M' ' 100M' ' 1000M']
# [[2.57 2.58 2.6 2.67]
#  [4.23 4.28 4.22 4.44]
#  [2.57 2.58 2.6 2.67]]

# 创建网格，X轴对应树大小，Y轴对应不同配置
X, Y = np.meshgrid(np.arange(len(x_labels)), np.arange(len(y_labels)))

# 创建图形
fig = plt.figure(figsize=(10, 7)) 
ax = fig.add_subplot(111, projection='3d')

# 绘制三维网格图
ax.plot_surface(X, Y, z_values_basic, color='red', alpha=0.7)  # 使用 z_values.T 转置矩阵以确保维度匹配
ax.plot_surface(X, Y, z_values_grouping, color='blue', alpha=0.7)  # 使用 z_values.T 转置矩阵以确保维度匹配

# 设置轴标签
ax.set_xlabel('Tree Size')
ax.set_ylabel('Configuration')

# 设置Z轴标签位置在右侧
ax.set_zlabel('Compute (SM) Throughput [%]', rotation=90)
ax.zaxis.set_rotate_label(False)  # 禁用标签自动旋转
ax.zaxis.label.set_ha('right')    # 水平对齐方式设为右对齐
ax.zaxis.label.set_va('center')   # 垂直对齐方式设为居中
ax.zaxis.labelpad = 15            # 增加标签与轴的距离

# 设置轴刻度
ax.set_xticks(np.arange(len(x_labels)))
ax.set_xticklabels(x_labels)  # 使用 x_labels 设置 X 轴刻度标签
ax.set_yticks(np.arange(len(y_labels)))
ax.set_yticklabels(y_labels)  # 使用 y_labels 设置 Y 轴刻度标签

ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 20

# 设置视角 - 调整视角使Z轴在右侧更明显
ax.view_init(elev=20, azim=120)

# 添加图例
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color='red', lw=4, label='Basic'),
    Line2D([0], [0], color='blue', lw=4, label='Grouping')
]
ax.legend(handles=legend_elements, loc='upper right')

# 显示图形
plt.tight_layout()
plt.show()

