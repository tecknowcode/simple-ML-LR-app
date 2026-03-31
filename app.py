from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model/model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    age = int(request.form["age"])
    experience = int(request.form["experience"])

    data = np.array([[age, experience]])
    prediction = model.predict(data)[0]

    return render_template("index.html", income=round(prediction,0))

if __name__ == "__main__":
    app.run(debug=True)