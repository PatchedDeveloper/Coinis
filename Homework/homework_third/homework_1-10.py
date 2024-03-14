import math
import random
import re

# Coinis_homework_3

# Domaći zadatak 3


# ----------------------------------------------------------------
# TASK 1

# def get_words_with_end_letter(words,key):

#     split_sentences = re.split(r"[.!?]", words)[:-1]
#     new_array_with_words = []

#     # first cycle
#     for i in split_sentences:
#         words = i.split()
#         print(words)

#         time_array = []
#         # second cycle
#         for j in words:
#             if j[-1] == key:
#                 time_array.append(j)
#         time_array.append(len(time_array))
#         time_array = tuple(time_array)
#         new_array_with_words.append(time_array)
#     print(new_array_with_words)

# get_words_with_end_letter(
#     input("Enter Text: ")
#     input("Enter Key: ")
# )

# ----------------------------------------------------------------
# TASK 2

# def count_of_sets():

#     a = [1, 2, 2, 2, 4, 4]

#     max_product = 1
#     max_repeat_count = 1
#     number = 0

#     for i in range(len(a)):
#         repeat_count = 1
#         for k in range(i+1, len(a)):
#             if a[k] == a[i]:
#                 repeat_count += 1
#                 number = a[k]
#             else:
#                 break
#         product = pow(a[i],repeat_count)
#         if product > max_product:
#             max_product = product
#             max_repeat_count = repeat_count

#     print("Max product:", max_product)
#     print("Number of repetitions:", max_repeat_count," Number : ", number)


# count_of_sets()

# ----------------------------------------------------------------
# TASK 3


# ----------------------------------------------------------------
# TASK 4

# def repeater_symbols():
#     a = "aabaaaccccc"
#     max_count = 0
#     current_count = 1

#     for i in range(len(a) - 1):
#         if a[i] == a[i + 1]:
#             current_count += 1
#         else:
#             max_count = max(max_count, current_count)
#             current_count = 1

#     max_count = max(max_count, current_count)

#     print("Number of repetitions:", max_count)


# repeater_symbols()

# ----------------------------------------------------------------
# TASK 5

# def Podcasts():

#     podcast_array = [
#         {"name": "Science VS.", "num_pos": 600, "num_neg": 45},
#         {"name": "Español para principiantes", "num_pos": 1000, "num_neg": 10},
#         {"name": "Philophize This!", "num_pos": 500, "num_neg": 30},
#     ]
#     max = float("inf")
#     name_podcast = ""

#     for i in range(0, len(podcast_array)):
#         for podcast in podcast_array:
#             mid_rate = podcast["num_pos"] / podcast["num_neg"]
#             if mid_rate < max:
#                 max = mid_rate
#                 name_podcast = podcast["name"]

#     return name_podcast

# print(Podcasts())
