
import pandas as pd
from matplotlib import pyplot as plt
plt.style.use("ggplot")

country = "serbia"
data = pd.read_csv("/home/olivera/Documents/side/{}/{}.csv".format(country,country),sep=",",index_col=0)
data = data.transpose()

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


women_abuse7 = data.iloc[:,data.columns == "Proportion of women subjected to physical and/or sexual violence in the last 12 months (% of women age 15-49)"].dropna()

plt.figure(figsize=(19.5,10))
plt.plot(women_abuse7,"o-")
plt.title("Proportion of women subjected to physical and/or sexual violence in the last 12 months (% of women age 15-49)")
plt.show()


# dac_italy = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, Italy (current US$)"]
# dac_iceland = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, Iceland (current US$)"]
# dac_ireland = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, Ireland (current US$)"]
# dac_greece = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, Greece (current US$)"]
# dac_uk = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, United Kingdom (current US$)"]
# dac_france = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, France (current US$)"]
# dac_finland = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, Finland (current US$)"]
# dac_spain = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, Spain (current US$)"]
# dac_denmark = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, Denmark (current US$)"]
# dac_germany = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, Germany (current US$)"]
# dac_czechia = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, Czech Republic (current US$)"]
# dac_switzerland = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, Switzerland (current US$)"]
# dac_eu = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, European Union institutions (current US$)"]
# dac_canada = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, Canada (current US$)"]
# dac_belgium = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, Belgium (current US$)"]
# dac_austria = data.iloc[:,data.columns == "Net bilateral aid flows from DAC donors, Austria (current US$)"]

# plt.figure(figsize=(19.5,10))
# plt.plot(dac_uk, "o-")
# plt.plot(dac_france, "o-")
# plt.plot(dac_germany, "o-")
# plt.plot(dac_switzerland, "o-")
# plt.plot(dac_eu, "o-")
# plt.plot(dac_canada, "o-")
# plt.xticks(rotation='vertical')
#
# plt.title("Net bilateral aid flows from DAC donors (US$)")
# plt.legend(["uk", "france", "germany", "switzerland", "eu", "canada"])
# plt.show()
#
#
# plt.figure(figsize=(19.5,10))
# plt.plot(dac_germany, "o-")
# plt.plot(dac_eu, "o-")
# plt.xticks(rotation='vertical')
#
# plt.title("Net bilateral aid flows from DAC donors (US$)")
# plt.legend(["germany", "eu"])
# plt.show()
