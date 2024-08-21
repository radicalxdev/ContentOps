import streamlit as st
from tools.components.documents_manager import DocumentProcessor
from tools.components.base import Canvas
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


st.title(f"Probe Generator")
st.subheader(f"This tool helps you generate probes for your journeys.")
canvas = Canvas.from_components({
    'PDFs': DocumentProcessor
})

canvas.render('PDFs')