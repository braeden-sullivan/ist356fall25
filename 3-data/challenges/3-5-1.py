'''## Challenge 3-5-1

https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv


Create a streamlit to allow the user to select one of the following:

- one of: Made_Own_Study_Guide, Did_Exam_Prep Assignment, Studied_In_Groups	
- after the selection is made display a dataframe that summarized the count of students and the average student score by the selection

'''

import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv"
    df = pd.read_csv(url)
    return df

df = load_data()
st.title("Exam Scores Analysis")
option = st.selectbox(
    'Select an activity:',
    ('Made_Own_Study_Guide', 'Did_Exam_Prep Assignment', 'Studied_In_Groups')
)
if option:
    summary_df = df.groupby(option).agg(
        Student_Count=('Student_ID', 'count'),
        Average_Score=('Score', 'mean')
    ).reset_index()
    st.write(f"Summary based on {option}:")
    st.dataframe(summary_df)
    st.bar_chart(summary_df.set_index(option)['Average_Score'])
