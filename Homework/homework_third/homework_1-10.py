import math
import random
import re


# Coinis_homework_3 by Danila Kardashevskii

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

# ----------------------------------------------------------------
# TASK 6

# class Tv:
#     current_chanel = 0  # to lenght
#     name_channel = ""  # enter name channel
#     all_channels = None  # all avarage channels
#     volume = 0

#     # initialize first start tv
#     def initialize():
#         Tv.current_chanel = 1
#         Tv.name_channel = "First"
#         Tv.all_channels = []
#         Tv.volume = 0

#     # GETTERS
#     # _______________________________________

#     # function for getting channel without errors
#     def get_current_chanel(num):
#         if (0 <= num) and (num <= len(Tv.all_channels)):
#             print(Tv.all_channels[num - 1])
#         else:
#             print("This channel not available")
#             return 1

#     # function for getting all channels
#     def get_all_channels():
#         return Tv.all_channels

#     # function for getting current name channel
#     def get_name_channel():
#         print("Current chanel : ", Tv.name_channel)

#     # Other functions
#     # _______________________________________

#     # function for set volume without errors
#     def set_volume(volume):
#         if 0 <= volume <= 10:
#             Tv.volume = volume
#             print(Tv.volume)
#         else:
#             print("This volume not available")
#             return 0

#     # function for addding new channel
#     def add_new_chanel(chanel):
#         Tv.all_channels.append(str(chanel))
#         print("Channel added")

#     # function fot delete channel
#     def delete_chanel(chanel_name):
#         Tv.all_channels.remove(chanel_name)
#         print("Deleted")

#     def volume_up():
#         if 0 <= Tv.volume < 10:
#             Tv.volume += 1
#         else:
#             Tv.volume = 10
#             print("Limit volume")

# Tv.initialize()
# Tv.add_new_chanel("First")
# Tv.add_new_chanel("Second")
# Tv.get_current_chanel(1)

# ----------------------------------------------------------------
# TASK 7
class Library:

    class Book:
        def __init__(self, name, author, year_publication, number_of_copies):
            self.name = name
            self.author = author
            self.year_publication = year_publication
            self.number_of_copies = number_of_copies

    array_book = []

    # setters
    def add_new_book():
        name = input("Enter book name: ")
        author = input("Enter book author: ")
        year_publication = input("Enter book year publication: ")
        number_of_copies = int(input("Enter number of copies: "))

        new_book = Library.Book(name, author, year_publication, number_of_copies)

        Library.array_book.append(new_book)

    def delete_book():
        name = input("Enter book name what do you want delete: ")
        for book in Library.array_book:
            if book.name == name:
                Library.array_book.remove(book)
                print("Book deleted")
                break
        else:
            print("Book not found")

    def edit_book():
        name = input("Enter book name you want to change: ")

        for book in Library.array_book:
            if book.name == name:
                new_name = input(
                    f"Enter new book name (if you don't want change - press enter): "
                )
                new_author = input(
                    f"Enter new book author (if you don't want change - press enter): "
                )
                new_year_publication = input(
                    f"Enter new year publication (if you don't want change - press enter): "
                )
                new_number_of_copies = input(
                    f"Enter new number copies (if you don't want change - press enter): "
                )

                if new_name.strip():
                    book.name = new_name
                if new_author.strip():
                    book.author = new_author
                if new_year_publication.strip():
                    book.year_publication = new_number_of_copies
                if new_number_of_copies.strip():
                    book.number_of_copies = new_number_of_copies

                print("Book edited")
                break
        else:
            print("Book not found")

    # getters
    def get_all_books():
        print("All books: ")
        print("___________")
        for book in Library.array_book:
            print(
                f"Name :{book.name} \nAuthor: {book.author} \nYear publication: {book.year_publication} \nNumber Copies: {book.number_of_copies}"
            )
        print("___________")

    def search_book_by_name():
        name = input("Enter book name: ")
        for book in Library.array_book:
            if book.name == name:
                print(
                    f"Name :{book.name} \nAuthor: {book.author} \nYear publication: {book.year_publication} \nNumber Copies: {book.number_of_copies}"
                )
                print("___________")
        else:
            print("Book not found")

    def search_book_by_author():
        author = input("Enter book name: ")
        for book in Library.array_book:
            if book.author == author:
                print(
                    f"Name :{book.name} \nAuthor: {book.author} \nYear publication: {book.year_publication} \nNumber Copies: {book.number_of_copies}"
                )
                print("___________")
        else:
            print("Book not found")


Library.add_new_book()
Library.add_new_book()
Library.get_all_books()
Library.edit_book()
Library.get_all_books()
