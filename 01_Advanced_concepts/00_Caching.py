import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("Caching")

# st.cache for expensive computation
@st.cache_data
def load_large_dataset(rows = 1000):
    """Simulate loading large dataset"""
    st.write("Loading large dataset... (This only runs when the cache is empty)")
    time.sleep(2) # simulate slow loading
    data = pd.DataFrame(
        {
            "id": range(rows),
            "value": np.random.randn(rows),
            "category": np.random.choice(['A', 'B', 'C'], rows),
        }
    )
    return data

# Application
st.header("Large dataset loading with Caching")
if st.button("Load Dataset"):
    data = load_large_dataset(5000)
    st.write(f"Loaded {len(data)} rows")
    st.dataframe(data.head())

st.header("Clear Cache")
if st.button("CLEAR"):
    st.cache_data.clear()
    st.success("Cache cleared")
