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


# ----------------------------------------------------------------
# task_51

# def task_51(password):

#     lower = False
#     upper = False

#     if len(password)< 100:
#         for i in range(len(password)):
#             if password[i].islower():
#               lower = True
#             elif password[i].isupper():
#               upper = True
#         if not (password.isdigit()) and (lower == True) and (upper == True):
#            print(f"Your password is valid")
#         else:
#             print(f"Your password is not invalid")
#     else:
#         print(f"Your password is too long")

# task_51(input("Enter your password: "))

# ----------------------------------------------------------------
# task_52

# def task_52(a,pre,suf,num):

#     new_string = ''
#     i = 0

#     while i < num:
#         new_string += pre
#         i+=1;
#     new_string += a
#     for j in range(num):
#         new_string += suf
#     print(new_string)

# task_52(
#     input('Enter text: '),
#     input('Enter prefix: '),
#     input('Enter sufix:'),
#     int(input('Enter number: '))
# )

# ----------------------------------------------------------------
# task_53

# def task_53(n):
#     sum = 0

#     for i in range(len(n)):
#         sum += int(n[i])

#     print(sum)


# task_53(input("Enter number: "))

# ----------------------------------------------------------------
# task_54

# def task_54(n, index):
#     length = len(n)

#     if index == 0:
#         if n[1] == "1":
#             print("First symbol, next is occupied")
#         else:
#             print("First symbol, next is free")
#     elif index == length - 1:
#         if n[index - 1] == "1":
#             print("Last symbol, previous is occupied")
#         else:
#             print("Last symbol, previous is free")
#     else:
#         if n[index - 1] == n[index + 1] and n[index - 1] == "1":
#             print("neighboring symbols is occupied")
#         else:
#             print(Neighboring symbols is free")

# task_54(input("Enter string: "), int(input("Enter index: ")))

# ----------------------------------------------------------------
# task_55

# def task_55(h, o):

#     max = h // 2
#     print(f"Max: {max}")

# task_55(int(input("Enter H: ")), int(input("Enter O: ")))

# ----------------------------------------------------------------
# task_56

def 