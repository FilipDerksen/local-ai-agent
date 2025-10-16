"""
Configuration file for Local AI Agent
Contains all configurable settings with default values
"""

# Model Configuration
LLM_MODEL = "llama3.2:1b"
EMBEDDING_MODEL = "mxbai-embed-large"

# Vector Database Configuration
DB_LOCATION = "./chrome_langchain_db"
COLLECTION_NAME = "restaurant_reviews"
RETRIEVAL_COUNT = 5

# Data Configuration
CSV_FILE = "realistic_restaurant_reviews.csv"
TITLE_COLUMN = "Title"
REVIEW_COLUMN = "Review"
RATING_COLUMN = "Rating"
DATE_COLUMN = "Date"

# Application Configuration
QUIT_COMMAND = "q"
PROMPT_TEMPLATE = """
You are an expert in answering questions about a pizza restaurant.

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}

"""

