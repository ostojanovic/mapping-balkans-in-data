
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
plt.style.use("ggplot")

countries = ["albania", "bosnia_and_herzegovina", "macedonia", "montenegro", "serbia"]
countries_ticks = ["ALB (2005)", "BIH", "FYROM (2005)", "MNE", "SRB"]

women_abuse1 = []
women_abuse2 = []
women_abuse3 = []
women_abuse4 = []
women_abuse5 = []
women_abuse6 = []

for country in countries:
    data = pd.read_csv("/home/olivera/Documents/side/{}/{}.csv".format(country,country),sep=",",index_col=0)
    data = data.transpose()

    abuse1 = data.iloc[:,data.columns == "Women who believe a husband is justified in beating his wife when she refuses sex with him (%)"].dropna()
    abuse2 = data.iloc[:,data.columns == "Women who believe a husband is justified in beating his wife when she neglects the children (%)"].dropna()
    abuse3 = data.iloc[:,data.columns == "Women who believe a husband is justified in beating his wife when she goes out without telling him (%)"].dropna()
    abuse4 = data.iloc[:,data.columns == "Women who believe a husband is justified in beating his wife when she burns the food (%)"].dropna()
    abuse5 = data.iloc[:,data.columns == "Women who believe a husband is justified in beating his wife when she argues with him (%)"].dropna()
    abuse6 = data.iloc[:,data.columns == "Women who believe a husband is justified in beating his wife (any of five reasons) (%)"].dropna()

    if abuse1.shape[0] > 1:
        women_abuse1.append(abuse1.iloc[0].values)
    else:
        women_abuse1.append(abuse1.iloc[0].values)

    if abuse2.shape[0] > 1:
        women_abuse2.append(abuse2.iloc[0].values)
    else:
        women_abuse2.append(abuse2.iloc[0].values)

    if abuse3.shape[0] > 1:
        women_abuse3.append(abuse3.iloc[0].values)
    else:
        women_abuse3.append(abuse3.iloc[0].values)

    if abuse4.shape[0] > 1:
        women_abuse4.append(abuse4.iloc[0].values)
    else:
        women_abuse4.append(abuse4.iloc[0].values)

    if abuse5.shape[0] > 1:
        women_abuse5.append(abuse5.iloc[0].values)
    else:
        women_abuse5.append(abuse5.iloc[0].values)

    if abuse6.shape[0] > 1:
        women_abuse6.append(abuse6.iloc[0].values)
    else:
        women_abuse6.append(abuse6.iloc[0].values)


women_abuse1 = np.squeeze(np.asarray(women_abuse1))
women_abuse2 = np.squeeze(np.asarray(women_abuse2))
women_abuse3 = np.squeeze(np.asarray(women_abuse3))
women_abuse4 = np.squeeze(np.asarray(women_abuse4))
women_abuse5 = np.squeeze(np.asarray(women_abuse5))
women_abuse6 = np.squeeze(np.asarray(women_abuse6))

# plt.figure(figsize=(25,15))
# x = np.linspace(1,len(countries),len(countries))
#
# plt.subplot(231)
# plt.bar(x=x, height=women_abuse1)
# plt.tick_params(axis='x', size=8, labelbottom=False)
# plt.title("... she refuses sex with him", fontsize=20)
#
# plt.subplot(232)
# plt.bar(x=x, height=women_abuse2)
# plt.tick_params(axis='x', size=8, labelbottom=False)
# plt.title("... she neglects the children", fontsize=20)
#
# plt.subplot(233)
# plt.bar(x=x, height=women_abuse3)
# plt.tick_params(axis='x', size=8, labelbottom=False)
# plt.title("... she goes out without telling him", fontsize=20)
#
# plt.subplot(234)
# plt.bar(x=x, height=women_abuse4)
# plt.xticks(x, ["Albania (2005)", "Bosnia and Herzegovina", "Macedonia (2005)", "Montenegro", "Serbia"], size=8, rotation=90, fontsize=18)
# plt.title("... she burns the food", fontsize=20)
#
# plt.subplot(235)
# plt.bar(x=x, height=women_abuse5)
# plt.xticks(x, ["Albania (2005)", "Bosnia and Herzegovina", "Macedonia (2005)", "Montenegro", "Serbia"], size=8, rotation=90, fontsize=18)
# plt.title("... she argues with him", fontsize=20)
#
# plt.subplot(236)
# plt.bar(x=x, height=women_abuse6)
# plt.xticks(x, ["Albania (2005)", "Bosnia and Herzegovina", "Macedonia (2005)", "Montenegro", "Serbia"], size=8, rotation=90, fontsize=18)
# plt.title("any of five reasons", fontsize=20)
#
# plt.suptitle("Women who believe a husband is justified in beating his wife when ... (%): 2006", fontsize=22)
# plt.tight_layout(rect=[0, 0.03, 1, 0.95])
#plt.show()
#plt.savefig("women_abuse.pdf",  pad_inches=0)


