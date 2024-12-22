# X轴刻度不均匀
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from the Excel file
file_path = './TrustVSGroupTC/lowDegree-buildIndex_sorted.xlsx'  # 请修改为实际的文件路径
df = pd.read_excel(file_path)

# Extract data for plotting
# edge_count = df['avg_degree'].astype(str)  # 将 Edge Count 转换为字符串以便作为标签
avg_degree = df['avg_degree'].astype(str)
speed_up_build = df['speed-up_build']
speed_up_search = df['speed-up_search']

# Set up the figure and axes for the speed-up plot
fig, ax = plt.subplots(figsize=(15, 8))

# Plotting the speed-up ratios as line plots
ax.plot(avg_degree, speed_up_build, marker='o', markersize=7, linestyle='-', color='#66CC00', label='Speed-up_build', linewidth=3)
ax.plot(avg_degree, speed_up_search, marker='s', markersize=7, linestyle='-', color='#A8D8EA', label='Speed-up Search', linewidth=3)

# Set axis labels and title with bold font
ax.set_xlabel('avg degree', fontsize=30, fontweight='bold')
ax.set_ylabel('Speedup', fontsize=30, fontweight='bold')

# Set x-ticks evenly spaced
num_ticks = len(avg_degree)
ax.set_xticks(np.linspace(0, num_ticks - 1, num_ticks))  # 设置均匀分布的tick位置
ax.set_xticklabels(avg_degree, rotation=20, ha='right', fontsize=25)

# Add legend with specified font size
ax.legend(fontsize=20)

# Set y-axis tick label size
ax.tick_params(axis='y', labelsize=25)

# Set thicker border for the plot
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)

# Show the plot
plt.tight_layout()
plt.show()

# X轴刻度均匀
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Load the data from the Excel file
# file_path = './TrustVSGroupTC/lowDegree-buildIndex_sorted.xlsx'  # 请修改为实际的文件路径
# df = pd.read_excel(file_path)
#
# # Extract data for plotting
# # edge_count = df['avg_degree'].astype(str)  # 将 Edge Count 转换为字符串以便作为标签
# avg_degree = df['avg_degree']
# speed_up_build = df['speed-up_build']
# speed_up_search = df['speed-up_search']
# speed_up_all = df['speed-up_all']
#
# # Set up the figure and axes for the speed-up plot
# fig, ax = plt.subplots(figsize=(15, 8))
#
# # Plotting the speed-up ratios as line plots
# ax.plot(avg_degree, speed_up_build, marker='o', markersize=7, linestyle='-', color='#66CC00', label='Speed-up_build', linewidth=3)
# ax.plot(avg_degree, speed_up_search, marker='s', markersize=7, linestyle='-', color='#A8D8EA', label='Speed-up_Search', linewidth=3)
# ax.plot(avg_degree, speed_up_all, marker='^', markersize=7, linestyle='-', color='#A8D8EA', label='Speed-up_all', linewidth=3)
#
# # Set axis labels and title with bold font
# ax.set_xlabel('avg_degree', fontsize=18, fontweight='bold')
# ax.set_ylabel('Speedup', fontsize=18, fontweight='bold')
#
# # 设置 x 轴刻度
# # 设置x轴的刻度范围和步长
# plt.xticks(range(0, 70, 5))  # 1到10的刻度，步长为1
# # ax.set_xticklabels(avg_degree, rotation=20, ha='center', fontsize=20)
#
# # Add legend with specified font size
# ax.legend(fontsize=20)
#
# # Set y-axis tick label size
# ax.tick_params(axis='y', labelsize=20)
#
# # Set thicker border for the plot
# ax.spines['top'].set_linewidth(2)
# ax.spines['right'].set_linewidth(2)
# ax.spines['bottom'].set_linewidth(2)
# ax.spines['left'].set_linewidth(2)
#
# # Show the plot
# plt.tight_layout()
# plt.show()
