from database import Database


# Создание базы данных
a = Database("Firstdb")

# Создание таблицы
a.create_table("example")

# Вставка данных в таблицу
a.insert("example", {"id" : 1, "name" : "Alibek" , "age" : 18})
a.insert("example", {"id" : 2, "name" : "Alex" , "age" : 32})
a.insert("example", {"id" : 3, "name" : "Didar" , "age" : 48})

# Получение всех записей из таблицы
all_records = a.select("example")

# Получение записей по условию
filtered_records = a.select("example", condition=lambda row: row["age"] > 30)

# Получение отсортированных записей
sorted_records = a.select("example", order_by={"column": "id", "reverse": True})

# Обновление записи
a.update("example", {"name" : "Alibek"}, {"age": 30})

# Удаление записи
a.delete("example", {"id": 1})

# # Удаление таблицы
# a.drop_table("example")
