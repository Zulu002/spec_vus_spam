import time
from database.API.dbase import db

def res():
    """Функция для автоматического сброса сообщений."""
    file = db.database.send_json() #Вызов метода отправки json файла.
    for i in file["user_username"]:
        if i["people"]["quantity_warning"] >= 3: #Удаление сообщений где предупреждений больше 3.
            db.database.delete_message(i["people"]["user_id"])

    #Сброс.
    time.sleep(1800) #Сброс каждый 30минут 
    db.database.reset_message() #Вызов метода очитски БД.
    return "База данных очищена"
