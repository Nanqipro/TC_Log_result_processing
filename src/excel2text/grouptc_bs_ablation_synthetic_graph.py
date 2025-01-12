# %%
import pandas as pd

from basic import excel_base_path

input_excel_path = excel_base_path + "grouptc_bs_ablation_time.xlsx"

result = (
    "VP achieves an average speedup of {speedup_vp_avg}×. And EF further increases the speedup, achieving an average of {speedup_ef_avg}×. "
    "On the other hand, benefiting from the significantly larger neighbor lists due to a higher average degree in these graphs, RL achieves an average speedup of {speedup_rl_avg}×. "
)

df = pd.read_excel(input_excel_path)

df = df[df["Datasets"].str.contains(r"s\d+-e\d+", regex=True)]

df["EF_speedup"] = df["VP+EF_speedup"] / df["VP_speedup"]
df["RL_speedup"] = df["VP+EF+RL_speedup"] / df["VP+EF_speedup"]

speedup_vp_avg = df["VP_speedup"].mean()
speedup_ef_avg = df["EF_speedup"].mean()
speedup_rl_avg = df["RL_speedup"].mean()


print({
    "speedup_vp_avg": round(speedup_vp_avg, 2),
    "speedup_ef_avg": round(speedup_ef_avg, 2),
    "speedup_rl_avg": round(speedup_rl_avg, 2),
})

print(
    result.format(
        speedup_vp_avg=round(speedup_vp_avg, 2),
        speedup_ef_avg=round(speedup_ef_avg, 2),
        speedup_rl_avg=round(speedup_rl_avg, 2),
    )
)

# %%
