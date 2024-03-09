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


# def task_9():

#     print("Enter window parametrs {\n}")
#     x1 = int(input("Enter x1: "))
#     y1 = int(input("Enter y1: "))
#     x2 = int(input("Enter x2: "))
#     y2 = int(input("Enter y2: "))
#     print("Enter curtain parametrs {\n}")
#     x3 = int(input("Enter x1: "))
#     y3 = int(input("Enter y1: "))
#     x4 = int(input("Enter x2: "))
#     y4 = int(input("Enter y2: "))


#     aw = x2-x1
#     bw = y2 - y1

#     ac = pow((x4 - x3), 2)
#     bc = pow((y4 - y3), 2)

#     dw = math.sqrt(pow(aw,2) + pow(bw,2))
#     dc = math.sqrt(ac + bc)

#     if dc > dw:
#         print("Yes")
#     else:
#         print("No")


# task_9()

# ----------------------------------------------------------------
# task_10


# def task_10():

#     radius_darts = int(input("Enter radius dart:"))
#     dart_x = int(input("Enter dart x:"))
#     dart_y = int(input("Enter dart y:"))
#     target_x = int(input("Enter target x:"))
#     target_y = int(input("Enter target y:"))

#     # radius
#     d = math.sqrt(pow(target_x, 2) + pow(target_y, 2))

#     if (dart_x - radius_darts <= target_x <= dart_x + radius_darts) and (dart_y - radius_darts <= target_y <= dart_y + radius_darts):
#         if d <= radius_darts:
#          print("Good shot!")
#         else:
#             print("Miss shot!")

#     else:
#         print("Arrow not in range")


# task_10()

# ----------------------------------------------------------------
# task_11


# def task_11():
#     # Ant
#     ant_x = int(input("Enter ant x: "))
#     ant_y = int(input("Enter ant y: "))

#     # A point
#     ax = int(input("Enter A x: "))
#     ay = int(input("Enter A y: "))

#     # B point
#     bx = int(input("Enter B x: "))
#     by = int(input("Enter B y: "))

#     # C point
#     cx = ax
#     cy = by

#     # D point
#     dx = bx
#     dy = ay

#     if (ax <= ant_x <= bx or bx <= ant_x <= ax) and (ay <= ant_y <= cy or cy <= ant_y <= ay):
#         if (cx <= ant_x <= dx or dx <= ant_x <= cx) and (by <= ant_y <= dy or dy <= ant_y <= by):
#             print("yes")
#         else:
#             print("no")
#     else:
#         print("no")

# task_11()

# ----------------------------------------------------------------
# task_12

# def task_12(str_num):

#     if int(str_num[0]) > int(str_num[1]):
#         print(print(int(str_num[0]) - int(str_num[1])))

#     elif int(str_num[0]) < int(str_num[1]):
#         print(print(int(str_num[1]) + int(str_num[0])))

#     else:
#         print(print(int(str_num[1]) * int(str_num[0])))


# task_12(input('Enter number: '))

# ----------------------------------------------------------------
# task_13

# def task_13(radius_1,radius_2):

#     pi = 3.14
#     if radius_1 > radius_2:
#             result =  3.12 * pow (radius_1,2)
#             print(f'S for First  = {result} ')
#     elif radius_1 < radius_2:
#             result =  3.12 * pow (radius_2,2)
#             print(f'S for Second  = {result} ')
#     else:
#            print('They are equal')

# task_13(int(input('Enter radius for 1: ')),int(input('Enter radius for 2: ')))

# ----------------------------------------------------------------
# task_14

# def task_14(first,second,third):

#     x = first + second
#     y = first + third
#     z = second + third

#     if x < y and x < z:
#         print(f'Low is first + second {x}')
#     elif y < x and y < z:
#         print(f'Low is first + third {y}')
#     elif z < y and z < x:
#         print(f'Low is second + third {z}')

# task_14(int(input('Enter 1: ')),int(input('Enter 2: ')),int(input('Enter 2: ')))

# ----------------------------------------------------------------
# task_15

# def task_15(year):

#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print(f"{year} - leap year")
#     else:
#         print(f"{year} - is not a leap year")

# task_15(int(input('Enter year: ')))

# ----------------------------------------------------------------
# task_16

# def task_16(x1, y1, x2, y2, x, y):

#     if (x2>x>x1) and (y2<y<y1):
#         print("The point lies inside the rectangle.")
#     else:
#         print("The point does not lie inside the rectangle.")

# task_16(
# # rectangle
# int(input("Enter the x top-left : ")),
# int(input("Enter the y top-left : ")),
# int(input("Enter the x bottom-right : ")),
# int(input("Enter the y bottom-right : ")),

# # point
# int(input("Enter the x for point: ")),
# int(input("Enter the y for point: ")),

# )

# ----------------------------------------------------------------
# task_17


# def task_17(a, b):

#     if a + a <= b:
#         print("Yes you can")
#     else:
#         print("No you cannot")


# task_17(
#     int(input("Enter side a (height) : ")),
#     int(input("Enter side b (width) : ")),
# )

# ----------------------------------------------------------------
# task_18

# def task_18(temp):

#     if temp > 0 and temp < 100:
#      print('Above 0°C and below 100°C - liquid state')
#     elif temp <= 0:
#         print('Not above 0°C - solid state')
#     elif temp > 100:
#        print('Not below 100°C - gaseous state.')

# task_18(
#     int(input("Enter temperature : ")),
# )

# ----------------------------------------------------------------
# task_19

# def task_19(sum, points, reward):

#     if points == 5.0:
#         print(f"Discount 40%")
#         sum = sum - (sum * 0.40)
#         print(f'You need to pay : {sum}')
#     elif 4.0 <= points < 5.0:
#         if reward == 1:
#             print(f"Discount 30%")
#             sum = sum - (sum * 0.30)
#             print(f'You need to pay : {sum}')
#         else:
#             print(f"Discount 20%")
#             sum = sum - (sum * 0.20)
#             print(f'You need to pay : {sum}')
#     elif 3.0 <= points < 4.0:
#         if reward == 1:
#             print(f"Discount 30%")
#             sum = sum - (sum * 0.30)
#             print(f'You need to pay : {sum}')
#         else:
#             print(f"Discount 10%")
#             sum = sum - (sum * 0.10)
#             print(f'You need to pay : {sum}')


# task_19(
#     float(input("Enter school sum :")),
#     float(input("Enter student middle point (2.0 - 5.0) :")),
#     int(input("Enter reward (1- Yes , 0 -No) :")),
# )

# ----------------------------------------------------------------
# task_20

def task_20(num):
    x = int(num[0])
    y = int(num[1])
    z = int(num[2])
    c = int(num[3])

    sum = 0
    multiply = 1

    if x % 2 == 0:
        sum += x
    else:
        multiply = multiply * x
    if y % 2 == 0:
        sum += y
    else:
        multiply = multiply * y
    if z % 2 == 0:
        sum += z
    else:
        multiply = multiply * z
    if c % 2 == 0:
        sum += c
    else:
        multiply = multiply * c

    print(f"Sum = {sum} , Multiplication = {multiply}")

task_20(
    input("Enter 4-th digit number : "),
)
