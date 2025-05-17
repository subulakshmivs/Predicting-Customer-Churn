# Customer Churn Prediction using Machine Learning

This project focuses on developing a machine learning model to predict customer churn in the telecom industry. It analyzes customer behavior and demographic data to determine the likelihood of a customer discontinuing the service.

## 📌 Objective

The primary goal of this project is to:

- Predict whether a customer will churn or not.
- Help telecom companies proactively retain customers.
- Identify the most influential factors contributing to churn.

## 🧠 Technologies & Tools Used

- **Python**  
- **Pandas**, **NumPy** for data manipulation  
- **Matplotlib**, **Seaborn** for data visualization  
- **Scikit-learn** for machine learning models  
- **Google Colab** for model training  
- **Streamlit** for creating a user-friendly dashboard  

## 📊 Dataset Description

The dataset contains customer information such as:

- Demographic details (age, gender, location)
- Account information (tenure, service usage, contract type)
- Customer activity (internet service, tech support, streaming)

Each record is labeled with a `Churn` column indicating whether the customer has left the company.

## 🔍 Exploratory Data Analysis

Comprehensive EDA was conducted to understand:

- Distribution of churn vs non-churn customers
- Impact of features such as contract type, internet service, and tenure on churn
- Correlation between numerical features

## 🧪 Model Building

Multiple machine learning models were evaluated including:

- Logistic Regression  
- Random Forest Classifier  
- Decision Tree  
- Support Vector Machine (SVM)  

The **Random Forest Classifier** provided the best performance with high accuracy and robustness to overfitting.

## 📈 Model Evaluation

Models were evaluated based on:

- Accuracy  
- Precision, Recall, F1-Score  
- Confusion Matrix  
- ROC-AUC Curve  

## 🖥️ Streamlit Dashboard

A web-based interactive dashboard was built using Streamlit, allowing users to:

- Upload new data
- Visualize key insights
- Predict churn probability for each customer

## 🚀 How to Run the App

1. Clone this repository  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
