
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
plt.style.use("ggplot")

countries = ["albania", "bosnia_and_herzegovina", "croatia", "macedonia", "montenegro", "serbia", "slovenia"]

male_female_ratio = []
for country in countries:
    data = pd.read_csv("/home/olivera/Documents/side/{}/{}.csv".format(country,country),sep=",",index_col=0)
    data = data.transpose()

    male_female_ratio.append(data.iloc[:,data.columns=="Sex ratio at birth (male births per female births)"].dropna())

fig, ax = plt.subplots(figsize=(25,15))
plt.plot(male_female_ratio[0], "o--", markersize=10)
plt.plot(male_female_ratio[1], "o--", markersize=10)
plt.plot(male_female_ratio[2], "o--", markersize=10)
plt.plot(male_female_ratio[3], "^--", markersize=10)
plt.plot(male_female_ratio[4], "o--", markersize=10)
plt.plot(male_female_ratio[5], "o--", markersize=10)
plt.plot(male_female_ratio[6], "v--", markersize=10)

plt.title("Sex ratio at birth (male/female), around 1.05 is considered normal", fontsize=22)
ax.text(x=0.05, y=0.65, s="Albania", transform=ax.transAxes, fontsize=18)
ax.text(x=0.045, y=0.5, s="Bosnia and Herzegovina", transform=ax.transAxes, fontsize=18)
ax.text(x=0.045, y=0.3, s="Croatia", transform=ax.transAxes, fontsize=18)
ax.text(x=0.15, y=0.13, s="Macedonia", transform=ax.transAxes, fontsize=18)
ax.text(x=0.05, y=0.97, s="Montenegro", transform=ax.transAxes, fontsize=18)
ax.text(x=0.32, y=0.05, s="Serbia", transform=ax.transAxes, fontsize=18)
ax.text(x=0.05, y=0.13, s="Slovenia", transform=ax.transAxes, fontsize=18)

plt.xticks(size=18)
plt.yticks(size=18)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("male_female_ratio_timeline.pdf",  pad_inches=0)

#plt.show()
