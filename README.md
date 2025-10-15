[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# Knowledge Base Search Engine

A **Retrieval-Augmented Generation (RAG) application** that allows users to upload PDF documents and interact with an AI assistant that provides accurate, context-aware answers based on the document content.  

This project is ideal for students, researchers, or professionals who want to **quickly query large sets of documents** without manually reading through them. It handles uploads and queries, use vector database for embeddings, and a **Streamlit frontend** for an interactive user interface.



## Demo

link

## Features

- Upload and parse PDFs  
- Embed document chunks with **Generative AI embeddings**  
- Store embeddings in ** vector database**  
- Query documents using **LLM + RAG**  
- Microservice architecture (Streamlit client + FastAPI server)



## How RAG Works

**Retrieval-Augmented Generation (RAG)** enhances LLMs by injecting external knowledge.  
Instead of relying solely on pre-trained data, the model retrieves relevant information from a vector database (like Pinecone) and uses it to generate accurate, context-aware responses.


## Application Diagram
<img width="1600" height="554" alt="image" src="https://github.com/user-attachments/assets/19fb65e8-e1f4-486e-9810-e72608d20b1f" />


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

## Tech Stack

| Layer       | Technology / Tool                       | Purpose                                      |
|------------|----------------------------------------|---------------------------------------------|
| Frontend    | Streamlit                               | UI for PDF upload and query submission      |
| Backend     | FastAPI                                 | API endpoints for document ingestion & query handling |
| Vector Store| FAISS / ChromaDB                        | Store embeddings for retrieval              |
| Embeddings  | HuggingFace (`all-MiniLM-L6-v2`)       | Convert document chunks into vector embeddings |
| LLM         | Google Generative AI (`gemini-2.5-flash`) | Generate context-aware answers             |
| PDF Parsing | PyPDF2                                  | Extract text from uploaded PDFs             |
| Environment | Python 3.12, venv                       | Dependency management                        |
| Others      | dotenv                                   | Manage API keys and environment variables   |

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

## API Endpoints

| Method | Endpoint        | Description                      | Payload                                 |
|--------|----------------|----------------------------------|----------------------------------------|
| POST   | `/upload_pdfs/` | Upload PDFs and build vectorstore | `files: List[UploadFile]`              |
| POST   | `/ask/`         | Ask a question and get an answer | `{"question": "your question here"}`  |
| GET    | `/health/`      | Check server health              | None                                   |


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
