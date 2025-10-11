'''## Challenge 3-4-1

#### Modularize our work!

Let's take what we did so far, and create a dataset that would be better prepared for analysis / machine learning.

1. create a module `check_functions.py`
    - add the `clean_currency()` function definition to it.
    - under `if __name__=='__main__':` add the tests
    - run the code to make sure it works.
2. create your challenge file `3-4-1.py`
    - import streamlit, pandas and your clean_currency function
    - load the checks dataset into a dataframe: 
    - clean the `total amount of check` and `gratuity` columns
    - calculate the `price_per_item`  as total amount of check / total items on check
    - calcualte the `price_per_person` as total amont of check / party size
    - calcualte the `items_per_person` as total items on check / party size
    - calcualte the `tip_percentage` as the total amount of check / gratuity
    - display dataframe
    - describe dataframe
    


checks dataset `https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/dining/check-data.csv`
'''

import streamlit as st
import pandas as pd

from check_functions import clean_currency
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/dining/check-data.csv"
    data = pd.read_csv(url)
    return data

st.title("Restaurant Check Data Analysis")
st.write("Analyzing dining check data with additional calculated metrics.")
data = load_data()
data['total amount of check'] = clean_currency(data['total amount of check'])
data['gratuity'] = clean_currency(data['gratuity'])
data['price_per_item'] = data['total amount of check'] / data['total items on check']
data['price_per_person'] = data['total amount of check'] / data['party size']
data['items_per_person'] = data['total items on check'] / data['party size']
data['tip_percentage'] = data['gratuity'] / data['total amount of check'] * 100
st.write("Data with calculated metrics:")
st.dataframe(data)
st.write("Descriptive statistics:")
st.write(data.describe())

