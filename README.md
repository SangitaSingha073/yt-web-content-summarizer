# LLM Content Summarizer

An LLM-powered web application that generates concise summaries from **YouTube videos** and **website URLs** using **LangChain** and **Groq LLaMA-3.1**, with an interactive **Streamlit** interface.

---

##  Features

- Summarizes content from **YouTube videos** and **web pages**
- Uses **Large Language Models (LLaMA-3.1 via Groq)** for high-quality summaries
- Supports **multi-source content ingestion** using LangChain document loaders
- Implements **prompt engineering** for context-aware summarization
- Interactive and user-friendly **Streamlit UI**
- Secure **API key handling** and **URL validation**

---

##  Architecture Overview

1. User provides a **YouTube or website URL**
2. Application detects the content source
3. Appropriate **document loader** extracts text
4. Extracted content is passed through a **LangChain document chain**
5. **Groq LLaMA-3.1** generates a concise, context-aware summary
6. Summary is displayed in real time via Streamlit

---

##  Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/SangitaSingha073/yt-web-content-summarizer.git
cd yt-web-content-summarizer
```
### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate 
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash 
streamlit run app.py
```
## Prerequisites

1. Python 3.10
2. Groq API Key. Enter the API key securely in the Streamlit sidebar when prompted . 


