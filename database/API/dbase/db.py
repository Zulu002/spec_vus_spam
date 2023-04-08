import json

class database:

    @staticmethod
    def create_data_base():
        """Создание БД.
        Необходим ВЕЗДЕ ensure_ascii=КОДИРОВКА, русская не поддерживается без параметра False."""
        with open("database.json", "w", encoding='UTF-8') as f:
            data = {"user_username": []}
            json.dump(data, f, indent=3, ensure_ascii=False) #Загрузка данных.

    @staticmethod
    def write_in_data_base(user_id, name, message=None):
        """Функция для записи новых пользователей, или сообщений к ним."""
        with open("database.json", encoding='UTF-8') as f2:
            if message:
                data = {"people": {"user_id": int(user_id), "name": str(name), "messages": [message], "reason_ban": [], "quantity_warning": 0}}
            else:
                data = {"people": {"user_id": int(user_id), "name": str(name), "messages": [], "reason_ban": [], "quantity_warning": 0}}
            a = json.load(f2) #Загрузка json, чтение.
            a["user_username"].append(data) 
        with open("database.json", "w", encoding='UTF-8') as f3:
            json.dump(a, f3, indent=3, ensure_ascii=False) #Загрузка нового, обновленного json файла.
            

    @staticmethod
    def delete_message(user_id):
        """Функция которая удаляет пользователей со всеми данными."""
        with open("database.json", encoding="UTF-8") as file:
            f = json.load(file)

            for i in f["user_username"]:
                if user_id == i["people"]["user_id"]:
                    f["user_username"].remove(i)
                    continue
        
        with open("database.json", "w", encoding='UTF-8') as f4:
            json.dump(f, f4, indent=4, ensure_ascii=False) #Сохранение изменений.


    @staticmethod
    def send_message(user_id, message):
        """Отдельная функция для загрузки сообщений от пользователей."""
        with open("database.json", encoding='UTF-8') as file:
            f3 = json.load(file)
        
            for k in f3["user_username"]:
                if user_id == k["people"]["user_id"]:
                    k["people"]["messages"].append(message)
            
        with open("database.json", "w", encoding='UTF-8') as f4:
            json.dump(f3, f4, indent=4, ensure_ascii=False)


    @staticmethod
    def reset_message():
        """Функция для сброса сообщений."""
        with open("database.json", encoding="UTF-8") as file:
            f = json.load(file)
            for i in f["user_username"]:
                i["people"]["messages"] = [] #Сброс всех сообщений до пустого списка.
                i['people']['quantity_warning'] = 0 #Сброс предупреждений до 0
        
        with open("database.json", "w", encoding="UTF_8") as fl:
            json.dump(f, fl, indent=4, ensure_ascii=False) #Сохранение результатов.

    @staticmethod
    def read_message(user_id):
        """Функция для чтения конкретного пользователя - json файла, БД."""
        with open("database.json", encoding="UTF-8") as ms:
            fl = json.load(ms)
            
            for k in fl["user_username"]:
                if k["people"]["user_id"] == user_id:
                    return k["people"] #Возвращает ключ people - всех пользователей и их содержимое.

    @staticmethod
    def send_json():
        """Функция для чтения всего json файла."""
        with open("database.json", encoding="UTF-8") as f1:
            return json.load(f1)

    
    @staticmethod
    def ban(user_id: int, reason: str): #Где reason -> Причина бана.
        """Функция выполняющая блокировку пользователя и всех его данных.
        Удаление из БД."""
        with open("database.json", encoding="UTF-8") as f4:
            file = json.load(f4)
        try:
            for i in file['user_username']:
                if i["people"]["user_id"] == user_id and i["people"]["quantity_warning"] >= 3:
                    i["people"]["reason_ban"].append(reason) #Недоработано, нехватает причин бана, либо ручная вносимость причин.
                    return "Пользователь успешно удален"
        except Exception:
            return "Данный пользователь не подналежит бану."

    @staticmethod
    def add_warning(user_id):
        """Функция для добавления предупреждения о спаме."""
        with open("database.json", encoding='UTF-8') as f:
            file = json.load(f)
            for k in file["user_username"]:
                if k["people"]['user_id'] == user_id:
                    k["people"]["quantity_warning"] += 1 #Прибавление к указанной переменной 1, 3 - бан.

        with open("database.json", "w", encoding="UTF-8") as fil:
            json.dump(file, fil, indent=4, ensure_ascii=False) #Сохранение результатов.
        
