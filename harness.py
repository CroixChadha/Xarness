# harness.py: Croix's real harness (chat-loop feature)
# Spec: docs/xstack/features/chat-loop/leaf-tasks/ask-model.md

import os
from dotenv import load_dotenv
from openai import OpenAI
from openai import APIConnectionError
import sys


def load_config():
    #load the model name and base url
    load_dotenv()
    base_url = os.getenv("LLM_BASE_URL")
    model_name = os.getenv("LLM_MODEL")
    #error handling if the env is empty
    if not base_url:
        sys.exit("You are missing the LLM_BASE_URL, please fix it")
    elif not model_name:
        sys.exit("You are missing the LLM_MODEL, please fix it")

    client = OpenAI(
        base_url= base_url,
        api_key="this is not a real key"
    
    )
    return client, model_name


def ask_model(client, model_name, messages):
    responses = client.chat.completions.create(model=model_name, messages=messages)
    return responses.choices[0].message.content

if __name__ == "__main__":
    client, model_name = load_config()
    messages = [{"role": "user", "content": "This is a test message, what is the capital of France?"}]
    try:
        print(ask_model(client=client, model_name=model_name, messages=messages))
    except APIConnectionError:
        sys.exit("Model server unreachable, please check the env.")
    
    
