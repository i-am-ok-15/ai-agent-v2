import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI
from config import BASE_URL, MODEL

def client_setup():
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if not api_key:
        raise RuntimeError("No OpenRouter API Key Found")

    client = OpenAI(
        base_url=BASE_URL,
        api_key=api_key,
    )

    return client

def get_completion(client, messages, model):
    return client.chat.completions.create(model=model, messages=messages)

def user_input():
    parser = argparse.ArgumentParser(description="AI Agent")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    return args.user_prompt

def verify_completion(completion):
    if completion.usage is None:
        raise RuntimeError("Incorrect API response")
    return True

def completion_printer(prompt, completion, messages):
    print(f"User Prompt: {prompt}")
    print(f"Prompt tokens: {completion.usage.prompt_tokens}")
    print(f"Response tokens: {completion.usage.completion_tokens}")
    print("Response:")
    print(completion.choices[0].message.content)

def main():
    client = client_setup()
    prompt = user_input()

    messages = [
        {
            "role": "user",
            "content": prompt,
        }
    ]

    completion = get_completion(client, messages, MODEL)

    verify_completion(completion)
    completion_printer(prompt, completion, messages)

if __name__ == "__main__":
    main()