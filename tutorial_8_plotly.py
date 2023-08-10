
import streamlit as st
import numpy as np
import plotly.express as px

def main():
    st.title("Interactive Plotting with Plotly")

    # Generate data
    x = np.arange(100)
    y = np.sin(x)

    fig = px.line(x=x, y=y, title="Sin Wave")
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()
