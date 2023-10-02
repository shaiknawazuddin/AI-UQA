import streamlit as st
import pandas as pd
import openai
from docx import Document
import zipfile
import os
import time
from io import BytesIO




st.set_page_config(
    page_title = "Home",
    page_icon = ":kaaba:"
)

st.markdown("""
<style>
.st-emotion-cache-6q9sum.ef3psqc3
{
            visibility: hidden;
}
</style>
""", unsafe_allow_html = True)

st.markdown("""
<style>
.st-emotion-cache-cio0dv.ea3mdgi1
{
            visibility: hidden;
}
</style>
""", unsafe_allow_html = True)

st.markdown("""
<style>
.st-emotion-cache-ch5dnh.ef3psqc4
{
            visibility: hidden;
}
</style>
""", unsafe_allow_html = True)

st.title("Assalam Alaikum!")
st.write('Welcome to Story Generator, a place for kids to learn from hadiths and incorporate right values in their lives in a way best suitable for them :sparkles:')
