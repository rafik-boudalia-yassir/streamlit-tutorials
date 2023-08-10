
import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.title("Data Filtering with Sidebar")

    # Create a dataframe
    df = pd.DataFrame({
        'A': np.random.randn(100),
        'B': np.random.randint(1, 5, 100)
    })

    # Sidebar
    min_val = st.sidebar.slider("Minimum value of A", float(df["A"].min()), float(df["A"].max()), float(df["A"].min()))
    max_val = st.sidebar.slider("Maximum value of A", float(df["A"].min()), float(df["A"].max()), float(df["A"].max()))

    # Filter the dataframe
    filtered_df = df[(df["A"] >= min_val) & (df["A"] <= max_val)]
    st.write(filtered_df)

if __name__ == '__main__':
    main()
