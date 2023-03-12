
import streamlit as st
import openai
import os
from streamlit.components.v1 import html

import csv


st.set_page_config(page_title="Text improvement")

    openai.api_key = os.getenv('OPENAI_KEY')
html_temp = """
                <div style="background-color:{#f3fadc};padding:1px">
                
                </div>
                """
  openai.api_key = os.getenv('OPENAI_KEY')
  
with st.sidebar:

  
    st.markdown("""
    # :)
    chart gpt please correct grammatical and spelling mistakes, suggest improvement tips and add more keywords for more efficient search indexing: 
    """)
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
   
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    ,
    unsafe_allow_html=True,
    )


input_text = None
if 'output' not in st.session_state:
    st.session_state['output'] = 0

if st.session_state['output'] <=2:
    st.markdown("""
    # Text
    """)
   
input_text = st.text_area(label="Enter full text:", value="", height=250)

st.button(
      "Submit",
      on_click=summarize,
      kwargs={"prompt": input_text},
  )
  output_text = st.text_area(label="Summarized text:", value=st.session_state["summary"], height=250)

  
def summarize(prompt):
    augmented_prompt = f"chart gpt please correct grammatical and spelling mistakes, suggest improvement tips and add more keywords for more efficient search indexing: {prompt}"
    try:
        st.session_state["summary"] = openai.Completion.create(
            engine="text-davinci-003",
            prompt=augmented_prompt,
            temperature=.5,
            max_tokens=2000,
        )["choices"][0]["text"]
    except:
        st.write('There was an error =(')


