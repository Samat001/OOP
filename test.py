# class Animal:
#     def __str__(self) -> str:
#         return self.name
    
#     def __init__(self,name) -> None:
#         self.name = name

#     def get_name(self):
#         return self.name

# cat = Animal("Barsik")
# dog = Animal('Sharik')
# print(cat.get_name())
# print(dog.get_name())


# # print(cat)

'''
Необходимо написать класс Game 
у которого есть приватный атрибут класса "level" который равен нулю
 и атрибут экземпляра класса name (ваше имя).
Класс Game должен иметь два метода: "set_level" 
и приватный метод "validate_name".
При инициализации экземпляра класса вызывается приватный метод validate_name который возвращает имя в котором первая буква в верхнем регистре, а остальные в нижнем (JOHN -> John).
Также в классе необходимо реализовать метод "set_level" который принимает в себя переменную "level" и увеличивает значение приватного атрибута класса "level" на значение этой переменной которую передали только в том случае если имя объекта (который сейчас играет в эту игру) "Tolik", 
иначе выведите на экран
"имя_объекта" ты не Tolik!'.
Создайте сначала экземпляр класса "game" и передайте ему имя Raychel в качестве аргумента. Далее вызовите метод set_level и передайте ему значение 5. После выведите в терминал значение атрибута "level" (так как у нас не реализован метод get_level, выведите это "нелегальным" способом). Теперь создайте экземпляр класса game2 и передайте ему имя "TOLIK" в качестве аргумента. Далее вызовите метод set_level и передайте ему значение 5. После выведите в терминал значение атрибута "level" (так как у нас не реализован метод get_level, выведите это "нелегальным" способом).
Ожидаемый вывод:

Raychel ты не Tolik!
0
5'''

# class Game:
#     __level = 0
#     def __init__(self,name) -> None:
#         self.name = self.__validate_name(name)

#     def set_level(self,number):
#         if self.name == 'Tolik' :
#             self.__level = 0
#             self.__level += number
#         else :
#             print(f'{self.name} ты не Tolik!')  


#     def __validate_name(self,name):
#         self.name = name.title()
#         return name.title()
         


# game = Game('Raychel')
# game.set_level(5)
# print(game.name)
# print(game._Game__level)

# game2 = Game('Tolik')
# game2.set_level(5)
# print(game2.name)
# print(game2._Game__level)


'''Необходимо написать класс Game
 у которого есть приватный атрибут класса level который равен нулю 
 и атрибут экземпляра класса name (ваше имя).
Так как атрибут класса level приватный и поэтому недоступен извне, необходимо реализовать два метода для работы с ним: get_level и set_level. Где get_level возвращает значение атрибута level и set_level принимает значение и присваивает его атрибуту level.
Создайте экземпляр game класса Game. Выведите на экран значение атрибута level затем присвойте ему значение 10 и выведите его на экран.'''
# class Game:
#     def __init__(self, name):
#         self.name = name
#         self.__level = 0  # приватный атрибут level

#     def get_level(self):
#         return self.__level

#     def set_level(self, level):
#         self.__level = level

# # создаем экземпляр класса Game
# game = Game("Моя игра")

# # выводим значение атрибута level
# print(game.get_level())

# # присваиваем атрибуту level значение 10
# game.set_level(10)

# # выводим значение атрибута level
# print(game.get_level())

# class Game:
#     __level = 0
#     def __init__(self, name):
#         self.name = name
        

#     def get_level(self):
#         return self.__level

#     def set_level(self, level):
#         self.__level = level

# game = Game()
# print(game._Game__level)
# game.set_level(10)
# print(game._Game__level)

# class Game:
#     __level = 0
#     @property
#     def level(self):
#         return self.__level

#     @level.setter
#     def level(self,level):
#         self.__level = level

# game = Game()
# print(game.level)
# game.level = 10
# print(game.level)   

