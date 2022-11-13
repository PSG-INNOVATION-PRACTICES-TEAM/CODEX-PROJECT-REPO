# -*- coding: utf-8 -*-
"""RNN_CONSTRUCTION.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LzQ82uiFTuS4xJGUQLb4wdj1rO97kFAy
"""

import nltk
nltk.download('punkt')

# !pip install tensorflow
# tensorflow.reset_default_graph()

from nltk.stem.lancaster import LancasterStemmer
import numpy as np
import tflearn
import tensorflow as tf
import random
import pickle
import json

with open('D:\\7th Semester\\PROJECT-WORK-PHASE-1\\CODEX-PROJECT-REPO\\intents.json') as file:
  data = json.load(file)
data

#Initialize Stemmer
stemmer = LancasterStemmer()
tf.compat.v1.reset_default_graph()

"""DATA PRE-PROCESSING"""

all_words = []
intents = []
pattern_set = []
tag_set = []
for intent in data['intents']:
  for pattern in intent['patterns']:
    wrds = nltk.word_tokenize(pattern)
    all_words.extend(wrds)
    pattern_set.append(wrds)
    tag_set.append(intent['tag'])
  if intent not in intents:
    intents.append(intent['tag'])

all_words = [stemmer.stem(w.lower()) for w in all_words if w!="?"]
all_words = sorted(list(set(all_words)))
intents = sorted(intents)

len(all_words)
# alL_words[:10]

pattern_set

len(intents)

len(data['intents'])

training_set = []
output = []

#output format - one hot encoding to decide which intent it belongs to
out_format = [0 for _ in range(len(intents))]

#creating one hot encoding for each sentence with respect to the vocabulary
for x,doc in enumerate(pattern_set):
  bag = []
  wrds = [stemmer.stem(w.lower()) for w in doc]
  for w in all_words:
    if w in wrds:
      bag.append(1)
    else:
      bag.append(0)
  output_row = out_format[:]
  output_row[intents.index(tag_set[x])]=1
  training_set.append(bag)
  output.append(output_row)

len(training_set[0])

len(output[0])

training_set = np.array(training_set)
output = np.array(output)

#Saving the training and output format as a pickle file
with open("data.pickle","wb") as f:
  pickle.dump((all_words,intents,training_set,output),f)

"""MODEL CONSTRUCTION"""

model = tflearn.input_data(shape=[None ,len(training_set[0])])
model = tflearn.fully_connected(model,8)
model = tflearn.fully_connected(model,8)

model = tflearn.fully_connected(model,len(output[0]),activation="softmax")
model = tflearn.regression(model)

model = tflearn.DNN(model)

model.fit(training_set,output,n_epoch=300,batch_size=8,show_metric=True)
model.save("model.tflearn")

"""MODEL PREDICTION"""

#To pre-process the input text
def bag_of_words(inp,words):
  bag = [0 for _ in range(len(words))]
  user_words = nltk.word_tokenize(inp)
  user_words = [stemmer.stem(word.lower()) for word in user_words]

  for element in user_words:
    for i,w in enumerate(words):
      if w == element:
        bag[i]=1
  return bag

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

def predict(input):
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

def preprocess(string):
    string = string.replace('equals equals','equalsequals').replace('slash slash','slashslash').replace('is equals to','isequalsto').replace('is equal to','isequalto').replace('less than or equals to','lessthanorequalsto').replace('less than equals to','lessthanequalsto').replace('greater than or equals to','greaterthanorequalsto').replace('greater than equals to','greaterthanequalsto').replace('equals to','equalsto').replace('equalto','equalto').replace('less than or','lessthanor').replace('greater than or','greaterthanor').replace('less than','lessthan').replace('greater than','greaterthan').replace('else if','elseif').replace('range of','rangeof').replace('print of','printof')
    return string

print(preprocess("for i in range of five"))
print(preprocess("if i equals to three"))
print(preprocess("else if i less than or equals to nine"))

"""PARSE ALGORITHM"""

# bag_of_words("for",all_words).count(1)
string = input('Enter Your String : ')
string = preprocess(string)
print("Pre-processed String: ",string)
result = []
for word in string.split(' '):
  print(word,end=" ")
  result.append(predict(word))
  # print(predict(word))
  print(result)
print("Final Statement: ",' '.join(result))