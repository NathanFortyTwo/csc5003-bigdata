import matplotlib.pyplot as plt
import pandas as pd
import json


def get_true_value(encoded_value):
    JSON_PATH = "/mnt/d/csc5003data/2005_codes.json"
    with open(JSON_PATH) as f:
        json_file = json.load(f)
        if str(encoded_value) == "nan":
            return "Unknown"

        try:
            res = json_file[COL_NAME].get(str(int(encoded_value)))
            return res
        except:
            res = json_file[COL_NAME].get(str(encoded_value))
            return res


# Read CSV data from a file
file_path = "./data/mannerOfDeathByDay.csv"
df = pd.read_csv(file_path)

COL_NAME = "manner_of_death"
df["manner_of_death"] = df["manner_of_death"].apply(get_true_value)
COL_NAME = "day_of_week_of_death"
df["day_of_week_of_death"] = df["day_of_week_of_death"].apply(get_true_value)

# Pivot the DataFrame for better visualization
df_pivot = df.pivot(
    index="day_of_week_of_death", columns="manner_of_death", values="percentage"
)


# Plot stacked bar chart
ax = df_pivot.plot(kind="bar", stacked=True, figsize=(10, 6), colormap="viridis")

# Customize the chart
ax.set_ylabel("Percentage")
ax.set_xlabel("day_of_week")
ax.set_title("Stacked Bar Chart - day_of_week_of_death vs. Manner of Death")

# Show the plot
plt.tight_layout()
plt.xticks(rotation=30, ha="right")
plt.savefig("./img/mannerOfDeathByDay.png")
