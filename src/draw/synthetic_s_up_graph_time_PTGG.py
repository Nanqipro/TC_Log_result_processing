#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from the Excel file
file_path = '../../excel/synthetic_s_up_graph_time_PTGG.xlsx'  # 请确保文件路径正确
df_speedup = pd.read_excel(file_path)

# Extract data for plotting
datasets = df_speedup['Datasets']
group_tc_speedup = df_speedup['GroupTC-BS_speedup']
trust_speedup = df_speedup['TRUST_speedup']
group_tc_hash_speedup = df_speedup['GroupTC-HS_speedup']
baseline = df_speedup['Polak_speedup']

# Set up the figure and axes for the speed-up plot
fig, ax = plt.subplots(figsize=(16, 10))

# Plotting the speed-up ratios as line plots
ax.plot(datasets, trust_speedup, marker='s', markersize=15, linestyle='-', alpha=1, color='#77E4C8', label='TRUST', linewidth=5)
ax.plot(datasets, group_tc_speedup, marker='o', markersize=15, linestyle='-', alpha=1, color='#577d97', label='GroupTC-BS', linewidth=5)
ax.plot(datasets, group_tc_hash_speedup, marker='^', markersize=15, linestyle='-', alpha=1, color='#c2b79a', label='GroupTC-HS', linewidth=5)
ax.plot(datasets, baseline, marker='*', markersize=15, linestyle='-', alpha=1, color='red', label='baseline', linewidth=5)

# Set axis labels and title with bold font
# ax.set_xlabel('Datasets', fontsize=14, fontweight='bold')
ax.set_ylabel('Speedup', fontsize=55, fontweight='bold')
# ax.set_title('Speed-up Ratios of Different Algorithms Relative to Polak Baseline', fontsize=16)

# Set x-ticks
ax.set_xticks(np.arange(len(datasets)))
ax.set_xticklabels(datasets, rotation=20, ha='center', fontsize=45)

# Add legend with specified font size
ax.legend(fontsize=40, loc='lower right', bbox_to_anchor=(0.98, 0.08), ncol=1)
# fig.legend(loc='upper center', bbox_to_anchor=(0.35, 0.97), ncol=4, fontsize=20)
# Set y-axis tick label size and tick width
ax.tick_params(axis='x', labelsize=45, width=4)
ax.tick_params(axis='y', labelsize=45, width=4)

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
plt.savefig('../../pdf/G500_speed-up_change_S_v4.pdf', format='pdf')

plt.show()

# %%
