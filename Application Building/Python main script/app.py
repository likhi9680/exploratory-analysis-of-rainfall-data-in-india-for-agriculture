from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

# Load saved model and preprocessing objects
model = pickle.load(open('rainfall.pkl', 'rb'))
scaler = pickle.load(open('scale.pkl', 'rb'))
encoder = pickle.load(open('encoder.pkl', 'rb'))
imputer = pickle.load(open('imputer.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get inputs from form
    input_data = [
        float(request.form['MinTemp']),
        float(request.form['MaxTemp']),
        float(request.form['Rainfall']),
        float(request.form['Humidity9am']),
        float(request.form['Humidity3pm']),
        float(request.form['Pressure9am']),
        float(request.form['Pressure3pm']),
        float(request.form['Temp9am']),
        float(request.form['Temp3pm']),
        int(request.form['RainToday'])
    ]

    columns = [
        'MinTemp', 'MaxTemp', 'Rainfall',
        'Humidity9am', 'Humidity3pm',
        'Pressure9am', 'Pressure3pm',
        'Temp9am', 'Temp3pm',
        'RainToday'
    ]

    df = pd.DataFrame([input_data], columns=columns)

    # Scale data
    df_scaled = scaler.transform(df)

    # Get prediction probabilities
    probs = model.predict_proba(df_scaled)[0]
    no_rain_prob = round(probs[0] * 100, 2)
    rain_prob = round(probs[1] * 100, 2)

    # Render result
    if rain_prob >= 50:
        return render_template(
            'chance.html',
            rain_prob=rain_prob,
            no_rain_prob=no_rain_prob
        )
    else:
        return render_template(
            'noChance.html',
            rain_prob=rain_prob,
            no_rain_prob=no_rain_prob
        )

if __name__ == "__main__":
    app.run(debug=True)