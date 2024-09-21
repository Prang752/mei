# a = int(input("input a : "))
# b = int(input("input b : "))
# print("type of a : ",type(a))
# print("type of b : ",type(b))
# a = a+
# print("value a : ", a)
# fahrenheit = float(input('Type in a temperature in Fahrenheit: '))
# Celsius = 5*(((fahrenheit)-32)/9)
# print('That is' , Celsius, 'degrees Celsius')
# x = 2
# print(x)
# x+=4
# print(x)
# x/=2
# print(x)
# x = 'Prang'
# print(x)
# print('He' in 'Hello, World!')
# print('earth' in 'Hello, World!')
# print('He' not in 'Hello, World!')
# print('earth' not in 'Hello, World!')
# hello = 'Hello'
# world = 'World'
# lucky_number = 13.1313
# print('Hello, {}!'.format(world))
# print('{hello}, {world}!'.format(world=world, hello='Helloooo'))
# print('{2} => {1}, {0}!'.format(hello, world, lucky_number))
# print('{}, {}! The lucky number is {} and {:.2f}'.format(hello, world, lucky_number, lucky_number))
# text = "nopphakao PPP"
# print(len(text))
# print(text.strip('P'))
# print(text.upper())
# print(text.lower())
# print(text.index('p'))
# print(text.count('p'))
# print(text.replace('n','P'))
# print(text.capitalize())
# from random import *
# print('1st random()  value is', random())
# print('2st random() value is', random())
# print('3st random() value is', random())
# print('1st randint(1, 5) value is', randint(1, 5))
# print('2st randint(1, 5) value is', randint(1, 5))
# print('1st uniform(1.0, 5.5) value is',uniform(1.0, 5.5))
# print('2st uniform(1.0, 5.5) value is',uniform(1.0, 5.5))
# print('3st uniform(1.0, 5.5) value is',uniform(1.0, 5.5))
# colors = 'red green blue black white'.splpit()
# print('1st choice(colors) value is', choice(colors))
# print('2st choice(colors) value is', choice(colors))
# print('3st choice(colors) value is', choice(colors))
# import math

# print('PI =', math.pi)
# print('Floor PI =',
#     math.floor(math.pi))
# print('Ceil(math.pi =)',
#     math.ceil(math.pi))
# print('sin 30 radian =',
#     math.sin(30))
# print('sin 30 degree =',
#     math.sin(math.radians(30)))
# print('PI to degree =',
#     math.degrees(math.pi))
# print('sqrt 2=', math.sqrt(2))
# print('log 2 =', math.log(2, 10))

# r =int(input('input :'))
# print("r =",r)
# circle_line=2*math.pi*r
# print("{:.4f}".format(circle_line))

# circle_area = math.pi*(r**2)
# print("{:.}")

# num = input("Enter number 5 unit: ")

# number = '01223456789'
# thai_number = '๐๑๒๓๔๕๖๗๘๙'

# num1 = number.index(num[0])
# num2 = number.index(num[1])
# num3 = number.index(num[2])
# num4 = number.index(num[3])
# num5 = number.index(num[4])

# print(thai_number[num1]+
#       thai_number[num2]+
#       thai_number[num3]+
#       thai_number[num4]+
#       thai_number[num5])

# temp = float(input('Enter current temperature: '))
# print('temperature is', temp, 'Celsius.')
# if temp>35:
#     print('Current temperature is hot.')
# if temp<23:
#     print('Current Temperature is cool.')
# if temp>23<35:
#     print('Current Temperature is Good')
# print('Good bye')

# sid = int(input('Enter student id: '))
# if sid %2==0:
#     print('Your number is odd number')
# else:
#     print('YOur number is even nember')

# import random
# print('{:*^30s}' .format('Random Disk'))
# number = random.randint(1, 5)
# print('อาหารแนะนำวันนี้' ,end='')
# if number ==1:
#     print('ข้าวราดคะน้าหมูทอด')
# elif number ==2:
#     print('กระเพราไข่ดาว')
# elif number ==3:
#     print('พิซซ่า')
# elif number ==4:
#     print('ข้าวเหนียวไก่ทอด')
# else:
#     print('ก๋วยเตี๋ยวต้มยำ')
# print('*'*30)

# score = float(input('Enter student score'))
# if score >= 80:
#     print('Got 4')
# elif score >=75:
#     print('Got 3.5')
# elif score >=70:
#     print('Got 3')
# elif score >=65:
#     print('2.5')
# elif score >=60:
#     print('2')
# elif score >=55:
#     print('1.5')
# elif score >=50:
#     print('1')
# else:
#     print('Got 0')

