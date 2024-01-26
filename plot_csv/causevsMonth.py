import matplotlib.pyplot as plt
import pandas as pd
import json


def get_true_value(encoded_value):
    JSON_PATH = "/mnt/d/csc5003data/2005_codes.json"
    with open(JSON_PATH) as f:
        json_file = json.load(f)
        if str(encoded_value) == "nan":
            return "Unknown"
        if COL_NAME == "month_of_death":
            res = json_file[COL_NAME].get(str(encoded_value))
            return res

        res = json_file[COL_NAME].get("0" + str(encoded_value))
        return res


# Read CSV data from a file
file_path = "./data/causeRecodeByMonth.csv"
df = pd.read_csv(file_path, dtype={"39_cause_recode": str, "month_of_death": str})
COL_NAME = "39_cause_recode"
df["39_cause_recode"] = df["39_cause_recode"].apply(get_true_value)

COL_NAME = "month_of_death"
df["month_of_death"] = df["month_of_death"].apply(get_true_value)

# Pivot the DataFrame for better visualization
df_pivot = df.pivot(index="month_of_death", columns="39_cause_recode", values="total")

# Plot stacked bar chart
ax = df_pivot.plot(kind="bar", stacked=True, figsize=(10, 6), colormap="viridis")

# Customize the chart
ax.get_legend().remove()
ax.set_ylabel("Deaths")
ax.set_xlabel("month_of_death")
ax.set_title("Stacked Bar Chart - month_of_death vs. Manner of Death")

# Show the plot
plt.tight_layout()
plt.xticks(rotation=30, ha="right")
plt.savefig("./img/month_of_death.png")
