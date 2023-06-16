import openai
from langchain.embeddings import Embeddings

class Chatbot:
    def __init__(self):
        openai.api_key = "YOUR_API_KEY_HERE"
        self.model_engine = "text-davinci-002"
        self.max_tokens = 1024

    def generate_response(self, user_input: str, document_embeddings: Embeddings) -> str:
        prompt = f"{user_input} [SEP] {document_embeddings.to_string()}"
        response = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=self.max_tokens,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text.strip()