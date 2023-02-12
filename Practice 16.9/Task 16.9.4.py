class Customer:
    def __init__(self, first_name, last_name, city, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.balance = balance

    # согласно задания вывод данных в формате имя, фамилия, город клиента
    def getGuests(self):
        return f'{self.first_name} {self.last_name}, г. {self.city}'


# имеем данные Клиентов для корпоратива в виде словаря
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
    print(obj.getGuests())

# или можно так (2 вариант):
# задаем экземпляров класса с их данными-атрибутами
# customer_1 = Customer('Сергей','Галанин','Москва',150)
# customer_2 = Customer('Владимир','Шахрин','Екатеринбург',175)
# customer_3 = Customer('Сергей','Чиграков','Санкт-Петербург',200)

# список гостей получается такой:
# guests_list=[customer_1,customer_2,customer_3]

# перебираем список циклом, принтуем значения прогнав их через функцию класса.
# for guest in guests_list:
#     print(guest.getGuests())