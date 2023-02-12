class Customer:
    def __init__(self, first_name, last_name, city, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.balance = balance

# имеем данные Клиентов в виде словаря
customers = [
    {"first_name": "Сергей",
     "last_name": "Галанин",
     "city": "Москва",
     "balance": "150"
},
     {"first_name": "Владимир",
     "last_name": "Шахрин",
     "city": "Екатеринбург",
     "balance": "175"
},
    {"first_name": "Сергей",
     "last_name": "Чиграков",
     "city": "Санкт-Петербург",
     "balance": "200"
}
]
# достаем данные каждого клиента из словаря
for customer in customers:
    obj = Customer(first_name = customer.get("first_name"),
                  last_name = customer.get("last_name"),
                  city = customer.get("city"),
                   balance = customer.get("balance"))

    # выводим результат в формате имя, фамилия, город и баланс клиента
    print(obj.first_name, obj.last_name,".",obj.city,".", "Баланс:", obj.balance, "руб.")
