import speech_recognition as sr
import time
import playsound
import os
import random
from gtts import gTTS
from parse_statement import parse_statement
# from Parse_algorithm_1 import parse_statement


#################### HELPER CODES ######################################

# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print(f'{index}, {name}')
# speak('100')


# stmt = parse_statement('sum equals five')
# print(stmt)
# print(stmt)

#################### HELPER CODES ######################################

################################ INITIALISING MODEL AND CODE FILE ###########################

# model = build_model()
# file = open('code.txt','w+')
with open('code.txt','w+') as file:
    pass
################################ INITIALISING MODEL AND CODE FILE ###########################

################################ INITIALISING THE RECOGNIZER AND INPUT DEVICE ###########################
r = sr.Recognizer()
Microphone_list = list(sr.Microphone.list_microphone_names())
i=0
index=[]
while i < len(Microphone_list):
    if 'Microphone (2- C270 HD WEBCAM)' == Microphone_list[i]:
        index.append(i)
    i += 1
index = index[-1]

mic = sr.Microphone(device_index=index)

defaut_location = 'D:\\7th Semester\\PROJECT-WORK-PHASE-1\\CODEX-PROJECT-REPO'
# print(index)
################################ INITIALISING THE RECOGNIZER AND INPUT DEVICE ###########################

############### RECORD FUNCTION TO RECORD THE MICROPHONE INPUT ###########################

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


############### SPEAK FUNCTION TO SPEAK THE RESPONSES AND QUERIES ###########################

def speak(audio_string):
    tts = gTTS(text=audio_string,lang='en')
    r = random.randint(1,10000000)
    audio_file = 'audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(os.path.join(defaut_location,audio_file))
    print(audio_string)
    os.remove(audio_file)


############### RESPOND FUNCTION TO RESPOND ACCORDING TO THE INTENT ###########################

def respond(voice_data):
    if 'name' in voice_data:
        speak('My name is CODEX')
    
    elif 'assignment statement' in voice_data:
        stmt = record_audio('please dictate your assignment statement')
        print(stmt)
        stmt = parse_statement(stmt,'assignment statement')
        print(stmt)
        with open('code.txt','a+') as file:
            file.write(stmt)
        speak('assignment statement added successfully!')
    
    elif 'arithmetic statement' in voice_data:
        stmt = record_audio('please dictate your arithmetic statement')
        print(stmt)
        stmt = parse_statement(stmt,'arithmetic_statement')
        print(stmt)
        with open('code.txt','a+') as file:
            file.write(stmt)
        speak('arithmetic statement added successfully!')
    
    elif 'else if' in voice_data:
        stmt = record_audio('please dictate your else if condition')
        print(stmt)
        stmt = parse_statement(stmt,'else if')+':'
        print(stmt)
        with open('code.txt','a+') as file:
            file.write(stmt)
        speak('else if statement added successfully!')
    
    elif 'if' in voice_data:
        stmt = record_audio('please dictate your if condition')
        print(stmt)
        stmt = parse_statement(stmt,'if')+':'
        print(stmt)
        with open('code.txt','a+') as file:
            file.write(stmt)
        speak('else if statement added successfully!')
    
    elif 'else' in voice_data:
        print('else:')
        with open('code.txt','a+') as file:
            file.write('else:')
        speak('else statement added successfully!')
    
    elif 'for' in voice_data:
        stmt = record_audio('please dictate your loop declration statement')
        print(stmt)
        stmt = parse_statement(stmt,'loop declration')
        stmt+= stmt.count('(')*')'
        stmt+=':'
        print(stmt)
        with open('code.txt','a+') as file:
            file.write(stmt)
        speak('loop added successfully!')
    
    elif 'while' in voice_data:
        stmt = record_audio('please dictate your loop declration statement')
        print(stmt)
        stmt = parse_statement(stmt,'while loop')
        stmt+= stmt.count('(')*')'
        stmt+=':'
        print(stmt)
        with open('code.txt','a+') as file:
            file.write(stmt)
        speak('loop added successfully!')
    
    elif 'import' in voice_data:
        stmt = record_audio('please dictate your import statement')
        print(stmt)
        print(stmt)
        with open('code.txt','a+') as file:
            file.write(stmt)
        speak('import statement added successfully!')
    
    elif 'print sentence' in voice_data:
        stmt = record_audio('please dictate your print sentence')
        print(stmt)
        stmt = 'print("'+stmt+'")'
        print(stmt)
        with open('code.txt','a+') as file:
            file.write(stmt)
        speak('print statement added successfully!')
    
    elif 'print statement' in voice_data:
        stmt = record_audio('please dictate your print statement')
        print(stmt)
        stmt = parse_statement(stmt,'print statement')
        close_parantheses = stmt.count('(')
        stmt+=close_parantheses*')'
        print(stmt)
        with open('code.txt','a+') as file:
            file.write(stmt)
        speak('print statement added successfully!')
    
    elif 'add line' in voice_data:
        with open('code.txt','a+') as file:
            file.write("\n")
        speak('Line added successfully!')
    
    elif 'delete line' in voice_data:
        stmt = record_audio('which line number would you wish to delete?')
        print(stmt)
        number = int(parse_statement(stmt,'number').replace(' ',''))
        print(number)
        with open('code.txt','r'):
            lst = list(file.readlines())
        with open('code.txt','w+') as file:
            for num, line in enumerate(lst):
                if num not in [number]:
                    file.write(line)
        speak('Line Deleted successfully!')
    
    elif 'move' in voice_data:
        stmt = record_audio('which line would you like to move')
        print(stmt)
        number = int(parse_statement(stmt,'number').replace(' ',''))
        print(number)
    
    elif 'add indent' in voice_data:
        with open('code.txt','a+') as file:
            file.write("\t")
        speak('indent added successfully!')
    
    elif 'delete indent' in voice_data:
        with open('code.txt','r'):
            lst = list(file.readlines())
        last_line = lst[-1]
        if last_line[-1] == '\t':
            last_line = last_line[:len(last_line)-1]
        lst[-1]=last_line
        with open('code.txt','w+') as file:
            for num, line in enumerate(lst):
                    file.write(line)
        speak('indent deleted successfully!')
    
    elif 'exit' in voice_data:
        speak('See You soon. Bye!')
        return -1
    
    else:
        speak('Sorry! Could You Please repeat?')
    return 0
    
############################# Driver Program #######################################################

# time.sleep(1)
# speak('How Can I Help You ?')
# while 1:
#     try:
#         voice_data = record_audio()
#     except Exception as e:
#         continue
#     voice_data = voice_data.lower()
#     print(voice_data)
#     respond(voice_data)
#     with open('code.txt','r+') as file:
#         print(len(file.readlines()))
#         for line in file.readlines():
#             print(line)