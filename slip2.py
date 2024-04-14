Import numpy as np
Import pandas as pd
From sklearn.model_selection import train_test_split
From sklearn.linear_model import LinearRegression
# Create the Salary dataset
Data = {‘YearsExperience’: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
 ‘Salary’: [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000]}
Df = pd.DataFrame(data)
# Identify the independent and target variables
X = df.iloc[:, 0:1].values
Y = df.iloc[:, 1].values
# Split the variables into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
# Print the training and testing sets
Print(“X_train:\n”, X_train)
Print(“y_train:\n”, y_train)
Print(“X_test:\n”, X_test)
Print(“y_test:\n”, y_test)
# Build a simple linear regression model
Regressor = LinearRegression()
Regressor.fit(X_train, y_train)
# Print the coefficients and intercept
Print(“Coefficients:”, regressor.coef_)
Print(“Intercept:”, regressor.intercept_
