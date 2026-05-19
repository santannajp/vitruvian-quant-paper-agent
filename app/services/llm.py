from openai import OpenAI

client = OpenAI()

def ask_llm(prompt: str):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content":prompt
            }
        ]
    )
    
    return response.choices[0].message.content