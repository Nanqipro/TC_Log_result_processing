import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file into a DataFrame
file_path = './TrustVSGroupTC/lowDegree_log_copy.xlsx'
data = pd.read_excel(file_path)

# Assuming the columns are named 'dataset_Vnumber' and 'speed-up'
# Plotting the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(data['dataset_Vnumber'], data['speed-up'], color='r', alpha=0.6, edgecolors='w', linewidth=0.5)
plt.xlabel('Dataset Vnumber')
plt.ylabel('Speed-up (GroupTC-Hash vs Trust)')
# plt.title('Speed-up of GroupTC-Hash Algorithm Compared to Trust Algorithm')
plt.grid(False)

# Adjusting the scale of axes
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot to a file
plot_path = './TrustVSGroupTC/T_VS_G_inall.png'
plt.savefig(plot_path)

# Display the plot
plt.show()
