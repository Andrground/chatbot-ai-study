import os


from langchain_groq import ChatGroq


os.environ['GROQ_API_KEY'] = ''


chat = ChatGroq(model='llama-3.3-70b-versatile')