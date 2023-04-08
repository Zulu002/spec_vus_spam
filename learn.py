from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from math import log, sqrt
import nltk
from database.API.dbase.db import database


nltk.download("stopwords")
class  learning:
    def __init__(self):
        self.db = database #Экземпляр базы данных.

    def text_lit(self, text, stemmer=PorterStemmer(),stop_words=set(stopwords.words("russian"))):
        """Функция которая анализирует переданный текст."""
        message = text
        self.user_id = [i["people"]["user_id"] for i in text] #Добавление всех id, длядальнейшей обработки.
        self.filter_words = [] #Пустой список в который будут добавлять отфильтрованные данные.
        for i in message:
            for k in i["people"]["messages"]:
                k = k.lower()
                self.filter_words.append(k) #Добавление сообщений.

        for word in self.filter_words:
            if word in stop_words and word.isalpha():
                self.filter_words.append(stemmer.stem(word))
        return self.filter_words, self.user_id
    
    def analitics(self):
        """Функция, которая анализирует повторение сообщений
            Более 3 или ровно 3 сообщения -- +1 Предупреждение.
            3 предупреждения - бан."""
        list_res = self.filter_words() #Получение данных с 1-ой функции, отфильтрованной информации.
        set_res = set(list_res) #Множество,отфильтрованные сообщения без повторений.
        if len(list_res) - len(set_res): #Условие вычета >=3 прд.
            self.db.add_warning()



if __name__ == "__main__":
    fl = learning()
    a = database.send_json()
    b = a["user_username"] #Тестовая передача данных.
    v = fl.text_lit(b)
    print(v)
