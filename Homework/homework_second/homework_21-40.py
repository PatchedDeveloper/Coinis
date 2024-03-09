import math
import random
from error_handling import Enum


# Coinis_homework_2 by Danila Kardasehvskii

# Domaći zadatak 2

# ----------------------------------------------------------------
# task_21

# def task_21(x):

#     if x<= -7:
#         y  = -2*x + (7/2)
#         print(y)
#     elif -7< x <1:
#         y = (pow(x,2)-3*x + 5)/(pow(x,2)+ 2)
#         print(y)
#     elif 1< x < 8:
#        y =  math.sqrt(pow(x,2)+2*x + 2) + math.sqrt(abs((3/2)*x - (4/7)))
#        print(y)
#     elif x>8:
#         y= abs((3/pow(x,2)) -11*x)
#         print(y)
#     else:
#         print(Enum.wrong_task.value)
# task_21(
#     int(input('Enter x: '))
# )

# ----------------------------------------------------------------
# task_22

# def task_22(x, y):
#     if x > 0 and y > 0:
#         print("I quadrant")
#     elif x < 0 and y > 0:
#         print("II quadrant")
#     elif x < 0 and y < 0:
#         print("III quadrant")
#     elif x > 0 and y < 0:
#         print("IV quadrant")
#     elif not (x == 0 and y != 0) and not (y == 0 and x != 0):
#         print("Lies on the origin")


# task_22(int(input("Enter x: ")), int(input("Enter y: ")))

# ----------------------------------------------------------------
# task_23


# ----------------------------------------------------------------
# task_24


# def task_24(text):

#     if len(text) > 30:
#         short_text = text[:27] + "..."
#         print(short_text)
#     else:
#         print(text)

# task_24(input("Enter text: "))


# ----------------------------------------------------------------
# task_25

# def task_25(text):

#     print("New text:", text[1:-1])

# task_25(
#     input('Enter text:')
# )

# ----------------------------------------------------------------
# task_26


# def task_26(num):

#     if num.startswith("0b"):
#         print("Binary number")
#     elif num.startswith("0o"):
#         print("Octal number")
#     elif num.startswith("0x"):
#         print("Hexadecimal number")
#     else:
#         print("Decimal number")


# task_26(input("Enter number: "))

# ----------------------------------------------------------------
# task_27


# def task_27(str):
#     samoglas = ["a", "e", "i", "o","u"]

#     for char in str:
#         if char in samoglas:
#             print("Yes, there are vowels here")
#             break
#         else:
#             print("No there are no vowels here")
#             break


# task_27(input("Enter string: "))

# ----------------------------------------------------------------
# task_28

# def task_28(str,target):

#     if str.endswith(target):
#         print('Yes')
#     else:
#         print('No')

# task_28(
#     input('Enter string: '),
#     input('target: ')
# ,
# )

# ----------------------------------------------------------------
# task_29

# def task_29(string):

#     if string.isdigit():
#         for char in string:
#             if char != "0" and char != "1":
#                 print("No, it's not binary number")
#                 return
#         print("Yes it's binary number")
#     else:
#         print("Not a number")

# task_29(input("Enter string: "))


# ----------------------------------------------------------------
# task_30

# def task_30(n):

#     sum = 0
#     multiply = 1
#     count_even = 0
#     count_odd = 0

#     for i in range(1, n+1):
#         if i % 2 == 0:
#             sum += i
#             count_even += 1
#         else:
#             multiply *= i
#             count_odd += 1

#     print("Sum of even numbers from 1 to", n, ":", sum)
#     print("Product of odd numbers from 1 to", n, ":", multiply)
#     print("Number of even numbers:", count_even)
#     print("Number of odd numbers:", count_odd)

# task_30(int(input("Enter number n: "))
# )

# ----------------------------------------------------------------
# task_31


# def task_31(start, end):

#     total_sum = 0

#     for num in range(start, end + 1):
#         if num % 2 == 0 and num % 4 != 0:
#             total_sum += pow(num, 2)

#     print("Sum, in the range ", start, "to", end, "=", total_sum)


# task_31(int(input("Enter the initial value: ")), int(input("Enter the final value: ")))

# ----------------------------------------------------------------
# task_32

# def task_32(a, b, divisor):

#     sum_divisible = 0
#     count_divisible = 0

#     for num in range(a + 1, b):
#         if num % divisor == 0:
#             sum_divisible += num
#             count_divisible += 1

#     print("Sum", sum_divisible)
#     print("Count Divisible", count_divisible)


# task_32(
#     int(input("Enter the value of a: ")),
#     int(input("Enter the value of b: ")),
#     int(input("Enter the divisor: ")),
# )

# ----------------------------------------------------------------
# task_33


# def task_33(number):

#     total_sum = 0
#     for i in range(0,number+1):
#         total_sum += int(i)
#     print("Sum :", total_sum)

# task_33(int(input("Enter number: ")))

# ----------------------------------------------------------------
# task_34

# def task_34(string):
#     multiply = 1

#     digits = [int(char) for char in str(string) if char.isdigit()]
#     if digits:

#         for digit in digits:
#             multiply *= digit
#         print("Multiply = :", multiply)
#     else:
#         print("Str don't have digits.")


# task_34(input("Enter str: "))

# ----------------------------------------------------------------
# task_35

# def task_35(text):

#     digit_string = ""

#     for char in text:
#         if char.isdigit():
#             digit_string += char
#     integer_result = int(digit_string)

#     print("Digit string :", integer_result)

# task_35(input('Enter Text: '))

# ----------------------------------------------------------------
# task_36


# def task_36(s):
#     encrypted_string = ""
#     consonants = set("bcdfghjklmnpqrstvwxyz")

#     for char in s:
#         if char in consonants:
#             encrypted_string += "0"
#         else:
#             encrypted_string += "1"

#     print(encrypted_string)


# task_36(input("Enter string: ").lower())

# ----------------------------------------------------------------
# task_37

# def task_37():
#     def calculate_score(text):
#         score = 0
#         for char in text:
#             if char == "1":
#                 score += 1
#             elif char == "0":
#                 score += 0
#             elif char == "*":
#                 score -= 1
#         return score

#     random_string = "".join(random.choices(["1", "0", "*"], k=10))

#     print("Generated string:", random_string)

#     player_score = calculate_score(random_string)

#     print("Result players:", player_score)

#     if player_score > 0:
#         print("Player in +.")
#     elif player_score == 0:
#         print("Player in 0.")
#     else:
#         print("Player in -.")

# task_37()


# ----------------------------------------------------------------
# task_38

# def task_38(s):
#     encrypted_string = ""

#     for char in s:
#         if char.isdigit():
#             num = int(char)
#             if num % 2 == 0:
#                 encrypted_string += "0"
#             else:
#                 encrypted_string += "1"

#     print(encrypted_string)


# task_38(input('Enter string: '))

# ----------------------------------------------------------------
# task_39

# def task_39(number):
#     num_str = str(number)
#     num_digits = len(num_str)

#     digit_sum = sum(int(digit) ** num_digits for digit in num_str)

#     if digit_sum == number:
#         print("Yes")
#     else:
#         print("No")


# task_39(int(input("Enter number: ")))

# ----------------------------------------------------------------
# task_40

# def task_40():

#     numbers = [-2, 7, -5, 3, 1, -4]
#     total_sum = 0

#     for num in numbers:
#         if num < 0 and num % 2 == 0:
#             total_sum += abs(num)
#     print("Output:", total_sum)

# task_40()
