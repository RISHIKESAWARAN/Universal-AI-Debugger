from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from huggingface_hub import InferenceClient
import os

app = FastAPI()

# HF Token fetch from Secrets
HF_TOKEN = os.getenv("HF_TOKEN")

# Client-ah model name illama initialize pannuvom to avoid provider conflicts
client = InferenceClient(token=HF_TOKEN)

html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Rishi's AI Debugger</title>
    <style>
        body { font-family: sans-serif; background: #121212; color: white; padding: 20px; text-align: center; }
        textarea { width: 90%; height: 200px; background: #1e1e1e; color: #00ff00; border: 1px solid #333; padding: 10px; font-family: monospace; border-radius: 8px; }
        button { background: #6200ee; color: white; border: none; padding: 12px 25px; cursor: pointer; margin-top: 15px; font-size: 16px; border-radius: 5px; font-weight: bold; }
        button:hover { background: #7722ff; }
        #result { background: #222; padding: 15px; margin-top: 20px; text-align: left; white-space: pre-wrap; border-left: 5px solid #6200ee; border-radius: 4px; min-height: 50px; }
    </style>
</head>
<body>
    <h1>🚀 Universal AI Code Debugger</h1>
    <p>Paste any code (Python, Java, SQL, etc.) below to fix it instantly!</p>
    <textarea id="code-input" placeholder="Paste your buggy code here..."></textarea><br>
    <button onclick="debugCode()">Debug Now</button>
    <div id="result">Waiting for code...</div>
    <script>
        async function debugCode() {
            const codeInput = document.getElementById('code-input').value;
            const resDiv = document.getElementById('result');
            if (!codeInput.trim()) {
                resDiv.innerText = "Please paste some code first!";
                return;
            }
            resDiv.innerText = "⏳ AI is analyzing your code...";
            try {
                const response = await fetch("/", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ user_code: codeInput })
                });
                const data = await response.json();
                resDiv.innerText = data.debug_report || data.message;
            } catch (e) {
                resDiv.innerText = "❌ Error connecting to AI: " + e;
            }
        }
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def get_home():
    return html_content

@app.post("/")
async def post_debug(request: Request):
    try:
        data = await request.json()
        user_code = data.get("user_code", "")
        
        # Novita-ku pudicha "Conversational" format (Chat Completion)
        messages = [
            {"role": "system", "content": "You are an expert programmer. Debug and fix the following code."},
            {"role": "user", "content": f"Debug this code:\n{user_code}"}
        ]
        
        # Calling chat_completion directly on the model
        response = client.chat_completion(
            model="meta-llama/Meta-Llama-3-8B-Instruct",
            messages=messages,
            max_tokens=1000
        )
        
        return {"debug_report": response.choices[0].message.content}
    except Exception as e:
        return {"message": f"Server Error: {str(e)}"}
