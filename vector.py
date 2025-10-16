from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd
from config import (
    EMBEDDING_MODEL, DB_LOCATION, COLLECTION_NAME, RETRIEVAL_COUNT,
    CSV_FILE, TITLE_COLUMN, REVIEW_COLUMN, RATING_COLUMN, DATE_COLUMN
)

df = pd.read_csv(CSV_FILE)
embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)

db_location = DB_LOCATION

add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []

    for i, row in df.iterrows():
        document = Document(
            page_content=row[TITLE_COLUMN] + " " + row[REVIEW_COLUMN],
            metadata={"rating": row[RATING_COLUMN], "date": row[DATE_COLUMN]},
            id = str(i)
        )
        ids.append(str(i))
        documents.append(document)

vector_store = Chroma(
    collection_name = COLLECTION_NAME,
    persist_directory = db_location,
    embedding_function = embeddings,
)

if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)

retriever = vector_store.as_retriever(
    search_kwargs = {"k": RETRIEVAL_COUNT}
)