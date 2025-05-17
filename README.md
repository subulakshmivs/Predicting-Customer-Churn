# Customer Churn Prediction using Machine Learning

[![Streamlit App](https://img.shields.io/badge/Live-Demo-green?logo=streamlit)](https://predicting-customer-churn-model.streamlit.app/)

This project focuses on developing a machine learning model to predict customer churn in the telecom industry. It analyzes customer behavior and demographic data to determine the likelihood of a customer discontinuing the service.

## ✅ Objective

The primary goal of this project is to:

- Predict whether a customer will churn or not.
- Help telecom companies proactively retain customers.
- Identify the most influential factors contributing to churn.

## 🧰 Technologies & Tools Used

- **Python**  
- **Pandas**, **NumPy** for data manipulation  
- **Matplotlib** for data visualization  
- **Scikit-learn** for machine learning models  
- **Google Colab** for model training  
- **Streamlit** for creating a user-friendly dashboard  

## 📊 Dataset Description

The dataset contains customer information such as:

- Demographic details (age, gender, location)
- Account information (tenure, service usage, contract type)
- Customer activity (internet service, tech support, streaming)

Each record is labeled with a `Churn` column indicating whether the customer has left the company.

## 🔎 Exploratory Data Analysis

EDA was conducted to understand:

- Distribution of churn vs non-churn customers
- Impact of features such as contract type, internet service, and tenure
- Correlation between numerical features

## 🧪 Model Building

Multiple machine learning models were evaluated:

- Logistic Regression  
- Random Forest  
- Decision Tree  
- Support Vector Machine (SVM)  

The **Random Forest Classifier** gave the best results in terms of accuracy and robustness.

## 📈 Model Evaluation

Models were evaluated using:

- Accuracy  
- Precision, Recall, F1-Score  
- Confusion Matrix  
- ROC-AUC  

## 🖥️ Streamlit Dashboard

An interactive web app was built using **Streamlit** to:

- Upload and filter customer data
- Visualize churn statistics
- Predict churn risk
- Download filtered datasets

**🔗 Live App**: [https://predicting-customer-churn-model.streamlit.app/](https://predicting-customer-churn-model.streamlit.app/)

## 🛠️ How to Run Locally

1. Clone the repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
