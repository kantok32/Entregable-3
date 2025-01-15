def delete_document(collection, document_id):
    collection.delete(ids=[document_id])
    print(f"Documento {document_id} eliminado correctamente.")
