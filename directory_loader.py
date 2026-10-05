#DirectoryLoader is a document loader that loads documents from a directory. 
# It can load documents from a single directory or recursively from subdirectories. 
# It supports various file types and can be customized to include or exclude certain files based on their extensions.

from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader 
#DirectoryLoader is used to load documents from a directory

loader = DirectoryLoader(
    'docs', 
    glob='**/*.pdf', 
    loader_cls=PyPDFLoader
    )
docs = loader.load()

# print(type(docs))
# print(len(docs))
# print(docs[0].page_content)

#lazy loading of documents from a directory using DirectoryLoader.
# lazy loading is a technique where the documents are loaded only when they are needed,
#  rather than loading all the documents at once. This can be useful when dealing with 
# large directories or when you want to save memory.

docs = loader.lazy_load()
for document in docs:
    print(document.page_content)
    print(document.metadata)