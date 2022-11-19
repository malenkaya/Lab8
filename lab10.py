from functools import reduce
import operator

def inc(x):
            x = x + 1
            return x

print("Привет! Добро пожаловать в мир программирования! ")
print("Вместе со мной тебе будет легко запомнить информацию. Давайте начнем!")
print("Напиши 1 если хочешь вывести сам лист, \n2-вывести минимум листа, \n3-каждому элементу прибавить одно значение, \n4-развернуть порядок элементов в последовательности, \n5-выполнить переданную в качестве аргумента функцию для каждого элемента, \n6-сортировать лист, \n7-вычислить сумму, \n8-перенос на кортеж, \n9-возвращает строку, представляющую символ Unicode для переданного числа, \n10-перебор итерируемых объектов и последовательностей, \n11-ВЫХОД")

value = int(input("Пожалуйста, введите значение: "))


array = [5, 7, 8, 2, 5]

if(value==1):
    for x in array:
            print(x)
elif(value==2):
    print("Minimum: ", min(array))
elif(value==3):
    result = map(inc,array)
    for x in result:
            print(x)
elif(value==4):
    b = reversed(array)
    for x in b:
            print(x)
elif(value==5):
    print(reduce(operator.add,array))
elif(value==6):
    for x in sorted(array):
            print(x)
elif(value==7):
    print(sum(array))
elif(value==8):
    print(tuple(array))
elif(value==9):
    for x in array:
            print(chr(x))
elif(value==10):
    result = list(filter(lambda x: (x%2 != 0) , array))
    print(result)
elif(value==11):
    print("Вы хотите выйти. До скорой встречи!")
else:
    print("Такого действия к сожалению нету...")


