import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
st.title("this is my first app")
# add user input 
number = st.slider("Select a range of values", 0, 100, (25, 75))
# print number 
st.write("The selected range is", number)
# adding a button
if st.button("Submit"):
    st.write("You clicked the button!")
else:
    st.write("You did not click the button.")
 # add radio button with options 
option = st.radio("Select an option", ("Option 1", "Option 2", "Option 3"))
# print option 
st.write("You selected", option)
