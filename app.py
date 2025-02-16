import streamlit as st
import pandas as pd
import numpy as np


st.title("Student Score Tracker")
st.write("Add student scores and filter by minimum score.")
st.header("Add Student Data")

if "data" not in st.session_state:
    st.session_state.data = [] 

name=st.text_input("Enter your name (surname first):")
score=st.number_input("Enter your score (0-100):", min_value=0, max_value=100)

st.write("Verify details before submitting")
if st.button("Add Student"):
    if name:
        st.session_state.data.append({"Name": name, "Score": score})
        st.session_state.data = st.session_state.data

student_df = pd.DataFrame(st.session_state.data)

if not student_df.empty:
    st.write("Students' Data:")
    st.dataframe(student_df)

if not student_df.empty:
    st.header("Filter by Minimum Score")
    min_score = st.slider("Minimum Score", value=50, min_value=0, max_value=100)
    filtered_student_df = student_df[student_df["Score"] >= min_score]

    st.write("Students that meet the cut-off mark by scoring >=", (min_score))
    st.dataframe(filtered_student_df)