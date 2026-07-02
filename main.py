import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI
from config import *

def client_setup():
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if not api_key:
        raise RuntimeError("No OpenRouter API Key Found")

    client = OpenAI(
        base_url=BASE_URL,
        api_key=api_key,
    )

    model = MODEL

    return client, model

def get_completion(client, messages, model):
    return client.chat.completions.create(model=model, messages=messages)

def user_input():
    parser = argparse.ArgumentParser(description="AI Agent")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    messages=[
        {
            "role": "user",
            "content": args.user_prompt,
        }
    ]
    return messages

def verify_completion(completion):
    if not completion:
        return RuntimeError("Completion == None")
    return True

def completion_printer(completion, messages):
    print(f"User Prompt: {messages[0]["content"]}")
    print(f"Prompt tokens: {completion.usage.prompt_tokens}")
    print(f"Response tokens: {completion.usage.completion_tokens}")
    print("Response:")
    print(completion.choices[0].message.content)

def main():
    client, model = client_setup()
    messages = user_input()
    completion = get_completion(client, messages, model)

    if verify_completion(completion):
        completion_printer(completion, messages)
    else:
        print("Failed to generate completion.")

main()