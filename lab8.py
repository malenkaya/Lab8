#hello guys

# Самат начинаю функцию
"""
def summa(a , b):
    return a+b

a = int(input("Введите первое число : "))
b = int(input("Введите второе число : "))
print("Сумма двух чисел = ",summa(a,b))
"""
# Добавляем новуя функция и перемещяем его в новую ветку
def intervalArray(a,b):
    A = set()
    for i in range(a,b+1):
        A.add(i)
    return sorted(A)


a = int(input("Введите начальную точку : "))
b = int(input("Введите окончательную точку : "))
print(intervalArray(a,b))