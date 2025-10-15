from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse
from utils.pdf_processor import extract_text_from_pdfs
from utils.vector_store import build_vector_store, query_vector_store
from utils.qa_chain import get_qa_chain
import traceback

app = FastAPI()

@app.post("/upload_pdfs/")
async def upload_pdfs(files: list[UploadFile]):
    pdfs = [await f.read() for f in files]
    text = extract_text_from_pdfs(pdfs)
    build_vector_store(text)
    return {"message": "PDFs processed and vector store created."}

@app.post("/ask/")
async def ask_question(question: str = Form(...)):
    try:
        docs = query_vector_store(question)
        chain = get_qa_chain()
        response = chain(
            {"input_documents": docs, "question": question},
            return_only_outputs=True
        )
        return {"answer": response.get("output_text", "No output found")}
    except Exception as e:
        # Print full stacktrace to terminal for debugging
        traceback.print_exc()
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )
