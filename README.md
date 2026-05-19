# vitruvian-quant-paper-agent

# Resumo do Projeto

Este é um agente que ler artigos científicos em pdf e resume o conteúdo em linguagem natural.

# Como Rodar

    uv venv
    source .venv/bin/activate
    uv add fastapi pydantic-settings pymupdf

# Testar parser

    uv run python -m tests.test_parser

# O que falta fazer

1. melhorar o parser para ler tabelas e gráficos
2. implementar o chunking inteligente
3. implementar o embedding e salvar no qdrant
4. criar uma api para upload de pdfs
5. criar um sistema de busca semantica
6. testar o sistema e colocar em prod

# Estrutura do projeto

    app/
        main.py
        core/
            config.py
        parsers/
            pdf_parser.py
        services/
            pdf_service.py
        models/
            pdf.py
        schemas/
            pdf.py
        utils/
            pdf_utils.py
    storage/
        pdfs/
    tests/
        test_pdf_parser.py

# Stack

- FastAPI
- Pydantic-settings
- PyMuPDF

