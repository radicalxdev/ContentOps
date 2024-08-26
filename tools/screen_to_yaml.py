import os
import streamlit as st
from tools.components.features.screen_to_yaml.core import *

if not os.getenv('OPENAI_API_KEY'):
    st.warning(f"No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")

st.title("Screen to YAML")
st.subheader("This tool helps you convert text to YAML.")

with st.form("my_form", clear_on_submit=True):
    text = st.text_area("Enter your text here")
    submit = st.form_submit_button("Submit")

with st.container(border=True):
    if submit:
        st.write("Your text has been converted to YAML.")   
        output_yaml_stream = TeeIterator(generate_yaml(text))
        st.write_stream(output_yaml_stream.get_tee())
        output_yaml = ''.join(output_yaml_stream)
        st.write("Summary of the YAML:")
        summary = generate_summary(output_yaml)
        st.write_stream(summary)