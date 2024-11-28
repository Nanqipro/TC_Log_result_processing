import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取Excel文件
file_path = './TrustVSGroupTC/lowDegree-buildIndex.xlsx'  # 修改为实际的文件路径
df = pd.read_excel(file_path)

# 检查数据结构，确保列名正确
print(df.head())

# 假设 Excel 中列名分别是 'edge-count' 和 'speed-up'，如果不同请根据实际修改
x = df['edge-count']
y = df['speed-up_build']

# 对数据进行对数变换，以e为底的对数
x_log = np.log1p(x)
# y_log = np.log1p(y)

# 创建散点图
plt.figure(figsize=(10, 6))
plt.scatter(x_log, y, marker='o', color='blue', alpha=0.5)

# 设置横纵坐标的刻度
plt.xticks(np.arange(10, int(x_log.max()) + 1, 0.5))
plt.yticks(np.arange(0, int(y.max())+0.5, 0.2))  # 每隔 0.5 进行刻度显示

# 设置标题和标签
# plt.title('Log Transformed Edge Count vs Speed-up', fontsize=14)
plt.xlabel('Log(Edge Count)', fontsize=12)
plt.ylabel('Log(Speed-up)', fontsize=12)

# 显示网格
plt.grid(False)

# 显示图像
plt.show()

