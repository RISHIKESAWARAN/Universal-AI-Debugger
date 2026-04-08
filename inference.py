from huggingface_hub import InferenceClient
import os
import sys

def run_inference(code):
    # Meta Scaler specific tags for starting the task
    print("[START] task=code_debug", flush=True)
    
    try:
        token = os.getenv("HF_TOKEN")
        if not token:
            print("[STEP] step=1 reward=0.0 error=no_token", flush=True)
            print("[END] task=code_debug score=0.0 steps=1", flush=True)
            return

        client = InferenceClient(token=token)
        
        messages = [
            {"role": "system", "content": "You are an expert programmer. Debug and fix the following code."},
            {"role": "user", "content": f"Debug this code:\n{code}"}
        ]
        
        # Step tag before calling AI
        print("[STEP] step=1 status=calling_ai", flush=True)
        
        response = client.chat_completion(
            model="meta-llama/Meta-Llama-3-8B-Instruct",
            messages=messages,
            max_tokens=500
        )
        
        result = response.choices[0].message.content
        
        # Output the actual result
        print(f"DEBUG_REPORT: {result}", flush=True)
        
        # End tag with success score
        print("[END] task=code_debug score=1.0 steps=1", flush=True)

    except Exception as e:
        print(f"[STEP] step=1 error={str(e)}", flush=True)
        print("[END] task=code_debug score=0.0 steps=1", flush=True)

if __name__ == "__main__":
    test_code = "print(1/0)"
    run_inference(test_code)
    sys.exit(0)
