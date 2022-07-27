import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import os
for dirname, _, filenames in os.walk(r'C:\Users\user\PycharmProjects\Titanic_NLP\titanic'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

train_data = pd.read_csv(r"C:\Users\user\PycharmProjects\Titanic_NLP\titanic\train.csv")
print(train_data.head())

def sectionOff():
    print("")
    print("---------------------------------------------------------------------------------------------")

# Calculating survival chances ---------------------------------------------------------------------------------

# Gender -------------------------------------------------------------------------------------------

women = train_data.loc[train_data.Sex == 'female']["Survived"]
rate_women = sum(women)/len(women)

men = train_data.loc[train_data.Sex == 'male']["Survived"]
rate_men = sum(men)/len(men)

print("Women have a " + "{:.2f}".format(rate_women*100) + "% chance of survival.")
print("Men have a " + "{:.2f}".format(rate_men*100) + "% chance of survival.")
sectionOff()

# Socioeconomic Class -------------------------------------------------------------------------------

firstClass = train_data.loc[train_data.Pclass == 1]["Survived"]
rate_firstClass = sum(firstClass)/len(firstClass)
print("First class (upper) passengers have a " + "{:.2f}".format(rate_firstClass*100) + "% chance of survival.")

secondClass = train_data.loc[train_data.Pclass == 2]["Survived"]
rate_secondClass = sum(secondClass)/len(secondClass)
print("Second class (middle) passengers have a " + "{:.2f}".format(rate_secondClass*100) + "% chance of survival.")

thirdClass = train_data.loc[train_data.Pclass == 3]["Survived"]
rate_thirdClass = sum(thirdClass)/len(thirdClass)
print("Third class (lower) passengers have a " + "{:.2f}".format(rate_thirdClass*100) + "% chance of survival.")
sectionOff()

# Ages -----------------------------------------------------------------------------------------------

# Children
children = train_data.loc[train_data.Age <= 15]["Survived"]
rate_children = sum(children)/len(children)
print("Children (15 and under) have a  " + "{:.2f}".format(rate_children*100) + "% chance of survival.")

# Youths (teens + young adults)
youths = train_data.loc[(train_data.Age > 15) & (train_data.Age <= 24)]["Survived"]
rate_youths = sum(youths)/len(youths)
print("Youths (16-23) have a  " + "{:.2f}".format(rate_youths*100) + "% chance of survival.")

# Adults
adults = train_data.loc[(train_data.Age >= 25) & (train_data.Age < 60)]["Survived"]
rate_adults = sum(adults)/len(adults)
print("Adults (25-60) have a  " + "{:.2f}".format(rate_adults*100) + "% chance of survival.")

# Senior citizens
seniors = train_data.loc[(train_data.Age >= 60)]["Survived"]
rate_seniors = sum(seniors)/len(seniors)
print("Seniors (60+) have a  " + "{:.2f}".format(rate_seniors*100) + "% chance of survival.")

sectionOff()

# TODO: Multiply all probabilities together for total (or add??)

# Number of siblings/spouses of people aboard ------------------------------------------------------

sibsps = []
rate_sibsps = []
rate_sibsps_percent = []

MAX_SIBSP = train_data['SibSp'].max()

for x in range(MAX_SIBSP+1):
    sibsps.append(train_data.loc[(train_data.SibSp == x)]["Survived"])
    try:
        rate_sibsps.append(sum(sibsps[x]) / len(sibsps[x]))
    except:
        rate_sibsps.append("N/A")
        rate_sibsps_percent.append("N/A")
        print("Data not available for people with " + "{:.2f}".format(x) + " number of siblings/spouses.")
    else:
        rate_sibsps_percent.append(rate_sibsps[x] * 100)
        print("People with " + "{:.2f}".format(x) + " number of siblings/spouses have a " + "{:.2f}".format(
            rate_sibsps_percent[x]) + "% chance of survival.")

sectionOff()

# Family member status ---------------------------------------------------------------------------

parchs = []
rate_parchs = []
rate_parchs_percent = []

MAX_PARCHS = train_data['Parch'].max()

for x in range(MAX_PARCHS+1):
    parchs.append(train_data.loc[(train_data.Parch == x)]["Survived"])
    try:
        rate_parchs.append(sum(parchs[x]) / len(parchs[x]))
    except:
        rate_parchs.append("N/A")
        rate_parchs_percent.append("N/A")
        print("Data not available for people with " + "{:.2f}".format(x) + " number of parents/children.")
    else:
        rate_parchs_percent.append(rate_parchs[x] * 100)
        print("People with " + "{:.2f}".format(x) + " number of parents/children have a " + "{:.2f}".format(
            rate_parchs_percent[x]) + "% chance of survival.")

sectionOff()

# TODO: Ignoring ticket number: too many types: could do letter + numbers vs numbers only (and compare in numbers only)

# Passenger Fare
MIN_FARES = train_data['Fare'].min()
MAX_FARES = train_data['Fare'].max()

print(MIN_FARES,"\n", MAX_FARES)

# categories = [0-10, 10-20, 20-30, 30-40, 40-50, 50-60, 60-70, 70-80, 80-90, 90-100, 100-125, 125-150
#               , 150-200, 200-250, 250-300, 300-400, 400-500, 500-515]
categories = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 125, 150, 200, 250, 300, 400, 500, 515]

fares = []
rate_fares = []
rate_fares_percent = []


for x in range(len(categories)-1):
    fares.append(train_data.loc[(train_data.Fare >= categories[x]) & (train_data.Fare < categories[x+1])]["Survived"])
    try:
        rate_fares.append(sum(fares[x]) / len(fares[x]))
    except:
        rate_fares.append("N/A")
        rate_fares_percent.append("N/A")
        print("Data not available for people who paid between $" + "{:.2f}".format(categories[x]) + "-" + "{:.2f}".format(categories[x+1])  + " as their fare")
    else:
        rate_fares_percent.append(rate_fares[x] * 100)
        print("People who paid between $" + "{:.2f}".format(categories[x]) + "-" + "{:.2f}".format(
            categories[x + 1]) + " as their fare have a " + "{:.2f}".format(rate_fares_percent[x]) + "% chance of survival.")
sectionOff()
# TODO: do CABIN NUMBER

# Embarked -----------------------------------------------------------------------------------

# C = Cherbourg
cherbourg = train_data.loc[(train_data.Embarked == "C")]["Survived"]
rate_cherbourg = sum(cherbourg)/len(cherbourg)
print("People embarking from Cherbourg have a " + "{:.2f}".format(rate_cherbourg*100) + "% chance of survival.")

# S = Southampton
southampton = train_data.loc[(train_data.Embarked == "S")]["Survived"]
rate_southampton = sum(southampton)/len(southampton)
print("People embarking from Southampton have a " + "{:.2f}".format(rate_southampton*100) + "% chance of survival.")

# Q = Queenstown
queenstown = train_data.loc[(train_data.Embarked == "Q")]["Survived"]
rate_queenstown = sum(queenstown)/len(queenstown)
print("People embarking from Queenstown have a " + "{:.2f}".format(rate_queenstown*100) + "% chance of survival.")
