import os
import streamlit as st
from lesson_plan import Lesson_Plan


os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]


page = Lesson_Plan


with st.container():
    page.app()

st.divider()

