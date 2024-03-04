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