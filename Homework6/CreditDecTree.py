# pip install pyarrow
# pip install pandas
# pip install scikit-learn
# pip install matplotlib

# ************************************************************
# relatively simple example of a Decision Tree
# ************************************************************

# ***************************  Code - phase 1: **********************
import pandas as pd

credit = pd.read_csv('sample_credit_data.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)  # added after the inclass assignment
print(credit)

# ************************************************************************
#                                              Code - phase 2: Separate the data
print()

X = credit.iloc[:, :-1]
y = credit.iloc[:, [-1]]
print()
print('X is ')
print(X)
print()
print('y is ', y)

X = pd.get_dummies(X)
pd.set_option('display.max_columns', None)
print()
print('X is now')
print(X)
# *************************************************************************
#                                             Code - phase 3:

from sklearn import tree

dt = tree.DecisionTreeClassifier(random_state=0) # defining decision tree classifier
dt.fit(X,y) # train on feature data and target

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(20,20))
tree.plot_tree(dt, feature_names=X.columns.tolist(), filled=True, rounded=True)
plt.title("Credit Card Prediction")
plt.show()
fig.savefig('creditcard.png')
