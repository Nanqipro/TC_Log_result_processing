# %%
import pandas as pd

from basic import excel_base_path

datasets = [
    "WN",
    "CD",
    "AM",
    "RC",
    "WT",
    "IM",
    "WB",
    "AS",
    "CP",
    "SP",
    "SX",
    "CL",
    "SL",
    "K5",
    "HW",
    "CO",
    "EN",
    "K4",
    "TW",
    "CF",
]

input_excel_path = excel_base_path + "grouptc_bs_ablation_time.xlsx"

result = (
    "VP achieves an average speedup of {speedup_vp_avg}×. In the best case, {dataset_speedup_vp_max} graph, VP achieves a speedup of {speedup_vp_max}×. "
    "With the addition of EF, an additional average speedup of {speedup_ef_avg}× is observed, reaching a maximum of {speedup_ef_max}× on the {dataset_speedup_ef_max} graph. "
    "RL only achieves a maximum speedup of {speedup_rl_max}×, as it introduces additional recording overhead and is effective only on graphs with many large neighbor lists."
)

df = pd.read_excel(input_excel_path)

df = df[df["Datasets"].isin(datasets)]

df["EF_speedup"] = df["VP+EF_speedup"] / df["VP_speedup"]
df["RL_speedup"] = df["VP+EF+RL_speedup"] / df["VP+EF_speedup"]


speedup_vp_avg = df["VP_speedup"].mean()
speedup_vp_max = df["VP_speedup"].max()
speedup_ef_avg = df["EF_speedup"].mean()
speedup_ef_max = df["EF_speedup"].max()
speedup_rl_avg = df["RL_speedup"].mean()
speedup_rl_max = df["RL_speedup"].max()

dataset_speedup_vp_max = df["Datasets"][df["VP_speedup"].idxmax()]
dataset_speedup_ef_max = df["Datasets"][df["EF_speedup"].idxmax()]

print({
    "speedup_vp_avg": round(speedup_vp_avg, 2),
    "speedup_vp_max": round(speedup_vp_max, 2),
    "speedup_ef_avg": round(speedup_ef_avg, 2),
    "speedup_ef_max": round(speedup_ef_max, 2),
    "speedup_rl_max": round(speedup_rl_max, 2),
    "dataset_speedup_vp_max": dataset_speedup_vp_max,
    "dataset_speedup_ef_max": dataset_speedup_ef_max,
})

print(
    result.format(
        speedup_vp_avg=round(speedup_vp_avg, 2),
        speedup_vp_max=round(speedup_vp_max, 2),
        speedup_ef_avg=round(speedup_ef_avg, 2),
        speedup_ef_max=round(speedup_ef_max, 2),
        speedup_rl_max=round(speedup_rl_max, 2),
        dataset_speedup_vp_max=dataset_speedup_vp_max,
        dataset_speedup_ef_max=dataset_speedup_ef_max,
    )
)

# %%
