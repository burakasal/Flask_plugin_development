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
import nltk 
from matplotlib import pyplot as plt
import collections
from wordcloud import WordCloud

app = flask.Flask(__name__)
app.config["DEBUG"] = True


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


    jres = {'detail':'Descriptive Terms: ',
            'detail2': term
            }
    return jsonify(jres)


@app.route('/api/fetch2', methods=['POST'])
def fetch2():
    data = request.get_data()  
    data2 = data.decode("ascii")
    html_content = requests.get(data2).text
    soup = BeautifulSoup(html_content, 'lxml')
    
    for a in soup.findAll('a', href=True):
        a.extract()
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
            if ent.text not in PersonList:
                PersonList.append(ent.text)
        if ent.label_ == "ORG":
            if ent.text not in OrganizationList:
                OrganizationList.append(ent.text)
        if ent.label_ == "GPE":
            if ent.text not in GPEList:
                GPEList.append(ent.text)
        
    TaggedOrganizations = ', '.join(OrganizationList)
    TaggedPersons = ', '.join(PersonList)
    TaggedGeographicalEntities = ', '.join(GPEList)

    jres = {'org': "Organizations: ",
            'org2': TaggedOrganizations,
            'per': 'Persons: ',
            'per2': TaggedPersons,
            'loc': 'Locations: ',
            'loc2': TaggedGeographicalEntities
            }
    return jsonify(jres)    

@app.route('/api/fetch3', methods=['POST'])
def fetch3():
    data = request.get_data()  
    data2 = data.decode("ascii")
    html_content = requests.get(data2).text
    soup = BeautifulSoup(html_content, 'lxml')
    mytext= soup.find_all("p")
    text = ""
    for points in mytext:
        point = str(points.text)
        text += point
    new_text = ""
    for sen in text:
        new_text = new_text + sen

    text = new_text
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)

    words = nltk.wordpunct_tokenize(text)

    i = 0
    mydict = set()

    term = []
    voc_size = []
    for word in words:
        i = i + 1
        mydict.add(word)  # words exist only once

        term.append(i)
        voc_size.append(len(mydict))

    plt.scatter(term, voc_size)
    plt.xlabel('term occurrence')
    plt.ylabel('vocabulary size')

    jres = {'detail': plt.show() }

    return jsonify(jres)

@app.route('/api/fetch4', methods=['POST'])
def fetch4():
    data = request.get_data()  
    data2 = data.decode("ascii")
    html_content = requests.get(data2).text
    soup = BeautifulSoup(html_content, 'lxml')
    mytext= soup.find_all("p")
    text = ""
    for points in mytext:
        point = str(points.text)
        text += point
    sentence = ""    
    for i in text:
        i = i.lower()
        new = re.sub(r'[^\w\s]', '', i)
        sentence = sentence + new

    text=sentence
    words = nltk.wordpunct_tokenize(text)

    # counter function returns a dictionary that includes words and their frequencies
    word_freqs = collections.Counter(words)

    top_word_freqs = word_freqs.most_common(len(words))

    rr = []
    z_f = []
    a = 0
    for r, i in top_word_freqs:
        a = a + 1
        z_f.append(i)
        rr.append(a)

    ax = plt.gca()
    ax.set_yscale('log')
    ax.set_xscale('log')
    plt.scatter(rr, z_f)
    plt.xlabel('log(rank)')
    plt.ylabel('log(freq)')

    jres = {'detail': plt.show() }

    return jsonify(jres)

@app.route('/api/fetch5', methods=['POST'])
def fetch5():
    sword = set(sw.words('turkish'))
    sword2 = set(sw.words('english.txt'))
    data = request.get_data()  
    data2 = data.decode("ascii")
    html_content = requests.get(data2).text
    soup = BeautifulSoup(html_content, 'lxml')
    mytext= soup.find_all("p")
    text = []
    for points in mytext:
        point = str(points.text)
        text.append(point)

    a = 0
    for i in text:
        i = i.lower()
        new = re.sub(r'[^\w\s]', '', i)
        text[a] = new
        a = a + 1

    aa = 0
    for i in text:  # for every sentence
        sentence = i

        sentence = nltk.wordpunct_tokenize(sentence)

        mylist = []
        for a in sentence:
            if a in sword:
                mylist.append(a)   
            if a in sword2:
                mylist.append(a)      

        for u in mylist:
            sentence.remove(u)

        new_s = ""
        for y in sentence:
            new_s = new_s + " " + y

        text[aa] = new_s
        aa = aa + 1

    vectorizer = TfidfVectorizer()
    vecs = vectorizer.fit_transform(text)
    feature_names = vectorizer.get_feature_names()
    aaa = vecs.transpose().sum(axis=1)
    lst1 = aaa.tolist()

    myl = []
    for i in lst1:
        res = str(i)[1:-1]
        ress = float(res)
        myl.append(ress)

    # creating the dictionary to give as a parameter to wordcloud function
    mydict = {}
    n = 0
    for name in feature_names:
        mydict[name] = myl[n]
        n = n + 1

    mywc = WordCloud(background_color="black", width=1000, height=1000)
    mywc.generate_from_frequencies(mydict)

    plt.figure(figsize=(6, 6), facecolor=None)
    plt.imshow(mywc, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad=0)
    
    jres = {'detail': plt.show()}

    return jsonify(jres)

app.run()
