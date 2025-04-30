import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
#
# # letter pool
# pw_letters = []
# count_letters = 0
#
# # numbers pool
# pw_numbers = []
# count_numbers = 0
#
# # symbols poop
# pw_symbols = []
# count_symbols = 0
#
# # Easy Level PW Generator
# # adding up the letters
# for letter in letters:
#     if count_letters == nr_letters:
#         break
#     else:
#         count_letters += 1
#     pw_letters += letter
# print(pw_letters)
#
# # adding up the numbers
# for number in numbers:
#     if count_numbers == nr_numbers:
#         break
#     else:
#         count_numbers += 1
#     pw_numbers += number
# print(pw_numbers)
#
# # adding up the  symbols
# for symbol in symbols:
#     if count_symbols == nr_symbols:
#         break
#     else:
#         count_symbols += 1
#     pw_symbols += symbol
# print(pw_symbols)
#
# # Add it all together the easy way.
# easy_password = ''.join(pw_letters + pw_numbers + pw_symbols)
# print(f"Your new password, given your wishes is the following:")
# print("###############")
# print(easy_password)
# print("###############")
# print("Enjoy.")

# Hard Level PW Generator

# random.shuffle(letters)
# random.shuffle(numbers)
# random.shuffle(symbols)
#
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#
# # letter pool
# pw_letters = []
# count_letters = 0
#
# # numbers pool
# pw_numbers = []
# count_numbers = 0
#
# # symbols poop
# pw_symbols = []
# count_symbols = 0
#
# # Easy Level PW Generator
# # adding up the letters
# for letter in letters:
#     if count_letters == nr_letters:
#         break
#     else:
#         count_letters += 1
#     pw_letters += letter
#
# # adding up the numbers
# for number in numbers:
#     if count_numbers == nr_numbers:
#         break
#     else:
#         count_numbers += 1
#     pw_numbers += number
#
# # adding up the  symbols
# for symbol in symbols:
#     if count_symbols == nr_symbols:
#         break
#     else:
#         count_symbols += 1
#     pw_symbols += symbol
#
# #print(f"Here are the pw_lists: \n{pw_letters}\n{pw_numbers}\n{pw_symbols}")
# random.shuffle(pw_letters)
# random.shuffle(pw_symbols)
# random.shuffle(pw_numbers)
# #print(f"Here are the random pw_lists: \n{pw_letters}\n{pw_numbers}\n{pw_symbols}")
#
# # Add it all together the hard way.
# hard_password_list = pw_letters + pw_numbers + pw_symbols
# random.shuffle(hard_password_list)
# print(f"Your new password, given your wishes is the following:")
# print("###############")
# print(''.join(hard_password_list))
# print("###############")
# print("Enjoy.")

######### Angela version
password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

for char in range(0, nr_symbols):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
print(f"Your password is: {''.join(password_list)}")