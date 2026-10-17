import streamlit as st
st.title("🤖Ai ASSITANCE FOR STUDENTS")
st.write("Student Career Mentor")
question = st.chat_input("Ask you academic related question ?")
if question:
    with st.chat_message("User"):
        st.write(question)