import math

# Coinis_homework_1

#----------------------------------------------------------------

# #task_1
# Napisati program koji racuna površinu i obim pravougaonika.

# def task_1(weight,height):

#     square = weight * height
#     perimeter = (weight + height) * 2

#     print(f"Square - {square} : Perimeter - {perimeter}")


# task_1(int(input('Enter variable for weight: ')),int(input('Enter variable for height: ')))

#----------------------------------------------------------------

# task_2
#  Napisati program koji koristi tri varijable a, b i c, a racuna vrijednosti x1 i x2 kvadratne jednacine ax^2 + bx + c = 0. Zanemariti slučaj negativnih vrijednosti ispod korijena (kompleksni brojevi).
# def task_2(a, b, c):
#     # ax^2 + bx + c = 0

#     d = pow(b, 2) - (4 * a * c)

#     if d < 0:
#         print("wrong discriminant!")
#     else:
#         x1 = (-b + math.sqrt(d)) / (2 * a)
#         x2 = (-b - math.sqrt(d)) / (2 * a)
#         print(f"x1 = {x1} , x2 = {x2}")


# task_2(
#     int(input("Enter variable for a: ")),
#     int(input("Enter variable for b: ")),
#     int(input("Enter variable for c: ")),
# )

#----------------------------------------------------------------

# task_3
# napisati program koji racuna razliku kvadrata.
# def task_3(a,b):

#     x = (pow(a,2) - pow(b,2))

#     print(f'x = {x}')

# task_3(
#     int(input("Enter variable for a: ")),
#     int(input("Enter variable for b: ")),
# )

#----------------------------------------------------------------

# task_4
# # Sportista se na početku treninga zagrijeva tako što trči po ivicama pravougaonog terena dužine d i širine s. Napisati program kojim se određuje koliko metara pretrči sportista dok obiđe teren 4 puta.
# def task_4(d, s):
#     p = ((d + s) * 2) * 4
#     print(f"{p} m")


# task_4(int(input("Enter variable d: ")), int(input("Enter variable s: ")))

#----------------------------------------------------------------

#task_5
# Napisati program koji na osnovu zadate širine i visine lista papira (pravougaonog oblika) u milimetrima određuje njegovu površinu u kvadratnim centimetrima.

# def task_5(a,b):
#     p = (a*b)/10
#     print(f"{p} cm")


# task_5(int(input("Enter variable a: ")), int(input("Enter variable b: ")))

#----------------------------------------------------------------

#task_6
# Napisati program koji racuna kvadrat trinoma(a, b, c) koja za unijete parametre a, b i c računa kvadrat trinoma za unešene parametre. Formula: 𝑎^2 + 𝑏^2 + 𝑐^2 + 2𝑎𝑏 + 2𝑎𝑐 + 2𝑏c

# def task_6(a,b,c):
#     result = pow(a,2) + pow(b,2) + pow(c,2) + 2*a*b + 2*a*c + 2*b*c
#     print(f'Result {result}')


# task_6(int(input("Enter variable a: ")), int(input("Enter variable b: ")),int(input("Enter variable c: ")))

#----------------------------------------------------------------

#task_7
