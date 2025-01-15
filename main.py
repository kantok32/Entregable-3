from chromadb.client import Client
from chromadb.config import Settings
from chroma_crud.create import insert_document
from chroma_crud.read import read_document
from chroma_crud.update import update_document
from chroma_crud.delete import delete_document

# Configuración de la base de datos
settings = Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="./chroma_db"
)
client = Client(settings)

# Crear colección
collection = client.create_collection(name="my_collection")

# Insertar un documento
insert_document(collection, "doc_1", [0.1, 0.2, 0.3], {"title": "Mi documento", "author": "Usuario"})

# Leer un documento
read_document(collection, "doc_1")

# Actualizar un documento
update_document(collection, "doc_1", [0.2, 0.3, 0.4], {"title": "Documento actualizado", "author": "Usuario"})

# Eliminar un documento
delete_document(collection, "doc_1")
