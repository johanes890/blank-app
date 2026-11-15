import streamlit as st
import time

@st.fragment
def silahkan_masuk():
    st.button("silahkan masuk", help="Fragment rerun")
    st.balloons()

with st.spinner("Inflating balloons..."):
    time.sleep(5)
silahkan masuk()
st.button("silahkan pulang", help="Full rerun")
