import json

class database:

    @staticmethod
    def create_data_base():
        """Создание БД."""
        with open("database.json", "w", encoding='UTF-8') as f:
            data = {"user_username": []}
            json.dump(data, f, indent=3, ensure_ascii=False)

    @staticmethod
    def write_in_data_base(user_id, name, text):
        with open("database.json", encoding='UTF-8') as f2:
            data = {"people": {"user_id": int(user_id), "name": str(name), "messages": [str(text)]}}
            a = json.load(f2)
            a["user_username"].append(data)
        with open("database.json", "w", encoding='UTF-8') as f3:
            json.dump(a, f3, indent=3, ensure_ascii=False)
            

    @staticmethod
    def delete_message(user_id):
        with open("database.json", encoding="UTF-8") as file:
            f = json.load(file)

            for i in f["user_username"]:
                if user_id == i["people"]["user_id"]:
                    f["user_username"].remove(i)
                    continue
        
        with open("database.json", "w", encoding='UTF-8') as f4:
            json.dump(f, f4, indent=4, ensure_ascii=False)


    @staticmethod
    def send_message(user_id, message):
        with open("database.json", encoding='UTF-8') as file:
            f3 = json.load(file)
        
            for k in f3["user_username"]:
                if user_id == k["people"]["user_id"]:
                    k["people"]["messages"].append(message)
            
        with open("database.json", "w", encoding='UTF-8') as f4:
            json.dump(f3, f4, indent=4, ensure_ascii=False)


    @staticmethod
    def reset_message():
        with open("database.json", encoding="UTF-8") as file:
            f = json.load(file)
            for i in f["user_username"]:
                i["people"]["messages"] = []
        
        with open("database.json", "w", encoding="UTF_8") as fl:
            json.dump(f, fl, indent=4, ensure_ascii=False)


