# %%
import pandas as pd

from basic import excel_base_path

input_excel_path = excel_base_path + "grouptc_hs_vs_trust_time.xlsx"

result = (
    "For the total time, GroupTC-HS achieves an average speedup of {speedup_total_avg}×, with a maximum speedup of {speedup_total_max}×. "
    "In hash table construction, GroupTC-HS performs worse than TRUST, achieving an average speed ratio of {speedup_hash_table_construction_avg}×, "
    "due to higher conflict rates when inserting keys into the hash table. "
    "However, in hash search time, GroupTC-HS achieves an average speedup of {speedup_hash_search_avg}×, with a maximum speedup of {speedup_hash_search_max}×, "
    "benefiting from its constant time complexity for searches."
)

df = pd.read_excel(input_excel_path)
df = df[df["large degree vertex avg degree"].notna()]

speedup_total_avg = df["large degree vertex total time_speedup"].mean()
speedup_total_max = df["large degree vertex total time_speedup"].max()
speedup_hash_table_construction_avg = df[
    "large degree vertex hash table construction time_speedup"
].mean()
speedup_hash_table_construction_max = df[
    "large degree vertex hash table construction time_speedup"
].max()
speedup_hash_search_avg = df["large degree vertex hash search time_speedup"].mean()
speedup_hash_search_max = df["large degree vertex hash search time_speedup"].max()

print(
    {
        "speedup_total_avg": round(speedup_total_avg, 2),
        "speedup_total_max": round(speedup_total_max, 2),
        "speedup_hash_table_construction_avg": round(
            speedup_hash_table_construction_avg, 2
        ),
        "speedup_hash_search_avg": round(speedup_hash_search_avg, 2),
        "speedup_hash_search_max": round(speedup_hash_search_max, 2),
    }
)

print(
    result.format(
        speedup_total_avg=round(speedup_total_avg, 2),
        speedup_total_max=round(speedup_total_max, 2),
        speedup_hash_table_construction_avg=round(
            speedup_hash_table_construction_avg, 2
        ),
        speedup_hash_table_construction_max=round(
            speedup_hash_table_construction_max, 2
        ),
        speedup_hash_search_avg=round(speedup_hash_search_avg, 2),
        speedup_hash_search_max=round(speedup_hash_search_max, 2),
    )
)

# %%
