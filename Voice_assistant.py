import speech_recognition as sr
import time
import playsound
import os
import random
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


# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print(f'{index}, {name}')
# speak('100')

defaut_location = 'D:\\7th Semester\\PROJECT-WORK-PHASE-1\\CODEX-PROJECT-REPO'

def parse_statement(stmt,intent):
    pass


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
            voice_data=record_audio()
        except sr.RequestError:
            speak('Sorry My Speech Service is down!')
            voice_data=record_audio()
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
    if 'name' in voice_data:
        speak('My name is CODEX')
    elif 'assignment statement' in voice_data:
        stmt = record_audio('please dictate your assignment statement')
        stmt = parse_statement(stmt,'assignment')
        print(stmt)
        speak('assignment statement added successfully!')
    elif 'arithmetic statement' in voice_data:
        stmt = record_audio('please dictate your arithmetic statement')
        stmt = parse_statement(stmt,'arithmetic')
        print(stmt)
        speak('arithmetic statement added successfully!')
    elif 'else if' in voice_data:
        stmt = record_audio('please dictate your else if condition')
        stmt = parse_statement(stmt,'else if')
        print(stmt)
        speak('else if statement added successfully!')
    elif 'if' in voice_data:
        stmt = record_audio('please dictate your if condition')
        stmt = parse_statement(stmt,'else if')
        print(stmt)
        speak('else if statement added successfully!')
    elif 'else' in voice_data:
        print('else:')
        speak('else statement added successfully!')
    elif 'for loop' in voice_data:
        stmt = record_audio('please dictate your loop declration statement')
        stmt = parse_statement(stmt,'loop declaration')
        print(stmt)
        speak('loop added successfully!')
    elif 'exit' in voice_data:
        speak('See You soon. Bye!')
        exit()
    else:
        speak('Sorry! Could You Please repeat?')
    
#Driver Program
time.sleep(1)
speak('How Can I Help You ?')
while 1:
    voice_data = record_audio()
    print(voice_data)
    respond(voice_data)