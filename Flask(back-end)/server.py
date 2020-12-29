
import datetime
import flask
from flask import request, jsonify
from bs4 import BeautifulSoup
import requests
import re 
import pandas as pd
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords as sw

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def index():
    return "<h1>Backend Homepage</h1><p>This site does...</p>"

@app.route('/api/fetch', methods=['POST'])
def fetch():
    data = request.get_data()  
    data2 = data.decode("ascii")
    html_content = requests.get(data2).text
    soup = BeautifulSoup(html_content, 'lxml')
    mytext= soup.find_all("p")
    text = []
    for points in mytext:
        point = str(points.text)
        # text += point
        text.append(point)


    # Pre-processing
    stopWords = sw.words('english.txt')
    Data = []
    for item in text:
        item = item.lower()
        item = re.sub(r'[^\w\s]', '', item)
        Data.append(item)

    vectorizer = TfidfVectorizer(stop_words=stopWords)
    X = vectorizer.fit_transform(Data).toarray()
    
    myDictionary = []
    featureCount = 0
    for item in vectorizer.get_feature_names():
        myDictionary.append(item)
        featureCount += 1

    (row, column) = X.shape
    tfidf = [0] * featureCount
    counter = 0
    while counter < featureCount:
        for j in range(0, row):
            tfidf[counter] += X[j][counter]
        counter += 1


    TFIDF = {}
    for i in range(0, featureCount):
        TFIDF[myDictionary[i]] = tfidf[i]


    SortedDict= {k: v for k, v in sorted(TFIDF.items(), key=lambda item: item[1])}   
    TFIDFListesi = []
    for item, value in SortedDict.items():
        TFIDFListesi.append(item + ":")
        TFIDFListesi.append(value)

    
    mostImportantwords = TFIDFListesi[-20:]
    term = ""
    for i in range(0, len(mostImportantwords)):
        term += str(mostImportantwords[i]) + " "


    jres = {'detail':'Descriptive Terms: ' + term}
    return jsonify(jres)

@app.route('/api/fetch2', methods=['POST'])
def fetch2():
    data = request.get_data()  
    data2 = data.decode("ascii")
    html_content = requests.get(data2).text
    soup = BeautifulSoup(html_content, 'lxml')
    mytext= soup.find_all("p")
    text = ""
    for points in mytext:
        point = str(points.text)
        text += point

    nlp = spacy.load("en_core_web_sm")

    doc = nlp(text)

    OrganizationList = []
    GPEList = []
    PersonList = []
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            PersonList.append(ent.text)
        if ent.label_ == "ORG":
            OrganizationList.append(ent.text)
        if ent.label_ == "GPE":
            GPEList.append(ent.text)
        
    TaggedOrganizations = ' '.join(OrganizationList)
    TaggedPersons = ' '.join(PersonList)
    TaggedGeographicalEntities = ' '.join(GPEList)

    jres = {'org': 'Organizations: ' + TaggedOrganizations,
            'per': 'Persons: ' + TaggedPersons,
            'loc': 'Locations: ' + TaggedGeographicalEntities
            }
    return jsonify(jres)    

app.run()

