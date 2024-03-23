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

# def avarage_point():
#     students = [
#         {
#             'name': 'Alexa',
#             'lesson_name': 'Math',
#             'average_point': 10
#         },
#         {
#             'name': 'John',
#             'lesson_name': 'Math',
#             'average_point': 8.5
#         },
#         {
#             'name': 'Leila',
#             'lesson_name': 'Informatics',
#             'average_point': 10
#         },
#         {
#             'name': 'Nika',
#             'lesson_name': 'Informatics',
#             'average_point': 7
#         },
#     ]

#     filtered_students = lambda lesson: filter(lambda x: x['lesson_name'] == lesson, students)
    
#     lesson_averages = lambda lesson: map(lambda x: x['average_point'], filtered_students(lesson))
    
#     average_points = lambda lesson: reduce(lambda x, y: x + y, lesson) / len(lesson)
    
#     unique_lessons = set(student['lesson_name'] for student in students)
    
#     for lesson in unique_lessons:
#         lesson_avg = average_points(list(lesson_averages(lesson)))
#         print(f"Average point for {lesson}: {lesson_avg}")

# avarage_point()

#________________________________________________________________
#Task 6

# def calculate_difference(time_series):
#     differences = list(map(lambda x, y: y - x, time_series[:-1], time_series[1:]))
#     return differences


# time_series = [10, 15, 20, 18, 25, 30]

# differences = calculate_difference(time_series)
# print("Differences between successive::", differences)

#________________________________________________________________
#Task 7

# def calculate_frequency(elements):
    
#     element_counts = map(lambda x: (x, elements.count(x)), elements)
    
#     merged_counts = reduce(lambda x, y: {**x, **y}, (dict([pair]) for pair in element_counts))
    
#     return merged_counts

# elements_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# frequency_dict = calculate_frequency(elements_list)
# print("The sum of the elements:", frequency_dict)


#________________________________________________________________
#Task 8