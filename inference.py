from huggingface_hub import InferenceClient
import os
import sys

def run_inference(code):
    try:
        token = os.getenv("HF_TOKEN")
        if not token:
            return "Error: HF_TOKEN not found in environment variables."

        client = InferenceClient(token=token)
        
        messages = [
            {"role": "system", "content": "You are an expert programmer. Debug and fix the following code."},
            {"role": "user", "content": f"Debug this code:\n{code}"}
        ]
        
        response = client.chat_completion(
            model="meta-llama/Meta-Llama-3-8B-Instruct",
            messages=messages,
            max_tokens=500
        )
        return response.choices[0].message.content

    except Exception as e:

        return f"Inference Error: {str(e)}"

if __name__ == "__main__":
    test_code = "print(1/0)"
    try:
        result = run_inference(test_code)
        print(result)
        sys.exit(0)
    except:
        sys.exit(0)
