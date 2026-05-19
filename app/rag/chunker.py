# fazendo uum chunk inteligente dos artigos: não devo cortar por tokens aleatórios, mas sim por sessions, como abstract, intro, methods, results, etc"
# estratégia: regex por headers cientificos e depois juntar os pedacos por proximidade de texto

import pydantic_settings
import re

SECTIONS = [
    "Abstract",
    "Introduction",
    "Related Work",
    "Methodology",
    "Experiments",
    "Results",
    "Discussion",
    "Conclusion",
    "References",
    "Appendix",
]

def chunk_sections(text:str):
    chunks = []

    for section in SECTIONS:
        pattern = rf"{section}(.*?)(?=\n[A-Z])"

        match = re.search(pattern, text, re.I | re.S)

        if match:
            chunks.append({
                "section": section,
                "content": match.group(1)
            })

    return chunks