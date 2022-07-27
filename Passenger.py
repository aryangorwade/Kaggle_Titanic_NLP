class Passenger:
    # create "survived" instance var?
    def __init__(self, passenger, pclass, sex, age, sibsp, parch, fare, embarked):
        self.passenger = passenger # integer
        self.pclass = pclass # integer (1, 2, 3: 1 is richest)
        self.sex = sex # string: "male" or "female"
        self.age = age # int
        self.sibsp = sibsp # int
        self.parch = parch # int
        self.fare = fare # float
        self.embarked = embarked # string: 'C', 'S', 'Q'