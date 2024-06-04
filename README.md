**Building Vector Databases with FastAPI and ChromaDB**

**Requirements:-**
1) Langchain
2) Chromadb
3) FastAPI
   
**Steps:-**
1) Setting up FastAPI
2) Build an API using FastAPI
3) Flow of the Project:-
   a) Chunking the PDF Document using Langchain.
   b) Generating word embeddings for the chunks using an open-source embedding model.
   c) Uploading word embeddings to the vector database.
   d) Fetching the nearest neighbouring chunks to the user query using similarity search.
   e) Deleting the database.
   f) Create endpoints for the functions in FastAPI.
