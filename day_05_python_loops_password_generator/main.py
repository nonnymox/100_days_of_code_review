# Returning the highest number in a list without m
# scores = [3, 7, 9, 6, 5]
# highest = 0
# for score in scores:
#     if score > highest:
#         highest = score
#
# print(highest)
# The FizzBuzz game
# for n in range(1,101):
#     if n % 3== 0 and n %5 == 0:
#         print("FizzBuzz")
#     elif n%3 == 0:
#         print("Fizz")
#     elif n%5== 0:
#         print("Buzz")
#     else:
#         print(n)
#Password Generator Project
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
try:
    nr_letters = int(input("How many letters would you like in your password?\n"))
    password = ""
    for n in range(0, nr_letters):
        password += random.choice(letters)
except ValueError:
    print("Please enter a number")
    exit()
try:
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    for n in range(0, nr_symbols):
        password += random.choice(symbols)
except ValueError:
    print("Please enter a number")
    exit()
try:
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    for n in range(0, nr_numbers):
        password += random.choice(numbers)
except ValueError:
    print("Please enter a number")
    exit()
else:
    print(password)
    password = list(password)
    random.shuffle(password)
    shuffled_password = ''.join(password)
    print(shuffled_password)






