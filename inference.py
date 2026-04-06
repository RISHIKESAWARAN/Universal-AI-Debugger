from huggingface_hub import InferenceClient
import os

def run_inference(code):
    client = InferenceClient(token=os.getenv("HF_TOKEN"))
    messages = [
        {"role": "system", "content": "Debug and fix the following code."},
        {"role": "user", "content": code}
    ]
    response = client.chat_completion(
        model="meta-llama/Meta-Llama-3-8B-Instruct",
        messages=messages,
        max_tokens=500
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    # Test call
    print(run_inference("print(1/0)"))
