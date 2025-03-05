import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
data = {
    "Size": [500, 700, 800, 1000, 1200, 1500, 1800, 2000, 2200, 2500],
    "Price": [100, 150, 180, 200, 240, 300, 350, 400, 450, 500]
}

df = pd.DataFrame(data)
x = df[["Size"]]
y = df["Price"] 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)