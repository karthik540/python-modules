import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('Data.csv')
ind_dataset = dataset.iloc[:, :-1].values
dep_dataset = dataset.iloc[:, 3].values

###     Data Preprocessing
"""
#   Replacing missing data with mean values
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer.fit(ind_dataset[:, 1:3])
ind_dataset[:, 1:3] = imputer.transform(ind_dataset[:, 1:3])

#   Encoding the Labels
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
ind_dataset[:, 0] = labelencoder.fit_transform(ind_dataset[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
ind_dataset = onehotencoder.fit_transform(ind_dataset).toarray()

#   Encoding the dependent var
dep_dataset = labelencoder.fit_transform(dep_dataset)

X = ind_dataset
Y = dep_dataset
"""
#   Splitting the dataset into Training / Testing dataset...
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X , Y , test_size = 0.2, random_state = 0)

"""
#   Feature Scalling..
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
"""

###     Linear Regression
"""
#   Training the dataset
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train , Y_train)

#   Predicting the result
Y_predict = regressor.predict(X_test)
"""


###     Polynomial regression
"""
# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X)
poly_reg.fit(X_poly, y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)
"""


###     Support Vector Regression     
"""
# Fitting SVR to the dataset
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X, y)

# Predicting a new result
y_pred = regressor.predict(6.5)
"""


###     Decision Tree Regression
"""
# Fitting Decision Tree Regression to the dataset
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X, y)

# Predicting a new result
y_pred = regressor.predict(6.5)
"""


###     Random Forest Regression
"""
# Fitting Random Forest Regression to the dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
regressor.fit(X, y)

# Predicting a new result
y_pred = regressor.predict([[6.5]])
"""