import streamlit as st
import pandas as pd
import numpy as np

x = st.slider('x') # this is a widget a slider
st.write(x, "squared is: ", x**2)

st.text_input("Your name", key = "name")
st.session_state.name

if st.checkbox("Show me some data"):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'],
    )

    chart_data

df = pd.DataFrame(
    {
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    }
)

option =  st.selectbox(
    "Which number do you like best?",
    df["first column"]
)

st.write("You selected: ", option)