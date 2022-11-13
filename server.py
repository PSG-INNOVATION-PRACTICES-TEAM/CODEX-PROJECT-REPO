from flask import Flask,render_template,url_for,redirect,jsonify
from Voice_assistant import record_audio,speak,respond
from flask_cors import CORS, cross_origin
import time
# import speech_recognition as sr

#Initialising the App


app = Flask(__name__)
CORS(app, support_credentials=True)


#####################  Initialising the microphone and recogniser object ##################### 
# r = sr.Recognizer()
# Microphone_list = list(sr.Microphone.list_microphone_names())
# i=0
# index=[]
# while i < len(Microphone_list):
#     if 'Microphone (2- C270 HD WEBCAM)' == Microphone_list[i]:
#         index.append(i)
#     i += 1
# index = index[-1]

# mic = sr.Microphone(device_index=index)
# defaut_location = 'D:\\7th Semester\\PROJECT-WORK-PHASE-1\\CODEX-PROJECT-REPO'
#####################  Initialising the microphone and recogniser object ##################### 

@app.route('/start-voice-assistant',methods=["GET"])
@cross_origin(supports_credentials=True)
def home_route():
    with open('D:\\7th Semester\\PROJECT-WORK-PHASE-1\\CODEX-PROJECT-REPO\\code.txt','w+'):
        pass
    time.sleep(1)
    speak('How Can I Help You ?')
    src_pgm={
            'source_code':''
        }
    while 1:
        voice_data = record_audio()
        voice_data = voice_data.lower()
        print(voice_data)
        exit_flag = respond(voice_data)
        if exit_flag<0:
            break
    with open('code.txt','r+') as file:
        for line in file.readlines():
            print(line)
            src_pgm['source_code']+=line
    # print('Server Side Called')
    return jsonify(src_pgm)
    

@app.route('/stop-voice-assistant',methods=["GET"])
def exit_program():
    exit()

@app.route('/compile',methods=["POST"])
def run_program():
    speak('Running Your Program')
    pass


if __name__ == "__main__":
    app.run()