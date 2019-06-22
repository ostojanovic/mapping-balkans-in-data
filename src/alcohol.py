
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
plt.style.use("ggplot")

countries = ["albania", "bosnia_and_herzegovina", "croatia", "montenegro", "northern_macedonia", "serbia", "slovenia"]
alcohol = []

for idx, country in enumerate(countries):
    data = pd.read_csv("../data/{}/{}.csv".format(country,country),sep=",",index_col=0)
    data = data.transpose()
    alcohol.append(data.iloc[:,data.columns == "Total alcohol consumption per capita (liters of pure alcohol, projected estimates, 15+ years of age)"].dropna().values)
alcohol = np.squeeze(np.asarray(alcohol))

plt.figure(figsize=(25,15))
x = np.linspace(1,len(countries),len(countries))
plt.bar(x=x,height=alcohol)
plt.xticks(x, ["Albania", "Bosnia and Herzegovina", "Croatia", "Montenegro", "Northern Macedonia", "Serbia", "Slovenia"], rotation=45, fontsize=18)
plt.yticks(fontsize=18)
plt.title("Total alcohol consumption per capita (liters of pure alcohol, projected estimates, 15+ years of age): 2016", fontsize=22)
plt.tight_layout()
plt.savefig("alcohol.pdf",  pad_inches=0)