# Create a dataframe
abuse_df = pd.DataFrame({'countries': countries, "countries_ticks": countries_ticks, 'refuses sex': women_abuse1, "neglects the children": women_abuse2, "goes out without telling him": women_abuse3,
"burns the food": women_abuse4, "argues with him": women_abuse5, "any of five reasons": women_abuse6 })

my_range = range(1,len(abuse_df.index)+1)

plt.figure(figsize=(25,15))

plt.subplot(231)
plt.hlines(y=my_range, xmin=0, xmax=abuse_df.sort_values(by='refuses sex')['refuses sex'], color='skyblue', linewidth=3.0)
plt.plot(abuse_df.sort_values(by='refuses sex')['refuses sex'], my_range, "o", markersize=9)

plt.yticks(my_range, abuse_df.sort_values(by='refuses sex')['countries_ticks'], fontsize=16)
plt.tick_params(axis="x", labelsize=16)
plt.title("... she refuses sex with him", fontsize=20)

plt.subplot(232)
plt.hlines(y=my_range, xmin=0, xmax=abuse_df.sort_values(by='neglects the children')['neglects the children'], color='skyblue', linewidth=3.5)
plt.plot(abuse_df.sort_values(by='neglects the children')['neglects the children'], my_range, "o", markersize=9)

plt.yticks(my_range, abuse_df.sort_values(by='neglects the children')['countries_ticks'], fontsize=16)
plt.tick_params(axis="x", labelsize=16)
plt.title("... she neglects the children", fontsize=20)

plt.subplot(233)
plt.hlines(y=my_range, xmin=0, xmax=abuse_df.sort_values(by='goes out without telling him')['goes out without telling him'], color='skyblue', linewidth=3.0)
plt.plot(abuse_df.sort_values(by='goes out without telling him')['goes out without telling him'], my_range, "o", markersize=9)

plt.yticks(my_range, abuse_df.sort_values(by='goes out without telling him')['countries_ticks'], fontsize=16)
plt.tick_params(axis="x", labelsize=16)
plt.title("... she goes out without telling him", fontsize=20)

plt.subplot(234)
plt.hlines(y=my_range, xmin=0, xmax=abuse_df.sort_values(by='burns the food')['burns the food'], color='skyblue', linewidth=3.0)
plt.plot(abuse_df.sort_values(by='burns the food')['burns the food'], my_range, "o", markersize=9)

plt.yticks(my_range, abuse_df.sort_values(by='burns the food')['countries_ticks'], fontsize=16)
plt.tick_params(axis="x", labelsize=16)
plt.title("... she burns the food", fontsize=20)

plt.subplot(235)
plt.hlines(y=my_range, xmin=0, xmax=abuse_df.sort_values(by='argues with him')['argues with him'], color='skyblue', linewidth=3.0)
plt.plot(abuse_df.sort_values(by='argues with him')['argues with him'], my_range, "o", markersize=9)

plt.yticks(my_range, abuse_df.sort_values(by='argues with him')['countries_ticks'], fontsize=16)
plt.tick_params(axis="x", labelsize=16)
plt.title("... she argues with him", fontsize=20)

plt.subplot(236)
plt.hlines(y=my_range, xmin=0, xmax=abuse_df.sort_values(by='any of five reasons')['any of five reasons'], color='skyblue', linewidth=3.0)
plt.plot(abuse_df.sort_values(by='any of five reasons')['any of five reasons'], my_range, "o", markersize=9)

plt.yticks(my_range, abuse_df.sort_values(by='any of five reasons')['countries_ticks'], fontsize=16)
plt.tick_params(axis="x", labelsize=16)
plt.title("any of five reasons", fontsize=20)

plt.suptitle("Women who believe a husband is justified in beating his wife when ... (%): 2006", fontsize=22)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
#plt.show()
plt.savefig("women_abuse_lollipop_plot.pdf",  pad_inches=0)
