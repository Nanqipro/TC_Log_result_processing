# %%
import pandas as pd

from basic import excel_base_path

input_excel_path = excel_base_path + "real_world_graph_time_PTGG.xlsx"


result = (
    "GroupTC-BS and GroupTC-HS perform well across all graphs. "
    "GroupTC-BS consistently outperforms Polak, being faster on {num_datasets_bs_polak} out of {total_datasets} datasets, achieving a speedup of {speedup_bs_polak_min}-{speedup_bs_polak_max}×. "
    "Compared to TRUST, GroupTC-BS excels on {num_datasets_bs_trust} out of {total_datasets} datasets, with a speedup of {speedup_bs_trust_min}-{speedup_bs_trust_max}×. "
    "On the other {num_datasets_bs_trust_other} datasets, GroupTC-BS also performs comparable to TRUST, with a speed ratio of {speedup_bs_trust_other_min}-{speedup_bs_trust_other_max}×. "
    "GroupTC-HS outperforms Polak on {num_datasets_hs_polak} out of {total_datasets} graphs and is less effective only on very small datasets, "
    "where the cost of constructing the hash table outweighs the benefits of hash searching. "
    "But on larger datasets, GroupTC-HS demonstrates significant superiority over Polak with a speedup of {speedup_hs_polak_min}-{speedup_hs_polak_max}×. "
    "Compared with TRUST, GroupTC-HS maintains leading on all {total_datasets} datasets, achieving a speedup of {speedup_hs_trust_min}-{speedup_hs_trust_max}×."
)

df = pd.read_excel(input_excel_path)
total_datasets = df.shape[0]

df["speedup_bs_polak"] = df["Polak"] / df["GroupTC-BS"]
df["speedup_hs_polak"] = df["Polak"] / df["GroupTC-HS"]
df["speedup_bs_trust"] = df["TRUST"] / df["GroupTC-BS"]
df["speedup_hs_trust"] = df["TRUST"] / df["GroupTC-HS"]

num_datasets_bs_polak = (df["speedup_bs_polak"] > 1).sum()
filtered_speedup_bs_polak = df[df["speedup_bs_polak"] > 1]
speedup_bs_polak_min = filtered_speedup_bs_polak["speedup_bs_polak"].min()
speedup_bs_polak_max = filtered_speedup_bs_polak["speedup_bs_polak"].max()

num_datasets_bs_trust = (df["speedup_bs_trust"] > 1).sum()
filtered_speedup_bs_trust = df[df["speedup_bs_trust"] > 1]
speedup_bs_trust_min = filtered_speedup_bs_trust["speedup_bs_trust"].min()
speedup_bs_trust_max = filtered_speedup_bs_trust["speedup_bs_trust"].max()

num_datasets_bs_trust_other = (df["speedup_bs_trust"] <= 1).sum()
filtered_speedup_bs_trust_other = df[df["speedup_bs_trust"] <= 1]
speedup_bs_trust_other_min = filtered_speedup_bs_trust_other["speedup_bs_trust"].min()
speedup_bs_trust_other_max = filtered_speedup_bs_trust_other["speedup_bs_trust"].max()


num_datasets_hs_polak = (df["speedup_hs_polak"] > 1).sum()
filtered_speedup_hs_polak = df[df["speedup_hs_polak"] > 1]
speedup_hs_polak_min = filtered_speedup_hs_polak["speedup_hs_polak"].min()
speedup_hs_polak_max = filtered_speedup_hs_polak["speedup_hs_polak"].max()


speedup_hs_trust_min = df["speedup_hs_trust"].min()
speedup_hs_trust_max = df["speedup_hs_trust"].max()

print(
    {
        "total_datasets": total_datasets,
        "num_datasets_bs_polak": num_datasets_bs_polak,
        "num_datasets_bs_trust": num_datasets_bs_trust,
        "num_datasets_bs_trust_other": num_datasets_bs_trust_other,
        "speedup_bs_polak_min": round(speedup_bs_polak_min, 2),
        "speedup_bs_polak_max": round(speedup_bs_polak_max, 2),
        "speedup_bs_trust_min": round(speedup_bs_trust_min, 2),
        "speedup_bs_trust_max": round(speedup_bs_trust_max, 2),
        "speedup_bs_trust_other_min": round(speedup_bs_trust_other_min, 2),
        "speedup_bs_trust_other_max": round(speedup_bs_trust_other_max, 2),
        "num_datasets_hs_polak": num_datasets_hs_polak,
        "speedup_hs_polak_min": round(speedup_hs_polak_min, 2),
        "speedup_hs_polak_max": round(speedup_hs_polak_max, 2),
        "speedup_hs_trust_min": round(speedup_hs_trust_min, 2),
        "speedup_hs_trust_max": round(speedup_hs_trust_max, 2),
    }
)

print(
    result.format(
        total_datasets=total_datasets,
        num_datasets_bs_polak=num_datasets_bs_polak,
        num_datasets_bs_trust=num_datasets_bs_trust,
        num_datasets_bs_trust_other=num_datasets_bs_trust_other,
        speedup_bs_polak_min=round(speedup_bs_polak_min, 2),
        speedup_bs_polak_max=round(speedup_bs_polak_max, 2),
        speedup_bs_trust_min=round(speedup_bs_trust_min, 2),
        speedup_bs_trust_max=round(speedup_bs_trust_max, 2),
        speedup_bs_trust_other_min=round(speedup_bs_trust_other_min, 2),
        speedup_bs_trust_other_max=round(speedup_bs_trust_other_max, 2),
        num_datasets_hs_polak=num_datasets_hs_polak,
        speedup_hs_polak_min=round(speedup_hs_polak_min, 2),
        speedup_hs_polak_max=round(speedup_hs_polak_max, 2),
        speedup_hs_trust_min=round(speedup_hs_trust_min, 2),
        speedup_hs_trust_max=round(speedup_hs_trust_max, 2),
    )
)

# %%
