# Challenge 2-2-1

#Write a streamlit to input a length and width of a rectangle, and output the permieter 
# 2 x (L+W) and area (L x W) of that rectangle 
#use a "calculate" button and a "clear" button 
#use `st.number_input()` for numbers

import streamlit as st
# initialize
if 'length' not in st.session_state:
    st.session_state.length = 0
if 'width' not in st.session_state:
    st.session_state.width = 0
if 'area' not in st.session_state:
    st.session_state.area = 0
if 'perimeter' not in st.session_state:
    st.session_state.perimeter = 0

# widget setup
st.title('Rectangle Calculator')
st.write("Calculate the perimeter and area of a rectangle")
length = st.number_input('Enter the length of the rectangle:', min_value=0.0, step=0.1)
width = st.number_input('Enter the width of the rectangle:', min_value=0.0, step=0.1)
calculate_clicked = st.button('Calculate', type='primary')
clear_clicked = st.button('Clear', type='secondary')

# interactions
if clear_clicked:
    st.session_state.length = 0
    st.session_state.width = 0
    st.session_state.area = 0
    st.session_state.perimeter = 0
elif calculate_clicked:
    st.session_state.length = length
    st.session_state.width = width
    st.session_state.area = st.session_state.length * st.session_state.width
    st.session_state.perimeter = 2 * (st.session_state.length + st.session_state.width)

# display session state, after interations
st.write(f'Length: {st.session_state.length}')
st.write(f'Width: {st.session_state.width}')
st.write(f'Area: {st.session_state.area}')
st.write(f'Perimeter: {st.session_state.perimeter}')
