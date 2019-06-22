
import pandas as pd
from matplotlib import pyplot as plt
plt.style.use("ggplot")

country = "albania"
data = pd.read_csv("../data/{}/{}.csv".format(country,country),sep=",",index_col=0)
data = data.transpose()


categories = list(data.columns)
for idx, val in enumerate(categories):
    print(idx, val)

tractors = data.iloc[:,data.columns=="Agricultural machinery, tractors"].dropna()

plt.figure(figsize=(19.5,10))
plt.plot(tractors, "o-")
plt.xticks(rotation='vertical')
plt.title("Agricultural machinery, tractors")
plt.show()

male_female_ratio = data.iloc[:,data.columns=="Sex ratio at birth (male births per female births)"].dropna()

plt.figure(figsize=(19.5,10))
plt.plot(male_female_ratio, "o-")
plt.xticks(rotation='vertical')
plt.title("Sex ratio at birth (male births per female births)")
plt.show()


# y1 = data.iloc[:,data.columns=="Completeness of birth registration (%)"].dropna()
# y2 = data.iloc[:,data.columns=="Completeness of birth registration, urban (%)"].dropna()
# y3 = data.iloc[:,data.columns=="Completeness of birth registration, rural (%)"].dropna()
# y4 = data.iloc[:,data.columns=="Completeness of birth registration, male (%)"].dropna()
# y5 = data.iloc[:,data.columns=="Completeness of birth registration, female (%)"].dropna()
#
# plt.plot(y1)
# plt.plot(y2)
# plt.plot(y3)
# plt.plot(y4)
# plt.plot(y5)
#
# plt.title("Completeness of birth registration")
# plt.legend(["total", "urban", "rural", "male", "female"], loc="best")


lowest_10 = data.iloc[:,data.columns == "Income share held by lowest 10%"].dropna()
lowest_20 = data.iloc[:,data.columns == "Income share held by lowest 20%"].dropna()

highest_10 = data.iloc[:,data.columns == "Income share held by highest 10%"].dropna()
highest_20 = data.iloc[:,data.columns == "Income share held by highest 20%"].dropna()

second_20 = data.iloc[:,data.columns == "Income share held by second 20%"].dropna()
third_20 = data.iloc[:,data.columns == "Income share held by third 20%"].dropna()
fourth_20 = data.iloc[:,data.columns == "Income share held by fourth 20%"].dropna()

# plt.plot(lowest_10)
# plt.plot(lowest_20)
#
# plt.plot(highest_10)
# plt.plot(highest_20)
#
# plt.plot(second_20)
# plt.plot(third_20)
# plt.plot(fourth_20)
#
# plt.legend(["lowest_10", "lowest_20", "highest_10", "highest_20", "second_20", "third_20", "fourth_20"])
# plt.title("Income held by a percentage of population")

plt.figure(figsize=(19.5,10))
plt.plot(lowest_10, "o-")
plt.plot(highest_10, "o-")

plt.legend(["lowest_10", "highest_10"])
plt.title("Income held by a percentage of population")
plt.show()

# plt.plot(lowest_20)
# plt.plot(highest_20)
#
# plt.legend(["lowest_20", "highest_20"])
# plt.title("Income held by a percentage of population")


defecation = data.iloc[:,data.columns == "People practicing open defecation (% of population)"].dropna()
defecation_urban = data.iloc[:,data.columns == "People practicing open defecation, urban (% of urban population)"].dropna()
defecation_rural = data.iloc[:,data.columns == "People practicing open defecation, rural (% of rural population)"].dropna()

plt.figure(figsize=(19.5,10))
plt.plot(defecation, "o-")
plt.plot(defecation_urban, "x-")
plt.plot(defecation_rural, "+-")
plt.xticks(rotation='vertical')

plt.legend(["total", "urban", "rural"])
plt.title("Percentage of population practicing open defecation")
plt.show()

condoms_male = data.iloc[:,data.columns == "Condom use, population ages 15-24, male (% of males ages 15-24)"].dropna()
condoms_female = data.iloc[:,data.columns == "Condom use, population ages 15-24, female (% of females ages 15-24)"].dropna()

plt.plot(condoms_male,"o")
plt.plot(condoms_female, "x")

plt.legend(["male", "female"])
plt.title("Condom use, population ages 15-24")


smoking = data.iloc[:,data.columns == "Smoking prevalence, total (ages 15+)"].dropna()
smoking_females = data.iloc[:,data.columns == "Smoking prevalence, females (% of adults)"].dropna()

plt.figure(figsize=(19.5,10))
plt.plot(smoking,"o-")
plt.plot(smoking_females, "x-")

plt.legend(["total (ages 15+)", "females (% of adults)"])
plt.title("Smoking_prevalence")
plt.show()


peace_keepers = data.iloc[:, data.columns == "Presence of peace keepers (number of troops, police, and military observers in mandate)"].dropna()

plt.figure(figsize=(19.5,10))
plt.plot(peace_keepers, "o-")
plt.title("Presence of peace keepers (number of troops, police, and military observers in mandate")
plt.show()


displaced_conflict_total = data.iloc[:,data.columns == "Internally displaced persons, total displaced by conflict and violence (number of people)"].dropna()
displaced_conflict_new = data.iloc[:,data.columns == "Internally displaced persons, new displacement associated with conflict and violence (number of cases)"].dropna()
displaced_disasters = data.iloc[:,data.columns == "Internally displaced persons, new displacement associated with disasters (number of cases)"].dropna()

