'''## Challenge 3-3-2

#### Who is not buying from minimart?

Observe the following data: [https://github.com/mafudge/datasets/tree/master/minimart](https://github.com/mafudge/datasets/tree/master/minimart)

You have been hired to build a UI to display names of customers who did not buy from minimart in any given month.

Provide a Streamlit UI with a drop down selection for the month. (jan, feb, mar, apr)

It then outputs a dataframe of customers who did not buy anything in that month. 


**HINT**

Access the raw data from this base url: `https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/minimart/`
'''

import streamlit as st
import pandas as pd

@st.cache_data
def load_data(month):
    url = f"https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/minimart/{month}.csv"
    data = pd.read_csv(url)
    return data

st.title("Minimart Customer Analysis")
st.write("Select a month to see customers who did not buy anything.")
month = st.selectbox("Select Month", ["jan", "feb", "mar", "apr"])
data = load_data(month)
st.write(f"Data for {month.capitalize()}:")
st.dataframe(data)
all_customers = pd.DataFrame({
    'customer_id': range(1, 21),
    'customer_name': [f'Customer {i}' for i in range(1, 21)]
})

bought_customers = data['customer_id'].unique()
not_bought_customers = all_customers[~all_customers['customer_id'].isin(bought_customers)]
st.write(f"Customers who did not buy anything in {month.capitalize()}:")
st.dataframe(not_bought_customers)
st.write(f"Total customers who did not buy: {len(not_bought_customers)}")