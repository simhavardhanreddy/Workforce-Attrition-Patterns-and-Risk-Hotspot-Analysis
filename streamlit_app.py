import streamlit as st
import pandas as pd

st.set_page_config(page_title="Workforce Attrition Analysis")

st.title("Workforce Attrition Patterns and Risk Hotspot Analysis")
st.subheader("Palo Alto Networks")

uploaded_file = st.file_uploader("Upload Dataset", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("Dataset Loaded Successfully")

    st.write("Dataset Shape")
    st.write(df.shape)

    st.write("First 5 Records")
    st.dataframe(df.head())

    attrition_rate = (df["Attrition"].sum() / len(df)) * 100

    st.metric("Overall Attrition Rate (%)", round(attrition_rate, 2))

    st.write("Department-wise Attrition")
    dept = df.groupby("Department")["Attrition"].mean() * 100
    st.bar_chart(dept)

    st.write("Job Role-wise Attrition")
    role = df.groupby("JobRole")["Attrition"].mean() * 100
    st.bar_chart(role)

    st.write("OverTime Impact")
    overtime = df.groupby("OverTime")["Attrition"].mean() * 100
    st.bar_chart(overtime)

else:
    st.info("Please upload Palo Alto Networks.csv")
