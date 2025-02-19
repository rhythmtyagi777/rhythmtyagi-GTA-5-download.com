#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hp
#
# Created:     18-02-2025
# Copyright:   (c) hp 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import streamlit as st

st.title ("Treasure of gifts")

st.header ("download gta 5")
st.subheader ("Contact")
st.markdown ("Thankyou for visiting us")
st.code ("""
               https://uploadhaven.com/download/a18aa8bae9f365b292936128eba7dc34
          """)
st.code ("""
               www.youtube.com
          """)

import streamlit as st
import pandas as pd

name2 = st.text_input("Enter your name: ")
fname = st.text_input("Enter your father name : ")
adr = st.text_area("Enter your address : ")
classdata1 = st.selectbox("Enter your class :",(1,2,3,4,5,6,7,8))

button = st.button("DONE")
if button :
   st.markdown(f"""
   name  :            {name2}
   father name :      {fname}
   address :          {adr}
   class :            {classdata1}""")