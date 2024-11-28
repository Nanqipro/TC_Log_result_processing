import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from the Excel file
file_path = './TrustVSGroupTC/lowDegree-buildIndex_sorted.xlsx'  # 请修改为实际的文件路径
df = pd.read_excel(file_path)

# Extract data for plotting
edge_count = df['degree<100'].astype(str)  # 将 Edge Count 转换为字符串以便作为标签
speed_up = df['speed-up_build']
speed_up_search = df['speed-up_search']

# Set up the figure and axes for the speed-up plot
fig, ax = plt.subplots(figsize=(15, 8))

# Plotting the speed-up ratios as line plots
ax.plot(edge_count, speed_up, marker='o', markersize=7, linestyle='-', color='#66CC00', label='Speed-up_build', linewidth=3)
ax.plot(edge_count, speed_up_search, marker='s', markersize=7, linestyle='-', color='#A8D8EA', label='Speed-up Search', linewidth=3)

# Set axis labels and title with bold font
ax.set_xlabel('Vertex count', fontsize=18, fontweight='bold')
ax.set_ylabel('Speed-up', fontsize=18, fontweight='bold')

# Set x-ticks evenly spaced
num_ticks = len(edge_count)
ax.set_xticks(np.linspace(0, num_ticks - 1, num_ticks))  # 设置均匀分布的tick位置
ax.set_xticklabels(edge_count, rotation=35, ha='right', fontsize=14)

# Add legend with specified font size
ax.legend(fontsize=18)

# Set y-axis tick label size
ax.tick_params(axis='y', labelsize=18)

# Set thicker border for the plot
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)

# Show the plot
plt.tight_layout()
plt.show()
