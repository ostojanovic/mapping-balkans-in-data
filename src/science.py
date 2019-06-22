
import pandas as pd
import numpy as np
from utils import load_data
from matplotlib import pyplot as plt
plt.style.use("ggplot")

countries = ["albania", "bosnia_and_herzegovina", "croatia", "kosovo", "macedonia", "montenegro", "serbia", "slovenia"]
countries_ticks = pd.DataFrame(["ALB", "BIH", "CRO", "XK", "MNE", "FYROM", "SRB", "SLO"])
colors = ["firebrick", "mediumblue", "palevioletred", "darkviolet", "darkorange", "seagreen", "sienna", "darkolivegreen"]

students = [35000, 45000, 72480, 40000, 50000, 20000, 89827, 40110]
personel = [900, 2233, 7915, 1403, 2700, 850, 4289, 5730]

plot_range = range(1,len(students)+1)

students = pd.Series(students)
students_df = pd.concat([countries_ticks, students], axis=1)
students_df.columns = ["countries", "number of students"]
students_df = students_df.sort_values(by="number of students")

plt.figure(figsize=(25,15))
plt.subplots_adjust(hspace=0.2)
plt.subplot(211)
plt.stem(plot_range, students_df["number of students"])
plt.title("Number of students", fontsize=22)
plt.xticks(plot_range, students_df["countries"])
plt.tick_params(axis="both", labelsize=16)

personel = pd.Series(personel)
personel_df = pd.concat([countries_ticks, personel], axis=1)
personel_df.columns = ["countries", "size of personel"]
personel_df = personel_df.sort_values(by="size of personel")
#plot_range = range(1,len(personel_df.index)+1)

plt.subplot(212)
plt.stem(plot_range, personel_df["size of personel"])
plt.title("Size of personel", fontsize=22)
plt.xticks(plot_range, personel_df["countries"])
plt.tick_params(axis="both", labelsize=16)
plt.savefig("students.pdf",  pad_inches=0)

#plt.show()

articles = []
plt.figure(figsize=(25,15))
plt.subplots_adjust(hspace=0.2)

plt.subplot(211)
for idx, country in enumerate(countries):
    data = load_data(path="/home/olivera/Documents/side/{}/{}.csv".format(country,country))
    # data = pd.read_csv("/home/olivera/Documents/side/{}/{}.csv".format(country,country),sep=",",index_col=0)
    # data = data.transpose()
    article = data.iloc[:,data.columns == "Scientific and technical journal articles"].dropna()

    articles.append(article)

    plt.plot(article, "o-", color=colors[idx])

plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

plt.legend(["Albania", "Bosnia and Herzegovina", "Croatia", "Kosovo", "Macedonia", "Montenegro", "Serbia", "Slovenia"], fontsize=18)
plt.title("Scientific and technical journal articles", fontsize=22)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

#plt.savefig("scientific_articles.pdf",  pad_inches=0)
#plt.show()

#countries.remove("kosovo")
#colors.remove("darkviolet")

rd_money = []
plt.subplot(212)
for idx, country in enumerate(countries):
    if country == "kosovo":
        pass
    else:
        data = pd.read_csv("/home/olivera/Documents/side/{}/{}.csv".format(country,country),sep=",",index_col=0)
        data = data.transpose()
        rd_money.append(data.iloc[:,data.columns == "Research and development expenditure (% of GDP)"].dropna())
    #plt.plot_date(rd_money.index, rd_money.values, "o", color=colors[idx])


plt.plot_date(rd_money[6].index, rd_money[6].values, "-o", color="darkolivegreen")

plt.plot_date(rd_money[0].index, rd_money[0].values, "-o", color="firebrick")

plt.plot_date(rd_money[1].index, rd_money[1].values, "-o", color="mediumblue")

plt.plot_date(rd_money[2].index, rd_money[2].values, "-o", color="palevioletred")

plt.plot_date(rd_money[3].index, rd_money[3].values, "-o", color="darkorange")

plt.plot_date(rd_money[4].index, rd_money[4].values, "-o", color="seagreen")

plt.plot_date(rd_money[5].index, rd_money[5].values, "-o", color="sienna")

#handles, labels = ax.get_legend_handles_labels()

plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.legend(("Slovenia", "Albania", "Bosnia and Herzegovina", "Croatia", "Macedonia", "Montenegro", "Serbia"), fontsize=18)
plt.title("Research and development expenditure (% of GDP)", fontsize=22)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("science.pdf",  pad_inches=0)

#plt.show()
