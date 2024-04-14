Import numpy as np
Import pandas as pd
From sklearn.linear_model import LinearRegression
From sklearn.model_selection import train_test_split
# Create a random dataset with 10 samples
Heights = np.random.normal(170, 10, 10)
Weights = np.random.normal(70, 5, 10)
# Combine the two arrays into a single dataset
Dataset = pd.DataFrame({‘Height’: heights, ‘Weight’: weights})
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(dataset[‘Height’], dataset[‘Weight’], test_size=0.2, 
random_state=42)
# Create a Linear Regression model and fit it to the training data
Lr_model = LinearRegression()
Lr_model.fit(X_train.values.reshape(-1, 1), y_train)
# Print the model coefficients
Print(‘Model Coefficients:’, lr_model.coef_)
# Predict the weights for the test data and print the predictions
Y_pred = lr_model.predict(X_test.values.reshape(-1, 1))
Print(‘Predictions:’, y_pred)
