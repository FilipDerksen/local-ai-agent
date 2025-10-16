# Local AI Agent

A local AI chatbot that answers questions about a pizza restaurant using customer reviews. Built with LangChain, Ollama, and vector embeddings - runs completely offline with no API costs.

## ✨ Features

- **100% Local AI** - No internet required, no API costs
- **RAG (Retrieval-Augmented Generation)** - Uses actual review data to answer questions
- **Interactive Chat Interface** - Ask questions in a conversational loop
- **Smart Review Retrieval** - Finds the most relevant reviews for each question
- **Vector Database** - Fast similarity search using Chroma
- **Local LLM** - Powered by Llama 3.2 1B model

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- [Ollama](https://ollama.ai/) installed and running
- Required Ollama models (see Setup section)

### Installation

1. **Clone or download this repository**
   ```bash
   git clone <your-repo-url>
   cd local-ai-agent
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   **Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Setup

1. **Install and start Ollama**
   - Download from [ollama.ai](https://ollama.ai/)
   - Start the Ollama service

2. **Pull required models**
   ```bash
   ollama pull llama3.2:1b
   ollama pull mxbai-embed-large
   ```

3. **Ensure you have the data file**
   - Make sure `realistic_restaurant_reviews.csv` is in the project directory
   - The vector database will be created automatically on first run

## 🎯 Usage

### Running the Application

```bash
python main.py
```

### Example Interaction

```
-------------------------------
Ask your question (q to quit): What do people say about the pizza?

The reviews show that people generally enjoy the pizza! Customers mention:
- "The pizza was delicious and fresh"
- "Great variety of toppings"
- "Crust was perfectly crispy"
- "Best pizza in town"

-------------------------------
Ask your question (q to quit): How is the service?

Based on the reviews, the service gets mixed feedback:
- Some customers praise the "friendly and fast service"
- Others mention "slow during busy hours"
- "Staff was helpful and attentive"

-------------------------------
Ask your question (q to quit): q
```

### Sample Questions to Try

- "What do people say about the pizza?"
- "How is the service?"
- "What are the most common complaints?"
- "What do customers like most?"
- "How is the atmosphere?"
- "What about the prices?"

## 🏗️ Architecture

### Components

- **`main.py`** - Main application with chat interface
- **`vector.py`** - Vector database setup and retrieval
- **`realistic_restaurant_reviews.csv`** - Sample restaurant review data
- **`requirements.txt`** - Python dependencies

### Tech Stack

- **LangChain** - AI framework for building applications
- **Ollama** - Local AI model hosting
- **Chroma** - Vector database for embeddings
- **Pandas** - Data processing
- **Llama 3.2 1B** - Local language model
- **mxbai-embed-large** - Embedding model

### How It Works

1. **Data Loading** - Loads restaurant reviews from CSV
2. **Embedding Creation** - Converts reviews to vector embeddings
3. **Vector Storage** - Stores embeddings in Chroma database
4. **Query Processing** - Converts user questions to embeddings
5. **Similarity Search** - Finds most relevant reviews (top 5)
6. **Context Generation** - Passes relevant reviews to LLM
7. **Answer Generation** - LLM generates answer based on context

## 📁 Project Structure

```
local-ai-agent/
├── main.py                          # Main application
├── vector.py                        # Vector database setup
├── config.py                        # Configuration settings
├── requirements.txt                 # Python dependencies
├── realistic_restaurant_reviews.csv  # Sample data
├── chrome_langchain_db/             # Vector database (auto-created)
└── README.md                        # This file
```

## 🔧 Configuration

### Model Settings

- **LLM Model**: `llama3.2:1b` (lightweight, fast)
- **Embedding Model**: `mxbai-embed-large` (high-quality embeddings)
- **Retrieval Count**: 5 most relevant reviews per question

### Customization

You can modify all settings in `config.py`:

```python
# Model Configuration
LLM_MODEL = "llama3.2:1b"                    # Change LLM model
EMBEDDING_MODEL = "mxbai-embed-large"         # Change embedding model

# Vector Database Configuration
RETRIEVAL_COUNT = 5                           # Number of reviews to retrieve

# Data Configuration
CSV_FILE = "realistic_restaurant_reviews.csv"  # Change data source
```

**Available Models:**
- **LLM Models**: `llama3.2:1b`, `llama3.2:3b`, `llama3.1:8b`, `llama3.1:70b`
- **Embedding Models**: `mxbai-embed-large`, `nomic-embed-text`, `all-minilm`

## 🐛 Troubleshooting

### Common Issues

1. **"Model not found" error**
   - Ensure Ollama is running: `ollama serve`
   - Pull required models: `ollama pull llama3.2:1b`

2. **"Chroma database" errors**
   - Delete the `chrome_langchain_db` folder and restart
   - The database will be recreated automatically

3. **Slow performance**
   - The first run is slower (building vector database)
   - Subsequent runs are much faster

4. **Memory issues**
   - Try a smaller model: `ollama pull llama3.2:1b`
   - Reduce retrieval count in `vector.py`

### Performance Tips

- **First run**: Takes longer to build vector database
- **Subsequent runs**: Much faster (database is cached)
- **Model size**: Llama 3.2 1B is optimized for speed
- **Retrieval**: Limited to 5 reviews for fast responses

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🔗 Links

- **Ollama**: https://ollama.ai/
- **LangChain**: https://python.langchain.com/
- **Chroma**: https://www.trychroma.com/

---

**Built with ❤️ for local AI experimentation**
