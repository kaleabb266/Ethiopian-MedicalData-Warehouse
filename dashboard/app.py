# dashboard/app.py
import streamlit as st
import pandas as pd
import plotly.express as px
from utils import get_data

# Page configuration
st.set_page_config(page_title="Ethiopian Medical Data Warehouse", layout="wide")

# Title
st.title("Ethiopian Medical Data Warehouse Dashboard")

# Sidebar filters
st.sidebar.header("Filters")
business_type = st.sidebar.selectbox("Select Business Type", ["All", "Pharmacy", "Cosmetics", "Equipment"])
date_range = st.sidebar.date_input("Select Date Range", [])

# Query data based on filters
query = "SELECT * FROM telegram_data"
if business_type != "All":
    query += f" WHERE business_type = '{business_type}'"
if date_range:
    start_date, end_date = date_range
    query += f" AND date BETWEEN '{start_date}' AND '{end_date}'"

data = get_data(query)

# Display raw data
st.subheader("Raw Data")
st.dataframe(data)

# Visualizations
st.subheader("Trends in Medical Businesses")
if not data.empty:
    fig = px.line(data, x="date", y="message_count", title="Messages Over Time")
    st.plotly_chart(fig)

st.subheader("Object Detection Results")
detection_query = "SELECT * FROM object_detections"
detections = get_data(detection_query)
if not detections.empty:
    st.dataframe(detections)
    fig = px.bar(detections, x="class_name", y="confidence", title="Detected Objects by Confidence")
    st.plotly_chart(fig)