# Document Analytics Assistant

An interactive document analysis application built with Python and Streamlit that allows users to upload documents and interact with their content through context-aware question answering.

## Overview

The Document Analytics Assistant processes uploaded documents, extracts and splits their content, generates embeddings, and uses vector-based retrieval to provide relevant context for user queries.

The project demonstrates practical implementation of document processing, semantic search, vector databases, and interactive application development using Python.

## Key Features

- Upload and process documents
- Extract and preprocess document text
- Split documents into manageable text chunks
- Generate document embeddings
- Perform semantic similarity search
- Retrieve relevant document context
- Ask questions about uploaded documents
- Interactive Streamlit-based user interface

## Technology Stack

- Python
- Streamlit
- LangChain
- FAISS
- Document Processing
- Semantic Search
- Git
- GitHub

## Project Structure

```text
document-analytics-assistant/
├── app.py
├── requirements.txt
├── utils/
│   ├── chatbot.py
│   ├── embeddings.py
│   ├── memory.py
│   ├── pdf_reader.py
│   └── text_splitter.py
└── vector_db/
