import this
import speech_recognition as sr
import time

r = sr.Recognizer()

class User:
    name=''
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name

def there_exists(lst,text_data):
    for term in lst:
        if term in text_data:
            return True

def recognize_audio(follow_up=False):
    if follow_up:
        print(follow_up)
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

def respond(query_string):
    #Greeting
    if there_exists(['hi','hello','halo','hiee'],query_string):
        print('Hello! my name is Codex. How can I help You?')
    
    #Name
    if there_exists(['what is your name',"what's your name","your name","name"],query_string):
        if user.name:
            print(f'Hello {user.name}. My name is Codex :)')
        else:
            print('Hello! my name is Codex.')
            text_data = recognize_audio("What is Your Name?")
            respond(text_data.lower())
    
    #Set User Name
    if there_exists(['my Name is',"i'am","myself"],query_string):
        name = query_string.split('')[-1].strip()
        print(f'Hello {name}!. Good to See you!!')
        user.set_name(name)
    
    #How are you
    if there_exists(['how are you',"how you doin","what's up"],query_string):
        print(f"I'am doin fine {user.name}. Nothing much just coding ^__^")
    
    #exit
    if there_exists(['bye',"see you soon","ok then"],query_string):
        print(f"Signing Off {user.name}. Going offline!!!")


time.sleep(1)
user = User()
print('Please Talk..')
text_data=''
while 1:
    text_data = recognize_audio()
    print('You Said :',text_data)
    text_data = text_data.lower()
    response = respond(text_data)
    print(response)
