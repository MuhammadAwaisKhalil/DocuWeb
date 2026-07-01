import PyPDF2
from typing import List

def chunk_text(text: str, chunk_size: int = 2000, overlap: int = 200)-> List[str]:
    start = 0
    end = 0
    text_length = len(text)
    chunks = []
    if text_length <=chunk_size:
        return [text]
    
    #Gets chunks of text while preserving context using a sliding window so that sentences are not cut off without context
    while start<text_length:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks

def get_text_from_pdf(filename: str)-> str:
    text = ""
    try:
        with open(filename, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + '\n'
            return text
    except Exception as e:
        print('Error in reading pdf')
        return ""

def get_chunks(filename: str, chunk_size: int=2000, overlap: int = 200)-> List[str]:
    #First get the entire text from pdf
    text = get_text_from_pdf(filename)
    if not text.strip():
        print('No text extracted from PDF')
        return []

    #Convert text to chunks
    chunks = chunk_text(text)

    return chunks
    

