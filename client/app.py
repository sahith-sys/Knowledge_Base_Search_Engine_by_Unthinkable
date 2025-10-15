import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config("Knowledge Base RAG App")
st.title("Knowledge Base Search Engine")

with st.sidebar:
    st.header("Upload PDF files")
    uploaded_files = st.file_uploader("Select PDFs", accept_multiple_files=True, type=["pdf"])
    if st.button("Process PDFs"):
        if uploaded_files:
            files = [("files", (f.name, f.getvalue(), "application/pdf")) for f in uploaded_files]
            res = requests.post(f"{BACKEND_URL}/upload_pdfs/", files=files)
            st.success(res.json()["message"])
        else:
            st.warning("Please upload PDFs first.")

question = st.text_input("Ask a question:")
if st.button("Submit"):
    if question:
        res = requests.post(f"{BACKEND_URL}/ask/", data={"question": question})
        try:
            st.write("**Answer:**", res.json().get("answer", "No answer key found"))
        except Exception as e:
            st.error(f"Failed to parse JSON. Error: {e}")

