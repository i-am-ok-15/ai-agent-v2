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

def parse_args():
    parser = argparse.ArgumentParser(description="AI Agent")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="enable verbose output")
    args = parser.parse_args()

    return args

def verify_completion(completion):
    if completion.usage is None:
        raise RuntimeError("Incorrect API response")

def simple_printer(completion):
    print("Response:")
    print(completion.choices[0].message.content)

def make_verbose_printer(base_printer, completion, prompt):
    def enhanced_printer():
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {completion.usage.prompt_tokens}")
        print(f"Response tokens: {completion.usage.completion_tokens}")
        base_printer(completion)
    return enhanced_printer

def main():
    client = client_setup()
    args = parse_args()
    prompt = args.user_prompt
    verbose = args.verbose

    messages = [
        {
            "role": "user",
            "content": prompt,
        }
    ]

    completion = get_completion(client, messages, MODEL)
    verify_completion(completion)

    if verbose:
        verbose_printer = make_verbose_printer(simple_printer, completion, prompt)
        verbose_printer()
    else:
        simple_printer(completion)

if __name__ == "__main__":
    main()