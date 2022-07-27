import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from Passenger import Passenger

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

def calcGender(gender):
    women = train_data.loc[train_data.Sex == 'female']["Survived"]
    rate_women = sum(women)/len(women)

    men = train_data.loc[train_data.Sex == 'male']["Survived"]
    rate_men = sum(men)/len(men)

    print("Women have a " + "{:.2f}".format(rate_women*100) + "% chance of survival.")
    print("Men have a " + "{:.2f}".format(rate_men*100) + "% chance of survival.")
    sectionOff()

    if gender == "male":
        return rate_men
    elif gender == "female":
        return rate_women

# Socioeconomic Class -------------------------------------------------------------------------------
def calcClass(socioecclass):

    if socioecclass == 1:
        firstClass = train_data.loc[train_data.Pclass == 1]["Survived"]
        rate_firstClass = sum(firstClass)/len(firstClass)
        print("First class (upper) passengers have a " + "{:.2f}".format(rate_firstClass*100) + "% chance of survival.")
        sectionOff()
        return rate_firstClass

    if socioecclass == 2:
        secondClass = train_data.loc[train_data.Pclass == 2]["Survived"]
        rate_secondClass = sum(secondClass)/len(secondClass)
        print("Second class (middle) passengers have a " + "{:.2f}".format(rate_secondClass*100) + "% chance of survival.")
        sectionOff()
        return rate_secondClass

    if socioecclass == 3:
        thirdClass = train_data.loc[train_data.Pclass == 3]["Survived"]
        rate_thirdClass = sum(thirdClass)/len(thirdClass)
        print("Third class (lower) passengers have a " + "{:.2f}".format(rate_thirdClass*100) + "% chance of survival.")
        sectionOff()
        return rate_thirdClass

# Ages -----------------------------------------------------------------------------------------------

def calcAge(age):
# TODO: make this like calcFare? (dynamic age brackets)
    if age <= 15: # Children
        children = train_data.loc[train_data.Age <= 15]["Survived"]
        rate_children = sum(children)/len(children)
        print("Children (15 and under) have a  " + "{:.2f}".format(rate_children*100) + "% chance of survival.")
        sectionOff()
        return rate_children

    if age > 15 and age <= 24: # Youths (teens + young adults)
        youths = train_data.loc[(train_data.Age > 15) & (train_data.Age <= 24)]["Survived"]
        rate_youths = sum(youths)/len(youths)
        print("Youths (16-23) have a  " + "{:.2f}".format(rate_youths*100) + "% chance of survival.")
        sectionOff()
        return rate_youths

    if age >= 25 and age < 60: # Adults
        adults = train_data.loc[(train_data.Age >= 25) & (train_data.Age < 60)]["Survived"]
        rate_adults = sum(adults)/len(adults)
        print("Adults (25-60) have a  " + "{:.2f}".format(rate_adults*100) + "% chance of survival.")
        sectionOff()
        return rate_adults

    if age >= 60: # Senior citizens
        seniors = train_data.loc[(train_data.Age >= 60)]["Survived"]
        rate_seniors = sum(seniors)/len(seniors)
        print("Seniors (60+) have a  " + "{:.2f}".format(rate_seniors*100) + "% chance of survival.")
        sectionOff()
        return rate_seniors

# TODO: Multiply all probabilities together for total (or add??)

# Number of siblings/spouses of people aboard ------------------------------------------------------
def calcSibSp(num):
    sibsps = []
    rate_sibsps = []
    rate_sibsps_percent = []

    MAX_SIBSP = train_data['SibSp'].max() # 8

    for x in range(MAX_SIBSP+1):
        sibsps.append(train_data.loc[(train_data.SibSp == x)]["Survived"])
        try:
            rate_sibsps.append(sum(sibsps[x]) / len(sibsps[x]))
        except:
            rate_sibsps.append("N/A")
            rate_sibsps_percent.append("N/A")
            print("Data not available for people with " + str(x) + " number of siblings/spouses.")

            temp = x
            notneeded = []
            if x == num:
                for g in range(100):
                    temp = temp + 1
                    try:
                        temp1 = train_data.loc[(train_data.SibSp == temp)]["Survived"]
                        # TODO: what if end does not have a data value? then go back instead of ahead? (temp = temp -1)?
                        notneeded.append(sum(temp1) / len(temp1))
                        # 6, 7 sibsp no data
                    except:
                        passage = True
                    else:
                        return notneeded[0]
        else:
            rate_sibsps_percent.append(rate_sibsps[x] * 100)
            print("People with " + str(x) + " number of siblings/spouses have a " + "{:.2f}".format(
                rate_sibsps_percent[x]) + "% chance of survival.")
            if x == num:
                return rate_sibsps[num]

# Family member status ---------------------------------------------------------------------------

