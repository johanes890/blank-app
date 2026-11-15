import streamlit as st
import time

@st.fragment
def silahkan_masuk():
    st.button("silahkan_masuk", help="Fragment rerun")
    st.balloons()

with st.spinner("Inflating balloons..."):
    time.sleep(5)
silahkan_masuk()
st.button("Inflate more balloons", help="Full rerun")
