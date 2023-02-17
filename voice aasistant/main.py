import webbrowser
import speech_recognition as sr
import pyttsx3
import datetime
import pyjokes
import os
import time
#speech to text
def sptext():
    while True: 
        recognizer = sr.Recognizer() # object of class recognizer
        with sr.Microphone() as source:
            print("Listening....")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            try:
                print("recognizng........")
                data = recognizer.recognize_google(audio)
                print(data)
                return data
            except sr.UnknownValueError:
                print("Not UNderstood") 
#text to speech            
def  txspeech(x):
    engine = pyttsx3.init()   
    #we can take male as well as female voice by default we can use other voice also by downloading
    #we can also set volume and speed
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    #voices[0] means male voicee voices[1] means female voice
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150) 
    engine.say(x)
    engine.runAndWait()  


#txspeech("helloooooooooooooooooooooo i am hot and cute")
if __name__ == '__main__':
    
    
    if sptext()== "hey babe":
       print("test") 
       txspeech("Welcome darling to zarax")
       while True:
                data1=sptext()
                ``
                if "your name" in data1:
                    name = "my name is zarrax"
                    txspeech(name)
                elif "your age" in data1:
                    age = "my age is 20"
                    txspeech(age)
                elif "studying" in data1:
                    study = "i am studying IT engineering"
                    txspeech(study)
                
                elif 'time' in data1:
                    time = datetime.datetime.now().strftime("%I%M%p")
                    #strftime to search  %I%M%p for hour min and am or pm
                    txspeech(time)
                    
                elif 'YouTube' in data1:
                    webbrowser.open("https://www.youtube.com/")
                    
                elif 'Google' in data1:
                    webbrowser.open("https://www.google.com/")
                
                elif "joke" in data1:
                    joke_1 =  pyjokes.get_joke(language="en", category="neutral")
                    txspeech(joke_1) 
                    print(joke_1)
                
                elif "chuck joke" in data1:
                    joke_2 =  pyjokes.get_joke(language="en",category="chuck")
                    txspeech(joke_2) 
                    print(joke_2)
                
                elif "open spotify" in data1:
                    song = webbrowser.open("https://open.spotify.com/")
                
                elif 'play song' in data1:
                    add = "E:\Downloads\Dekha Ek Khwab x Laila _ Sush and Yohan Mashup _ Phulwa Choreography_ Atif Aslam ♥️💙 #youtubeshorts.mp4"
                    listsong = os.listdir(add)
                    print(listsong)
                    os.startfile(os.path.join(add , listsong[0]))
                
                elif "goodbye" in data1:
                    txspeech("thank you")
                    break
                
                time.sleep(5)
    else:
        print("thanks but sorry")