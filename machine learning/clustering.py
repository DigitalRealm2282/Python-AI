import pandas as pd
from sklearn.cluster import KMeans

data = pd.read_csv("C:/Users/Mahmoud Elkolfat/OneDrive/Desktop/programs/AI/machine learning/dataset/iris/Iris.csv")
data = data.drop(["species"], axis=1)
c_num = []
j = []

for i in range (1, 10):

    model = KMeans(n_clusters=1)
    model.fit(data)
    c_num.append(1)
    j.append(model.inertia_)