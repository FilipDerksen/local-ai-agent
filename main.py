from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever
from config import LLM_MODEL, QUIT_COMMAND, PROMPT_TEMPLATE

model = OllamaLLM(model=LLM_MODEL)

prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
chain = prompt | model

while True:
    print("\n\n-------------------------------")
    question = input(f"Ask your question ({QUIT_COMMAND} to quit): ")
    print("\n\n")
    if question == QUIT_COMMAND:
        break

    reviews = retriever.invoke(question)
    result = chain.invoke({"reviews": reviews, "question": question})
    print(result)
