import streamlit as st

prompt = st.chat_input('please enter ypur request:')
if prompt:
    st.write('you start to communication')