# print(1>3 or 1<3)
# print(not 1 == 2 and 2 == 2 or False)
# print(1 and Ture)
# print(0 and Ture or False)
# print(1 + 3 == 4 and 2*2 == 2**2)
# print(not(True or True and False))
# print(not not not not True and False)

# import random
# rand_num = random.randint(0,20)
# guess_num=int(input())
# diff=abs( rand_num-guess_num)
# print('Random number is {}, your guessing number is{}.'.format(rand_num,guess_num))
# if guess_num >= 0 and guess_num <= 20:
#     if diff<=10:
#         print('close')
#     elif diff>=10:
#         print('far')
#     elif diff ==guess_num:
#         print('good job,it\'s equal')
# else:
#     print('out ot range')

# user_unit_input= input("Enter your unit to convert in m or mm or cm:")
# value = input("Enter value 10cm, 10mm 10m: ")
# if "cm" in  user_unit_input and value == "m":
#     resault = float(value.replace("cm", ""))/100
#     print(result)

# value = input("Enter value 10cm, 10mm 10m: ")
# unit = input("Enter unit to convert in m or mm or cm: ")

# if "cm" in value and unit == "m":
#     result = float(value.replace("cm", "")) / 100
#     print(result)
# elif "cm" in value and unit == "mm":
#     result = float(value.replace("cm", "")) * 10
#     print(result)
# elif"mm" in value and unit == "cm":
#     result = float(value.replace("mm", "")) / 10
#     print(result)
# elif "mm" in value and unit == "m":
#     result = float(value.replace("mm", "")) / 1000
#     print(result)
# elif "m" in value and unit == "cm":
#     result = float(value.replace("m", "")) * 100
#     print(result)
# elif "m" in value and unit == "mm":
#     result = float(value.replace("m", "")) * 1000
#     print(result)

# num = int(input("Enter Your number:"))
# if num %3 == 0 and num %5 == 0:
#     print("FizzBuzz")
# elif num %3 == 0:
#     print("Fizz")
# elif num %5 == 0:
#     print("Buzz")
# else :
#     print("not")


# import string
# print(string.ascii_lowercase)
# Text = input("Enter Your Text 5 unit: ").lower()
# print(Text)
# lowercate = string.ascii_lowercase
# reversed_lowercate = string.ascii_lowercase[::-1]
# print(reversed_lowercate)
# Text1 = Text.index(Text[0])
# Text2 = Text.index(Text[1])
# Text3 = Text.index(Text[2])
# Text4 = Text.index(Text[3])
# Text5 = Text.index(Text[4])

# print(reversed_lowercate[Text1]+reversed_lowercate[Text2]
#       +reversed_lowercate[Text3]+reversed_lowercate[Text4]+reversed_lowercate[Text5])


# import string
# print(string.ascii_uppercase[1:5])

# Text = str(input("Enter Your Text 3 unit")).upper()
# print("Text")
# Text_upper = string.ascii_uppercase
# print(Text_upper)
# Text_revsed = string.ascii_uppercase[1:]+string.ascii_uppercase[0]

# print(Text_revsed)

# if len(Text)==3:
#     Text1 = Text_upper.index(Text[0])# index find position
#     Text2 = Text_upper.index(Text[1])
#     Text3 = Text_upper.index(Text[2])
#     print(f"Resalt = {Text_revsed[Text1]}{Text_revsed[Text2]}{Text_revsed[Text3]}")

# else:
#     print("word length is mismatched")


# couter = 0
# while couter <10 :
#     print('Hello, while:', couter)
#     couter += 3
#    # couter = couter + 1
# print('Good bye')


# mul = int(input('Enter muliplier: '))
# counter = 1
# while True:
#     print(counter, 'times', mul, '=',
#           mul*counter)
#     if counter <=12:
#         counter += 2
#     else:
#         break


# import random
# counter = 1
# while counter <=10:
#     print('random number:', counter)
#     counter +=1
#     rand_num = random.randint(0,20)
#     guess_num=int(input())
#     diff=abs( rand_num-guess_num)
#     print('Random number is {}, your guessing number is{}.'.format(rand_num,guess_num))
#     if guess_num >= 0 and guess_num <= 20:
#         if diff<=10:
#             print('close')
#         elif diff>=10:
#             print('far')
#         elif diff ==guess_num:
#             print('good job,it\'s equal')
#     else:
#         print('out ot range')
# print('Good Bye')


