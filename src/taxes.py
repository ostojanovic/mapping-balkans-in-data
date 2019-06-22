
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
plt.style.use("ggplot")

countries = ["albania", "bosnia_and_herzegovina", "croatia", "kosovo", "montenegro", "macedonia", "serbia", "slovenia"]
countries_ticks = pd.DataFrame(["ALB", "BIH", "CRO", "XK", "MNE", "FYROM", "SRB", "SLO"])

taxes = []
for country in countries:
    data = pd.read_csv("/home/olivera/Documents/side/{}/{}.csv".format(country,country),sep=",",index_col=0)
    data = data.transpose()

    tax_time = data.loc[data.index=="2017",data.columns=="Time to prepare and pay taxes (hours)"].dropna()
    taxes.append(tax_time.values[0])

taxes = pd.Series(taxes)
taxes_df = pd.concat([countries_ticks, taxes], axis=1)
taxes_df.columns = ["countries", "tax time"]
taxes_df = taxes_df.sort_values(by="tax time")

range = range(1,len(taxes_df.index)+1)

plt.figure(figsize=(25,15))
plt.hlines(y=range, xmin=0, xmax=taxes_df["tax time"]/24, color="grey")
plt.scatter(taxes_df["tax time"]/24, range, color='firebrick', s=[100])

plt.title("Time to prepare and pay taxes", fontsize=20)
plt.yticks(range, taxes_df["countries"])
plt.xlabel('Days', fontsize=18)
plt.tick_params(axis="both", labelsize=16)
#plt.show()
plt.savefig("tax_days.pdf",  pad_inches=0)
