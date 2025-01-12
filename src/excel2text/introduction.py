# %%
import pandas as pd

from basic import excel_base_path

input_excel_path = excel_base_path + "real_world_graph_time_PTGG.xlsx"

result = (
    "Compared to Polak, "
    "GroupTC-BS achieved an average speedup of {speedup_bs_polak_avg}×, with a maximum of {speedup_bs_polak_max}×, "
    "while GroupTC-HS achieved an average speedup of {speedup_hs_polak_avg}×, with a maximum of {speedup_hs_polak_max}×. "
    "Compared to TRUST, "
    "GroupTC-BS achieved an average speedup of {speedup_bs_trust_avg}×, reaching up to {speedup_bs_trust_max}×, "
    "and GroupTC-HS achieved an average speedup of {speedup_hs_trust_avg}×, with a maximum of {speedup_hs_trust_max}×."
)

df = pd.read_excel(input_excel_path)


df["speedup_bs_polak"] = df["Polak"] / df["GroupTC-BS"]
df["speedup_hs_polak"] = df["Polak"] / df["GroupTC-HS"]
df["speedup_bs_trust"] = df["TRUST"] / df["GroupTC-BS"]
df["speedup_hs_trust"] = df["TRUST"] / df["GroupTC-HS"]

speedup_bs_polak_avg = df["speedup_bs_polak"].mean()
speedup_bs_polak_max = df["speedup_bs_polak"].max()
speedup_hs_polak_avg = df["speedup_hs_polak"].mean()
speedup_hs_polak_max = df["speedup_hs_polak"].max()
speedup_bs_trust_avg = df["speedup_bs_trust"].mean()
speedup_bs_trust_max = df["speedup_bs_trust"].max()
speedup_hs_trust_avg = df["speedup_hs_trust"].mean()
speedup_hs_trust_max = df["speedup_hs_trust"].max()

print(
    {
        "speedup_bs_polak_avg": round(speedup_bs_polak_avg, 2),
        "speedup_bs_polak_max": round(speedup_bs_polak_max, 2),
        "speedup_hs_polak_avg": round(speedup_hs_polak_avg, 2),
        "speedup_hs_polak_max": round(speedup_hs_polak_max, 2),
        "speedup_bs_trust_avg": round(speedup_bs_trust_avg, 2),
        "speedup_bs_trust_max": round(speedup_bs_trust_max, 2),
        "speedup_hs_trust_avg": round(speedup_hs_trust_avg, 2),
        "speedup_hs_trust_max": round(speedup_hs_trust_max, 2),
    }
)

print(
    result.format(
        speedup_bs_polak_avg=round(speedup_bs_polak_avg, 2),
        speedup_bs_polak_max=round(speedup_bs_polak_max, 2),
        speedup_hs_polak_avg=round(speedup_hs_polak_avg, 2),
        speedup_hs_polak_max=round(speedup_hs_polak_max, 2),
        speedup_bs_trust_avg=round(speedup_bs_trust_avg, 2),
        speedup_bs_trust_max=round(speedup_bs_trust_max, 2),
        speedup_hs_trust_avg=round(speedup_hs_trust_avg, 2),
        speedup_hs_trust_max=round(speedup_hs_trust_max, 2),
    )
)

# %%
