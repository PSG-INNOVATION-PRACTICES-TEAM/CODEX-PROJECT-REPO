import speech_recognition as sr
import time

r = sr.Recognizer()
def recognize_audio():
    with sr.Microphone() as source:
        try:
            audio_data = r.listen(source,timeout=5)
            print('Recognizing...')
            text_data = r.recognize_google(audio_data,language='en-US')
            return text_data
        except sr.WaitTimeoutError:
            print("Sorry, I didn't Hear you out!")
            #recognize_audio()
        except sr.UnknownValueError:
            print("Sorry, I didn't get you! Can you repeat it again?")
            #recognize_audio()
        except sr.RequestError:
            print('Some problem with my speech recognition..')
            #recognize_audio()


time.sleep(1)
print('Please Talk..')
while 1:
    text_data = recognize_audio()
    print('You Said :',text_data)
    if 'Exit' in text_data:
        break
