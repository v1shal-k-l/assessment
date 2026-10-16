import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv('urban_mobility.csv')

# A1. Load urban_mobility.csv into a Pandas DataFrame and display the first five rows.
print(df.head(5))
# A2. Create a new column Energy_Per_Km = Energy_Used_kWh / Distance_Km.
df["Energy_Per_Km"] = df["Energy_Used_kWh"] / df["Distance_Km"]
print(df["Energy_Per_Km"])
# A3. Display only Electric Van records where Maintenance_Flag is Yes.
mask = (df["Vehicle_Type"] == "Electric Van") & (df["Maintenance_Flag"] == "Yes")
print(df.loc[mask])
# A4. Group by Vehicle_Type and display average Distance_Km and total Trips_Count.
print(df.groupby("Vehicle_Type")["Distance_Km"].mean())
print(df.groupby("Vehicle_Type")["Trips_Count"].sum())
# A5. Use NumPy to calculate the mean, maximum and minimum of Energy_Used_kWh.
print(np.mean(df["Energy_Per_Km"]))
print(np.max(df["Energy_Per_Km"]))
print(np.min(df["Energy_Per_Km"]))
# A6. Create one bar chart showing average Energy_Used_kWh by Vehicle_Type using Matplotlib or Seaborn.
sns.barplot(data = df, x="Vehicle_Type", y="Energy_Used_kWh")
plt.show()