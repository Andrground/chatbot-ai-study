from langchain_community.document_loaders import WebBaseLoader

# Load sites
loader = WebBaseLoader('https://asimov.academy')
document_list = loader.load()
document = ''

for doc in document_list:
    document = document + doc.page_content