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
    height=100,)
DataFrame(
    {
        "widgets": [
            "st.selectbox",
            "st.number_input",
            "st.text_area",
            "st.button",
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "widgets": st.column_config.Column(
            "Streamlit Widgets",
            help="Streamlit **widget** commands 🎈",
            width="medium",
            required=True,
        )
    },
    hide_index=True,
    num_rows="dynamic",
)
