import pandas as pd

# 加载CSV文件到 DataFrame
df = pd.read_excel('./TrustVSGroupTC/lowDegree-buildIndex.xlsx')

# 按照 'edge-count' 列从小到大排序，所有列都会按此排序
df_sorted = df.sort_values(by='avg_degree', ascending=True)

# 保存排序后的 DataFrame 到一个新的 CSV 文件
df_sorted.to_excel('./TrustVSGroupTC/lowDegree-buildIndex_sorted.xlsx', index=False)

# 打印排序后的 DataFrame
print(df_sorted)

