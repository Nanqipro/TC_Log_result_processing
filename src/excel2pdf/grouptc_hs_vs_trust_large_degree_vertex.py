# %%
# speed-up,speed-up_build,speed-up_search  only scatter
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取Excel文件
file_path = "../../excel/grouptc_hs_vs_trust_time.xlsx"  # 修改为实际的文件路径
df = pd.read_excel(file_path)

# 检查数据结构，确保列名正确
# print(df.head())

# 假设 Excel 中列名分别是 'edge-count'、'speed-up'、'speed-up_search' 和 'speed-up_build'
df = df[df["large degree vertex avg degree"].notna()]  # 去掉 large degree vertex avg degree 为空的行
x = df["large degree vertex avg degree"]


# 检查并打印异常值
for index, value in df["large degree vertex total time_speedup"].items():
    if value > 100 or value < 0.1:
        print(f"total time_speedup 异常值: 数据集={df['Datasets'][index]}, 值={value}")
        df.at[index, "large degree vertex total time_speedup"] = np.nan

y = df["large degree vertex total time_speedup"].clip(upper=100, lower=0.1)

for index, value in df["large degree vertex hash search time_speedup"].items():
    if value > 100 or value < 0.1:
        print(f"hash search time_speedup 异常值: 数据集={df['Datasets'][index]}, 值={value}")
        df.at[index, "large degree vertex hash search time_speedup"] = np.nan

y_search = df["large degree vertex hash search time_speedup"].clip(upper=100, lower=0.1)

for index, value in df["large degree vertex hash table construction time_speedup"].items():
    if value > 100 or value < 0.1:
        print(f"hash table construction time_speedup 异常值: 数据集={df['Datasets'][index]}, 值={value}")
        df.at[index, "large degree vertex hash table construction time_speedup"] = np.nan

y_build = df["large degree vertex hash table construction time_speedup"].clip(
    upper=100, lower=0.1
)

# 对数据进行对数变换，以e为底的对数
x_log = x

# 创建图形和子图
fig, ax1 = plt.subplots(figsize=(25, 10))


# 添加 speed-up_build 的散点图
ax1.scatter(
    x_log,
    y_build,
    marker="^",
    color="#E29135",
    alpha=1,
    s=200,
    linewidths=9,
    label="Hash Table Construction",
)
# 添加 speed-up_search 的散点图
ax1.scatter(
    x_log,
    y_search,
    marker="o",
    color="#94C6CD",
    alpha=1,
    s=200,
    linewidths=9,
    label="Hash Search",
)
# 创建原始的散点图
ax1.scatter(
    x_log, y, marker="*", color="#4A5F7E", alpha=1, s=200, linewidths=9, label="Total"
)

# 添加基准线 y=1
ax1.axhline(y=1, color="red", linestyle="-", linewidth=4, label="baseline")

# 设置 x 轴和 y 轴的最大最小值
# ax1.set_xlim(left=100, right=1500)  # 根据数据范围设置 x 轴的最小值和最大值
# ax1.set_ylim(bottom=0, top=6)   # 根据数据范围设置 y 轴的最小值和最大值

# 设置坐标轴标签
ax1.set_xlabel("avg degree", fontsize=50, fontweight="bold")
ax1.set_ylabel("Speedup", fontsize=50, fontweight="bold")

# 设置 x 轴的刻度标签大小
ax1.tick_params(axis="x", labelsize=50)

# 设置 y 轴的刻度标签大小
ax1.tick_params(axis="y", labelsize=50)

# 设置边框线宽
ax = plt.gca()
ax.spines["top"].set_linewidth(2)
ax.spines["right"].set_linewidth(2)
ax.spines["bottom"].set_linewidth(2)
ax.spines["left"].set_linewidth(2)

# 显示网格
ax1.grid(False)

# 添加图例
fig.legend(
    loc="upper left",
    bbox_to_anchor=(0.51, 0.95),
    ncol=1,
    fontsize=50,
    frameon=True,
    facecolor=(1, 1, 1, 0.6),
)

# 显示图形
plt.tight_layout(pad=1.0, h_pad=2.0, w_pad=1.0)

plt.savefig("../../pdf/grouptc_hs_vs_trust_large_degree_vertex_v1.pdf", format="pdf")

# 显示图像
plt.show()
# %%
