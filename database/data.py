from API.dbase.db import database


data = [[1, "Владимир", "Как дела"],
        [2, "Дмитрий", "Привет всем!!"],
        [3, "Алексей", "Аллло"],
        [1, "Владимир", "АЛЛО"]]

# database.create_data_base() #Создание БД.
# for i in data:
#     database.write_in_data_base(i[0], i[1], i[-1])

# #database.delete_message(1) #Удаление значений.
# database.send_message(2, "Привееет!")

#database.reset_message()

#print(database.read_message(3))