import math
from datetime import datetime

# Coinis_homework_1 by Danila Kardasehvskii

# ----------------------------------------------------------------

# Napisati program za euclide_distance((x1, x2), (y1, y2)) kojom se računa i vraća
# euklidsko rastojanje izmedju dvije tacke A i B. Tacka A par (x1, y1), dok je tačka B par
# (x2, y2).

# def task_11(x1,x2,y1,y2):
#     #A = (X1,Y1)
#     #B = (X2,Y2)
#     a = x1 - x2
#     b = y2 - y1

#     c= math.sqrt(pow(a,2) + pow(b,2))

#     print(f'{c}')
# task_11(
#     int(input("Enter x1: ")),
#     int(input("Enter x2: ")),
#     int(input("Enter y1: ")),
#     int(input("Enter y2: ")),
# )

# ----------------------------------------------------------------

# Kreirati algoritam koji računa koje godine je rođen Miloš ukoliko je poznato da danas ima
# N godina.

# def task_12(year):
#     currentyear = datetime.now().year
#     x1 = currentyear - year
#     print(f'Milosh have : {x1} ')

# task_12(int(input('Enter years: ')))

# ----------------------------------------------------------------

# Zamislite da ste dobili tajanstveno pismo sa mapom i uputstvima za pronalaženje
# skrivenog blaga. Uputstva su sljedeća: "Trebate da krenete od starog hrasta koji ima
# sledeću poziciju G (x1,y1). Onda trebate ići pravo do stare kuće koja se nalazi na poziciji
# K(x2,y2). Blago je zakopano u susjedstvu, gdje se nalazi kuća, i to desno od pozicije
# kuće za dvije pozicije, i ispod za tri pozicije.
# a. Izračunajte koordinate blaga.
# b. Izračunajte (vazdušno) rastojanje od hrasta do blaga.
# c. Izračunajte rastojanje od hrasta do blaga tako da morate obići i kuću.

# def task_13(x1,x2,y1,y2):

#     x3 = x2 + 2
#     y3 = y2 - 3

#     #distance

#     a = abs(x1-x3)
#     b = abs(y1-y3)

#     c= math.sqrt(pow(a,2) + pow(b,2))

#     x4 = abs(x1-x2)
#     y4 = abs(y1-y2)
#     i= math.sqrt(pow(x4,2) + pow(y4,2))

#     x5 = abs(x2-x3)
#     y5 = abs (y2-y3)
#     o= math.sqrt(pow(x5,2) + pow(y5,2))

#     Summ = i + o
#     print(f'Distance = {c}, Coordinate = {x3} : {y3}, rastojanije = {Summ} ')

# task_13(
#     int(input("Enter x1: ")),
#     int(input("Enter x2: ")),
#     int(input("Enter y1: ")),
#     int(input("Enter y2: ")),
# )

# ----------------------------------------------------------------

# task_14
# Kreirati program za procjenu cijene stana. Na ukupnu cijenu najviše utiču sledeći
# parametrI: njegova veličina, lokacija (5 puta više nego veličina) i dostupnost parkinga (10
# puta više nego lokacija). Cijena kvadrata je 1200e. Fiksna cijena učešća je 1000e. Sve
# vrijednosti varijabli se mogu pretvoriti u numeričke. (parking ima = 1, parking nema = 0;
# zona 1 = 3, zona 2 =2, zona 3 = 1)

# def task_14(size, zone, parking):

#     price_for_m2 = 1200
#     fixed_price = 1000

#     def solve_location(price_for_m2):
#         return size * 5

#     location = solve_location(price_for_m2)
#     parking = 10 * location

#     match zone:
#         case 1:
#             zone = 3
#         case 2:
#             zone = 2
#         case 3:
#             zone = 1

#     price = fixed_price + (size * price_for_m2) + location + (parking * zone)

#     print(f"Price : {price} euros")


# task_14(
#     int(input("Enter Size in mm^2 :")),
#     int(input("Enter Zone :")),
#     int(input("Parking :")),
# )


# ----------------------------------------------------------------

# # task_15
# def task_15(x1, y1, x2, y2, x3, y3):

#     a1 = abs(x1 - x2)
#     a2 = abs(y1 - y2)

#     b1 = abs(x2 - x3)
#     b2 = abs(y2 - y3)

#     c1 = abs(x1 - x3)
#     c2 = abs(y1 - y3)

#     first_diag_a = math.sqrt(pow(a1, 2) + pow(a2, 2))
#     second_diag_b = math.sqrt(pow(b1, 2) + pow(b2, 2))
#     third_diag_c = math.sqrt(pow(c1, 2) + pow(c2, 2))

#     p = (first_diag_a + second_diag_b + third_diag_c) / 2

#     s = math.sqrt(p * (p - first_diag_a) * (p - second_diag_b) * (p - third_diag_c))

#     print(f"S = {s}")


# task_15(
#     int(input("Enter x1: ")),
#     int(input("Enter y1: ")),
#     int(input("Enter x2: ")),
#     int(input("Enter y2: ")),
#     int(input("Enter x3: ")),
#     int(input("Enter y3: ")),
# )


# ----------------------------------------------------------------

# task_16

# Ako je cijena taksija za jedan kilometar 0.5e, a početna cijena je 1e, napisati kod koji za
# unijeti broj pređenih kilometara računa cijenu vožnje.

# def task_16(km):
#     start = 1
#     euro_km = 0.5

#     price = start + (km*euro_km)

#     print(f'Price : {price}')


# task_16(float(input('Enter km: ')))

# ----------------------------------------------------------------

# task_17

# Knjižara "Bukvarnica" je posebno mjesto gdje svaka knjiga ima svoju priču. Kako bi
# proslavili dolazak novog godišnjeg doba, knjižara je odlučila da uvede popust - svaka
# knjiga dobija popust koji se može otkriti samo uz pomoć programa. Kao pomoćnik u
# knjižari, vaš zadatak je da kreirate program koji će izračunati konačnu cijenu knjige
# nakon primijenjenog popusta.


# def task_17(book, discont):

#     newprice = book - (book * (discont/100))
#     print(newprice)


# task_17(int(input("Enter book Price: ")), int(input("Discont for book: ")))


# ----------------------------------------------------------------
# task_18

# Cijena konzole za igre PlayStation 5 je prvo porasla 10%, pa je smanjena 10%. Ako je
# poznata početna cijena konzole, napisati program koji određuje cijenu nakon tih
# promjena.

# def task_18(start_price):
#     a = start_price + (start_price * 0.10)
#     last_price = a - (a * 0.10)
#     print(f" before {a} :  \n after {last_price}")


# task_18(int(input("Enter start price  ")))

# ----------------------------------------------------------------
# task_19
# Napisati program koji za zadati trocifreni broj računa zbir cifara tog broja.

# def task_19(number):

#     first = int(number[0])
#     second = int(number[1])
#     third = int(number[2])

#     summ = first + second + third
#     print(summ)

# task_19(input("Enter 3-th number "))

# ----------------------------------------------------------------
# task_20
#Dobili ste zadatak da dešifrujete kod kojim se otvaraju tajna vrata. Otkrili ste da na
# osnovu poznatog trocifrenog broja možete pronaći kod koji otvara tajna vrata tako što od
# proizvoda cifara tog broja oduzmete zbir cifara istog broja.

# def task_20(number):

#     first = int(number[0])
#     second = int(number[1])
#     third = int(number[2])

#     summ = first + second + third
#     multiplication = first * second * third

#     result = multiplication - summ

#     print(result)


# task_20(input("Enter 3-th number "))
