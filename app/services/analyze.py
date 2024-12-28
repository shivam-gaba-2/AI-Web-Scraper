from transformers import pipeline

extractor = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

class Analyze:
    def __init__(self, content: str):
        self.content = content

    def analyze_data(self, question: str):
        data = extractor(question=question, context=self.content)
        return data['answer']