plt.figure(figsize=(19.5,10))
plt.plot(displaced_conflict_total, "o-")
plt.plot(displaced_conflict_new, "o-")
plt.plot(displaced_disasters, "o-")

plt.legend(["total (by conflict and violence (number of people)", "new (conflict and violence (number of cases)", "disasters (number of cases)"])
plt.title("Internally displaced persons")
plt.show()


deaths_battle = data.iloc[:, data.columns == "Battle-related deaths (number of people)"].dropna()

plt.figure(figsize=(19.5,10))
plt.plot(deaths_battle, "o-")
plt.title("Battle-related deaths (number of people)")
plt.show()


alcohol = data.iloc[:,data.columns == "Total alcohol consumption per capita (liters of pure alcohol, projected estimates, 15+ years of age)"].dropna()

plt.figure(figsize=(19.5,10))
plt.plot(alcohol,"o-")
plt.title("Total alcohol consumption per capita (liters of pure alcohol, projected estimates, 15+ years of age)")
plt.show()


women_abuse1 = data.iloc[:,data.columns == "Women who believe a husband is justified in beating his wife when she refuses sex with him (%)"].dropna()

plt.figure(figsize=(19.5,10))
plt.plot(women_abuse1,"o-")
plt.title("Women who believe a husband is justified in beating his wife when she refuses sex with him (%)")
plt.show()


women_abuse2 = data.iloc[:,data.columns == "Women who believe a husband is justified in beating his wife when she neglects the children (%)"].dropna()

plt.plot(women_abuse2,"o-")
plt.title("Women who believe a husband is justified in beating his wife when she neglects the children (%)")


women_abuse3 = data.iloc[:,data.columns == "Women who believe a husband is justified in beating his wife when she goes out without telling him (%)"].dropna()

plt.plot(women_abuse3,"o-")
plt.title("Women who believe a husband is justified in beating his wife when she goes out without telling him (%)")


women_abuse4 = data.iloc[:,data.columns == "Women who believe a husband is justified in beating his wife when she burns the food (%)"].dropna()


plt.plot(women_abuse4,"o-")
plt.title("Women who believe a husband is justified in beating his wife when she burns the food (%)")


women_abuse5 = data.iloc[:,data.columns == "Women who believe a husband is justified in beating his wife when she argues with him (%)"].dropna()


plt.plot(women_abuse5,"o-")
plt.title("Women who believe a husband is justified in beating his wife when she argues with him (%)")


women_abuse6 = data.iloc[:,data.columns == "Women who believe a husband is justified in beating his wife (any of five reasons) (%)"].dropna()

plt.plot(women_abuse6,"o-")
plt.title("Women who believe a husband is justified in beating his wife (any of five reasons) (%)")


women_abuse7 = data.iloc[:,data.columns == "Proportion of women subjected to physical and/or sexual violence in the last 12 months (% of women age 15-49)"].dropna()

plt.figure(figsize=(19.5,10))
plt.plot(women_abuse7,"o-")
plt.title("Proportion of women subjected to physical and/or sexual violence in the last 12 months (% of women age 15-49)")
plt.show()


dac_italy = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, Italy (current US$)"]
dac_iceland = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, Iceland (current US$)"]
dac_ireland = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, Ireland (current US$)"]
dac_greece = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, Greece (current US$)"]
dac_uk = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, United Kingdom (current US$)"]
dac_france = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, France (current US$)"]
dac_finland = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, Finland (current US$)"]
dac_spain = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, Spain (current US$)"]
dac_denmark = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, Denmark (current US$)"]
dac_germany = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, Germany (current US$)"]
dac_czechia = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, Czech Republic (current US$)"]
dac_switzerland = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, Switzerland (current US$)"]
dac_eu = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, European Union institutions (current US$)"]
dac_canada = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, Canada (current US$)"]
dac_belgium = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, Belgium (current US$)"]
dac_austria = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, Austria (current US$)"]


# plt.plot(dac_italy)
# plt.plot(dac_iceland)
# plt.plot(dac_ireland)
# plt.plot(dac_greece)
# plt.plot(dac_uk)
# plt.plot(dac_france)
# plt.plot(dac_finland)
# plt.plot(dac_spain)
# plt.plot(dac_denmark)
# plt.plot(dac_germany)
# plt.plot(dac_czechia)
# plt.plot(dac_switzerland)
# plt.plot(dac_eu)
# plt.plot(dac_canada)
# plt.plot(dac_belgium)
# plt.plot(dac_austria)
# plt.xticks(rotation='vertical')
#
# plt.title("Net bilateral aid flows from DAC donors (US$)")
# plt.legend(["italy", "iceland", "ireland", "greece", "uk", "france", "finland", "spain",
#             "denmark", "germany", "czechia", "switzerland", "eu", "canada", "belgium", "austria"])

plt.figure(figsize=(19.5,10))
plt.plot(dac_uk, "o-")
plt.plot(dac_france, "o-")
plt.plot(dac_germany, "o-")
plt.plot(dac_switzerland, "o-")
plt.plot(dac_eu, "o-")
plt.plot(dac_canada, "o-")
plt.xticks(rotation='vertical')

plt.title("Net bilateral aid flows from DAC donors (US$)")
plt.legend(["uk", "france", "germany", "switzerland", "eu", "canada"])
plt.show()


plt.figure(figsize=(19.5,10))
plt.plot(dac_germany, "o-")
plt.plot(dac_eu, "o-")
plt.xticks(rotation='vertical')

plt.title("Net bilateral aid flows from DAC donors (US$)")
plt.legend(["germany", "eu"])
plt.show()
