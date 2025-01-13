# %%
import pandas as pd

from basic import excel_base_path

input_excel_path = excel_base_path + "trust_partition_time.xlsx"

df = pd.read_excel(input_excel_path)

df["low degree part"] = df["small degree vertex"] / df["all vertex"]
trust_percentage = df["low degree part"].mean()

print(round(trust_percentage, 4))

# %%
