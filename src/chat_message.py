import streamlit as st
import numpy as np


with st.chat_message("ai"):
    st.write("Hello :wave:")
    st.line_chart(np.random.randn(30, 3))
    
    
    

message = st.chat_message("User")
message.write("hello human")
message.bar_chart(np.random.randn(30, 3))