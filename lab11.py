# import math

# num = -4.28
# a = 14
# b = 8
 
# num_list = [10, 8.25, 75, 7.04, -86.23, -6.43, 8.4]
# x = 1e-4 # Малое значение x
 
# print('Число:', num)
# print('Округление числа вниз:', math.floor(num))
# print('Округление числа вверх:', math.ceil(num))
# print('Модуль числа:', math.fabs(num))
# print('Наибольший общий делитель a и b: ' + str(math.gcd(a, b)))
# print('Сумма элементов списка: ' + str(math.fsum(num_list)))
# print('e^x (при использовании функции exp()) равно:', math.exp(x)-1)
# print('e^x (при использовании функции expml()) равно:', math.expm1(x))




# import random 
# import secrets

# print("Вывод случайного числа ")
# print(random.random())
# print("Вывод случайного целого числа ", random.randint(0, 9))
# print("Вывод случайного целого числа ", random.randrange(0, 10, 2))

# city_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
# print("Выбор случайного города из списка - ", random.choice(city_list))

# random.shuffle(city_list)
# print ("Вывод перемешанного списка ", city_list) 
 
# number = random.SystemRandom().random()
# print("Надежное число ", number)
 
# print("Надежный токен байтов", secrets.token_bytes(16))

import datetime

dt_now = datetime.datetime.now()
print(dt_now)

current_date_time = datetime.datetime.now()
current_time = current_date_time.time()
print(current_time)

timeobj= datetime.time(8,48,45)
print(timeobj)

first_date = datetime.date(2020, 10, 2)
second_date = datetime.date(2020, 10, 30)
delta = second_date - first_date
print(delta)

date_string = "11/17/20"
date_obj = datetime.datetime.strptime(date_string, '%m/%d/%y')
print(date_obj)
