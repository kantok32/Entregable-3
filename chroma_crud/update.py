def update_document(collection, document_id, new_embedding, new_metadata):
    collection.update(embedding=new_embedding, ids=[document_id], metadatas=[new_metadata])
    print(f"Documento {document_id} actualizado correctamente.")
