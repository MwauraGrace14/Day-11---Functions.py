# Simple functions.
def greet():
  print("Hey you")
  print("Welcome back")
  print("Nice to see you")
greet()

#Functions with inputs
def greet_them(name):
  print(f"Hello {name}")
  print(f"How are you {name}?")
  print(f"{name},Doesnt the weather today look nice?")
greet_them(name = input("What's your name?"))


#Keyword argument
def stalk(name, location):
  print(f"Hey {name}")
  print(f"How's the weather in {location}?")
stalk(name=input("What is your name? "), location=input("Where do you live?"))


#Practical example 1

import math
def paint_calc(height, width, cover):
  number_of_cans = ((test_h*test_w)/coverage)
  round_cans = math.ceil(number_of_cans)
  print(f"You'll need {round_cans} cans of paint.")
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# Practical example 2
def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
      print("It's a prime number.")
  else:
      print("It's not a prime number.")

n = int(input()) # Check this number
prime_checker(number=n)