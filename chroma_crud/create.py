def insert_document(collection, document_id, embedding, metadata):
    collection.add(embedding=embedding, ids=[document_id], metadatas=[metadata])
    print(f"Documento {document_id} insertado correctamente.")
