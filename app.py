import streamlit as st

from utils.pdf_reader import extract_text
from utils.text_splitter import split_text
from utils.embeddings import create_vector_store
from utils.chatbot import ask_question

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="AI PDF Chatbot",
    page_icon="📄",
    layout="wide"
)

# ---------------------------
# Session State
# ---------------------------
if "processed" not in st.session_state:
    st.session_state.processed = False

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------
# Sidebar
# ---------------------------
with st.sidebar:

    st.header("📄 Upload PDF")

    uploaded_files = st.file_uploader(
        "Choose one or more PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if st.button("Process PDFs"):

        if uploaded_files:

            with st.spinner("Reading PDF files..."):

                raw_text = extract_text(uploaded_files)

                chunks = split_text(raw_text)

                create_vector_store(chunks)

            st.session_state.processed = True

            st.success("✅ PDFs processed successfully!")

        else:
            st.warning("Please upload at least one PDF.")

    st.markdown("---")

    if st.button("Clear Chat"):

        st.session_state.messages = []

        st.rerun()

# ---------------------------
# Main Title
# ---------------------------
st.title("🤖 AI PDF Chatbot")

st.write("Upload PDF documents and ask questions about them.")

st.markdown("---")

# ---------------------------
# Chat Section
# ---------------------------
if st.session_state.processed:

    # Display old messages
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    question = st.chat_input("Ask a question...")

    if question:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        with st.spinner("Thinking..."):

            try:
                answer = ask_question(question)

            except Exception as e:
                answer = f"Error: {str(e)}"

        with st.chat_message("assistant"):
            st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

else:

    st.info("👈 Upload PDF files and click **Process PDFs** to begin.")

    st.markdown("""
### Features

- 📄 Upload multiple PDF files
- 🤖 AI Question Answering
- 💬 Chat Interface
- 🔍 Semantic Search
- ⚡ Fast Retrieval using FAISS
- 🧠 OpenAI GPT
""")
# ---------------------------
# Footer
# ---------------------------
st.markdown("---")

st.markdown(
    """
    <style>
        .footer {
            text-align: center;
            color: #808080;
            font-size: 16px;
            padding: 15px;
        }
        .footer span {
            color: #00C853;
            font-weight: bold;
        }
    </style>

    <div class="footer">
        🤖 <b>AI PDF Chatbot</b><br><br>
        Made with ❤️ by <span>AM</span><br>
        © 2026 All Rights Reserved
    </div>
    """,
    unsafe_allow_html=True
)    