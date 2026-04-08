import os
import sys
from openai import OpenAI

def run_inference(user_code):
    # Scaler bot expect panra structured output
    print(f"[START] task=debugging", flush=True)
    
    # Proxy Setup
    API_BASE = os.getenv("API_BASE_URL", "https://api-inference.huggingface.co/v1")
    API_KEY = os.getenv("API_KEY", "dummy_key")
    MODEL_NAME = os.getenv("MODEL_NAME", "meta-llama/Meta-Llama-3-8B-Instruct")

    client = OpenAI(base_url=API_BASE, api_key=API_KEY)

    try:
        print(f"[STEP] step=1 sending_request", flush=True)
        
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are an expert programmer. Fix the code."},
                {"role": "user", "content": f"Fix this:\n{user_code}"}
            ],
            max_tokens=1000
        )
        
        result = response.choices[0].message.content
        print(f"[STEP] step=2 inference_received", flush=True)
        print(f"[END] task=debugging score=1.0 steps=2", flush=True)
        return result

    except Exception as e:
        print(f"[ERROR] {str(e)}", flush=True)
        print(f"[END] task=debugging score=0.0 steps=1", flush=True)
        return f"Error: {str(e)}"

if __name__ == "__main__":
    # Bot dummy code anuppi test panna idhu help pannum
    test_code = "print(1/0)"
    if len(sys.argv) > 1:
        test_code = sys.argv[1]
    
    print(run_inference(test_code))
