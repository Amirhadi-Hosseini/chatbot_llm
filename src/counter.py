import streamlit as st


if 'counter' not in st.session_state:
    st.session_state.counter = 0
    
if st.button('Increament'):
    st.session_state.counter += 1
    st.write(f'counter : {st.session_state.counter}')
    

if st.button('Reset'):
    st.session_state.counter = 0
    st.write(f'counter : {st.session_state.counter}')