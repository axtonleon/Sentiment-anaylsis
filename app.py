from flask import Flask, request, jsonify, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pickle
from model import text_cleaner
import os
from spacy.lang.en.stop_words import STOP_WORDS

app = Flask(__name__)
model=pickle.load(open("SVC.sav","rb"))


@app.route('/', methods=['GET'])
def home():
    path = 'static/img/'
    uploads = sorted(os.listdir(path), key=lambda x: os.path.getctime(path+x))#Sorting as per image upload date and time
    print(uploads)
    #uploads = os.listdir('static/uploads')
    uploads = ['img/' + file for file in uploads]
    uploads.reverse()
    return render_template('index.html',uploads=uploads)


@app.route("/predict",methods=["POST"])
def predict():
    
    values=[str(x) for x in request.form.values()]
    prediction=model.predict(values)
    if prediction== 0:
            prediction="Negative review"
            path = 'static/sad/'
            uploads = sorted(os.listdir(path), key=lambda x: os.path.getctime(path+x))#Sorting as per image upload date and time
            print(uploads)
            #uploads = os.listdir('static/uploads')
            uploads = ['sad/' + file for file in uploads]
            uploads.reverse()
    else:
            prediction="Positive review"
            path = 'static/happy/'
            uploads = sorted(os.listdir(path), key=lambda x: os.path.getctime(path+x))#Sorting as per image upload date and time
            print(uploads)
            #uploads = os.listdir('static/uploads')
            uploads = ['happy/' + file for file in uploads]
            uploads.reverse()
    
    T
    return render_template("index.html",prediction_text = "he sentiment is {}".format(prediction),uploads=uploads)

if __name__=="__main__":
          app.run(debug=True)
