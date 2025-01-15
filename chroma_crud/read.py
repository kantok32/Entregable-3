def read_document(collection, document_id):
    result = collection.get(ids=[document_id])
    print(f"Documento {document_id} leído correctamente: {result}")
