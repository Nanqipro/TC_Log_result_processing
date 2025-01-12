# %%
import pandas as pd

from basic import excel_base_path

input_excel_path = excel_base_path + "synthetic_s_up_graph_time_PTGG.xlsx"

result = (
    "GroupTC-HS achieves a maximum speedup of {speedup_hs_polak_max}× compared to Polak and {speedup_hs_trust_max}× compared to TRUST, performing better on smaller dataset sizes. "
    "However, as the dataset size increases, GroupTC-BS outperforms GroupTC-HS, with a speedup of up to {speedup_bs_polak_max}× compared to Polak and {speedup_bs_trust_max}× compared to TRUST."
)

df = pd.read_excel(input_excel_path)

df["speedup_bs_polak"] = df["GroupTC-BS_speedup"] / df["Polak_speedup"]
df["speedup_hs_polak"] = df["GroupTC-HS_speedup"] / df["Polak_speedup"]
df["speedup_bs_trust"] = df["GroupTC-BS_speedup"] / df["TRUST_speedup"]
df["speedup_hs_trust"] = df["GroupTC-HS_speedup"] / df["TRUST_speedup"]

speedup_bs_polak_min = df["speedup_bs_polak"].min()
speedup_bs_polak_max = df["speedup_bs_polak"].max()
speedup_bs_trust_min = df["speedup_bs_trust"].min()
speedup_bs_trust_max = df["speedup_bs_trust"].max()
speedup_hs_polak_min = df["speedup_hs_polak"].min()
speedup_hs_polak_max = df["speedup_hs_polak"].max()
speedup_hs_trust_min = df["speedup_hs_trust"].min()
speedup_hs_trust_max = df["speedup_hs_trust"].max()


print(
    {
        "speedup_bs_polak_min": round(speedup_bs_polak_min, 2),
        "speedup_bs_polak_max": round(speedup_bs_polak_max, 2),
        "speedup_bs_trust_min": round(speedup_bs_trust_min, 2),
        "speedup_bs_trust_max": round(speedup_bs_trust_max, 2),
        "speedup_hs_polak_min": round(speedup_hs_polak_min, 2),
        "speedup_hs_polak_max": round(speedup_hs_polak_max, 2),
        "speedup_hs_trust_min": round(speedup_hs_trust_min, 2),
        "speedup_hs_trust_max": round(speedup_hs_trust_max, 2),
    }
)

print(
    result.format(
        speedup_bs_polak_min=round(speedup_bs_polak_min, 2),
        speedup_bs_polak_max=round(speedup_bs_polak_max, 2),
        speedup_bs_trust_min=round(speedup_bs_trust_min, 2),
        speedup_bs_trust_max=round(speedup_bs_trust_max, 2),
        speedup_hs_polak_min=round(speedup_hs_polak_min, 2),
        speedup_hs_polak_max=round(speedup_hs_polak_max, 2),
        speedup_hs_trust_min=round(speedup_hs_trust_min, 2),
        speedup_hs_trust_max=round(speedup_hs_trust_max, 2),
    )
)

# %%
