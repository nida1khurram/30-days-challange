import streamlit as st
from utils.pdf_processor import process_pdf

def main():
    st.title("Study Notes Summarizer & Quiz Generator Agent")

    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        if st.button("Process PDF"):
            with st.spinner("Processing PDF..."):
                extracted_text = process_pdf(uploaded_file)
                st.text_area("Extracted Text", extracted_text, height=300)

if __name__ == "__main__":
    main()