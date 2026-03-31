import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv("data/LR_dataset.csv")

X = df[['age', 'experience']]
y = df['income']

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model/model.pkl")

print("Model saved")