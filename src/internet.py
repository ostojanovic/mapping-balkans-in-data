
import pandas as pd
import numpy as np
from utils import load_data
from matplotlib import pyplot as plt
plt.style.use("ggplot")

countries = ["albania", "bosnia_and_herzegovina", "croatia", "kosovo*",  "montenegro", "northern_macedonia", "serbia", "slovenia"]
countries_ticks = pd.DataFrame(["ALB", "BIH", "CRO", "XK", "MNE", "FYROM", "SRB", "SLO"])

for country in countries:
    data = pd.read_csv("../data/{}/{}.csv".format(country,country),sep=",",index_col=0)
    data = data.transpose()
    var = data.iloc[:,data.columns=="Individuals using the Internet (% of population)"].dropna()
    print(var)

    plt.plot(var)
    plt.xticks(rotation='vertical')
    plt.title("Individuals using the Internet (% of population)")

var = data.iloc[:,data.columns=="Secure Internet servers (per 1 million people)"].dropna()

plt.plot(var)
plt.xticks(rotation='vertical')
plt.title("Secure Internet servers (per 1 million people)")

var = data.iloc[:,data.columns=="Secure Internet servers"].dropna()

plt.plot(var)
plt.xticks(rotation='vertical')
plt.title("Secure Internet servers")

var = data.iloc[:,data.columns=="Fixed broadband subscriptions (per 100 people)"].dropna()

plt.plot(var)
plt.xticks(rotation='vertical')
plt.title("Fixed broadband subscriptions (per 100 people)")

var = data.iloc[:,data.columns=="Fixed broadband subscriptions"].dropna()

plt.plot(var)
plt.xticks(rotation='vertical')
plt.title("Fixed broadband subscriptions")

var = data.iloc[:,data.columns=="Fixed telephone subscriptions (per 100 people)"].dropna()

plt.plot(var)
plt.xticks(rotation='vertical')
plt.title("Fixed telephone subscriptions (per 100 people)")

var = data.iloc[:,data.columns=="Fixed telephone subscriptions"].dropna()

plt.plot(var)
plt.xticks(rotation='vertical')
plt.title("Fixed telephone subscriptions")
