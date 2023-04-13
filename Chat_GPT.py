import os
import playsound
import speech_recognition as sr
import time
from gtts import gTTS
import openai
import random
# Text - to - speech: Khai báo hàm chuyén doi van bán thanh giong nói


def speak(text):
    print("GPT: {}".format(text))
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3", True)
    os.remove("sound.mp3")

# Speech - to - text: Khai báo hàm chuyén doi giong nói thanh van bán


def get_text():
    print("GPT: Dang nghe...")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #print("Tôi: ", end='')
        audio = r.listen(source, phrase_time_limit=5)
        try:
            text = r.recognize_google(audio, language="en-En")
            print(text)
            return text.lower
        except:
            #print("Dang nghe...")
            return 0


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
    speak("Hello, Iam Chatgpt")
    question = get_again()
    while True:
        try:
            openai.api_key = "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"
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
                "Hello", "Hi", "Wapsup"
            ]))
        question = get_again()
        if "Good bye" in question or "Welcome" in question:
            speak("See you agian!!")
        time.sleep(1)
        break


chat_gpt()