def calcParch(parch):
    parchs = []
    rate_parchs = []
    rate_parchs_percent = []

    MAX_PARCHS = train_data['Parch'].max()

    # Only to show data
    for x in range(MAX_PARCHS+1):
        parchs.append(train_data.loc[(train_data.Parch == x)]["Survived"])
        try:
            rate_parchs.append(sum(parchs[x]) / len(parchs[x]))
        except:
            rate_parchs.append("N/A")
            rate_parchs_percent.append("N/A")
            print("Data not available for people with " + str(x) + " number of parents/children.")
            sectionOff()
            if x == parch:
                return rate_parchs[x]
        else:
            rate_parchs_percent.append(rate_parchs[x] * 100)
            print("People with " + str(x) + " number of parents/children have a " + "{:.2f}".format(
                rate_parchs_percent[x]) + "% chance of survival.")
            if x == parch:
                return rate_parchs[x]

# TODO: Ignoring ticket number: too many types: could do letter + numbers vs numbers only (and compare in numbers only)
def calcFare(fare):
    # Passenger Fare
    MIN_FARES = train_data['Fare'].min()
    MAX_FARES = train_data['Fare'].max()

    increment = MAX_FARES / 40 # number of fare brackets
    categories = [0]
    x = 0

    while x < MAX_FARES:
        if (x + increment) >= MAX_FARES:
            break
        x = x + increment
        categories.append(x)
    categories.append(MAX_FARES)

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

            temp = x
            notneeded = []
            if fare > categories[x] and fare <= categories[x+1]:
                for g in range(100):
                    temp = temp + 1
                    try:
                        temp1 = train_data.loc[(train_data.Fare > categories[x]) & (train_data.Fare <= categories[temp])]["Survived"]
                        # TODO: what if end does not have a data value? then go back instead of ahead? (temp = temp -1)?
                        notneeded.append(sum(temp1) / len(temp1))
                        # why is temp1 a dataframe and not a series
                        #  $512.3292
                    except:
                        passage = True
                    else:
                        return notneeded[0]
            sectionOff()
        else:
            rate_fares_percent.append(rate_fares[x] * 100)
            print("People who paid between $" + "{:.2f}".format(categories[x]) + "-" + "{:.2f}".format(
                categories[x + 1]) + " as their fare have a " + "{:.2f}".format(rate_fares_percent[x]) + "% chance of survival.")

            if fare >= categories[x] and fare < categories[x+1]:
                sectionOff()
                return rate_fares[x]

# TODO: do CABIN NUMBER

# Embarked -----------------------------------------------------------------------------------
def calcEmbarkPort(port):
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

    if port == 'C':
        sectionOff()
        return rate_cherbourg
    elif port == 'S':
        sectionOff()
        return rate_southampton
    elif port == 'Q':
        sectionOff()
        return rate_queenstown

def computeSurvivalScore(passenger):
    total_score = 0
    # TODO: If N/A is returned then what to do?? can you catch specific exceptions of specific variable exceptions
    rate_sex = calcGender(passenger.sex)
    rate_pclass = calcClass(passenger.pclass)
    rate_age = calcAge(passenger.age)
    rate_parch = calcParch(passenger.parch)
    rate_sibsp = calcSibSp(passenger.sibsp)
    rate_fare = calcFare(passenger.fare)
    rate_embarkport = calcEmbarkPort(passenger.embarked)

    total_score = 0
    totalcategs = 0

    if passenger.passenger is None:
        print("Error: passenger is nonetype")

    if rate_pclass is not None:
        totalcategs = totalcategs + 1
        total_score = total_score + rate_pclass
    if rate_sex is not None:
        totalcategs = totalcategs + 1
        total_score = total_score + rate_sex
    if rate_age is not None:
        totalcategs = totalcategs + 1
        total_score = total_score + rate_age
    if rate_sibsp is not None:
        totalcategs = totalcategs + 1
        total_score = total_score + rate_sibsp
    if rate_parch is not None:
        totalcategs = totalcategs + 1
        total_score = total_score + rate_parch
    if rate_fare is not None:
        totalcategs = totalcategs + 1
        total_score = total_score + rate_fare
    if rate_embarkport is not None:
        totalcategs = totalcategs + 1
        total_score = total_score + rate_embarkport

    final_score = total_score/totalcategs

    # TODO: calc weighted avg\

    # TODO: how to find weights for that?
    # multiplying doesnt seem to work
    return final_score

# TODO: test most favorable and least favorable
m_fav = Passenger(1, 1, "female", 40, 1, 3, 510.57, 'C') # most favorable
l_fav = Passenger(2, 3, "male", 65, 5, 6, 7.89, 'S' ) # least favorable
# change 510 to 140

m_score = computeSurvivalScore(m_fav) * 100
l_score = computeSurvivalScore(l_fav) * 100

avg = (m_score + l_score)/2

print("Most favorable: ", m_score)
print("Least favorable: ", l_score)
print("Average: ", avg/100)