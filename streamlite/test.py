"""
Fundamentals of Streamlit::

Understand what Streamlit is
Create a basic Streamlit application
Display text and data
Upload a CSV file
Calculate KPIs
Display KPI cards
Run a Python application as a web app


Python + Pandas  --> Streamit --> Web Dashboard or Application
--> pip install streamlit

"""
import streamlit as st
import pandas as pd

st.title("Sales Analytics Dashboard")
st.header("Upload Sales Data")
uploaded_file =st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:

    #read dataset
    df =pd.read_csv(uploaded_file)

    #calucate KPI
    total_sales = df['Sales'].sum()
    avg_sales = df['Sales'].mean()
    total_records = len(df)


    st.subheader("KPI Summary")
    st.metric("Total Sales", f"${total_sales:,.2f}")
    st.metric("Average Sales", f"${avg_sales:,.2f}")
    st.metric("Total Records", total_records)

    #display data 
    st.subheader("Sales Data")
    st.write(df)
