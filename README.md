# 🦜 LangChain Learning Project

A collection of Python scripts exploring LangChain's core features including chat models, embeddings, output parsers, and structured outputs.

---

## 📁 Project Structure

```
Langchain/
├── chatModels/
│   ├── chatmodel_google.py        # Google Gemini chat model
│   ├── chatmodel_groq.py          # Groq chat model
│   ├── chatmodel_hf_api.py        # HuggingFace API chat model
│   ├── chatmodel_ollama.py        # Ollama chat model
│   └── chatmodel_ollama_local.py  # Ollama local chat model
│
├── EmbeddedModels/
│   ├── document_similarity.py     # Document similarity using embeddings
│   ├── embedding_hf_docs.py       # HuggingFace document embeddings
│   ├── embedding_query.py         # Query embeddings
│   ├── mbedding_docs.py           # Document embeddings
│   └── mbedding_hf_local.py       # Local HuggingFace embeddings
│
├── LLMs/
│   └── llm_demo.py                # Basic LLM demo
│
├── Prompt/
│   ├── chatbot.py                 # Chatbot with prompt templates
│   ├── chat_history.txt           # Chat history logs
│   ├── message_placeholder.py     # Message placeholder usage
│   ├── messages.py                # Message types demo
│   ├── prompt_generator.py        # Dynamic prompt generation
│   ├── prompt_ui.py               # Prompt UI demo
│   └── template.json              # Prompt templates
│
├── langchain-output-parsers/
│   ├── json_parser.py             # JSON output parser
│   ├── pydantic_parser.py         # Pydantic output parser
│   └── string_parser.py           # String output parser
│
├── langchain-structured-output/
│   ├── json_schema.json           # JSON schema definition
│   ├── pydantic_demo.py           # Pydantic structured output
│   ├── typedDict.py               # TypedDict structured output
│   ├── with_structured_output_json.py      # Structured output with JSON
│   ├── with_structured_output_pydantic.py  # Structured output with Pydantic
│   └── with_sturctured_output_typeddict.py # Structured output with TypedDict
│
├── requirements.txt               # Project dependencies
└── test.py                        # Test scripts
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/anushsubba101/Langchain.git
cd Langchain
```

### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root directory:
```
OPENAI_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here
GROQ_API_KEY=your_key_here
HUGGINGFACEHUB_API_TOKEN=your_key_here
```

---

## 🛠️ Topics Covered

- ✅ Chat Models (Google, Groq, HuggingFace, Ollama)
- ✅ Embedding Models
- ✅ Prompt Templates
- ✅ Output Parsers (String, JSON, Pydantic)
- ✅ Structured Outputs (TypedDict, Pydantic, JSON Schema)

---

## 📦 Requirements

- Python 3.10+
- LangChain
- See `requirements.txt` for full list

---

## 👤 Author

**anushsubba101** — [GitHub](https://github.com/anushsubba101)
