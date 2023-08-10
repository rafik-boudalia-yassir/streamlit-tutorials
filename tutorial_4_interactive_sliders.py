
import streamlit as st
import numpy as np

def main():
    st.title("Interactive Slider Example")
    
    # Slider
    n_points = st.slider("Number of Points", 10, 100, 50)
    x = np.arange(n_points)
    y = np.random.randn(n_points)
    
    st.line_chart(y)
    
if __name__ == '__main__':
    main()
