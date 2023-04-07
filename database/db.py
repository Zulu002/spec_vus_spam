import json

class database:

    @staticmethod
    def create_data_base():
        """Создание БД."""
        with open("database.json", "w", encoding='UTF-8') as f:
            data = {"user_username": []}
            json.dump(data, f, indent=3)

    @staticmethod
    def write_in_data_base(user_id, name, text):
        with open("database.json") as f2:
            data = {"people": {"user_id": user_id, "name": name, "message": text}}
            a = json.load(f2)
            a["user_username"].append(data)
        with open("database.json", "w", encoding='UTF_8') as f3:
            json.dump(a, f3, indent=3)
            

    @staticmethod
    def delete_message(user_id):
        with open("database.json") as file:
            f = json.load(file)

            for i in f["user_username"]:
                if user_id == i["people"]["user_id"]:
                    f["user_username"].remove(i)
        
        with open("database.json", "w") as f4:
            json.dump(f, f4, indent=4)



