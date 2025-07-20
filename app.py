import streamlit as st
from wolfram import ask_wolframalpha

st.title("Wolfram Alpha Query App")
st.header("Ask a question to Wolfram Alpha")

user_question = st.text_input("Enter your question:")

if user_question:
    response = ask_wolframalpha(user_question)
    st.write("Answer:")
    st.write(response)
else:
    st.info("Please enter a question to get a response.")
