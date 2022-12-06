# from random import randint
# import os
# from PIL import Image, ImageDraw
 
 
# def circles_generator(num_of_circles=5):

#     if not os.path.exists('circles'):
#         os.mkdir('circles')

#     for pic_name in range(1, num_of_circles + 1):
#         img = Image.new('RGB', (600, 600), (255, 255, 255))
#         draw = ImageDraw.Draw(img)
#         draw.rectangle((0, 0, 600, 600), fill=(randint(0, 255), randint(0, 255), randint(0, 255)))
#         img.save(f'circles/{pic_name}.png', quality=85)
 
 
# circles_generator()

# def read_last(lines, file):
#     if lines > 0:
#         with open(file, encoding='utf-8') as text:
#             file_lines = text.readlines()[-lines:]
#         for line in file_lines:
#             print(line.strip())
#         else:
#             print('Количество строк может быть только целым положительным')

 
# # Тесты
# read_last(4, 'article.txt')
# read_last(-5, 'article.txt')

# def longest_words(file):
#     with open(file, encoding='utf-8') as text:
#         words = text.read().split()
#         max_length = len(max(words, key=len))
#         sought_words = [word for word in words if len(word) == max_length]
#         if len(sought_words) == 1:
#             return sought_words[0]
#         return sought_words
 
 
# print(longest_words('article1.txt'))

# import os
 
# def print_docs(directory):
# 	all_files = os.walk(directory)
# 	for catalog in all_files:
#          print(f'Папка {catalog[0]} содержит:')
#          print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
#          print(f'Файлы: {", ".join([file for file in catalog[2]])}')
#          print('-' * 40) 
 
 
# print_docs('C:\Program Files\Dilnaz')