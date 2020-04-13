#Libraries
from newspaper import  Article
import string
import re
import  random
import warnings
import nltk
from flask import Flask,request,render_template
from sklearn.feature_extraction.text import  TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from bs4 import BeautifulSoup
import numpy as np


warnings.filterwarnings('ignore')

#Packages for nltk
nltk.download('punkt',quiet=True)
nltk.download('wordnet',quiet=True)

app = Flask(__name__)

@app.route("/")
def index():
    return  render_template("index.html")


@app.route("/get")
def botResponse():
    #Getting user query
    user_query = request.args.get('msg')

    #Getting Contents/Articles
    url = 'article.html'
    page = open(url)
    soup = BeautifulSoup(page.read())
    corpus = soup.get_text()



    #Tokenization
    text=corpus
    tokens = nltk.sent_tokenize(text)


    #Punctuation removal
    remove_punctuation = dict( (ord(punct),None) for punct in string.punctuation)

    #Lemmatization and Normalization
    def LemmaNormalize(text):
        lemmas = nltk.word_tokenize(text.lower().translate(remove_punctuation))
        return lemmas


    #Small Talks
    Greeting_inputs =["hi","hello","namaskar","heya","hii","helo","hey","hiii"]
    Greeting_response = ["hello there","heya","hi","Hi there","Howdy","How can i help?","Hey","Nice to see you"]

    #Small Talk generator
    def Greetings(sentence):
        for word in sentence.split():
            if word.lower() in Greeting_inputs:
                return random.choice(Greeting_response)


    #Bot Response for queries

    def Response(user_response):
        response = ''
        tokens.append(user_response)
        Tfidfvector = TfidfVectorizer(tokenizer= LemmaNormalize, stop_words='english')
        tfidf = Tfidfvector.fit_transform(tokens)

        #Similarity Finder
        similarity = cosine_similarity(tfidf[-1],tfidf)
        index = similarity.argsort()[0][-2]
        flat = similarity.flatten()
        flat.sort()
        sim_score = flat[-2]

        if(sim_score == 0):
            response = response + "Didn't Get You, Sorry"

        else:
            response = response + tokens[index]

        tokens.remove(user_response)
        return  response


    flag = True

    while(flag==True):
            user_response = user_query
            user_response = user_response.lower()
            if(user_response!='bye'):
                if(user_response=='thanks' or user_response=='thank you'):
                    flag = False
                    response = 'Welcome'
                    return response
                else:
                    if(Greetings(user_response)!=None):
                        response = Greetings(user_response)
                        return response
                    else:
                        response = Response(user_response)
                        return response
            else:
                flag = False
                response = 'Bye'
                return response


if __name__ == "__main__":
    app.run()







