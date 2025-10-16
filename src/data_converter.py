import pandas as pd
from langchain_core.documents import Document 

class DataConverter:
    def __init__(self, file:str):
        self.file = file
    
    def convert_to_docs(self):
        df = pd.read_csv(self.file)[['product_title', 'review']]

        docs= [
            Document(page_content=row['review'], metadata ={'product_name': row['product_title']} )
            for _,row in df.iterrows()

        ]
        return docs
    

    