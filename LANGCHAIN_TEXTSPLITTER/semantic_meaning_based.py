from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text_splitter = SemanticChunker(
    OpenAIEmbeddings(),
    breakpoint_threshold_type = "standard_deviation",
    breakpoint_threshold_amount = 1
)

sample = """
Farmers work hard from early morning to late evening. They grow crops, take care of animals, and work in all kinds of weather. Their life is challenging, but their work is very important because they provide food for everyone. Farmers depend on nature, so rain, sunlight, and soil play an important role in their lives.

India is a diverse country known for its rich culture, traditions, and history.
It is home to many languages, religions, festivals, and beautiful landscapes.
The USA is a large and diverse country in North America.
It is known for its cultural diversity, technology, and innovation.
The country has many famous cities, landmarks, and national parks.
The USA has 50 states, each with its own unique character.
It plays an important role in the global economy and international affairs.
"""

docs = text_splitter.create_documents([sample ])

print(len(docs))
print(docs)