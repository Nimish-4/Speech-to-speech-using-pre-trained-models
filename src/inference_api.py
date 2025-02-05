from huggingface_hub import InferenceClient
import os

API_TOKEN = os.getenv("API_TOKEN_2")


def query_response(query):

    client = InferenceClient(
        token=API_TOKEN,
    )
    messages = [{"role": "user", "content": query}]
    completion = client.chat.completions.create(messages=messages, max_tokens=500)
    return completion.choices[0].message.content
