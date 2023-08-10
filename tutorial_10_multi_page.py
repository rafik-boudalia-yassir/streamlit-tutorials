
import streamlit as st

def page_one():
    st.title("Page One")
    st.write("This is the first page.")

def page_two():
    st.title("Page Two")
    st.write("This is the second page.")

def main():
    st.sidebar.title("Navigation")
    selected_page = st.sidebar.radio("Go to", ["Page One", "Page Two"])

    if selected_page == "Page One":
        page_one()
    else:
        page_two()

if __name__ == '__main__':
    main()
