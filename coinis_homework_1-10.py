import math

# Coinis_homework_1 by Danila Kardasehvskii

# ----------------------------------------------------------------

# #task_1
# Napisati program koji racuna površinu i obim pravougaonika.

# def task_1(weight,height):

#     square = weight * height
#     perimeter = (weight + height) * 2

#     print(f"Square - {square} : Perimeter - {perimeter}")


# task_1(int(input('Enter variable for weight: ')),int(input('Enter variable for height: ')))

# ----------------------------------------------------------------


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

# ----------------------------------------------------------------

# task_3
# napisati program koji racuna razliku kvadrata.
# def task_3(a,b):

#     x = (pow(a,2) - pow(b,2))

#     print(f'x = {x}')

# task_3(
#     int(input("Enter variable for a: ")),
#     int(input("Enter variable for b: ")),
# )

# ----------------------------------------------------------------

# task_4
# # Sportista se na početku treninga zagrijeva tako što trči po ivicama pravougaonog terena dužine d i širine s. Napisati program kojim se određuje koliko metara pretrči sportista dok obiđe teren 4 puta.
# def task_4(d, s):
#     p = ((d + s) * 2) * 4
#     print(f"{p} m")


# task_4(int(input("Enter variable d: ")), int(input("Enter variable s: ")))

# ----------------------------------------------------------------

# task_5
# Napisati program koji na osnovu zadate širine i visine lista papira (pravougaonog oblika) u milimetrima određuje njegovu površinu u kvadratnim centimetrima.

# def task_5(a,b):
#     p = (a*b)/10
#     print(f"{p} cm")


# task_5(int(input("Enter variable a: ")), int(input("Enter variable b: ")))

# ----------------------------------------------------------------

# task_6
# Napisati program koji racuna kvadrat trinoma(a, b, c) koja za unijete parametre a, b i c računa kvadrat trinoma za unešene parametre. Formula: 𝑎^2 + 𝑏^2 + 𝑐^2 + 2𝑎𝑏 + 2𝑎𝑐 + 2𝑏c

# def task_6(a,b,c):
#     result = pow(a,2) + pow(b,2) + pow(c,2) + 2*a*b + 2*a*c + 2*b*c
#     print(f'Result {result}')


# task_6(int(input("Enter variable a: ")), int(input("Enter variable b: ")),int(input("Enter variable c: ")))

# ----------------------------------------------------------------

# task_7

# Marko voli biciklizam. Pošto Marko zna da je važno biti hidratizovan, pije vodu na svakih sat vremena vožnje bicikla i to pola litara vode. Kao ulaz poznato je vrijeme u satima, a treba štampati broj litara koje će Marko popiti, zaokruženo na najmanju vrijednost (donje cijelo).

# def task_7(hours):

#     liters =  0.5 * hours
#     print(f'Time:{hours} -> Liters:{int(liters)}')

# task_7(float(input('Enter hours: ')))

# ----------------------------------------------------------------


# task_8
# Napisati program kojim se izračunava potrebna dužina trake za ivicu stoljnjaka kružnog
# oblika čija je površina P.

# def task_8(P):

#     pi = 3.14
#     R = math.sqrt(P * pi)
#     L = 2* pi * R
#     print(f'Result : {L}')


# task_8(int(input("Enter P: ")))

# ----------------------------------------------------------------

# task_9

# def task_9(d,s,r):
#     s = s+2*r
#     d = d+2*r

#     p = 2* (s+d)
#     print(f'P = {p}')


# task_9(int(input('Enter D: ')),int(input('Enter S: ')),int(input('Enter S: ')))


#----------------------------------------------------------------

# task_10
#Date su koordinate donje desne i gornje lijeve ivice zida (pravougaonik). Izračunati
# povrsinu i obim zida.

def task_10(x1, x2, y1, y2):
    a = x1 - x2
    b = y2 - y1

    p = (a + b) * 2
    s = a * b
    print(f"P = {p} :S = {s}")


task_10(
    int(input("Enter x1: ")),
    int(input("Enter x2: ")),
    int(input("Enter y1: ")),
    int(input("Enter y2: ")),
)
