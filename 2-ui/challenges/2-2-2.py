## Challenge 2-2-2

### Order total and history

#Write a streamlit to input an amount.

#create an "add to total" button to accumulate the amount in the total
#create a "clear" button to reset the session vars

#display the total and the history of each item entered 

#HINT: you'll need to manage a list for history!

import streamlit as st

# initialize
if 'amount' not in st.session_state:
    st.session_state.amount = 0
if 'total' not in st.session_state:
    st.session_state.total = 0
if 'history' not in st.session_state:
    st.session_state.history = []

# widget setup
st.title('Order Total Calculator')
st.write("Add amounts to the total and see the history of entries")
amount = st.number_input('Enter the amount to add:')
add_clicked = st.button('Add to Total', type='primary')
clear_clicked = st.button('Clear', type='secondary')

# interactions
if clear_clicked:
    st.session_state.amount = 0
    st.session_state.total = 0
    st.session_state.history = []
elif add_clicked:
    st.session_state.amount = amount
    st.session_state.total += st.session_state.amount
    st.session_state.history.append(st.session_state.amount)
    st.session_state.amount = 0

# display session state, after interations
st.write(f'Total: {st.session_state.total}')
st.write(f'History: {st.session_state.history}')
