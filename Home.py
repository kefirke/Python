per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input('Введите сумму вклада (рублей): '))
deposit = []
for key in per_cent:
    deposit.append(money*per_cent[key]/100)
    print(key, 'процент по депозитам=', deposit[-1])
print(deposit)
max_deposit = max(deposit)
print('Максимальная сумма, которую можно заработать:', max_deposit)
