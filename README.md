# 🌍 Kenya Travel & Hospitality Assistant

An AI-powered chatbot designed to assist users with travel and hospitality information in Kenya.  
Built with **LangChain**, **FastAPI**, **Groq**, and **Pinecone** for intelligent search and retrieval.

# How to run?

### 1. Clone the repository

```bash
Project repo: https://github.com/WambuaMalcolm/Medical-Chatbot-Generative-AI.git
```

### 2. Create a conda environment after opening the repository

```bash
conda create -n travelbot python=3.10 -y
```

```bash
conda activate travelbot
```

### 3. install the requirements

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory and add your Pinecone & groq credentials as follows:

```ini
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### 5. Run the App
```bash
uvicorn app:app --reload
```

Then open your browser and go to:

```bash
http://127.0.0.1:8000
```

### Techstack Used:

- Python
- LangChain
- FastAPI
- Groq
- Pinecone
- used intfloat/multilingual-e5-base embedding model
