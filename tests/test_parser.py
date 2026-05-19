# testa o parser simples de app/persers/pdf_parser.py para extrair texto de um pdf

from app.parsers.pdf_parser import extract_text

text = extract_text("storage/papers/paper.pdf")


print(text[:5000])