# import random
# rand_num = random.randint(1,100)
# couter = 1
# while True:
#     if counter <=10:
#         print("round:", counter)
#         number = int(input("Enter your number: "))

#         diff = abs(rand_num-number)

#         if number>=0 and number<=20:
#             if number ==rand_num:
#                 print("Good job")
#             elif diff <=10:
#                 print("close")
#             else:
#                 print


# for i in range (1,10) :
#     print('Hello, for:', i)
# print('Good Bye')


# import time
# sec = int(input('Eter second for a countdonw: '))
# for i in range(10, -1, -1):
#     print(i, '...')
#     if i > 0:
#         time.sleep(1)
# print('Let Go!')


# print('Print number with continue')
# for i in range(0,10):
#     print(i)
#     if i == 5:
#         continue
#     print("not continue")

# print('Print number with break')
# for i in range(0,10):
#     print(i)
#     if i ==5:
#         break
#     print("not break")


# n = int(input('Enter number: '))
# if n < 0:
#     print('Cannot get {}!'.format(n))
# else:
#     fac = 1
#     if n > 1:
#         for i in range(1,n + 1):
#             fac *= i
#             print(i)

#     print('{}! = {}'.format(n, fac))


# number = 1
# for i in range(1,5):
#     number += i
#     print(i)

# print(number)


# n = int(input('Enter number: '))
# if n < 0:
#     print('Cannot get {}!'.format(n))
# else:
#     fac = 1
#     if n > 1:
#         for i in range(n, 0, -1):
#             fac *= i
#             print(i)

#     print('{}! = {}'.format(n, fac))


# n = int(input('Enter the number of rows: '))
# for i in range(1, n+1):
#     print(' ' *(n-i)+'*'*i)


# n = int(input('Enter the number of rows: '))
# for i in range(1, n+1):
#     print('*'*i)


# n = int(input('Enter the number of rows: '))
# for i in range(n, 0, -1):
#     print('*'*i)


# n = int(input('Enter the number of rows: '))
# for i in range(n, 0, -1):
#     print(' '*(n-i)+'*'*i)


# n = int(input('Enter the number of rows: '))
# for i in range(1, n+ 1):
#     print(" " * (n - i) + "*" * (i - 1) + "*" * i)


# n = int(input('Enter the number of rows: '))
# for i in range(0, n+ 1):
#     print(" " * i, "*" * (n - i) + "*" * (n - i - 1))


# import string
# mesage_lower = string.ascii_lowercase
# mesage_upper = string.ascii_uppercase

# choice = input("Encrypt or Decryp")
# Text = input("Enter your Text")
# for char in Text:
#     if choice == "Encrypt":
#         if char.islower():
#             idx = mesage_lower.index(char)
#             print(mesage_lower[(idx+13)%26],end='')
#             print(char,"<<<")
#         if char.isupper():
#             idx = mesage_upper.index(char)
#             print(mesage_upper[(idx+13)%26],end='')
#             print(char)
#         else:
#             print("not choice your selec")
#         print("hahaha")
#     if choice == "Decryp":
#         print(char)
#         if char.islower():
#             idx = mesage_lower.index(char)
#             print[mesage_lower(idx - 13)%26]
#             print(char,"<<<")
#         if char.isupper():
#             idx = mesage_upper.index(char)
#             print(char)
#         else:
#             print("not choice your selec")
#         print("hahaha")


# import string

# upper_str = string.ascii_uppercase
# char = input("enter :")
# idx = upper_str.idx.(char)
# print(upper_str[(idx - 13) % 26])


# import string

# upper_case = string.ascii_uppercase
# lower_case = string.ascii_lowercase

# print("---Encrypt or Decrypt---")
# print("Enter 'E' for encrypt")
# print("Enter 'D' for decrypt")
# operation_type = input("Enter for select your operation : ")
# text_code = input("Enter your text :")

# result = ""

# if operation_type == "E" or operation_type == "D":
#     for c in text_code:
#         if operation_type == "E":
#             if c.isupper():
#                 idx = upper_case.index(c)
#                 result += upper_case[(idx + 13) % 26]
#             elif c.islower():
#                 idx = lower_case.index(c)
#                 result += lower_case[(idx + 13) % 26]
#             else:
#                 result += c
#         elif operation_type == "D":
#             if c.isupper():
#                 idx = upper_case.index(c)
#                 result += upper_case[(idx - 13) % 26]
#             elif c.islower():
#                 idx = lower_case.index(c)
#                 result += lower_case[(idx - 13) % 26]
#             else:
#                 result += c

#     print(f"Your {'encrypt' if operation_type == 'E' else 'decrypt'} is {result}")
# else:
#     print("Your operation type is not match")


