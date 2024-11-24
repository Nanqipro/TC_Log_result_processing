import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from the Excel file
file_path = './G500_log/G500_log2.xlsx'
df = pd.read_excel(file_path)

# Extract data for plotting
datasets = df['datasets']
polak = df['polak']
group_tc = df['GroupTC']
trust = df['TRUST']
group_tc_hash = df['GroupTC-HASH']
avg_degree = df['avg_degree'] if 'avg_degree' in df.columns else None  # Optional avg_degree column

# Set up the figure and axes
fig, ax1 = plt.subplots(figsize=(15, 8))

# Set width of bar
bar_width = 0.2

# Set positions for each bar group
bar_positions = np.arange(len(datasets))

# Plotting the bar chart with edgecolor
ax1.bar(bar_positions - 1.5 * bar_width, polak, bar_width, label='Polak', color='#FFC78E', edgecolor='black', linewidth=1)
ax1.bar(bar_positions - 0.5 * bar_width, trust, bar_width, label='TRUST', color='#A8D8EA', edgecolor='black', linewidth=1)
ax1.bar(bar_positions + 0.5 * bar_width, group_tc, bar_width, label='GroupTC', color='#60A3D9', edgecolor='black', linewidth=1)
ax1.bar(bar_positions + 1.5 * bar_width, group_tc_hash, bar_width, label='GroupTC-HASH', color='#C1E7FF', edgecolor='black', linewidth=1)

# Add avg_degree as a secondary line plot if available
if avg_degree is not None:
    ax2 = ax1.twinx()
    ax2.plot(bar_positions, avg_degree, 'k-', marker='s', label='avg degree', linewidth=2)
    ax2.set_ylabel('avg degree', fontsize=18)
    ax2.set_ylim(0, 100)

# Set axis labels and title
ax1.set_xlabel('', fontsize=18, fontweight='bold')
ax1.set_ylabel('Time (ms)', fontsize=18, fontweight='bold')
ax1.set_yscale('log')
# ax1.set_title('Running times of different algorithms under various datasets', fontsize=16)

# Set y-axis tick label size for the main axis
ax1.tick_params(axis='y', labelsize=18)

# Set x-ticks
ax1.set_xticks(bar_positions)
ax1.set_xticklabels(datasets, fontsize=18 ,rotation=20, ha='right')

# Add legends for both axes
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9), fontsize=18)

# Set thicker border for the plot
ax = plt.gca()
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)

# Show the plot
plt.tight_layout()
plt.show()
