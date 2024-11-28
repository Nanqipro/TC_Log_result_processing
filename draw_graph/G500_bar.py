# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Load the data from the Excel file
# file_path = './all_log/time_all.xlsx'
# df = pd.read_excel(file_path)
#
# # Extract data for plotting
# datasets = df['Datasets']
# polak = df['Polak']
# groupTC_BS = df['GroupTC-BS']
# trust = df['TRUST']
# groupTC_HS = df['GroupTC-HS']
# avg_degree = df['avg_degree'] if 'avg_degree' in df.columns else None  # Optional avg_degree column
#
# # Set up the figure and axes
# fig, ax1 = plt.subplots(figsize=(30, 10))
#
# # Set width of bar
# bar_width = 0.2
#
# # Set positions for each bar group
# bar_positions = np.arange(len(datasets))
#
# # Plotting the bar chart with edgecolor
# ax1.bar(bar_positions - 1.5 * bar_width, polak, bar_width, label='Polak', color='#f6c89a', edgecolor='black', linewidth=1)
# ax1.bar(bar_positions - 0.5 * bar_width, trust, bar_width, label='TRUST', color='#bce2ea', edgecolor='black', linewidth=1)
# ax1.bar(bar_positions + 0.5 * bar_width, groupTC_HS, bar_width, label='GroupTC-BS', color='#91d0fc', edgecolor='black', linewidth=1)
# ax1.bar(bar_positions + 1.5 * bar_width, groupTC_BS, bar_width, label='GroupTC-HS', color='#f2e5c1', edgecolor='black', linewidth=1)
#
# # Add avg_degree as a secondary line plot if available
# if avg_degree is not None:
#     ax2 = ax1.twinx()
#     ax2.plot(bar_positions, avg_degree, 'k-', marker='s', label='avg degree', linewidth=2)
#     ax2.set_ylabel('avg degree', fontsize=25, fontweight='bold')
#     ax2.set_ylim(0, 100)
#     ax2.tick_params(axis='both', labelsize=20)  # 设置 y 轴和 x 轴刻度标签字体大小为 20
#
# # Set axis labels and title
# ax1.set_xlabel('', fontsize=25, fontweight='bold')
# ax1.set_ylabel('Time (ms)', fontsize=25, fontweight='bold')
# ax1.set_yscale('log')
# # ax1.set_title('Running times of different algorithms under various datasets', fontsize=16)
#
# # Set y-axis tick label size for the main axis
# ax1.tick_params(axis='y', labelsize=20)
#
# # Set x-ticks
# ax1.set_xticks(bar_positions)
# ax1.set_xticklabels(datasets, fontsize=20, rotation=20, ha='center')
#
# # 添加图例
# # fig.legend(loc='upper left', bbox_to_anchor=(0.07, 0.95), fontsize=20)
# fig.legend(loc='upper center', bbox_to_anchor=(0.3, 0.95), ncol=5, fontsize=20)
# # Set thicker border for the plot
# ax = plt.gca()
# ax.spines['top'].set_linewidth(2)
# ax.spines['right'].set_linewidth(2)
# ax.spines['bottom'].set_linewidth(2)
# ax.spines['left'].set_linewidth(2)
#
# # Show the plot
# plt.tight_layout()
# plt.show()



