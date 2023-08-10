import streamlit as st
import numpy as np

def main():
    st.title("Simple Line Chart")
    
    # Generate random data
    x = np.arange(10)
    y = np.random.randn(10)
    
    st.line_chart(y)
    
if __name__ == '__main__':
    main()
