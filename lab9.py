# #1 нефункциональная функция
# def rectangle():
#     a = float(input("Ширина: "))
#     b = float(input("Высота: "))
#     print("Площадь: %.2f" % (a*b))
 
# def triangle():
#     a = float(input("Основание: "))
#     h = float(input("Высота: "))
#     print("Площадь: %.2f" % (0.5 * a * h))
 
# def circle():
#     r = float(input("Радиус: "))
#     print("Площадь: %.2f" % (3.14 * r**2))
 
# figure = input("1-прямоугольник, 2-треугольник, 3-круг: ")
# if figure == '1':
#   rectangle()
# elif figure == '2':
#   triangle()
# elif figure == '3':
#   circle()
# else:
#   print("Ошибка ввода")

# #1 функционалная функция
# def Reverse(s):
#     s2 = ''
#     i = len(s)-1
#     while i>=0:
#         s2 = s2 + s[i]
#         i = i-1
#     return s2

# s1 = "abcdef"
# s2 = Reverse(s1) 
# print("s2 = ", s2)


# import math

# def SquareTriangle(a,b,c):
#     if (((a+b)<c) or ((b+c)<a) or ((a+c)<b)):
#         return None
#     else:
#         p = (a+b+c)/2 
#         s = math.sqrt(p*(p-a)*(p-b)*(p-c))
#         return s

# s = SquareTriangle(5,4,5)

# if (s==None):
#     print("The values of a, b, c is incorrect.")
# else:
#     print("s = ", s)

# #2
# def has_permission(page):
#     def permission(username):
#         if username.lower() == "admin":
#           return f"'{username}' has right to open {page}."
#         else:
#              return f"'{username}' does not have right to open {page}."
#     return permission

# check_admin_page_permision = has_permission("Admin Page")
# print (check_admin_page_permision ("dilnaz"))


# #3
# def x_dict(list1, list2):
#     a = {}
#     for x, y in zip(list1, list2):
#         a.update(dict([(x, y)]))
#     return a


# print(x_dict(['Elliot', 'Spencer', 'John'], ['01/01/2000', '09/10/1999', '21/12/1990']))

# #4
# def square(number):
#     return number ** 2

# numbers = [1, 2, 3, 4, 5]
# squared = list(map(square, numbers))
# print(squared)


# students_gpa = [3.6, 4.0, 2.8, 4.9, 2.6, 4.0, 1.8, 2.4, 3.1, 1.5]

# def filteer(a):
#     return a > 2.5

# gpa = list(filter(filteer, students_gpa))

# print(gpa)

# from functools import reduce

# numbers = [1,2,3,4,5,6,7,8,9,10]

# def custom_sum(first, second):
#     return first + second

# result = reduce(custom_sum, numbers)
# print(result)