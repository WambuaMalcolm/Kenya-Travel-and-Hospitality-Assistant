from langchain.chains import create_retrieval_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate
from .prompt import qa_prompt, condense_prompt
from .helper import load_index, load_llm, load_embeddings

embeddings=load_embeddings()
vectorstore = load_index(embeddings=embeddings)
llm = load_llm()



#    IMPORTANT: Always begin with "query: " for E5 models.



retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
history_aware_retriever = create_history_aware_retriever(
    llm,
    retriever,
    prompt=condense_prompt
)

qa_chain = create_stuff_documents_chain(
    llm, qa_prompt
)

rag_chain = create_retrieval_chain(
    history_aware_retriever, qa_chain
)

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

def ask_bot(q: str):
    hist = memory.load_memory_variables({})["chat_history"]
    resp = rag_chain.invoke({"input": q, "chat_history": hist})
    memory.save_context({"input": q}, {"output": resp["answer"]})
    return resp["answer"]

