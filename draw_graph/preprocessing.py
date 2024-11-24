
import pandas as pd

# Load the data from the provided text file
file_path = './TrustVSGroupTC/GroupTCHash_lowDegree_log.txt'

# Read the text file into a DataFrame using sep='\s+'
data = pd.read_csv(file_path, sep='\s+', header=None)

# Assign column names for better understanding
data.columns = ['Column1', 'Column2']

# Save the DataFrame to an Excel file
excel_file_path = './TrustVSGroupTC/lowDegree.xlsx'
data.to_excel(excel_file_path, index=False)

print(f"Excel file saved to {excel_file_path}")
