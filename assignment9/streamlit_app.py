"""
Assignment 9 — Task 2: A Streamlit Dashboard

Run locally with:
    streamlit run assignment9/streamlit_app.py

See the Week 9 assignment page for full instructions. Uses Plotly's built-in
gapminder dataset, so no data files are needed.
"""

import streamlit as st
import pandas as pd
import plotly.express as px

df = px.data.gapminder()

st.title("Gapminder Dashboard")

# 1. Add a sidebar filter — for example, a selectbox for continent or a slider for year.
# 2. Filter the DataFrame by the selected value.
# 3. Show at least two st.metric values from the filtered data
#    (for example, average life expectancy and total population).
# 4. Add at least one Plotly chart of the filtered data with st.plotly_chart.
# 5. Confirm that changing the filter updates the metrics and the chart.
