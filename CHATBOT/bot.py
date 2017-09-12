
# parte do chatbot
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

# speech recognition
import speech_recognition as sr

# speech syntesis
import pyttsx3

bot = ChatBot('Black') # inicia bot

chats = ['hi', 'oi', 'hello', 'how are you?', 'I''m fine.', 'Thanks.'] # conversas

bot.set_trainer(ListTrainer) # Define o metodo de treinamento
bot.train(chats) # define a lista de conversas

while True:
    request = input('Enter text: ')
    print(bot.get_response(request))
