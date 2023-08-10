
import streamlit as st
import time

@st.cache
def expensive_computation():
    time.sleep(5)  # simulate a long-running computation
    return 42

def main():
    st.title("Caching in Streamlit")

    result = expensive_computation()
    st.write(f"Result of the expensive computation: {result}")

if __name__ == '__main__':
    main()
