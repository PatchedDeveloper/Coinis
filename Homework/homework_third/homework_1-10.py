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

# def find_longest_zigzag_subsequence(lst):
#     max_length = 0
#     length = 1
#     result = []
#     n = len(lst)

#     for i in range(n - 1):
#         if (i % 2 == 0 and lst[i] < lst[i + 1]) or (i % 2 == 1 and lst[i] > lst[i + 1]):
#             length += 1
#         else:
#             if length > max_length:
#                 max_length = length
#                 result = lst[i - length + 1 : i + 1]
#             length = 1

#     if length > max_length:
#         result = lst[n - length :]

#     return result

# lst = [3, 1, 4, 2, 8, 6, 5, 7]
# result = find_longest_zigzag_subsequence(lst)
# print(result)

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
# class Library:

#     class Book:
#         def __init__(self, name, author, year_publication, number_of_copies):
#             self.name = name
#             self.author = author
#             self.year_publication = year_publication
#             self.number_of_copies = number_of_copies

#     array_book = []

#     # setters
#     def add_new_book():
#         name = input("Enter book name: ")
#         author = input("Enter book author: ")
#         year_publication = input("Enter book year publication: ")
#         number_of_copies = int(input("Enter number of copies: "))

#         new_book = Library.Book(name, author, year_publication, number_of_copies)

#         Library.array_book.append(new_book)

#     def delete_book():
#         name = input("Enter book name what do you want delete: ")
#         for book in Library.array_book:
#             if book.name == name:
#                 Library.array_book.remove(book)
#                 print("Book deleted")
#                 break
#         else:
#             print("Book not found")

#     def edit_book():
#         name = input("Enter book name you want to change: ")

#         for book in Library.array_book:
#             if book.name == name:
#                 new_name = input(
#                     f"Enter new book name (if you don't want change - press enter): "
#                 )
#                 new_author = input(
#                     f"Enter new book author (if you don't want change - press enter): "
#                 )
#                 new_year_publication = input(
#                     f"Enter new year publication (if you don't want change - press enter): "
#                 )
#                 new_number_of_copies = input(
#                     f"Enter new number copies (if you don't want change - press enter): "
#                 )

#                 if new_name.strip():
#                     book.name = new_name
#                 if new_author.strip():
#                     book.author = new_author
#                 if new_year_publication.strip():
#                     book.year_publication = new_number_of_copies
#                 if new_number_of_copies.strip():
#                     book.number_of_copies = new_number_of_copies

#                 print("Book edited")
#                 break
#         else:
#             print("Book not found")

#     # getters
#     def get_all_books():
#         print("All books: ")
#         print("___________")
#         for book in Library.array_book:
#             print(
#                 f"Name :{book.name} \nAuthor: {book.author} \nYear publication: {book.year_publication} \nNumber Copies: {book.number_of_copies}"
#             )
#         print("___________")

#     def search_book_by_name():
#         name = input("Enter book name: ")
#         for book in Library.array_book:
#             if book.name == name:
#                 print(
#                     f"Name :{book.name} \nAuthor: {book.author} \nYear publication: {book.year_publication} \nNumber Copies: {book.number_of_copies}"
#                 )
#                 print("___________")
#         else:
#             print("Book not found")

#     def search_book_by_author():
#         author = input("Enter book name: ")
#         for book in Library.array_book:
#             if book.author == author:
#                 print(
#                     f"Name :{book.name} \nAuthor: {book.author} \nYear publication: {book.year_publication} \nNumber Copies: {book.number_of_copies}"
#                 )
#                 print("___________")
#         else:
#             print("Book not found")


# Library.add_new_book()
# Library.add_new_book()
# Library.get_all_books()
# Library.edit_book()
# Library.get_all_books()

# ----------------------------------------------------------------
# TASK 8

# # Player
# class Player:

#     def __init__(self, x, y, width, height, health):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.health = health

#     # Player
#     def add_player_parameters():
#         print("\nPlayer Parameters \n")
#         x = input("Enter x parameter for player: ")
#         y = input("Enter y parameter for player: ")
#         width = input("Enter width parameter for player: ")
#         height = input("Enter height parameter for player: ")
#         health = int(input("Enter health parameter for player: "))

#         if 0 <= health <= 100:
#             return Player(x, y, width, height, health)
#             print("Player parameters added")
#         else:
#             print("Error: player health parameter")
#             return None


# # Enemy

# # Array of enemies
# Enemies = []


# class Enemy:

#     def __init__(self, x, y, width, height, damage):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.damage = damage

#     def add_enemy_parameters():
#         print("\nEnemy Parameters \n")
#         x = input("Enter x parameter for enemy: ")
#         y = input("Enter y parameter for enemy: ")
#         width = input("Enter width parameter for enemy: ")
#         height = input("Enter height parameter for enemy: ")
#         damage = int(input("Enter damage parameter for enemy: "))

