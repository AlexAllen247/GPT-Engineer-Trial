from typing import List
from langchain.embeddings import Embeddings
from pdfminer.high_level import extract_text

class PDFDocument:
    def __init__(self, path: str):
        self.path = path
        self.text = ""
        self.embeddings = None

    def load(self):
        self.text = extract_text(self.path)
        self.embeddings = Embeddings.from_text(self.text)

    def get_sentences(self) -> List[str]:
        return self.text.split(".")