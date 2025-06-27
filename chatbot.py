import chat_personal
import load_websites

from langchain.prompts import ChatPromptTemplate

messages = []

def bot_answer(messages):
    # Define comportament of this chat
    model_messages = [
        ('system', 'You are a assistant that always answers with jokes'),
        ('system', 'You can get info for this documents if necessary: {websites_documents}')
    ]

    # concat the user messages with comportament
    model_messages += messages

    # Create a template
    template = ChatPromptTemplate.from_messages(model_messages)

    # Create a chat with template
    chain = template | chat_personal.chat

    # Execute without specified the params because the template already has the messages of user
    answer = chain.invoke({'websites_documents': load_websites.document})

    return answer.content


while True:
    user_question = input('User: ')
    if user_question.lower() == 'x':
        break

    messages.append(('user', user_question))
    new_answer = bot_answer(messages)
    messages.append(('assistant', new_answer))
    print(f'Bot: {new_answer}')

print('Thank you for using this bot')
    


