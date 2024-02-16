
import numpy as np
import pandas as pd

# **************************  Step 1:  Load the data **********************
dataset = pd.read_csv('startups.csv')
print('Input data:')
print(dataset.to_string()) 
print(dataset.shape)
print()

#Multiple x values and one y which is profit

# ************************  Step 2: Separate Indep X and Dependent y ***********
dataset = pd.get_dummies(dataset)
X = dataset.drop('Profit', axis=1)
y = dataset['Profit']
print(X)
print(y)

### ************************* Step 3: Reshape X ***********************
### The linear regression model requires a 2D array, but X is currently 1D so:
##X = X.reshape(-1,1)
##
# *********************** Step 4: Split the data into Training and Test sets ******
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=1/3, random_state=0)
# Split our dataset into 2 parts (training set, test set)

# *********************** Step 5: Create and Train the LR model *********************
from sklearn.linear_model import LinearRegression
LRmodel  = LinearRegression()
LRmodel.fit(X_train, y_train)  # fit data to a linear model

# Printing coefficient and intercept
print('Coeffcient:', LRmodel.coef_)
print('Intercept (or bias):', LRmodel.intercept_)
# In scikit-learn a trailing _ indicates the attribute is estimated

# *********************** Step 6: Assess  LR model with Test data ***************
from sklearn.metrics import mean_squared_error, r2_score
# how accurate was the training?
predicts = LRmodel.predict(X_train)
r2 = r2_score(y_train, predicts)
print()
print('The r2 score for Training is: ', r2)

# how close is the model as determined by Test data?
y_predictions = LRmodel.predict(X_test)
r2 = r2_score(y_test, y_predictions) 

print()
print('The r2 score for Test is: ', r2)

# *********************** Step 7+: Use model  ***************

print('Should we consider investing in this new startup?:')
predicted_profit = LRmodel.predict([[114524,122616,261000,0,0,1]])
print('Predicted profit is', predicted_profit)
