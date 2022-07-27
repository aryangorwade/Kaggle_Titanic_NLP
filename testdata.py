import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from Passenger import Passenger
from calcscore import computeSurvivalScore

import os
for dirname, _, filenames in os.walk(r'C:\Users\user\PycharmProjects\Titanic_NLP\titanic'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


test_data = pd.read_csv(r"C:\Users\user\PycharmProjects\Titanic_NLP\titanic\test.csv")
print(test_data.head())

rows = []
passenger = []
pclass = []
sex = []
age = []
sibsp = []
parch = []
fare = []
embarked = []
survival_scores = []
survived = []

for i in range(len(test_data)):
    rows.append(test_data.iloc[i])
    passenger.append(rows[i].PassengerId)
    pclass.append(rows[i].Pclass)
    sex.append(rows[i].Sex)
    age.append(rows[i].Age)
    sibsp.append(rows[i].SibSp)
    parch.append(rows[i].Parch)
    fare.append(rows[i].Fare)
    embarked.append(rows[i].Embarked)

for i in range(len(passenger)):
    temp = Passenger(passenger[i], pclass[i], sex[i], age[i], sibsp[i], parch[i], fare[i], embarked[i])
    survival_scores.append(computeSurvivalScore(temp))

for x in survival_scores:
    if x > 0.4096276901707785:
        survived.append(1)
    else:
        survived.append(0)

output = pd.DataFrame({'PassengerId': passenger, 'Survived': survived})
output.to_csv('submission.csv', index=False)



