class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

import json
with open('cat_list.json', encoding='utf8') as f: #загружаем список кошек из файла
    cats = json.load(f) #присваваем полученный список словарей переменной cats
    # print(cats)  # если нужно, проверяем что файл загрузился

for cat in cats:
    cat_obj = Cat(name=cat.get("name"),
                  gender=cat.get("gender"),
                  age=cat.get("age"))

    print(f'"Имя: {cat_obj.name},\tПол: {cat_obj.gender},\tВозраст: {cat_obj.age};')