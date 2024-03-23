import math

# name = 'Ivan'

# def a():
#     name = 'Marko'

#     def b():
#         print('Zdravo', name)
    
#     b()

# a()

#________________________________________________________________

# class Post:
#     def __init__(self, id ,name, description = "Default description", author="Admin"):
#         self.__id = id
#         self.name = name
#         self.description = description
#         self.author = author

#     def get_id(self):
#         return self.__id
    
#     def set_id(self,number):
#         self.__id = number
#         return self.__id


# post_a = Post(1,'Danila', 'Student')

# print(post_a)
# print(type(post_a))
# print(isinstance(post_a, Post))
# print(post_a.get_id())
# post_a.set_id(10)
# print(post_a.get_id())


#________________________________________________________________

# class Circle:


#     def __init__(self, radius = 1):
#         self.radius = radius

#     def area(self):
#         return pi * self.radius ** 2
    

# circle = Circle.area()

# print(circle)

#________________________________________________________________

# class User:
#     def __init__(self):
#         print('User init')

#     def who_am_i(self):
#         print('I am user')

#     def login(self):
#         print('User login')


# class Admin(User):
    
#     def __init__(self):
#         User.__init__(self)
#         print('Admin init')
    
#     def who_am_i(self):
#         print("I am Admin")

#     def delete_user(self):
#         print('Admin delete user')


# user1= User()
# admin = Admin()


# print(user1.who_am_i())
# print(admin.who_am_i())
        

#________________________________________________________________

# class Rectangle:

#     def __init__(self, lenght, widgth):
#         self.lenght = lenght
#         self.widgth = widgth

#     def area(self):
#         return self.lenght * self.widgth
    
#     def perimeter(self):
#         return 2 * self.lenght + 2 * self.widgth
    
# class Square(Rectangle):

#     def __init__(self, lenght):
#         super().__init__(lenght, lenght)



#________________________________________________________________

# Dictionary_book = []

# class Book:

#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
    
#     def __str__(self):
#         return f'Naslov: {self.title} Author: {self.author} Pages: {self.pages}'

#     def __len__(self):
#         return self.pages

#     def __del__(self):
#         pass

#     def __gt__(self, second_book):
        
#         return self.pages > second_book.pages

        
# book1 = Book("hhhh", "wwwww", 13)
# book2 = Book("ssssss", "qqqqq", 7)

# Dictionary_book.append(book1)
# Dictionary_book.append(book2)

# print(book1 > book2)


#________________________________________________________________


f = open('*******/in_class/text.txt')
saderzaj = f.read()

redovi = saderzaj.split('\n')
print(redovi)
max_povrshina = 0
for red in redovi:
    stranice = red.split(',')
    print(stranice[0], stranice[1])

    if  stranice[0] == stranice[1]:
        povrshina == int(stranice[0]) * int(stranice[1])
        if povrshina > max_povrshina:
            max_povrshina = povrshina
