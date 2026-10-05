from langchain_community.document_loaders import PyPDFLoader #pypdfloader is used to load pdf files
"""Page 1
 ├── text
 ├── images
 └── formatting

Page 2
 ├── text
 └── tables

Page 3
 └── text"""

loader = PyPDFLoader('sample.pdf')

docs = loader.load()

print(type(docs))
print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)