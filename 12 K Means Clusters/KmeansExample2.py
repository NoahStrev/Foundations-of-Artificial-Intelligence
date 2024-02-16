import pandas as pd #numerical analysis, for manipulating numerical tables and time series
import numpy as np #adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions

import seaborn as sns #Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
import matplotlib.pyplot as plt #plotting engine

pd.set_option('display.max_rows', None)

# Step 1: Load the data
df = pd.read_csv("customerspending.csv")


# Step 2: Filter the data 
df = df.dropna()  # drop records with missing data
df_original = df.copy()
df = df.drop(columns=["Gender", "CustomerID"])
print(df)

# Step 3: Determine the number of clusters (Elbow method)
from sklearn.cluster import KMeans
wcss = []

for i in range(1, 11):
    clustering = KMeans(n_clusters=i, init='k-means++', n_init=10, random_state=42)
    clustering.fit(df)
    wcss.append(clustering.inertia_)

print(wcss)

ks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # labels for our plot
import seaborn as sns
import matplotlib.pyplot as plt
sns.lineplot(x = ks, y = wcss);
plt.show()

# Step 4: Use the Elbow info to create the K-Means learning model
kmeans = KMeans(
    init="k-means++",
    n_clusters=5,   # based on the elbow info
    n_init=10,
    max_iter=10000,
    random_state=42
)
kmeans.fit(df)

labels = kmeans.fit_predict(df)
print()
print('******************* ')
print(labels)

#append cluster assignments to original DataFrame
df['cluster'] = kmeans.labels_
centroids = kmeans.cluster_centers_
print('centroids')
print(centroids)
print()

#Step 5: view updated DataFrame -- Cluster info for our data
print('The updated DataFrame:')
print(df)

# Step 6: Plot the data in their clusters
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x =df['Age']
y = df['AnnualIncome']
z = df['SpendingScore']
ax.scatter(x,y,z, c=df.cluster,cmap='Paired')  
ax.set_xlabel("Age")
ax.set_ylabel("Annual Income")
ax.set_zlabel("Spending Score")
plt.show()

