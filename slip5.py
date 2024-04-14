Import pandas as pd
From sklearn.datasets import load_iris
From sklearn.linear_model import LogisticRegression
From sklearn.model_selection import train_test_split
From sklearn.metrics import accuracy_score
# load the iris dataset
Iris = load_iris()
# create a dataframe from the dataset
Df = pd.DataFrame(iris.data, columns=iris.feature_names)
Df[‘target’] = iris.target
# view basic statistical details of the different species
Print(“Statistical details of Iris-setosa:”)
Print(df[df[‘target’]==0].describe())
Print(“Statistical details of Iris-versicolor:”)
Print(df[df[‘target’]==1].describe())
Print(“Statistical details of Iris-virginica:”)
Print(df[df[‘target’]==2].describe())
# split the data into training and testing sets
X = df.iloc[:,:-1]
Y = df.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# fit a logistic regression model
Logreg = LogisticRegression()
Logreg.fit(X_train, y_train)
# make predictions on the test set
Y_pred = logreg.predict(X_test)
# calculate the accuracy of the model
Accuracy = accuracy_score(y_test, y_pred)
Print(“Accuracy of the logistic regression model:”, accuracy)