#         if 0 <= damage <= 100:
#             new_enemy = Enemy(x, y, width, height, damage)
#             Enemies.append(new_enemy)
#             return new_enemy
#         else:
#             print("Error: Enemy damage parameter")
#             return None


# # Functions for game
# def decreate_health(player_health, enemy_damage):
#     player_x = player_health.x
#     enemy_x = enemy_damage.x

#     def check_collision(player, enemy):
#         if player.x == enemy.x:
#             print("The players collided")
#             return True
#         else:
#             print("No collision")
#             return False

#     is_collision = check_collision(player_health, enemy_damage)

#     if is_collision:
#         player_health.health -= enemy_damage.damage
#         print(f"Health: {player_health.health}")
#         return player_health.health
#     else:
#         print("Miss")
#         return player_health.health


# def get_all_enemies():
#     print("All Enemies: ")
#     print("___________")
#     for enemy in Enemies:
#         print(
#             f"X coordinate: {enemy.x}\nY coordinate: {enemy.y}\nWidth: {enemy.width}\nHeight: {enemy.height}\nDamage: {enemy.damage}\n"
#         )
#     print("___________")


# player = Player.add_player_parameters()
# enemy1 = Enemy.add_enemy_parameters()
# enemy2 = Enemy.add_enemy_parameters()

# get_all_enemies()


# ----------------------------------------------------------------
# # TASK 9

# class Tournament:

#     def __init__(self, tournament_name, number_of_rounds):
#         self.tournament_name = tournament_name
#         self.player_list = []
#         self.number_of_rounds = number_of_rounds


#     #Getters
#     def get_tournament_name(self):
#         return self.tournament_name

#     def get_number_of_rounds(self):
#         return self.number_of_rounds

#     def get_player_list(self):
#         return self.player_list

#     #Setters
#     def set_tournament_name(self, tournament_name):
#         self.tournament_name = tournament_name

#     def set_player_list(self, player_list):
#         self.player_list = player_list

#     def set_number_of_rounds(self, number_of_rounds):
#         if 0 < number_of_rounds < 10:
#             self.number_of_rounds = number_of_rounds
#         else:
#             print("Error: Number of rounds must be between 1 and 9.")


#     # Functions

#     def add_player(self, player_name):
#         self.player_list.append((player_name, 0))

#     def remove_player(self, player_name):
#         for player in self.player_list:
#             if player[0] == player_name:
#                 self.player_list.remove(player)
#                 break

#     def show_leader(self):
#         if not self.player_list:
#             print("No players in the tournament.")
#             return

#         leader = max(self.player_list, key=lambda x: x[1])
#         print(f"The current leader is: {leader[0]} with {leader[1]} points.")

#     def start_round(self):
#         if len(self.player_list) < 2:
#             print("Need at least 2 players to start a round.")
#             return

#         player1, player2 = random.sample(self.player_list, 2)
#         winner = player1 if random.random() < 0.6 else player2

#         print(f"Round started between {player1[0]} and {player2[0]}.")
#         print(f"The winner is: {winner[0]}")
#         winner_index = self.player_list.index(winner)
#         self.player_list[winner_index] = (winner[0], winner[1] + 1)
#         print(f"{winner[0]} gained 1 point.")
#         self.number_of_rounds += 1

# tournament = Tournament("Chess Tournament", 5)
# tournament.add_player("Alice")
# tournament.add_player("Bob")
# tournament.add_player("Charlie")

# tournament.start_round()
# tournament.show_leader()


# ----------------------------------------------------------------
# # TASK 10


class Color:

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def validate_color(color):
        if 0 <= color <= 255:
            return color
        else:
            print("Error: Enter number between 0 до 255.")
            return 0

    def add_red(self, change):
        self.red = Color.validate_color(self.red + change)

    def add_green(self, change):
        self.green = Color.validate_color(self.green + change)

    def add_blue(self, change):
        self.blue = Color.validate_color(self.blue + change)

    def get_red(self):
        return self.red

    def get_green(self):
        return self.green

    def get_blue(self):
        return self.blue

    def it(self, other):
        if self.red < other.red and self.green < other.green and self.blue < other.blue:
            print("True")
            return True
        else:
            print("False")
            return False

    def eq(self, other):
        if (
            self.red == other.red
            and self.green == other.green
            and self.blue == other.blue
        ):
            print("True")
            return True
        else:
            print("False")
            return False

    def str(self):
        print(f"Red: {self.red}, Green: {self.green}, Blue: {self.blue}")


color1 = Color(50, 100, 150)
color2 = Color(50, 100, 150)
Color.str(color1)
Color.eq(color1, color2)


# ----------------------------------------------------------------
# # TASK 11
