import os
import playsound
import speech_recognition as sr
import time
from gtts import gTTS
import openai
import random
import datetime

# Get the current date and time
now = datetime.datetime.now()

# Format the date and time as a string
date_string = now.strftime('%Y-%m-%d_%H-%M-%S')

# Text - to - speak


def speak(text):
    print("GPT: {}".format(text))
    write_log(text)
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3", True)
    os.remove("sound.mp3")

# Speech - to - text:


def get_text():
    print("GPT: Listening...")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, phrase_time_limit=5)
        try:
            text = r.recognize_google(audio, language="ev-En")
            write_log(text)
            print(text)
            return text.lower()
        except:
            return 0


def write_log(text):

    # Construct the filename using the date and time
    filename = f"my_file_{date_string}.txt"

    # Open the file for writing
    with open(filename, 'a') as f:
        # Write to the file
        f.write(text)
        f.write('\n')


def get_again():
    for i in range(5):
        text = get_text()
        if text:
            return text.lower()
        elif i < 4:
            time.sleep(0)
    time.sleep(0)
    speak("Good bye")
    return 0

# ChatGPT


def chat_gpt():
    speak("Hello, May I help you?")
    question = get_again()
    while True:
        try:
            openai.api_key = ""
            model_engine = "text-davinci-003"
            completions = openai.Completion.create(
                engine=model_engine,
                prompt=question,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            contents = completions.choices[0].text
            speak("Anser" + contents)
            time.sleep(1)
        except:
            time.sleep(2)
            speak(random.choice([
                "Sorry I can get it.Can you say it again",
                "I dont get it, Please repeat again!",
                "What you say, again please"
            ]))
        question = get_again()
        if "goodbye" in question or "welcome" in question:
            speak("See you again!!")
            time.sleep(1)
            break


chat_gpt()
