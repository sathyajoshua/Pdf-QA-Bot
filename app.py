import streamlit as st
from utils import (
    extract_documents_from_pdf,
    split_documents,
    create_faiss_index,
    ask_question
)

st.set_page_config(
    page_title="PDF Q&A Bot",
    page_icon="📄",
    layout="centered"
)

st.title("📄 PDF → Q&A Bot")
st.caption("Ask questions directly from your PDF using AI")

# --- Session state ---
if "pdf_processed" not in st.session_state:
    st.session_state.pdf_processed = False

# --- Upload PDF ---
uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])

if uploaded_file and not st.session_state.pdf_processed:
    with st.spinner("Processing PDF..."):
        text = extract_documents_from_pdf(uploaded_file)
        chunks = split_documents(text)
        create_faiss_index(chunks)

    st.session_state.pdf_processed = True
    st.success("PDF processed successfully. You can now ask questions.")

# --- Question input ---
if st.session_state.pdf_processed:
    question = st.text_input("Ask a question from the document")

    if question:
        with st.spinner("Thinking..."):
            answer, sources = ask_question(question)

        st.subheader("Answer")
        st.write(answer)
        st.caption(f"Sources: Pages {', '.join(map(str, sources))}")
