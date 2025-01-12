# %%
import pandas as pd

from basic import excel_base_path

datasets = [
    "s20-e2",
    "s20-e4",
    "s20-e8",
    "s20-e16",
    "s20-e32",
    "s20-e64",
    "s20-e128",
    "s20-e256",
    "s17-e32",
    "s18-e32",
    "s19-e32",
    "s20-e32",
    "s21-e32",
    "s22-e32",
    "s23-e32",
    "s24-e32",
]

input_excel_path = excel_base_path + "grouptc_bs_ablation_time.xlsx"

result = (
    "VP achieves an average speedup of {speedup_vp_avg}×. And EF further increases the speedup, achieving an average of {speedup_ef_avg}×. "
    "On the other hand, benefiting from the significantly larger neighbor lists due to a higher average degree in these graphs, RL achieves an average speedup of {speedup_rl_avg}×. "
)

df = pd.read_excel(input_excel_path)

df = df[df["Datasets"].isin(datasets)]

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
