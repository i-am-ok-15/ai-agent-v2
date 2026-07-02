import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if not api_key:
    raise RuntimeError("No OpenRouter API Key Found")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

model = "openrouter/free"
messages=[
    {
        "role": "user",
        "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
    }
]

completion = client.chat.completions.create(model=model, messages=messages)

def verify_completion(completion):
    if not completion:
        return RuntimeError("Completion == None")
    return True

def completion_printer(completion):
    print(f"User Prompt: {messages[0]["content"]}")
    print(f"Prompt tokens: {completion.usage.prompt_tokens}")
    print(f"Response tokens: {completion.usage.completion_tokens}")
    print("Response:")
    print(completion.choices[0].message.content)

def main():
    if verify_completion(completion):
        completion_printer(completion)

    else:
        print("Failed to generate completion.")

main()