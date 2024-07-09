import streamlit as st
import requests

st.title("Protein Design Optimization")
sequence_input = st.text_area("Input Protein Sequence")
if st.button("Optimize"):
    response = requests.post("http://127.0.0.1:5000/optimize", json={'sequence': sequence_input})    
    optimized_sequence = response.json()['optimized_sequence']
    st.text_area("Optimized Protein Sequence", optimized_sequence)