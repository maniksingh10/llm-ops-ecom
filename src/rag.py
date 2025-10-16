from langchain_groq import ChatGroq
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory

from config.config import Config

class ChainBuilder:
    def __init__(self,vs) -> None:
        self.vs = vs 
        self.llm = ChatGroq(model=Config.LLM_MODEL, temperature=0.5)
        self.history_dict = {}

    
    def _get_history(self, s_id:str) -> BaseChatMessageHistory:
        if s_id not in self.history_dict:
            self.history_dict[s_id] = ChatMessageHistory()
        
        return self.history_dict[s_id]

    def build_chain(self):
        retriver = self.vs.as_retriever(search_kwargs={"k":3})

        context_prompt = ChatPromptTemplate.from_messages([
            ("system", "Given the chat history and user question, rewrite it as a standalone question."),
            MessagesPlaceholder(variable_name="chat_history"), 
            ("human", "{input}")  
        ])

        qa_prompt = ChatPromptTemplate.from_messages([
            ("system", """You're an e-commerce bot answering product-related queries using reviews and titles.
                          Stick to context. Be concise and helpful.\n\nCONTEXT:\n{context}\n\nQUESTION: {input}"""),
            MessagesPlaceholder(variable_name="chat_history"), 
            ("human", "{input}")  
        ])

        history_retriever = create_history_aware_retriever(
            self.llm, retriver, context_prompt
        )

        qa_chain = create_stuff_documents_chain(
            self.llm, qa_prompt
        )

        rag_chain = create_retrieval_chain(
            history_retriever, qa_chain
        )


        return RunnableWithMessageHistory(
            rag_chain,
            self._get_history,
            input_messages_key="input",
            history_messages_key="chat_history",
            output_messages_key="answer"
        )