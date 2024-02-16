import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

#create DataFrame
df = pd.read_csv('bbteam.csv')

#drop rows with NA values in any columns
df = df.dropna()
print(df)
#create scaled DataFrame where each variable has mean of 0 and standard dev of 1
# We use scaling so that each variable has equal importance when fitting the k-means
# algorithm. Otherwise, the variables with the widest ranges would have too much influence.

scaled_df = StandardScaler().fit_transform(df)

#view first five rows of scaled DataFrame
print(scaled_df[:5])

from sklearn.cluster import KMeans
wcss = []

for i in range(1, 11):
    clustering = KMeans(n_clusters=i, init='k-means++', n_init=10, random_state=42)
    clustering.fit(scaled_df)
    wcss.append(clustering.inertia_)

print(wcss)

ks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # labels for our plot

import seaborn as sns
import matplotlib.pyplot as plt
sns.lineplot(x = ks, y = wcss);
plt.show()

kmeans = KMeans(
    init="k-means++",
    n_clusters=4,
    n_init=10,
    max_iter=10000,
    random_state=42
)
kmeans.fit(scaled_df)

labels = kmeans.fit_predict(scaled_df)
print()
print('******************* ')
print(labels)

#append cluster assignments to original DataFrame
df['cluster'] = kmeans.labels_
centroids = kmeans.cluster_centers_
# actually these are based on the scaled data so alone not enlightening

#view updated DataFrame
print('The updated DataFrame:')
print(df)

# now predict for the first missing row -- discovered the points is 21:
scaled_predict = StandardScaler().fit_transform([[21,3,14]])
predicted_label = kmeans.predict(scaled_predict)
print('predicted cluster for [21,3,14] is', predicted_label)

#### Players that belong to the same cluster have roughly similar values for the points,
####     assists, and rebounds columns.
##

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x =df['points']
y = df['assists']
z = df['rebounds']
ax.scatter(x,y,z, c=df.cluster,cmap='tab10')  
ax.set_xlabel("points")
ax.set_ylabel("assists")
ax.set_zlabel("rebounds")
plt.show()

