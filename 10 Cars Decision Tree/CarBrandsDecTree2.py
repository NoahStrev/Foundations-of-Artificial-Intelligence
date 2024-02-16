# pip install pyarrow
# pip install pandas
# pip install scikit-learn
# pip install matplotlib

# ************************************************************
# relatively simple example of a Decision Tree
# Which car brand purchase?
# ************************************************************

# ***************************  Code - phase 1: **********************
import pandas as pd

cars = pd.read_csv('cars.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)  # added after the inclass assignment
#print(cars.to_string())
print(cars)

# $$$$$$$$$$$$$        Take a look at the output -- this is our collected data
# $$$$$$$$$$$$$        We have 261 observations relative to mpg, cylinders, cubicinches, horsepower,
# $$$$$$$$$$$$$        weightinlbs, time-to-60, year, and the result which is brand
# $$$$$$$$$$$$$        
# $$$$$$$$$$$$$       brand: US  Europe  Japan

# ************************************************************************
#                                              Code - phase 2: Separate the data
print()

X = cars.iloc[:, :-1]
y = cars.iloc[:, [-1]]
print()
print('X is ')
print(X)
print()
print('y is ', y)


# *************************************************************************
#                                             Code - phase 3:

from sklearn import tree

dt = tree.DecisionTreeClassifier(random_state=0) # defining decision tree classifier
dt.fit(X,y) # train on feature data and target

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(20,20))
tree.plot_tree(dt, feature_names=X.columns.tolist(), filled=True, rounded=True)
plt.title("Car Brand Prediction")
plt.show()
fig.savefig('carbrandsdt.png')
