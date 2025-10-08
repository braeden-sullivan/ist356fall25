'''## Challenge 3-2-3

### Excel to JSON 

Write a streamlit accept an Excel file via file uploader and then writes out a record-oriented JSON file from the first tab in the excel file.

The program should display the contents of the dataframe and provide a download button for the converted the csv file. 


Advice:

 - https://docs.streamlit.io/develop/api-reference/widgets/st.file_uploader
 - https://docs.streamlit.io/develop/api-reference/widgets/st.download_button'''

import pandas as pd
import streamlit as st

st.title("Excel to JSON Converter")
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])
if uploaded_file:
    # Read the first sheet of the uploaded Excel file
    df = pd.read_excel(uploaded_file, sheet_name=0)
    
    # Display the dataframe
    st.write("Dataframe Preview:")
    st.dataframe(df)
    
    # Convert dataframe to JSON
    json_data = df.to_json(orient='records', lines=True)
    
    # Provide a download button for the JSON file
    st.download_button(
        label="Download JSON",
        data=json_data,
        file_name='data.json',
        mime='application/json'
    )
else:
    st.info("Please upload an Excel file to convert it to JSON.")