from transformers import AutoTokenizer, AutoModel

def generate_embedding(text):
    tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
    model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
    tokens = tokenizer(text, return_tensors="pt")
    embedding = model(**tokens).last_hidden_state.mean(dim=1)
    return embedding.detach().numpy().tolist()
