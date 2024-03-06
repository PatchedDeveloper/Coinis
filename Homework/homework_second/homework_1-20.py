import math
from random import randint as rand
from error_handling import Enum


# Coinis_homework_2 by Danila Kardasehvskii

# Domaći zadatak 2

# ----------------------------------------------------------------
# task_1

# def task_1():
#     number = rand(-100, 100)

#     if number % 2 == 0:

#         print(f"Number = {number}, Door Open!")
#     else:
#         print(f"Number = {number}, Door Closed!")

# task_1()


# ----------------------------------------------------------------
# task_2


# def task_2(m, p):

#     if m > p:
#         print(f"Milosh win")
#     elif p > m:
#         print(f"Petar win")
#     else:
#         print(Enum.wrong_task.value)


# task_2(
#     int(input("How many apples did Milos collect? : ")),
#     int(input("How many apples did Petar collect? : ")),
# )

# ----------------------------------------------------------------
# task_3


# def task_3(v, w):

#     if v > 75 and w == 1:
#         print(f"Yes student can visited exams!")
#     elif v < 75 and (w == 0 or w == 1):
#         print(f"No student can visited exams!")
#     else:
#         print(Enum.wrong_task.value)


# task_3(
#     int(input("Visited in % : ")),
#     int(input("All works done? (1- True, 0 - False):  ")),
# )

# ----------------------------------------------------------------
# task_4

# def task_4(h):

#     if h > 24:
#         print(Enum.wrong_task.value)
#     elif (h <= 6 or h > 22) or (h >= 13 and h <= 17):
#         print("Yes, you can.")
#     else:
#         print("No, you can't.")


# task_4(int(input("Enter current hour: ")))

# ----------------------------------------------------------------
# task_5


# def task_5(first, second, third):

#     if first + second < third:
#         print("Triangle can't be constructed")
#     elif first + third < second:
#         print("Triangle can't be constructed")
#     elif second + third < first:
#         print("Triangle can't be constructed")

#     else:
#         print(Enum.wrong_task.value)


# task_5(
#     int(input("Enter first side")),
#     int(input("Enter second side")),
#     int(input("Enter third side")),
# )

# ----------------------------------------------------------------
# task_6

# def task_6(x, y):

#     if y == 2*x+5:
#         print('The bee is moving along the wire!')
#     else:
#         print('The bee is not moving on the wire.')


# task_6(
#     int(input("Enter X: ")),
#     int(input("Enter Y:")),
# )

# ----------------------------------------------------------------
# task_7


# def create_array(students):
#     array_students = []

#     for i in range(students):
#         math_grade = rand(0, 50)
#         programming_grade = rand(0, 50)
#         sum_points = math_grade + programming_grade
#         array_students.append((math_grade, programming_grade, sum_points))

#     return array_students


# def task_7(students):
#     array = create_array(students)
#     sum_points = [x[2] for x in array]
#     max_sum = max(sum_points)

#     if array.count(max_sum) > 1:
#         programming_points = [x[1] for x in array]
#         max_programming_points = max([x[1] for x in array])
#         winner = programming_points.index(max_programming_points) + 1
#     else:
#         winner = sum_points.index(max_sum) + 1

#     print(
#         f"{winner}\n",
#         array,
#     )


# task_7(int(input("Enter how many students wrote the test: ")))


# ----------------------------------------------------------------
# task_8

# def points_detection(point):

#     if point >= 4.5:
#         print('Excellent')
#     elif 4.5 > point >= 3.5:
#         print('Very good')
#     elif 3.5 > point >= 2.5:
#         print('Good')
#     elif 2.5 > point >= 2:
#         print('Satisfactory')


# def task_8(math,lang,prog):

#     points = (math + lang + prog) / 3

#     if math == 1 or lang == 1 or prog == 1:
#         print('Dissatisfaction')
#     else:
#         points_detection(points)


# task_8(int(input('Enter points by math: ')),int(input('Enter points by lang: ')),int(input('Enter points by prog: ')))

# ----------------------------------------------------------------
# task_9


def task_9():

    print("Enter window parametrs {\n}")
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))
    print("Enter curtain parametrs {\n}")
    x3 = int(input("Enter x1: "))
    y3 = int(input("Enter y1: "))
    x4 = int(input("Enter x2: "))
    y4 = int(input("Enter y2: "))



    aw = x2-x1
    bw = y2 - y1

    ac = pow((x4 - x3), 2)
    bc = pow((y4 - y3), 2)

    dw = math.sqrt(pow(aw,2) + pow(bw,2))
    dc = math.sqrt(ac + bc)

    if dc > dw:
        print("Yes")
    else:
        print("No")


task_9()
