import math
import random
from error_handling import Enum

# Coinis_homework_2 by Danila Kardasehvskii

# Domaći zadatak 2

# ----------------------------------------------------------------
# task_41

# def task_41():
#     lst = [1, 2, 3]
#     max_value = 3
#     count = 0

#     for num in lst:
#         if num < max_value:
#             count += 1
#     print("Output:", count)

# task_41()

# ----------------------------------------------------------------
# task_42

# ----------------------------------------------------------------
# task_43

# ----------------------------------------------------------------
# task_44

# def task_44():
#     visited = [232, 2322, 3232, 121, 232, 445, 767, 878, 564, 65]
#     max = 0
#     index = 0

#     for i in range(len(visited)):
#         if max < visited[i]:
#             max = visited[i]
#             index = i

#     print(f"max: {max} : day : {index+1}")

# task_44()

# ----------------------------------------------------------------
# task_45

# def task_45():
#     payment = [300, 599, 600, 700, 200, 500, 300, 800, 200, 741]
#     i = 0
#     sum = 0

#     for i in range(i, len(payment)):
#         if payment[i] >= 700:
#             sum += 1

#     print(f"Sum: {sum}")

# task_45()

# ----------------------------------------------------------------
# task_46

# def task_46():
#     payment = [500, 400, 300, 599, 600]
#     i = 0
#     sum = 0

#     sorted_salaries = sorted(payment, reverse=False)

#     print(f"Sum: {sorted_salaries}")
#     print(f"Sum: {sorted_salaries[1]}")


# task_46()

# ----------------------------------------------------------------
# task_47

# def task_47(first, second, third):

#     min = 0
#     max = 0

#     if first < second and first < third:
#         min = first
#     if second < first and second < third:
#         min = second
#     if third < first and third < second:
#         min = third

#     if first > second and first > third:
#         max = first
#     if second > first and second > third:
#         max = second
#     if third > first and third > second:
#         max = third

#     print(f"min: {min} max: {max}")


# task_47(
#     input("First:"),
#     input("Second:"),
#     input("Third:"),
# )

# ----------------------------------------------------------------
# task_48

# def task_48(x, n):
#     m = 1
#     for _ in range(n):
#         m *= x
#         print(m)


# task_48(
#     int(input("Enter x: ")),
#     int(input("Enter n: ")),
# )

# ----------------------------------------------------------------
# task_49


# def task_49(text, limit):

#     if len(text) > limit:
#         short_text = text[:limit] + "..."
#         print(short_text)
#     else:
#         print(text + "...")


# task_49(input("Enter text: "), int(input("Enter limit number: ")))


# ----------------------------------------------------------------
# task_50

# def task_50(s):
#     encrypted_string = ""
#     consonants = set("aeioиu")

#     for char in s:
#         if char in consonants:
#             encrypted_string += char
#         else:
#             continue

#     print(encrypted_string)


# task_50(input("Enter string: ").lower())
