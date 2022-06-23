
import streamlit as st
import numpy as np
import pandas as pd
import time

st.markdown("### ADD TWO NUMBER")
text_input1=st.number_input('Enter first number:')
text_input2=st.number_input('Enter second number:')

if(st.button("ADD")):
    result = ((text_input1)+(text_input2))
    st.success(result)