# l = [0, 1, 2, 3, 4, 5, 6, 7]
# print(l)
# x = l[0: 4]
# print(x)
# x[0] = 20
# print(l)
# print(x)

# print(l[ :4])
# print(l[4: ])
# print(l[: len(l)-1])
# print(l[: -1])


# l = [0, 1, 2, 3, 4, 5, 6, 7]
# print(l)
# l[2: 4] = [2.2, 3.3]
# print(l)
# l[2: 4] = [5.5]
# print(l)
# l[2: 4] = [2, 3, 4]
# print(l)
# l[0] = [-1, 0]
# print(l)


# l = [0, 1, 2]
# print(l)
# l.append(3)
# print(l)
# l.extend([4, 5, 6])
# print(l)
# l.insert(1, 0.5)
# print(l)


# l = [0, 1, 2, 3, 2, 1, 0]
# print(l)
# l.remove(1)
# print(l)
# del(l[2])
# print(l)
# val = l.pop(2)
# print(l)
# print('pop val:', val)


# l1 = [0, 1, 2]
# l2 = [4, 5, 6]
# print('l1:' , l1)
# print('l2:', l2)
# l1 + l2
# print('l1:', l1)
# print('l2:', l2)
# l = l1 + l2
# print('l:', l)
# print('l1 * 3 = ', l1 * 3)


# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 97]

# num = int(input('Enter integer 1 - 100: '))
# if 1 <= num <= 100:
#  if num in primes:
#   print(num, 'is prime number.')
#  else:
#   print(num, 'is not prime number.')
# else:
#  print(num, 'out of test range.')
# print('Good Bye.')


# numbers = []
# for i in range(0,3):
#     numbers.append(int(input('Enter number #{}: '.format(i+1))))
# total = 0
# for i in numbers:
#     total +=i
# print('Average of input numbers is {}.'.format(total/len(numbers)))
# print(total)


# height = [100, 165, 95, 170, 175, 85]
# copy_height = height[:]
# print(height)
# height.sort()
# print(height)
# height.reverse()
# print(height)

# print(copy_height)
# height.sort(reverse=True)
# print(height)

# height = [100, 165, 95, 170, 175, 85]
# print(height)
# sorted(height)
# print(height)
# sorted_height = sorted(height)
# print(height)
# print(sorted_height)
# r_height= sorted(height, reverse=True)
# print(r_height)


# a = (1, 2, 3)
# b = 4, 5, 6
# print(a)
# print(b)
# print(a+b)
# print(a[0])
# c = a, b
# print(c)
# x, y, z = a
# print('x={}, y={}, z={}'.format(x, y, z))


# t = (1, 2, 3, 4)
# print(t)
# l = list(t)
# l.append('Hello')
# print(l)
# t = tuple(l)
# print(t)


# s0 = {1, 2, 3}
# s1 = set([3, 4, 5])
# s2 = set((4, 4, 5))

# print(s0)
# print(s1)
# print(s2)

# s0.add(4)
# s0.add(1)
# print(s0)

# s0.update(s1)
# s0.update(range(0, 10, 2))
# print(s0)

# s0.discard(9)


# a = {1, 2, 3}
# b = {2, 3, 4, 5 }

# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(a|b)
# print(a&b)
# print(a-b)
# print(a^b)
# print(1 in a)

# c = a|b
# print(a.issubset(c))
# print(a.issuperset(c))
# print(c.issuperset(a))


# user = dict(id=10, name="Thanathip", surname="Limna", weight=71.5, height=165)
# print(user)
# print(user.keys())
# print(user.values())
# print(user.items())

# for key in user:
#     print(key, user[key])
# for key in user.keys():
#     print(key, user[key])
# for value in user.values():
#     print(value)
# for key, value in user.item():
#     print(key, value)


# user = dict(id=10, name="Thanathip", surname="Limna", weight=71.5, height=165)
# print(user)
# user["hart_rate"] = 80
# user["weught"] = 70
# print(user)
# student = {"grade": {61: [3.6, 3.5], 62: [4.0]},
#            "skill": ["Computer", "Python Programming", "Basketball"],}
# print(student)
# user.update(student)
# print(user)
# tmp = user.pop("weught")
# user["weight"] = tmp
# print(user)
# print("*" * 60)
# for k, v in user.items():
#     print("{:10s} {}".format(k, v))
# print("*" * 60)


# function

# def get_input(num):
#     data = []
#     for i in range(num):
#         value = int(input("Enter number #{}: ".format(i)))
#         data.append(value)
#     return data


