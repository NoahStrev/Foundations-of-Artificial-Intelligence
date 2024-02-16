# *******************************************************************
# *   Use the MLP Neural Network Classifier in scikit-learn                                 *
# *    to predict employee churn for the given organization                                *
# *                                                                                                            *
# *******************************************************************

import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
pd.set_option('display.max_rows', None)

# ***************   Step 1:  Load data  ****************************************
data=pd.read_csv('HRdata.csv')

print(data)

# ***************   Step 2: Take care of categorical data *************************
# Salary values are low, medium and high -- we need them to be numeric
# so is department
# Could use get_Dummies as we did previously, but lets learn something new -- an alternative:
  
# Import LabelEncoder
from sklearn import preprocessing

# Creating labelEncoder
le = preprocessing.LabelEncoder()

# Converting string labels into numbers.
data['salary']=le.fit_transform(data['salary'])
data['department']=le.fit_transform(data['department'])

print(data)

# ***************   Step 3: Split the dataset into a training set and a test set  ********

# Spliting data into Feature and
X=data[['satisfaction_level', 'last_evaluation', 'number_project', 'average_montly_hours',
        'time_spend_company', 'Work_accident', 'promotion_last_5years', 'department', 'salary']]
y=data['left']

# Import train_test_split function
from sklearn.model_selection import train_test_split

# Split dataset into training set and test set
# try a 70% training and 30% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# ***************   Step 4: Build an employee churn prediction model  ********************
# Our objective is to predict churn using MLPClassifier

# Import MLPClassifer 
from sklearn.neural_network import MLPClassifier

# Create model object
clf = MLPClassifier(hidden_layer_sizes=(6,5),
                    random_state=5,
                    verbose=True,
                    learning_rate_init=0.01)

# Fit data onto the model
clf.fit(X_train,y_train)

# ***************   Step 5:  Use the test data to asses the accuracy **********************
ypred=clf.predict(X_test)

# Import accuracy score 
from sklearn.metrics import accuracy_score

# Calcuate accuracy
accuracy = accuracy_score(y_test,ypred)
print('Accuracy of our model is: ' , accuracy)

# WHAT IS ALL THAT OUTPUT ??????
# Multi-Layer Perceptron trains model in an iterative manner.
# In each iteration, partial derivatives of the loss function used to update the parameters.
# We can also use regularization of the loss function to prevent overfitting in the model.

# Can we now use this model to predict churn for an employee described by thesecharacteristics:

person1 = clf.predict([[0.41,0.48,2,141,3,0,1,0,1]])
print('Person1:', person1)

person2 = clf.predict([[0.61,0.68,2,141,3,0,1,7,2]])
print('Person2:', person2)
