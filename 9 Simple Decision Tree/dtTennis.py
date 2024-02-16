# Relatively simple Decision Tree example
# Using a feather data set which is a binary file format

# ********************* Phase 1: get the data ********************
import pandas as pd
tennis = pd.read_feather('tennis.feather')
print(tennis)

# ********************* Phase 2: split the data and transform it ********************

# Split out features (X) from target/result/output (y)
X = tennis[['outlook', 'temperature', 'humidity', 'wind']]
y = tennis.play

print(X)
print()
print(' and y')
print(y)

# Convert the categorical feature data into binary features (easier than numerical)

X = pd.get_dummies(X)
pd.set_option('display.max_columns', None)
print()
print('X is now')
print(X)

# ********************* Phase 3: generate Decision Tree ********************

from sklearn import tree

dt = tree.DecisionTreeClassifier() # defining a decision tree classifier model
# train the model (algo)
dt.fit(X, y) # train on feature data and target

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(12,12))

tree.plot_tree(dt, feature_names=X.columns.to_list(), class_names=["No","Yes"])
plt.show()
