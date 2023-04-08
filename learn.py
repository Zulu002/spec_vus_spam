from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from math import log, sqrt
import nltk
from database.API.dbase.db import database


nltk.download("stopwords")
class  learning:

    @staticmethod
    def text_lit(text, stemmer=PorterStemmer(),stop_words=set(stopwords.words("russian"))):
        message = text
        filter_words = []
        for i in message:
            i = i.lower()
            filter_words.append(i)

        for word in filter_words:
            if word in stop_words and word.isalpha():
                filter_words.append(stemmer.stem(word))
        return filter_words



if __name__ == "__main__":
    fl = learning()
    a = database.send_json()
    b = a["user_username"][1]['people']["messages"]
    v = fl.text_lit(b)
    print(v)