# print(get_input(5))
# print(get_input(3))


# import random


# def average_random_number(num):
#     total = 0
#     for i in range(num):
#         total += random.random()

#     average = total / num
#     return average


# print(average_random_number(6))


# import random

# def average_random_number(num):
#     return sum([random.random() for i in rage(num)]) / num
# print(average_random_number(6))


# import random


# def average_random_number(num):
#     data = []
#     for i in range(num):
#         random_number = random.randint

#         data.append(random())
#     return sum(data) / len(data)


# print(average_random_number(6))


# class Pokemon:
#     def __init__(self, name, type, weight, height):
#         self.name = name
#         self.type = type
#         self.weight = weight
#         self.height = height
#         self.hp = 100

#     def eat(self, food):
#         if food == "electric":
#             self.hp += 10

#     def print(self):
#         print(self.name, "type:", self.hp)
#         print("type:", self.type)
#         print("weight:", self.weight, "height:", self.height)


# pikachu = Pokemon("Pikachu", "electric", 5, 20)
# pikachu.print()
# print(pikachu.name)
# pikachu.weight = 7
# pikachu.print()
# pikachu.eat("electric")
# pikachu.print()


#


# class Pokemon:
#     def __init__(self, name, type, weight, height):
#         self.name = name
#         self.type = type
#         self.weight = weight
#         self.height = height
#         self.hp = 100

#     def eat(self, food):
#         if food == "electric":
#             self.hp += 10

#     def print(self):
#         print(self.name, "hp:", self.hp)
#         print("type:", self.type)
#         print("weight:", self.weight, "height:", self.height)


# class Pikachu(Pokemon):
#     def __init__(self, name, weight, height):
#         super().__init__(name, "electric", weight, height)

#     def thunderbplt(self, pokemon):
#         pokemon.hp -= 10


# class Raichu(Pokemon):
#     def __init__(self, name, weight, height):
#         super().__init__(name, "qqq", weight, height)

#     def wwww(self, pokemon):
#         pokemon.hp -= 15

# class sui(Pokemon):
#     def __init__

# pika1 = Pikachu("Pika1", 5, 12)
# pika2 = Pikachu("Pika2", 3, 12)
# raichu = Raichu("raichu", 7, 10)

# pika1.print()
# pika2.print()
# raichu.print()

# pika1.thunderbplt(pika2)

# raichu.wwww(pika2)

# pika2.eat("electric")

# pika1.print()
# pika2.print()
# raichu.print()


# user = int(input("Enter 20 values"))
# number = []
# for i in range(0, 20):
#     number.append(int(input("Enter 20 values #{}:".format(i + 1))))
# a = set(number)
# print(a)
# gg = list(a)
# output = []
# for i in range(0, len(gg)):
#     if i % 2 == 0:
#         output.append(gg[i])
# print(output)
# total = 0
# for i in output:
#     total += i
# print("Average of input number is {}.".format(total / len(output)))


# set_number = set([int(input(f"Enter Number #{i+1 :} :"))])


# list_number = []
# for i in range(20):
#     enter_number = int(input(f"Enter Number #{i+1}  :"))
#     list_number.append(enter_number)

# set_number = set(list_number)
# print("set Number :" set_number)
# number_even_index = []
# for number in range(1, len(set_number, 2)):
#     number_even_index.append(list(set_number)[number])

# print("average is", sum(number_even_index / len(number_even_index)))


# user = input("Enter your word")
# if user =='end':


# count = 0
# list_character = []
# while True:
#     text = input("Enter : ")
#     for character in text:
#         if character.isalpha():
#             count += 1
#             list_character


# if

# a = float(input())
# ab = a
# if a < 0:
#     ab = -a
# print(f"|{a}| = {ab}")


# score = float(input())
# if score >= 40.0:
#     grade = "P"
# else:
#     grade = "F"
# if grade == "P":
#     print("Pass")
# else:
#     print("Fail")


x = 6
print(x)


# def max3(a, b, c):
#     if a >= b:
#         if a >= c:
#             print(a)
#         else:
#             print(c)
#     else:
#         if b >= c:
#             print(b)
#         else:
#             print(c)

# def func1( ) :
# print(“Hello World”)
# return
# def func2( p ) :
# print(“Hello ”*p, end=‘’)
# print(“World”)
# def func3( a, b ) :
# c = (a*a + b*b)**0.5
# return c

# func1( )
# func2(2)
# x = 3
# func2(x)
# y = func3( 3.0, 4.0 )
# print(y, func3(6.0, 8.0) )
