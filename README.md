[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# Knowledge Base Search Engine

A **Retrieval-Augmented Generation (RAG) application** that allows users to upload PDF documents and interact with an AI assistant that provides accurate, context-aware answers based on the document content.  

This project is ideal for students, researchers, or professionals who want to **quickly query large sets of documents** without manually reading through them. It handles uploads and queries, use vector database for embeddings, and a **Streamlit frontend** for an interactive user interface.



## Demo

link

## Features

- 📄 Upload and parse PDFs  
- 🧠 Embed document chunks with **Generative AI embeddings**  
- 💂️ Store embeddings in **Pinecone vector database**  
- 💬 Query documents using **LLM + RAG**  
- 🌍 Microservice architecture (Streamlit client)



## How RAG Works

**Retrieval-Augmented Generation (RAG)** enhances LLMs by injecting external knowledge.  
Instead of relying solely on pre-trained data, the model retrieves relevant information from a vector database (like Pinecone) and uses it to generate accurate, context-aware responses.


## Application Diagram
<img width="1320" height="521" alt="image" src="https://github.com/user-attachments/assets/b6d8de40-2b81-4d4c-b475-b1e1ba81263f" />


## Folder Structure

```bash

├── client/
│   ├── app.py
│   ├── requirements.txt
│
├── server/
│   ├── faiss_index/
│   ├── main.py
│   ├── requirements.txt
│   ├── .env
│   └── utils/
│       ├── pdf_processor.py
│       ├── vector_store.py
│       └── qa_chain.py
├── .gitignore
├── LICENSE
└── README.md

```

## Getting started it locally

### 1. Clone the Repository
```bash
git clone https://github.com/sahith-sys/Knowledge_Base_Search_Engine_by_Unthinkable.git
```
### 2. Create the environment
```bash
python -m venv venv
```
### 3. Activate the environment
```bash
#windows
venv\Scripts\activate

# For macOS/Linux
source venv/bin/activate
```
### 4. Install requirements
```bash
#Frontend
cd client
pip install -r requirements.txt

#Backend
cd server
pip install -r requirements.txt
```
### 5. Run the app
```bash
#Frontend
cd client
streamlit run app.py

#Backend Fastapi
cd server
uvicorn main:app --reload
```

# Environmental variables
GOOGLE_API_KEY="your_gemini_api_key_here"


## Todo

- Add authentication for endpoints
- Dockerize the project
- Add support for more file types


## Credits

- Streamlit
- Langchain
- eraser.io

## License
This project is licensed under the [MIT License](LICENSE).
