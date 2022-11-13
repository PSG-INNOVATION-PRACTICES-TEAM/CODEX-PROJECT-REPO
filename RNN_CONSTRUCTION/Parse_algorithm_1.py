# #Replace Functions
# #replaces the number in words with corresponding numbers
# def number_replacer(string):
#     temp = string.replace(' zero ','0').replace(' one ','1').replace(' two ','2').replace(' three ','3').replace(' four ','4').replace(' five ','5').replace(' six ','6').replace(' seven ','7').replace(' eight ','8').replace(' nine ','9')
#     temp = temp.replace('zero ','0').replace('one ','1').replace('two ','2').replace('three ','3').replace('four ','4').replace('five ','5').replace('six ','6').replace('seven ','7').replace('eight ','8').replace('nine ','9')
#     temp = temp.replace(' zero','0').replace(' one','1').replace(' two','2').replace(' three','3').replace(' four','4').replace(' five','5').replace(' six','6').replace(' seven','7').replace(' eight','8').replace(' nine','9')
#     temp = temp.replace('zero','0').replace('one','1').replace('two','2').replace('three','3').replace('four','4').replace('five','5').replace('six','6').replace('seven','7').replace('eight','8').replace('nine','9')
#     return temp

# #replaces the operators with corresponding operators
# def operator_replacer(string):
#     temp = string.replace('equals equals','==').replace('less than equals','<=').replace('greater than equals','>=').replace('not equals','!=').replace('plus equals','+=').replace('minus equals','-=').replace('star equals','*=').replace('slash equals','/=').replace('and equals','&=').replace('xor equals','|=').replace('or equals','^=').replace('less than','<').replace('greater than','>').replace('equals','=').replace('plus','+').replace('minus','-').replace('slash slash','//').replace('slash','/').replace('star star','**').replace('star','*').replace('and','&').replace('xor','^').replace('or','|').replace('percent','%').replace('true','True').replace('false','False')
#     return temp

# def for_loop_replacer(string):
#     temp = string
#     if 'range of' in string:
#         temp = string.replace('range of','range(')
#         temp = temp+"):"
#     return temp

# def parse_statement(statement,key):
#     temp = operator_replacer(number_replacer(statement))
#     if key=='if':
#         temp=temp+":"
#     elif key=="else if":
#         temp =temp.replace('else if','elsif')
#         temp = temp+":"
#     elif key=='loop declaration':
#         temp = for_loop_replacer(number_replacer(statement))
#     return temp


##################### DNN PARSING ###########################

# from build_model import build_model
import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
import tflearn
import tensorflow as tf
import random
import pickle
import json

#initialise model
# model = build_model()

#Function to pre process the string so that DNN yields more accuracy
def preprocess(string):
    string = string.replace('equals equals','equalsequals').replace('slash slash','slashslash').replace('is equals to','isequalsto').replace('is equal to','isequalto').replace('less than or equals to','lessthanorequalsto').replace('less than equals to','lessthanequalsto').replace('greater than or equals to','greaterthanorequalsto').replace('greater than equals to','greaterthanequalsto').replace('equals to','equalsto').replace('equalto','equalto').replace('less than or','lessthanor').replace('greater than or','greaterthanor').replace('less than','lessthan').replace('greater than','greaterthan').replace('else if','elseif').replace('range of','rangeof').replace('print of','printof')
    return string

#To pre-process the input text
def bag_of_words(inp,words):
    stemmer = LancasterStemmer()
    bag = [0 for _ in range(len(words))]
    user_words = nltk.word_tokenize(inp)
    user_words = [stemmer.stem(word.lower()) for word in user_words]
    for element in user_words:
        for i,w in enumerate(words):
            if w == element:
                bag[i]=1
    return bag

def predict(input,data,all_words,intents):

    number_map={
    "one":'1',
    "two":'2',
    "three":'3',
    "four":'4',
    "five":'5',
    "six":'6',
    "seven":'7',
    "eight":'8',
    "nine":'9',
    "zero":'0'
    }
    results = model.predict([bag_of_words(input,all_words)])
    result_index = np.argmax(results)
    tag = intents[result_index]
    print(tag,end=" ")
    if results[0][result_index]>0.2:
        if tag == "keywords":
            return input
    elif tag=="else_if":
        return "elif"
    elif tag == "inbuilt_functions":
        input = input.replace('of','')
        input+="("
        return input
    elif tag=="numbers":
        if input in number_map:
            return number_map[input]
        else:
            return input
    elif tag == "greeting" or tag=="goodbye":
        for t in data['intents']:
            if t['tag']==tag:
                responses = t['responses']
                return(random.choice(responses))
    else:
        for t in data['intents']:
            if t['tag']==tag:
                responses = t['responses']
                return(responses[0])
        else:
            print(results[0][result_index])
            return input

def parser(string):
    with open("D:\\7th Semester\\PROJECT-WORK-PHASE-1\\CODEX-PROJECT-REPO\\data.pickle","rb") as f:
        all_words,intents,training_set,output = pickle.load(f)
    with open('D:\\7th Semester\\PROJECT-WORK-PHASE-1\\CODEX-PROJECT-REPO\\intents.json') as file:
        data = json.load(file)
    string = preprocess(string)
    print("Pre-processed String: ",string)
    result = []
    for word in string.split(' '):
        print(word,end=" ")
        result.append(predict(word,data,all_words,intents))
    print(result)
    # print("Final Statement: ",' '.join(result))


parser('sum equals five')