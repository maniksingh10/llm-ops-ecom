from langchain_astradb import AstraDBVectorStore
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from src.data_converter import DataConverter
from config.config import Config

class DataIngestor:
    def __init__(self):
        self.embeds = HuggingFaceEndpointEmbeddings(model=Config.EMBEDDING_MODEL)
        self.vs = AstraDBVectorStore(
            embedding= self.embeds,
            collection_name= "ecom_vs_db",
            api_endpoint=Config.ASTRA_DB_API_ENDPOINT,
            token=Config.ASTRA_DB_APPLICATION_TOKEN,
            namespace=Config.ASTRA_DB_KEYSPACE
        )


    def get_vs(self, load_exist = True):
        
        if load_exist:
            return self.vs
        
        docs = DataConverter("data/raw.csv").convert_to_docs()

        self.vs.add_documents(docs)

        return self.vs
