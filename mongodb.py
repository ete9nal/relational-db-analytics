from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import PyMongoError

try:
    client = MongoClient(
        "mongodb+srv://<username>:<password>@cluster0.ly0lvcv.mongodb.net/test_db?appName=Cluster0",
        server_api=ServerApi("1")
    )

    db = client.test_db
except PyMongoError as e:
    print(f"Помилка підключення до бази даних: {e}")


def find_all():
    """Виводить всі записи колекції cats"""
    try:
        cats = db.cats.find()
        for cat in cats:
            print(cat)
    except PyMongoError as e:
        print(f"Помилка при читанні: {e}")

def find_by_name(name):
    """Виводить запис за вказаним імʼям"""
    try:
        cat = db.cats.find_one({"name":name})
        if cat:
            print(cat)
        else:
            print(f"Кота {name} не знайдено.")
    except PyMongoError as e:
        print(f"Помилка при пошуку: {e}")

def update_age(name, age):
    """Оновлює вік за вказаним імʼям"""
    try:
        result = db.cats.update_one({"name":name}, {"$set":{"age":age}})
        if result.matched_count:
            print(f"Вік кота {name} успішно оновлено.")
        else:
            print(f"Кота {name} не знайдено.")
    except PyMongoError as e:
        print(f"Помилка при оновлені віку: {e}")

def add_feature(name, feature):
    """Додає нову характеристику до списку features за імʼям кота"""
    try:
        result = db.cats.update_one({"name":name}, {"$push":{"features":feature}})
        if result.matched_count:
            print(f"Характеристику '{feature}' додано коту {name}.")
        else:
            print(f"Кота {name} не знайдено.")
    except PyMongoError as e:
        print(f"Помилка при додавання характеристики: {e}")

def delete_by_name(name):
    """Видаляє запис кота за імʼям"""
    try:
        result = db.cats.delete_one({"name":name})
        if result.deleted_count:
            print(f"Кота {name} видалено.")
        else:
            print(f"Кота {name} не знайдено.")
    except PyMongoError as e:
        print(f"Помилка при видаленні: {e}")

def delete_all():
    """Видаляє усі записи з колекції cats"""
    try:
        result = db.cats.delete_many({})
        print(f"Видалено котів: {result.deleted_count}")
    except PyMongoError as e:
        print(f"Помилка при повному видаленні: {e}")

if __name__ == "__main__":
    delete_all()

    db.cats.insert_one({
        "name": "Naomi",
        "age": 666,
        "features": ['гарна', 'чорна', 'викликає демонів']
    })

    db.cats.insert_one({
        "name": "Vaska",
        "age": 10,
        "features": ['вуличний', 'гадить', 'рижий']
    })

    db.cats.insert_one({
        "name": "Schrodinger's cat",
        "age": 3,
        "features": ['квантовий', 'невизначений', 'вірогідний']
    })

    print("\n $$$ Всі коти $$$")
    find_all()

    print("\n $$$ Шукаємо Naomi $$$")
    find_by_name("Naomi")

    print("\n $$$ Оновлюємо вік $$$")
    update_age("Vaska", 11)

    print("\n $$$ Додаємо характеристику для киці $$$")
    add_feature("Schrodinger's cat", "заплутаний")

    # print("\n $$$ Видалення за імʼям $$$")
    # delete_by_name("Vaska")

    # print("\n $$$ Видалення усіх котів")
    # delete_all()