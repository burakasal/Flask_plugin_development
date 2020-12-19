
import datetime
import flask
from flask import request, jsonify
from bs4 import BeautifulSoup
import requests
import re 
import pandas as pd
import spacy
from spacy.lang.en.stop_words import STOP_WORDS

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
    text = ""
    for points in mytext:
        point = str(points.text)
        text += point

    sentence = text
    # make the sentence a clear array
    sentence = sentence.lower()  # lower the letters

    alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8,
                'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16,
                'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24,
                'z': 25, ' ': 26}

    #sentence1 = ""
    '''for i in sentence:  # remove the marks
        if i in alphabet:
            sentence1 += i'''
    sentence1 = re.sub(r'[^\w\s]', '', sentence)
    #Removed the punctuation marks from the sentece using regular expression library of Python.
    sentence = sentence1

    sentence = sentence.split(" ")

    # _______________________________________
    # removing stopwords will increase computation and space efficiency.

    WorddictA = []
    # _________________________________

    # create a dictionary, print as a dataframe
    word_dict = dict.fromkeys(sentence, 0)
    for word in sentence:
        word_dict[word] += 1
    print("\nAs a dictionary: ",word_dict)

    df = pd.DataFrame([word_dict])
    print("\nAs a table: \n", df)

    #create a frequency table
    def freq_function(dict, text):
        tf_dict={}
        corpus_count=len(text)
        for word, count in dict.items():
            tf_dict[word]= (count / corpus_count)*100

        return (tf_dict)

    '''
    my_tf= freq_function(word_dict, sentence)
    tf= pd.DataFrame([my_tf])
    print("The frequency table is: \n",tf)    
    print(text)'''
    
    word_dict= {k: v for k, v in sorted(word_dict.items(), key=lambda item: item[1])}


    my_tf= freq_function(word_dict, sentence)
    
    
    jres = {'detail':'NLP FUNCTION:' + str(my_tf)}
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
    #TOKENIZATION IMPLEMENTATION
    for token in doc:
        print(token.text,token.pos_)

    tetx = []
    labels = []
    #NER
    my_str = ""
    for ent in doc.ents:
        tetx.append(ent.text)
        labels.append(ent.label_)
        #print(ent.text, ent.label_)  
        my_str = my_str+ ent.text + ent.label_ + "," 

    tetXXX = ''.join(tetx)
    labelZZ  = ''.join(labels)
    jres = {'detail':'NLP FUNCTION:' + my_str}
    return jsonify(jres)    

app.run()

