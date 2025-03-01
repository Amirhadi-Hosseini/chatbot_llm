import streamlit as st


if 'key' not in st.session_state:
    st.session_state['key'] = 'value'
    #st.session_state['counter'] = 0

def form_callback():
    st.write(st.session_state.my_slider)
    st.write(st.session_state.my_checkbox)
    #st.write(st.session_state.Counter)
    
with st.form(key='my_from'):
    #st.session_state['counter'] = +1  
    slider_input = st.slider('my slider', 0, 10, 5, key='my_slider')
    checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
    submit_button = st.form_submit_button(label='submit', on_click=form_callback)
    