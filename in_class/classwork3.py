import math

from functools import reduce


# def get_val():
#     while True:
#         try:
#             input_user = int(input("Enter num: "))
#         except Exception as e:
#             print(f"That error : {e}")
#         else:
#             print("Good num")
#             break
#         finally:
#             print("Block Completed")
#             print(input_user)


# get_val()


# def square(a):
#     return a * a


# l = lambda a: a * a


# print(square(2))
# print(l(2))


# def build_quadratic(a, b, c):
#     return lambda x: a * x * x + b * x + c


# f = build_quadratic(2, 3, -5)

# print(f(2))
# print(f(3))
# print(f(4))

# paper = [10, 15, 20, 23, 24, 28]

# double_element = filter(lambda x: x % 2 == 0, paper)

# print(list(double_element))


# city_temperature = [("Podgorica", 15), ("Nikshic", 20), ("Budva", 2), ("Bar", 30)]

# converted_Cel_to_Far = map(
#     lambda city: (city_temperature[0], (9 / 5) + city[1] + 32), city_temperature
# )

# lista_a = [10, 15, 20, 23, 24, 28]
# lista_b = [2, 3, 5, 3, 2, 4]

# list_c = list(map(lambda x, y: x + y, lista_a, lista_b))


# sum = reduce(lambda x, y: x + y, list_c)

# max = reduce(lambda x, y: max(lista_a), lista_a)

# print(max)

# a = [1, 2, 3]
# b = [4, 5, 6]

# c = zip(a, b)

# print(list(c))


# l = [True, False]
# print(all(l))
# print(any(l))


# l = ["Petar", "Stefan", "Danila", "Milos"]

# print(sorted(l))
# print(l)

planet = [("Merkur", 0.395), ("Venera", 0.72), ("Earth", 1)]

sort_distance = lambda planet: planet[1]
planet.sort(key=sort_distance, reverse=True)
print(planet)
