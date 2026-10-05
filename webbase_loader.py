from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text \n {text}',
    input_variables=['question', 'text'],
)

parser = StrOutputParser()

url = "https://www.amazon.in/s?k=anarkali+suit&crid=F6QXJWZ9NT2U&sprefix=anak%2Caps%2C251&ref=nb_sb_ss_mvt-t11-ranker_1_4"

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

print(chain.invoke({
    'question': 'what is the best price for the products?',
    'text': docs[0].page_content
}))