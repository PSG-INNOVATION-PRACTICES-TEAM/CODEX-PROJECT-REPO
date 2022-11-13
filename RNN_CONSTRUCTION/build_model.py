import pickle
import tflearn
import tensorflow as tf
def build_model():
    with open("D:\\7th Semester\\PROJECT-WORK-PHASE-1\\CODEX-PROJECT-REPO\\data.pickle","rb") as f:
        all_words,intents,training_set,output = pickle.load(f)
    model = tflearn.input_data(shape=[None ,len(training_set[0])])
    model = tflearn.fully_connected(model,8)
    model = tflearn.fully_connected(model,8)

    model = tflearn.fully_connected(model,len(output[0]),activation="softmax")
    model = tflearn.regression(model)

    model = tflearn.DNN(model)

    model.fit(training_set,output,n_epoch=300,batch_size=8,show_metric=True)
    return model