# class Person:
#     def __init__(self):
#         self.__name = None
#         self.__last_name = None 
#         self.__age = None
#         self.__email= None
    
#     def get_name(self):
#         return self.__name 
    
#     def set_name(self, name):
#         self.__name = name
        
#     def get_last_name(self):
#         return self.__last_name
#     def set_last_name(self, last_name):
#         self.__last_name = last_name
#     def get_age(self):
#         return self.__age 
#     def set_age(self,age):
#         self.__age = age 
#     def get_email(self):
#         return self.__email
#     def set_email(self, email):
#         self.__email = email
# john = Person()
# print(john.get_name()) # None
# print(john.get_last_name()) # None
# print(john.get_age()) # None
# print(john.get_email()) # None
# john.set_name('John')
# john.set_last_name('Snow')
# john.set_age(30)
# john.set_email('johnsnow@gmail.com')
# print(john.get_name()) # John
# print(john.get_last_name()) # Snow
# print(john.get_age()) # 30
# print(john.get_email()) # johnsnow@gmail.com

# class Person:
#     def __init__(self):
#         self.__name = None
#         self.__last_name = None
#         self.__age = None
#         self.__email = None
    
#     @property
#     def name(self):
#         return self.__name
    
#     @name.setter
#     def name(self, name):
#         self.__name = name
    
#     @property
#     def last_name(self):
#         return self.__last_name
    
#     @last_name.setter
#     def last_name(self, last_name):
#         self.__last_name = last_name
    
#     @property
#     def age(self):
#         return self.__age
    
#     @age.setter
#     def age(self, age):
#         self.__age = age
    
#     @property
#     def email(self):
#         return self.__email
    
#     @email.setter
#     def email(self, email):
#         self.__email = email

# john = Person()
# print(john.name) # None
# print(john.last_name) # None
# print(john.age) # None
# print(john.email) # None
# john.name = 'John'
# john.last_name = 'Snow'
# john.age = 30
# john.email = 'johnsnow@gmail.com'
# print(john.name) # John
# print(john.last_name) # Snow
# print(john.age) # 30
# print(john.email) # johnsnow@gmail.com

# class Dad:
#     name = 'John'
#     _last_name = 'Snow'
#     __age = 40

# class Me(Dad):
#     name = 'Sam'
#     _last_name = 'Snow'
#     __age = 10
#     def about_me(self):
#         print(f'My name is {self.name} {self._last_name} I am {self.__age} years old')
    
#     def about_father(self):
#         print(f'My father is {Dad.name} {self._last_name}')

# me = Me()
# me.about_me()
# me.about_father()
 # task 17
# class Dad:
#     name = 'John'
#     _last_name = 'Snow'
#     __age = 40

# class Me(Dad):
#     name = 'Sam'
#     _last_name = 'Snow'
#     __age = 10
#     def about_me(self):
#         print(f'My name is {self.name} {Dad._last_name} and I am {self.__age} years old')
    
#     def about_my_father(self):
#         print(f'My father is {Dad.name} {Dad._last_name}')

# me = Me()
# me.about_me()
# me.about_my_father()


# def add(x, y):
#     x + y

# a = '12342342345' 
# b = [1,['a',5,6],2,3,4,5] 
# c = {1:'a', 2: {'a': 1, 'b': 2}, 3:'c'} 
# # add(a , a)
# # add(b , b)
# add(c , c)
# print(c)

# class Dog:
#     def vois(self):
#         print( 'Гав')

# class Cat:
#     def vois(self):
#         print( 'Мяу')

# rex = Dog()
# barsik = Cat()

# def to_pet(animal):
#     animal.voise()

# to_pet(barsik)
# to_pet(rex)


class Dog:
    def voice(self):
        print("Гав")

class Cat:
    def voice(self):
        print("Мяу")

barsik = Cat()
rex = Dog()

def to_pet(animal):
    animal.voice()

to_pet(barsik)
to_pet(rex)



