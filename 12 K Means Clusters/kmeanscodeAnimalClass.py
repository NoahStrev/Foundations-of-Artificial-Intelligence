# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd 

data = pd.read_csv("zoo.csv")
data.head()

names = data["animal_name"]
class_types = data["class_type"].unique()

data_cleaned = data.drop(["animal_name", "class_type"], axis=1)

# Use the Elbow method to get an indication of number of clusters for our data.
# It consists in the interpretation of a line plot with an elbow shape.
# The number of clusters is where the elbow bends.
# The x axis of the plot is the number of clusters and the y axis is the
# Within Clusters Sum of Squares (WCSS) for each number of clusters:

from sklearn.cluster import KMeans
wcss = []

for i in range(1, 11):
    clustering = KMeans(n_clusters=i, init='k-means++', n_init=10, random_state=42)
    clustering.fit(data_cleaned)
    wcss.append(clustering.inertia_)

print(wcss)
    
ks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # labels for our plot

import seaborn as sns
import matplotlib.pyplot as plt
sns.lineplot(x = ks, y = wcss);
plt.show()

# Looks to me like 6 clusters
# Since K-means is sensitive to data variance, let's look at the descriptive statistics of
# the columns we are clustering:
print
print('Descriptive stats for our data:')
print(data_cleaned.describe().T) # T is to transpose the table and make it easier to read

# Notice that the mean is relatively far from the standard deviation (std), this indicates high variance.
# Let's try to reduce it by scaling the data with Standard Scaler:

from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
scaled = ss.fit_transform(data_cleaned)
# and now let's repeat the Elbow method process for the scaled data:
wcss_sc = []

for i in range(1, 11):
    clustering_sc = KMeans(n_clusters=i, init='k-means++', n_init=10, random_state=42)
    clustering_sc.fit(scaled)
    wcss_sc.append(clustering_sc.inertia_)
    
ks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sns.lineplot(x = ks, y = wcss_sc);
plt.show()

kmeans = KMeans(
    init="k-means++",
    n_clusters=6,
    n_init=10,
    max_iter=10000,
    random_state=42
)
kmeans.fit(data_cleaned)

labels = kmeans.fit_predict(data_cleaned)
print()
print('******************* ')
print(labels)

clusters = [[], [], [], [], [], []]

for idx in range(len(labels)):
    clusters[labels[idx]].append(names[idx])

for ct in range(6):
    print("\nCluster ", ct, ":", sep="")
    for i in range(len(clusters[ct])): print(clusters[ct][i])




