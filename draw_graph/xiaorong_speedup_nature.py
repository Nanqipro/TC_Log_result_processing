import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from the Excel file
file_path = './xiaorong_for_GroupTC-BS/GroupTC-BS-xiaorong-natureDatasets.xlsx'  # 请确保文件路径正确
df_speedup = pd.read_excel(file_path)

# Extract data for plotting
datasets = df_speedup['datasets']
speedup1 = df_speedup['speedup-opt1']
speedup2 = df_speedup['speedup-opt12']
speedup3 = df_speedup['speedup-opt123']
baseline = df_speedup['baseline']


# Set up the figure and axes for the speed-up plot
fig, ax = plt.subplots(figsize=(30, 10))

# Plotting the speed-up ratios as line plots
ax.plot(datasets, speedup1, marker='s', markersize=15, linestyle='-', alpha=1, color='#77E4C8', label='o1', linewidth=5)
ax.plot(datasets, speedup2, marker='o', markersize=15, linestyle='-', alpha=1, color='#577d97', label='o1+o2', linewidth=5)
ax.plot(datasets, speedup3, marker='^', markersize=15, linestyle='-', alpha=1, color='#c2b79a', label='o1+o2+o3', linewidth=5)
ax.plot(datasets, baseline, marker='*', markersize=15, linestyle='-.', alpha=1, color='red', label='baseline', linewidth=5)
# Set axis labels and title with bold font
# ax.set_xlabel('Datasets', fontsize=14, fontweight='bold')
ax.set_ylabel('Speedup', fontsize=25, fontweight='bold')
# ax.set_title('Speed-up Ratios of Different Algorithms Relative to Polak Baseline', fontsize=16)

# Set x-ticks
ax.set_xticks(np.arange(len(datasets)))
ax.set_xticklabels(datasets, rotation=20, ha='center', fontsize=20)

# Add legend with specified font size
ax.legend(fontsize=20)
# fig.legend(loc='upper center', bbox_to_anchor=(0.35, 0.97), ncol=4, fontsize=20)
# Set y-axis tick label size and tick width
ax.tick_params(axis='x', labelsize=22, width=4)
ax.tick_params(axis='y', labelsize=20, width=4)

# Set y-axis label to bold
# ax.yaxis.label.set_weight('bold')

# Set thicker border for the plot
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)

# Show the plot
plt.tight_layout()

# 保存图形为 PDF 文件
plt.savefig(r'D:\BaiduNetdiskDownload\xiaorong_speedup_natureDatasets.pdf', format='pdf')

plt.show()
