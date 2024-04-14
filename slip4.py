Import pandas as pd
Import random
From sklearn.linear_model import LinearRegression
# create the dataset
Fish_species = [‘Tuna’, ‘Salmon’, ‘Trout’, ‘Bass’, ‘Sardine’, ‘Cod’, ‘Mackerel’]
Weights = []
For i in range(50):
 Fish_weight = []
 For j in range(7):
 Weight = random.randint(1, 20)
 Fish_weight.append(weight)
 Weights.append(fish_weight)
Df = pd.DataFrame(weights, columns=fish_species)
# create the linear regression model
X = df.iloc[:, :-1] # independent variables
Y = df.iloc[:, -1] # target variable
Model = LinearRegression()
Model.fit(X, y)
# predict the weight of a new fish species
New_fish = [[10, 12, 15, 7, 4, 8]] # example input
Predicted_weight = model.predict(new_fish)
Print(“Predicted weight:”, predicted_weight)
