import streamlit as st
import time

@st.fragment
def silahkan_masuk():
    st.button("silahkan masuk", help="Fragment rerun")
    st.balloons()

with st.spinner("Inflating balloons..."):
    time.sleep(5)
silahkan_masuk()
st.button("silahkan pulang", help="Full rerun")

st.iframe(
    '''
    <style>body { font-family: sans-serif; padding: 1rem; }</style>
    <p>This is <strong>kalau tidakmua masuk pulang saja karana web ini tidak ada pintunya</strong>.</p>
    ''',
    height=100,
)
