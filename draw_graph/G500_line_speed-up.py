import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from the Excel file
file_path = './G500_log/G500_log2-speed-up.xlsx'  # 请确保文件路径正确
df_speedup = pd.read_excel(file_path)

# Extract data for plotting
datasets = df_speedup['datasets']
group_tc_speedup = df_speedup['GroupTC-speed-up']
trust_speedup = df_speedup['TRUST-speed-up']
group_tc_hash_speedup = df_speedup['GroupTC-HASH-speed-up']

# Set up the figure and axes for the speed-up plot
fig, ax = plt.subplots(figsize=(15, 8))

# Plotting the speed-up ratios as line plots
ax.plot(datasets, group_tc_speedup, marker='o', markersize=7, linestyle='-', color='#FF8C00', label='GroupTC-BS', linewidth=3)
ax.plot(datasets, trust_speedup, marker='s', markersize=7, linestyle='-', color='#B0E0E6', label='TRUST', linewidth=3)
ax.plot(datasets, group_tc_hash_speedup, marker='^', markersize=7, linestyle='-', color='#DAA520', label='GroupTC-HS', linewidth=3)

# Set axis labels and title with bold font
# ax.set_xlabel('Datasets', fontsize=14, fontweight='bold')
ax.set_ylabel('Speed-up', fontsize=25, fontweight='bold')
# ax.set_title('Speed-up Ratios of Different Algorithms Relative to Polak Baseline', fontsize=16)

# Set x-ticks
ax.set_xticks(np.arange(len(datasets)))
ax.set_xticklabels(datasets, rotation=0, ha='center', fontsize=20, fontweight='bold')

# Add legend with specified font size
ax.legend(fontsize=20)

# Set y-axis tick label size and tick width
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
plt.show()
