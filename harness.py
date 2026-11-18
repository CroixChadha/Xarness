# harness.py: Croix's real harness (chat-loop feature)
# Spec: docs/xstack/features/chat-loop/leaf-tasks/ask-model.md

import os
from dotenv import load_dotenv
from openai import OpenAI
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


# TODO(xstack): def ask_model(...): takes the client, the model name and the messages list
def ask_model(client, model_name):
    responses = client.chat.completions.create
    return responses
# TODO(xstack):   send them with client.chat.completions.create
# TODO(xstack):   return just the reply text (no printing in here)


# TODO(xstack): temporary run block: if __name__ == "__main__":
# TODO(xstack):   get the client and model name from load_config()
# TODO(xstack):   build a messages list with one hard-coded user message
# TODO(xstack):   call ask_model() and print what it returns
