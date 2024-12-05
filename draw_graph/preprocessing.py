import pandas as pd

# Load the data from the provided text file
file_path = r"C:\Users\nanqipro\Desktop\log_temp12-04-v1_duibi\GroupTC-OPT\time_output.txt"

# Read the text file into a DataFrame using sep='\s+'
data = pd.read_csv(file_path, sep='\s+', header=None)

# Assign column names for better understanding
data.columns = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5', 'Column6', 'Column7', 'Column8', 'GroupTC-HS', 'vertex_count', 'edge_count']

# Save the DataFrame to an Excel file
excel_file_path = r"C:\Users\nanqipro\Desktop\log_temp12-04-v1_duibi\GroupTC-BS-duibi.xlsx"
data.to_excel(excel_file_path, index=False)

print(f"Excel file saved to {excel_file_path}")

# # *1000转换为ms
# import pandas as pd
#
# # 设置文件路径
# input_file_path = './all_log/'  # 请替换为你文件的实际路径
# output_file_path = input_file_path  # 保存到原始文件位置
#
# # 读取Excel文件
# df = pd.read_excel(input_file_path)
#
# # 要处理的列名列表
# columns_to_multiply = ['GroupTC-HASH',  'TRUST']
#
# # 获取每列的小数位数，假设这些列是浮动数值
# def get_decimal_places(column):
#     # 获取列的最大小数位数
#     decimals = column.dropna().apply(lambda x: len(str(x).split('.')[-1]) if '.' in str(x) else 0)
#     return max(decimals) if len(decimals) > 0 else 0
#
# # 对每列乘以1000并保留原始精度
# for col in columns_to_multiply:
#     if col in df.columns:
#         decimal_places = get_decimal_places(df[col])  # 获取原始小数位数
#         df[col] = (df[col] * 1000).round(decimal_places)  # 保留原始小数精度
#
# # 保存回原Excel文件
# df.to_excel(output_file_path, index=False)
#
# print(f"文件已保存到: {output_file_path}")

