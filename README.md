# Kenya-Travel-and-Hospitality-Assistant

# How to run?

### STEPS:

Clone the repository

```bash
Project repo: https://github.com/WambuaMalcolm/Medical-Chatbot-Generative-AI.git
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n travelbot python=3.10 -y
```

```bash
conda activate travelbot
```

### STEP 02- install the requirements

```bash
pip install -r requirements.txt
```

### Create a `.env` file in the root directory and add your Pinecone & groq credentials as follows:

```ini
ZILLIZ_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

```bash
# run the following command
uvicorn app:app --reload
```

Now,

```bash
open up localhost:
```

### Techstack Used:

- Python
- LangChain
- FastAPI
- Groq
- Pinecone

- used intfloat/multilingual-e5-base model
