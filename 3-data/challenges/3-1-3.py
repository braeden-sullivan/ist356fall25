"""Challenge 3-1-3

Load the customers dataset and provide Streamlit widgets:
- a radio to choose gender ("M" or "F")
- a multiselect to pick which columns to display

Filter the dataframe by the chosen gender and display only the selected columns.
"""

import pandas as pd
import streamlit as st

st.title("Customers — filter by gender and columns")
url = "https://raw.githubusercontent.com/mafudge/datasets/master/customers/customers.csv"

@st.cache_data
def load_data():
    return pd.read_csv(url)
customers = load_data()

if 'gender' in customers.columns:
    gender = st.radio("Select gender to filter", options=['M', 'F'], index=0)
else:
    st.warning("The dataset does not contain a 'gender' column. Gender filter disabled.")
    gender = None

all_columns = customers.columns.tolist()
selected_columns = st.multiselect("Select columns to display", options=all_columns, default=all_columns)

if gender and 'gender' in customers.columns:
    filtered = customers[customers['gender'] == gender]
else:
    filtered = customers.copy()
if not selected_columns:
    st.info("No columns selected — showing all columns.")
    selected_columns = all_columns
st.write(f"Showing {len(filtered)} rows")
st.dataframe(filtered[selected_columns])

