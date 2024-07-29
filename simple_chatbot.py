import nltk
from nltk.chat.util import Chat, reflections
import re


pairs = [
    (r'Hi|Hello|Hey', ['Hello! How can I assist you today?', 'Hi there! How can I help?']),
    (r'What is your name?', ['I am a chatbot created by OpenAI.', 'I don’t have a name, but you can call me Chatbot.']),
    (r'How are you?', ['I am doing well, thank you!', 'I am just a computer program, but I am here to help you.']),
    (r'What can you do?', ['I can help answer questions and have a conversation with you.',
                           'I am here to chat and assist with your queries.']),
    (r'Bye|Goodbye', ['Goodbye! Have a great day!', 'See you later!']),
    (r'(.*) your (.*)', ['Why do you want to know about my %2?', 'I don’t really have a %2.']),
    (r'(.*) help (.*)', ['Sure, I can help with that. What do you need assistance with?',
                         'I am here to help. Could you please provide more details?']),
    (r'(.*) name (.*)',
     ['My name is Chatbot. What can I do for you?', 'I don’t have a personal name, but you can call me Chatbot.']),
    (r'What time is it?', ['Sorry, I don’t have access to the current time.']),
    (r'Can you (.*) math?', ['Yes, I can do some basic math. Just ask me a question like "What is 5 plus 3?"']),
    (r'What is (\d+) plus (\d+)', lambda m: f'The result is {int(m.group(1)) + int(m.group(2))}.'),
    (r'What is (\d+) minus (\d+)', lambda m: f'The result is {int(m.group(1)) - int(m.group(2))}.'),
    (r'What is (\d+) multiplied by (\d+)', lambda m: f'The result is {int(m.group(1)) * int(m.group(2))}.'),
    (r'What is (\d+) divided by (\d+)', lambda m: f'The result is {int(m.group(1)) / int(m.group(2)):.2f}.'),
    (r'How is the weather (.*)',
     ['I don’t have real-time weather information, but you can check a weather website or app.']),
    (r'(.*) joke', ['Why did the scarecrow win an award? Because he was outstanding in his field!',
                    'Why don’t scientists trust atoms? Because they make up everything!']),
    (r'What is your favorite color?', ['I don’t have a favorite color, but I think blue is nice!',
                                       'Colors are fascinating! I don’t have preferences, though.']),
    (r'Can you tell me a fact?', [
        'Did you know honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old!']),
    (r'What are you doing?',
     ['I am here to chat with you! How can I assist you today?', 'I’m just waiting for your questions.']),
    (r'(.*)',
     ['I’m not sure how to respond to that.', 'Can you please clarify?', 'That’s interesting! Can you tell me more?'])
]


chatbot = Chat(pairs, reflections)


def chat():
    print("Hello! I am a chatbot. Type 'Bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'goodbye']:
            print("Chatbot: Goodbye! Have a great day!")
            break


        print(f"User input: {user_input}")

        response = chatbot.respond(user_input)


        if response:
            print(f"Chatbot: {response}")
        else:
            print("Chatbot: I'm not sure how to respond to that. Can you please provide more details?")


if __name__ == "__main__":
    chat()
