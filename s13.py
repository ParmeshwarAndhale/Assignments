Import pandas as pd
Import numpy as np
From sklearn.model_selection import train_test_split
From sklearn.linear_model import LinearRegression
# Load the dataset
url = https://archive.ics.uci.edu/ml/machine-learning-databases/nursery/nursery.data
names = [‘parents’, ‘has_nurs’, ‘form’, ‘children’, ‘housing’, ‘finance’, ‘social’, ‘health’, ‘class’]
dataset = pd.read_csv(url, names=names)
# Identify independent and target variables
X = dataset.drop(‘class’, axis=1)
Y = dataset[‘class’]
# Convert categorical variables into numerical variables using one-hot encoding
X = pd.get_dummies(X)
# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Build a linear regression model
Model = LinearRegression()
Model.fit(X_train, y_train)
# Print the coefficients of the model
Print(“Intercept: “, model.intercept_)
Print(“Coefficients: “, model.coef_)
# Predict the target variable for the testing set
Y_pred = model.predict(X_test)
# Evaluate the model using Mean Squared Error (MSE)
Mse = np.mean((y_test – y_pred) ** 2)
Print(“MSE: “, mse)
