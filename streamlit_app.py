import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set page config
st.set_page_config(page_title="Customer Churn Analysis", layout="wide")

# Title
st.title("Customer Churn Analysis Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("customer_churn.csv")
    # Clean data - remove rows with empty TotalCharges
    df1 = df[df.TotalCharges != ' ']
    # Convert TotalCharges to numeric
    df1['TotalCharges'] = pd.to_numeric(df1['TotalCharges'])
    return df1

df = load_data()

# Sidebar filters
st.sidebar.header("Filter Data")
churn_filter = st.sidebar.selectbox("Churn Status", ["All", "Churned", "Not Churned"])
gender_filter = st.sidebar.selectbox("Gender", ["All", "Male", "Female"])
contract_filter = st.sidebar.selectbox("Contract Type", ["All", "Month-to-month", "One year", "Two year"])

# Apply filters
filtered_df = df.copy()
if churn_filter != "All":
    filtered_df = filtered_df[filtered_df['Churn'] == ('Yes' if churn_filter == "Churned" else 'No')]
if gender_filter != "All":
    filtered_df = filtered_df[filtered_df['gender'] == gender_filter]
if contract_filter != "All":
    filtered_df = filtered_df[filtered_df['Contract'] == contract_filter]

# Display filtered data
st.subheader("Filtered Customer Data")
st.write(f"Showing {len(filtered_df)} customers")
st.dataframe(filtered_df.head())

# Main content tabs
tab1, tab2, tab3 = st.tabs(["Overview", "Churn Analysis", "Demographics"])

with tab1:
    st.header("Dataset Overview")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Basic Statistics")
        st.write(filtered_df.describe())

    with col2:
        st.subheader("Data Types")
        st.write(filtered_df.dtypes)

    st.subheader("Missing Values")
    st.write(filtered_df.isnull().sum())

with tab2:
    st.header("Churn Analysis")

    # Churn distribution
    st.subheader("Churn Distribution")
    churn_counts = filtered_df['Churn'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(churn_counts, labels=churn_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

    # Tenure vs Churn
    st.subheader("Tenure Distribution by Churn Status")
    tenure_churn_no = filtered_df[filtered_df['Churn'] == 'No']['tenure']
    tenure_churn_yes = filtered_df[filtered_df['Churn'] == 'Yes']['tenure']

    fig, ax = plt.subplots()
    ax.hist([tenure_churn_yes, tenure_churn_no], rwidth=0.95, color=['green', 'red'],
            label=['Churn=Yes', 'Churn=No'])
    ax.set_xlabel("Tenure (months)")
    ax.set_ylabel("Number of Customers")
    ax.set_title("Customer Tenure Distribution")
    ax.legend()
    st.pyplot(fig)

    # Monthly Charges vs Churn
    st.subheader("Monthly Charges by Churn Status")
    fig, ax = plt.subplots()
    ax.boxplot(
        [filtered_df[filtered_df['Churn'] == 'No']['MonthlyCharges'],
         filtered_df[filtered_df['Churn'] == 'Yes']['MonthlyCharges']],
        labels=['Not Churned', 'Churned']
    )
    ax.set_ylabel("Monthly Charges ($)")
    st.pyplot(fig)

with tab3:
    st.header("Demographic Analysis")

    col1, col2 = st.columns(2)

    with col1:
        # Gender distribution
        st.subheader("Gender Distribution")
        gender_counts = filtered_df['gender'].value_counts()
        fig, ax = plt.subplots()
        ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

        # Senior citizen distribution
        st.subheader("Senior Citizen Distribution")
        senior_counts = filtered_df['SeniorCitizen'].value_counts()
        fig, ax = plt.subplots()
        ax.pie(senior_counts, labels=['Not Senior', 'Senior'], autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

    with col2:
        # Contract type distribution
        st.subheader("Contract Type Distribution")
        contract_counts = filtered_df['Contract'].value_counts()
        fig, ax = plt.subplots()
        ax.pie(contract_counts, labels=contract_counts.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

        # Payment method distribution
        st.subheader("Payment Method Distribution")
        payment_counts = filtered_df['PaymentMethod'].value_counts()
        fig, ax = plt.subplots()
        ax.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

# Add download button for filtered data
st.sidebar.download_button(
    label="Download Filtered Data",
    data=filtered_df.to_csv().encode('utf-8'),
    file_name='filtered_customer_churn.csv',
    mime='text/csv'
)

# Sidebar Footer - Attribution
st.sidebar.markdown("---")
st.sidebar.markdown(
    """
    **Student Name**: Subulakshmi  
    **Register Number**: 511923205046  
    **Institution**: Priyadarshini Engineering College  
    **Department**: B.Tech - IT  
    """,
    unsafe_allow_html=True
)