#*****************************************************
# relatively simple example of a Decision Tree
# Which car brand purchase?
# Noah Streveler
# Inclass Assignment - CarDT
#*****************************************************

#**************** Code - phase 1: ********************
import pandas as pd

cars = pd.read_csv('cars.csv')
pd.set_option('display.max_columns', None)
print(cars)

# Take a look at the output -- this is our collected data

#*****************************************************
#                 Code - phase 2:
print()

X = cars.iloc[:, :-1]
y = cars.iloc[:, [-1]]
print()
print('X is ')
print(X)
print()
print('y is ', y)

#*****************************************************
#                 Code - phase 3:

from sklearn import tree

dt = tree.DecisionTreeClassifier() #defining decision tree classifier
dt.fit(X,y) # train on feature data and target

import matplotlib.pyplot as plt
fig = plt.figure(figsize = (20,20))
tree.plot_tree(dt, feature_names = X.columns.tolist(), filled = True, rounded=True)
plt.title("Car Brand Prediction")
plt.show()
fig.savefig('carbrandsdt.png')
