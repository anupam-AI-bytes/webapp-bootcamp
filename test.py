import streamlit as st

st.title("❤️ For Someone Special")

st.write("Welcome to Anupam's first deployed app!")

name = st.text_input("Enter your name")

if name:
    st.write(f"Hello {name}! 😊")

if st.button("Click Me"):
    st.balloons()
    st.success("You make my life better every day ❤️")