# 🚀 Universal AI Code Debugger (Meta-Llama-3 Powered)

### 🌟 Project Overview
The **Universal AI Code Debugger** is a lightweight, web-based tool designed to help developers (especially those using mobile devices) debug and optimize their code instantly. It uses the state-of-the-art **Meta-Llama-3-8B-Instruct** model to provide professional-grade code reviews and error fixes.

---

### 📱 Why I Built This? (The Inspiration)
As a 23-year-old software engineering student, I realized that many aspiring developers in India start their journey on **mobile phones** due to a lack of high-end laptops. Debugging complex logic on a small screen is a massive hurdle. This project bridges that gap by providing a high-end AI mentor accessible through any smartphone browser.

---

### ✨ Key Features
* **Deep Logic Analysis:** Identifies hidden bugs like `ZeroDivisionError`, `Index Out of Range`, and `Type Conflicts`.
* **Multi-Language Support:** Debugs Python, Java, SQL, C++, and more.
* **Mobile-First UI:** Responsive design optimized for rapid code input on mobile keyboards.
* **Professional Explanations:** Doesn't just fix the code; it explains *why* the error occurred to help the user learn.

---

### 🛠️ Technical Stack
* **AI Model:** Meta-Llama-3-8B-Instruct (via Hugging Face Inference API)
* **Backend:** FastAPI (Python)
* **Frontend:** HTML5, CSS3, JavaScript
* **Deployment:** Hugging Face Spaces (Streamlit/FastAPI SDK)

---

### 🚀 How to Run Locally
1. Clone the repo:
   `git clone https://github.com/Rishi9216/Universal-AI-Debugger`
2. Install requirements:
   `pip install -r requirements.txt`
3. Set your `HF_TOKEN` in environment variables.
4. Run the app:
   `uvicorn app:app --reload`
