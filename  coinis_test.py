import math
import random

# #task_1a

# def task_1a(width, height):
#     p = width * height
#     kv = p/100
#     print(f"Povrsina je {kv} ^2m")

# task_1a(int(input("Enter Width: ")), int(input("Enter Height: ")))


# task_1b

# def task_1b(n, x):

#     x = x + (x * 0.15)

#     if n >= x:
#         print(f"Broker can buy action")
#     else:
#         print(f"Broker can't buy action, because broker have {n}: price {x}")


# task_1b(int(input("Enter N eusros: ")), int(input("Enter X price: ")))


# task_2a


# def task_2a(str):
#     N = str.split(' ')
#     samoglas = ['a', 'e', 'j', 'i', 'o','q','y','u']

#     for i in range(len(N)):
#      str = N[i]
#      print(str)
#      for i in range(len(samoglas)):
#       f = samoglas[i]
#       if f in str[0]:
#         if len(N[i+1]) == 5:
#          print(f"samoglas - {N[i+1]}")

# task_2a(input("Enter string: "))


# task_2b


def task_2b():

    alphavit = [
        "Hello World",
        "World hi",
        "Be desarest",
        "Like sunrise",
        "after night",
        "Moon Light",
        "Right side",
        "Left siders",
        "Big moon",
        "Small body",
    ]
    k = 0
    i = 0

    for i in range(a):
        word = " "
        word = random.choice(alphavit)

        for i in range(0, random.randint(5, 15)):
            while k < i:
                u = word + random.choice(alphavit)
                print(u)
        print(i)


task_2b()  # - not complite


# # task3


# def task3(string):
#     N = string.split(" ")
#     all = 0

#     for i in range(len(N)):
#         str = N[i]
#         print(str)
#         if "S" == str[0]:
#             s = int(str[1:])
#             print(f"buy - {s}")
#             all += s

#         elif "B" == str[0]:
#             s = int(str[1:])
#             print(f"sell - {s}")
#             all -= s

#     print(f"total: {all}")


# task3(input("Enter S B: "))


# # task4


# def task4(string):
#     N = string.split(" ")
#     zbir = 0

#     for i in range(len(N)):
#         str = N[i]
#         print(str)
#         if "0" == str[0]:
#             if "x" == str[1]:
#              zbir += 1


#     print(f"total: {zbir}")


# task4(input("Enter S B: "))


# # task5
