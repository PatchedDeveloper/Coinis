import math
import random
from functools import reduce

# Coinis_homework_2 by Danila Kardasehvskii

# Domaći zadatak 4

#________________________________________________________________
#Task 1

# def max_len():

#     lst = ['Flower','Flow','Flight']

#     max_len = reduce(lambda x,y: x if len(x) > len(y) else y , lst )
#     print((max_len))

# max_len()

#________________________________________________________________
#Task 2

# def student_point_filter():

#     students = ['Alexa', 'John', 'Nick', 'Michael']
#     points = [6,9,10,8.5]

#     #create 1 array with sutudent name and points
#     new_list = list(zip(students,points))
#     print(new_list) 
#     #lambda filter by points
#     students_hight = filter(lambda x: x[1] > 8.5 , new_list)
#     print(list(students_hight))

# student_point_filter()

#________________________________________________________________
#Task 3

# def sorted_students():

#     students = [
#         {
#             'name': 'Alexa',
#             'age': 19,
#             'avarage_point': 6
#         },
#           {
#             'name': 'John',
#             'age': 21,
#             'avarage_point': 8.5
#         },
#           {
#             'name': 'Igor',
#             'age': 43,
#             'avarage_point': 10
#         },
#           {
#             'name': 'Danila',
#             'age': 20,
#             'avarage_point': 10
#         },
#     ]

#     students_years = filter(lambda x: x['age'] > 21 , students)
#     students_points = sorted(students_years, key=lambda x: x['avarage_point'])

#     print(list(students_points))


# sorted_students()

#________________________________________________________________
#Task 4

# def str_counter():

#     lst = ['Hello world!', 'Python is cool', 'Functional programming rocks']

#     words = list(map(lambda x: x.split(' '), lst))
#     print(words)
#     counter = list(reduce(lambda x,y: x + y, words))
#     print(len(counter))

# str_counter()

#________________________________________________________________
#Task 5

def avarage_point():

        students = [
        {
            'name': 'Alexa',
            'lesson_name': 'Math',
            'avarage_point': 10
        },
          {
            'name': 'John',
            'lesson_name': 'Math',
            'avarage_point': 8.5
        },
          {
            'name': 'Alexa',
            'lesson_name': 'Informatics',
            'avarage_point': 10
        },
          {
            'name': 'John',
            'lesson_name': 'Informatics',
            'avarage_point': 7
        },
    ]
