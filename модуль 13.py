tickets = int(input("Введите количество билетов: "))
visitors = tickets

sum = 0
while visitors != 0:
    age_for_ticket = int(input(f'Укажите возраст посетителя {visitors} ? '))
    if age_for_ticket < 18:
        print('Билет бесплатный')
    elif 25 > age_for_ticket >= 18:
        sum += 990
        print('Стоимость билета: 990 руб.')
    else:
        sum += 1390
        print('Стоимость билета: 1390 руб.')
    visitors -= 1

if tickets > 3:
    sale = sum - ((sum / 100) * 10)
    print(f'Сумма к оплате {sale} руб., с учетом скидки 10% за покупку более 3х билетов')
else:
    print(f'Сумма к оплате {sum} руб.')

