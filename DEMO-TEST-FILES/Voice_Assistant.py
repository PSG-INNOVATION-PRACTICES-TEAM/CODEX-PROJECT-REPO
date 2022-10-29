import speech_recognition as sr
import time
import webbrowser
import playsound
import os
import random
from time import ctime
from gtts import gTTS

r = sr.Recognizer()
Microphone_list = list(sr.Microphone.list_microphone_names())
i=0
index=[]
while i < len(Microphone_list):
    if 'Microphone (2- C270 HD WEBCAM)' == Microphone_list[i]:
        index.append(i)
    i += 1
index = index[-1]
# print(index)
mic = sr.Microphone(device_index=index)


# # for index, name in enumerate(sr.Microphone.list_microphone_names()):
# #     print(f'{index}, {name}')
# # speak('100')

defaut_location = 'D:\\7th Semester\\PROJECT-WORK-PHASE-1\\CODEX-PROJECT-REPO\\DEMO-TEST-FILES'

def record_audio(ask=False):
    if ask:
        speak(ask)
    with mic as source:
        r.adjust_for_ambient_noise(source)
        voice_data=''
        try:
            audio = r.listen(source)
            print('Recognizing')
            voice_data=r.recognize_google(audio)
        except sr.UnknownValueError:
            speak('Sorry I did not get that')
        except sr.RequestError:
            speak('Sorry My Speech Service is down!')
        return voice_data

def speak(audio_string):
    tts = gTTS(text=audio_string,lang='en')
    r = random.randint(1,10000000)
    audio_file = 'audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(os.path.join(defaut_location,audio_file))
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        speak('My name is CODEX')
    elif 'what time is it' in voice_data:
        speak(ctime())
    elif 'search' in voice_data:
        search_text = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q='+search_text
        webbrowser.get().open(url)
        speak('Here is what I found for'+search_text)
    elif 'find location' in voice_data:
        location = record_audio('Which location do you want to search for?')
        url = 'https://google.nl/maps/place/'+location+'/&amp;'
        webbrowser.get().open(url)
        speak('Here is the location of '+location)
    elif 'exit' in voice_data:
        speak('See You soon. Bye!')
        exit()
    else:
        speak('Sorry Can You Please repeat?')
    
#Driver Program
time.sleep(1)
speak('How Can I Help You ?')
while 1:
    voice_data = record_audio()
    print(voice_data)
    respond(voice_data)