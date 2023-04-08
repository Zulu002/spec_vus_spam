import time
from database.API.dbase import db

def res():
    file = db.database.send_json()
    for i in file["user_username"]:
        if i["people"]["quantity_warning"] >= 3:
            db.database.delete_message(i["people"]["user_id"])

    #Сброс.
    time.sleep(10)
    db.database.reset_message()
    return "База данных очищена"
