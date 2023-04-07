import time
from database.API.dbase import db

def res():
    #Сброс.
    time.sleep(10)
    db.database.reset_message()
    return "База данных очищена"
