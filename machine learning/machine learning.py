import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("C:/Users/Mahmoud Elkolfat/OneDrive/Desktop/programs/AI/machine learning/dataset/iris/Iris.csv")
data = data.dropna()

x = data.iloc[:,:-1]
y = data.iloc[:,-1]

x_train , x_test , y_train , y_test = train_test_split( x , y , train_size=0.95)

m = RandomForestClassifier()
m.fit(x_train, y_train)
print(m.score(x_train , y_train))
print(m.score(x_test , y_test))
