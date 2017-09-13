
# parte do chatbot
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

# speech recognition
import speech_recognition as sr

# speech syntesis
import pyttsx3

bot = ChatBot('Black') # inicia bot

speak = pyttsx3('sapi5')

chats = ['hi', 'oi', 'hello', 'how are you?', 'I''m fine.', 'Thanks.'] # conversas

bot.set_trainer(ListTrainer) # Define o metodo de treinamento
bot.train(chats) # define a lista de conversas

r = sr.Recognizer()

with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s) # se adaptar ao ruido

    while True:
        print("Say something: ")
        audio = r.listen(s) # escutar
        speech = r.recognize_google(audio) # falar

        print(bot.get_response(speech))
