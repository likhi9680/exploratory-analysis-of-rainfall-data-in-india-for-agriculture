<img width="1674" height="976" alt="image" src="https://github.com/user-attachments/assets/d622e41f-6b11-46eb-8829-7c611e7a8658" /># Exploratory-Analysis-of-Rainfall-Data-in-India-for-Agriculture
📌 Project Overview

This project focuses on predicting the likelihood of rainfall using machine learning techniques based on historical weather data. The system performs data preprocessing, exploratory data analysis, model training, and deploys the trained model using a Flask web application to provide real-time rainfall predictions with probability percentages.

🎯 Objectives

To analyze historical weather data and identify rainfall patterns

To build an accurate machine learning model for rainfall prediction

To deploy the model as a user-friendly web application

🛠️ Technologies Used

Programming Language: Python

Libraries: NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn

Machine Learning Model: Random Forest Classifier

Web Framework: Flask

Tools: Jupyter Notebook, VS Code, GitHub

📂 Project Structure
Rainfall_Prediction_System/
│
├── app.py
├── Rainfall_prediction.ipynb
├── rainfall.pkl
├── scale.pkl
├── encoder.pkl
├── imputer.pkl
│
├── templates/
│   ├── index.html
│   ├── chance.html
│   └── noChance.html
│
├── Data collection/
├── Data preprocessing/
├── Model Building/
├── Output/
├── Documentation/
└── Demo Video/
🚀 How to Run the Project

Clone or download the repository

Install the required Python packages

Run the Flask application:

python app.py

Open your browser and go to:

http://127.0.0.1:5000
📊 Output

User-friendly input form for weather parameters

Rainfall prediction results displayed with probability percentages

Separate result pages for rain and no-rain predictions



🎥 Demo Video of the Project

✨ Click on "View raw" to download and watch the demo video

🔗 Drive Link:
https://drive.google.com/file/d/1U2M1GHS7OLWBWjnBm2z2-eGCoW3IW79W/view?usp=sharing

🔮 Future Scope

Integration with real-time weather APIs

Use of advanced models like XGBoost or Deep Learning

Mobile and location-based rainfall prediction support

✅ Conclusion

The Rainfall Prediction System demonstrates the effective use of machine learning and web technologies to provide accurate and probability-based rainfall forecasts. This project highlights the importance of data preprocessing, model evaluation, and real-world deployment through a web interface.
