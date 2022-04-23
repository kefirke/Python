n = int(input("Сколько билетов вы хотите забронировать? - "))
print("Укажите возраст каждого посетителя")
sum = 0
for i in range(n):
    age = int(input("Возраст: "))
    if age < 18:
        sum += 0
        print("Проход бесплатный")
    elif 18 <= age < 25:
        sum += 990
    else:
        sum += 1390
print("Итого - ", sum, "рублей")
if n > 3:
    m = 0.9
else:
    m = 1
sum1 = sum * m
print("Итоговая сумма -", sum1, "рублей")
