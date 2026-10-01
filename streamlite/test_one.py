"""

Interactive Streamlit Analytics 
st.selectbox() :: 
st.multiselect()
st.slider()
st.date_input()
st.dataframe()
Interactive charts
Filtering DataFrames
Connecting filters to Pandas

Interactive Sales Dashboard
"""
import streamlit as st
import pandas as pd

st.title("Interactive Sales Analytics Dashboard")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:

    #read dataset 
    df = pd.read_csv(uploaded_file)

    #display data
    st.header("Data Filtering")

    #prodcut filter
    products = st.multiselect(
        "Select Products",
        df["product"].unique()
    )

    # Category filter
    categories = st.multiselect(
        "Select Categories",
        df["category"].unique()
    )

    #sales filter 
    min_sales = st.slider(
        "Select Minimum Sales",
        min_value=0,
        max_value=int(df["Sales"].max()),
        value=0
    )

    # start with complete datset
    filtered_df = df.copy()

    #product filtering
    if products:
        filtered_df = filtered_df[filtered_df["product"].isin(products)]

    # Category filtering
    if categories:
        filtered_df = filtered_df[filtered_df["category"].isin(categories)]

    #sales filtering

    filtered_df = filtered_df[filtered_df["Sales"] >= min_sales]

    #dispay filtered data
    st.subheader("Filtered Sales Data")

    st.dataframe(
        filtered_df,
        use_container_width=True
    )

    #create KPI's

    total_sales = filtered_df["Sales"].sum()
    avg_sales = filtered_df["Sales"].mean()
    # total_products = filtered_df["product"].nunique()

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Sales", f"${total_sales:,.2f}")


    with col2:
        st.metric("Average Sales", f"${avg_sales:,.2f}")


    #Monthly sales
    st.header("Monthly Sales Analysis")

    monthly_sales = filtered_df.groupby("Month")["Sales"].sum()

    st.bar_chart(monthly_sales)
else:
    st.info("Please upload a CSV file to proceed.")


  
