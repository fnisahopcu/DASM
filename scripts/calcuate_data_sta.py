import seaborn as sns
import os
import pandas as pd
from matplotlib import pyplot as plt


sns.set(style="whitegrid")
sns.set_style("ticks", {"xtick.major.size": 8, "ytick.major.size": 8})

data_dict = {
    "Class" : [" building_low", " building_mid", " building_high", " bridge_low", " bridge_mid", " bridge_high", " road_low", " road_mid", " road_high"],
    "Count" : [509, 163, 390, 762, 330, 243, 553, 386, 291]
}

data_frame = pd.DataFrame(data_dict)

plt.figure(figsize = (10, 10))

ax = sns.barplot(y="Class", x="Count", data=data_frame)
fig = ax.get_figure()
fig.savefig("./sta.jpg")



data_dict = {
    "Class" : ["building", "bridge", "road"],
    "Count" : [1062, 1299, 1230]
}

data_frame = pd.DataFrame(data_dict)

plt.figure(figsize = (10, 10))

ax = sns.barplot(y="Class", x="Count", data=data_frame)
fig = ax.get_figure()
fig.savefig("./sta2.jpg")
