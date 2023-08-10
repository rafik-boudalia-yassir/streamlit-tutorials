
import streamlit as st
import numpy as np
import pandas as pd

def main():
    st.title("Map Visualization")
    
    # Generate random latitude and longitude
    n = 1000
    df = pd.DataFrame({
        'lat': np.random.randn(n) + 37.76,  # centered around San Francisco
        'lon': np.random.randn(n) - 122.4
    })
    
    st.map(df)
    
if __name__ == '__main__':
    main()
