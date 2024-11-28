
import pandas as pd

# Load the data from the provided text file
file_path = './all_log/GroupTC-HS.txt'

# Read the text file into a DataFrame using sep='\s+'
data = pd.read_csv(file_path, sep='\s+', header=None)

# Assign column names for better understanding
data.columns = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5', 'Column6', 'Column7', 'Column8', 'GroupTC-HS', 'vertex_count', 'edge_count']

# Save the DataFrame to an Excel file
excel_file_path = './all_log/GroupTC-HS.xlsx'
data.to_excel(excel_file_path, index=False)

print(f"Excel file saved to {excel_file_path}")
