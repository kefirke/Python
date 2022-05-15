class Client:
    def __init__(self, first_name, second_name, city, balance):
        self.first_name = first_name
        self.second_name = second_name
        self.city = city
        self.balance = balance

    def __str__(self):
        return f"'{self.first_name} {self.second_name}'. {self.city}. Баланс: {self.balance} руб."

    def get_guest(self):
        return f'{self.first_name} {self.second_name}, г. {self.city}'

client_1 = Client('Анна', 'Петрова', 'Москва', 50)
client_2 = Client('Иван', 'Сидоров', 'Тула', 45)
client_3 = Client('Петр', 'Иванов', 'Рязань', 30)

print(client_1)

guest_list = [client_1,client_2,client_3]
for guest in guest_list:
    print(guest.get_guest())

