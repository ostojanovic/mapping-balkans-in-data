
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
plt.style.use("ggplot")

countries = ["albania", "bosnia_and_herzegovina", "croatia", "montenegro", "serbia", "slovenia"]
countries_ticks = ["ALB", "BIH", "CRO", "MNE", "SRB", "SLO"]

smoking = []
smoking_2000 = []
smoking_2016 = []

for country in countries:
    data = pd.read_csv("/home/olivera/Documents/side/{}/{}.csv".format(country,country),sep=",",index_col=0)
    data = data.transpose()

    smoking.append(data.iloc[:,data.columns == "Smoking prevalence, total (ages 15+)"].dropna())
    #smoking_females = data.iloc[:,data.columns == "Smoking prevalence, females (% of adults)"].dropna()
    smoking_2000.append(data.loc[data.index == "2000", data.columns == "Smoking prevalence, total (ages 15+)"].dropna().values)
    smoking_2016.append(data.loc[data.index == "2016", data.columns == "Smoking prevalence, total (ages 15+)"].dropna().values)

smoking_2000 = np.squeeze(np.asarray(smoking_2000))
smoking_2016 = np.squeeze(np.asarray(smoking_2016))

diff = smoking_2016 - smoking_2000

plt.figure(figsize=(25,15))
plt.plot(smoking[0],"o-")
plt.plot(smoking[1],"o-")
plt.plot(smoking[2],"o-")
plt.plot(smoking[3],"o-")
plt.plot(smoking[4],"o-")
plt.plot(smoking[5],"o-")
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

#plt.plot(smoking_females, "x-")

plt.legend(["Albania", "Bosnia and Herzegovina", "Croatia",  "Montenegro", "Serbia", "Slovenia"], fontsize=18)
plt.title("Smoking prevalence (ages 15+)", fontsize=22)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
#plt.savefig("smoking.pdf",  pad_inches=0)


fig, ax = plt.subplots(figsize=(25,15))

x = np.linspace(1,len(countries),len(countries))
rects1 = plt.barh(x=x,height=smoking_2016)

for rect in rects1:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,
            '%.1f' % height,
            ha='center', va='bottom', fontsize=18)

plt.xticks(x, ["Albania", "Bosnia and Herzegovina", "Croatia", "Montenegro", "Serbia", "Slovenia"], rotation=45, fontsize=18)
plt.yticks(fontsize=18)
plt.title("Smoking prevalence, total (ages 15+): 2016", fontsize=22)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
#plt.savefig("smoking_2016.pdf",  pad_inches=0)


fig1, ax1 = plt.subplots(figsize=(25,15))
x = np.linspace(1,len(countries),len(countries))
rects2 = plt.bar(x=x,height=diff)

for rect2 in rects2:
    height2 = rect2.get_height()
    ax1.text(rect2.get_x() + rect2.get_width()/2., 1.06*height2,
            '%.1f' % height2,
            ha='center', va='bottom', fontsize=18)

plt.xticks(x, ["Albania", "Bosnia and Herzegovina", "Croatia", "Montenegro", "Serbia", "Slovenia"], rotation=45, fontsize=18)
plt.yticks(fontsize=18)
plt.title("Gain/loss of smoking prevalence (%), total (ages 15+): 2000 - 2016", fontsize=22)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
#plt.savefig("smoking_diff.pdf",  pad_inches=0)
#plt.show()

# Create a dataframe
smoking_df = pd.DataFrame({'countries': countries, "countries_ticks": countries_ticks, 'smoking 2000':smoking_2000, 'smoking 2016':smoking_2016 })

# Reorder it following the values of the first value:
ordered_df = smoking_df.sort_values(by='smoking 2000')
my_range = range(1,len(smoking_df.index)+1)

plt.figure(figsize=(25,15))

plt.hlines(y=my_range, xmin=ordered_df['smoking 2000'], xmax=ordered_df['smoking 2016'], color="grey", linewidth=3, alpha=0.7)
plt.scatter(ordered_df['smoking 2000'], my_range, color='firebrick', label='2000', s=[100])
plt.scatter(ordered_df['smoking 2016'], my_range, color='seagreen', label='2016', s=[100])
plt.legend(fontsize=16)

plt.title("Gain/loss of smoking prevalence (ages 15+)", fontsize=20)
plt.yticks(my_range, ordered_df['countries_ticks'])
plt.xlabel('Percentage (%)', fontsize=18)
plt.tick_params(axis="both", labelsize=16)
#plt.savefig("smoking_diff_lollipop_plot.pdf",  pad_inches=0)
plt.show()
