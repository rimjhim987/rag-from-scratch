from langchain_community.document_loaders import CSVLoader #csvloader is used to load csv files

loader = CSVLoader(file_path='sample.csv')

docs = loader.load()

print(docs[0].page_content)         