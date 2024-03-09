import math
import random

# ----------------------------------------------------------------
# task_1
# def sum_poz(list):

#     sum = 0
#     for i in range(0, len(list), 2):
#         if (type(list[i]) is int) and list[i] > 0:
#             sum += list[i]

#     return sum


# print(sum_poz([2, 3, 2, 1, 4, 5, 3, -2, -2, 1, "asd", "wq1",1]))

# ----------------------------------------------------------------
# task_2

# сделать задачу чтобы она сплитовала стрингу и складывала самую длинную строчку из цифер

# def lenght(str):

#     pom_sum = 0
#     max_sum = 0
#     max_substring = 0

#     new_var = ""

#     for i in range(0, len(str)):
#         if str[i].isdigit():
#             pom_sum += int(str[i])
#             pom_sub += i
#             if pom_sum > max_sum:
#                 max_sum = pom_sum
#                 max_substring = pom_sub
#         else:
#             pom_sum = 0
#             pom_sub = ""
#     return max_sum


# print(lenght("123b213b"))


def cinemas():

    films = [
        {
            "name": "Крестный отец",
            "rateUp": 1000,
            "rateDown": 10,
        },
        {
            "name": "Пионист",
            "rateUp": 500,
            "rateDown": 30,
        },
        {
            "name": "Красивый",
            "rateUp": 600,
            "rateDown": 45,
        },
        {
            "name": "Не Красивый",
            "rateUp": 520,
            "rateDown": 45,
        },
    ]
    max = 0

    for film in films:
        if film["rateUp"] > max:
            max = film["rateUp"]
            return film["name"]


print(cinemas())
