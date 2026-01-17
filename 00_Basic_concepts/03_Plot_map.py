import streamlit as st
import pandas as pd
import numpy as np

latitude = 33.622296625414464
longitude = 35.41153828939856
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [latitude, longitude],
    columns=['lat', 'lon'],
)

st.map(map_data)