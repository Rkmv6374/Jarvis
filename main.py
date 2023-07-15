import os.path
import pyttsx3
import speech_recognition as sr
import webbrowser as wb
from bardapi import Bard
from bardapi import ChatBard
import wikipedia
from chatbot import Chat , register_call


chatstr = ""
token = 'Yghp8PCw-e9WYFOxEK5xtvq0an7s-4ycukgMWnH0FJMn7W_j4-27tfbmZXP9GAdSPDx1eQ.'


def say ( text ):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# def ask(text):
#     global chatstr,token
#     print("Processing... through chat with Jarvis.....")
#     say("Thankyou sir for asking me!")
#     chatstr += f'Aman: {text}\n Jarvis:'
#     response = Bard(token=token).get_answer(f'{text}')['content']
#     # response = ChatBard(token).start(text)
#     say(response)
#     chatstr += response
#     # say(response)
#     print(response)
#     return response

# @register_call("whoIs")
def ask(query):
    try:
        ChatBard
        say(wikipedia.summary(query))
    except wikipedia.exceptions.DisambiguationError as e:
        # If there are multiple options, return the summary of the first option
        say(wikipedia.summary(e.options[0]))
    except Exception:
        say(f"I don't know about {query}")
#
# def ask(first_question):
#     chatbot = Chat()
#     # print(f"user :{first_question}")
#     response = chatbot.converse(first_question)
#     # print("Chatbot:", response)
#     # print(first_question)
#     say(response)



def ai(prompt):
    global token
    text =""
    response = Bard(token=token).get_answer(f'{prompt}')['content']
    text += f'Acoording to Jarvis!/n{response}'
    say("your text will be saved in a file !")
    if not os.path.exists("BardAI"):
        os.mkdir("BardAI")
    with open(f'BardAI/{"".join(prompt.split("using")[1:]).strip()}.txt','w') as f:
        f.write(text)


def takeCommand ():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("speak from microphone")
        r.pause_threshold = 0.8
        r.adjust_for_ambient_noise(source, duration=5)
        # r.recognizer_instance.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
        # print(audio)
        try:
            print("recognizing ....")
            query = r.recognize_google(audio, language="en-in" )
            print(f'Aman:{query}')
            return query
        except Exception as e:
            return "something went wrong! sorry from Jarvis"



if  __name__ == "__main__":
    # text = str(input("Enter the text"))
    say("hi, I am Jarvis!")
    End_Conversation = True
    while End_Conversation:

        cmdtaken = False
        print("listening")
        query = takeCommand()
        # say(query)
        sites = [
            ["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
            ["google", "https://www.google.com"]]

        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say(f"sir, i am opening {site[0]} for you")
                wb.open(site[1])
                cmdtaken = True

        #  ending the conversation or stoping the jarvis to be continued!!!
        endStatement = ["end", "exit", "stop"]

        for q in query.lower().split(" "):
            if cmdtaken == True: break
            if q in endStatement:
                say(f"okay sir i am {q} conversation")
                End_Conversation = False

        # todo : openai assistance

        cmd = ["using artifical" , "using ai" ,"using a.i", "using internet"]


        for text in cmd:
            if text.lower() in  query.lower():
                ai(query)
                cmdtaken = True



        if (cmdtaken ==  False) :
            say("Thank you, Sir for choosing me to talk!")
            ask(query)
        # todo:chat assistance



