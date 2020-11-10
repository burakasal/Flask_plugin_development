from flask import Flask, render_template
from bs4 import BeautifulSoup
from lxml import etree
import requests
import pandas as pd
import math
from nltk.corpus import stopwords
import nltk as nltk
import re
app = Flask(__name__)


@app.route("/")  # this sets the route to this page
def home():
    source = requests.get("https://en.wikipedia.org/wiki/Wiki").text
    soup = BeautifulSoup(source, 'lxml')
    results = soup.find(id='bodyContent')
    wanted_text = results.find_all("div", class_= "mw-parser-output")
    mytext= ""
    for string in wanted_text:
        mytext += string.text.strip()
        
    sentence = mytext
    print("\nThe original text is: ", sentence)

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
    print("\nAs an array: ",sentence, "\n")



    # _______________________________________
    # removing stopwords will increase computation and space efficiency.

    WorddictA = []

    sword = set(stopwords.words('english.txt'))
    filtered_sentence = [w for w in WorddictA if not w in sword]

    print("The stop words should be removed from the text. \nThe stopwords are: ", sword)

    for word in sentence:
        if (word in sword):
            sentence.remove(word)
    print("The text without the stopwords: ",sentence)



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


    my_tf= freq_function(word_dict, sentence)
    tf= pd.DataFrame([my_tf])
    print("The frequency table is: \n",tf)

    return render_template("index.html", **locals())

if __name__ == "__main__":
    app.run(debug=True)

   