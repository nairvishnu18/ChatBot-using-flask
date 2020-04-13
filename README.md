# ChatBot-using-flask
A simple chatbot using flask 

Libararies needed: Flask, newspaper/bs4 , nltk

This is chatbot which fetches the article from a website and compares it with user query to give relevant answers.
This is a rule based chatbot.


Using flask a web ui is created .

Using nltk TfidVectorizer Cosine similarity NL tools the bot calculates the similarity of scrapped articles with the user query and returns a response


article.html should include article about the content the bot should use to reply.Eg Article about corona virus, NLP, AI etc.
index.html and style.css should be included in templates and static folder respectively as flask by default uses this folders tonaccess index.html
