
import streamlit as st
import pandas as pd

def main():
    st.title("Display DataFrames")
    
    # Create a dataframe
    df = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8]
    })
    
    st.write(df)
    
if __name__ == '__main__':
    main()
