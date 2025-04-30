rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

logo = '''
##########################
########## GAME ##########
#Rock, Paper and Scissors#
##########################
####### made be me #######
######------##------######
'''

'''
rules of rps:
- Rock (1) wins against scissors (2).
- Scissors (2) win against paper (3).
- Paper (3) wins against rock (1).
'''
# import random and generate a random number range of 3
import random
random_num_of_3 = random.randint(1,3)
# start with print statements
print(logo)
print("\nHi there,\nwould you like to play\na RPS game with me?")

# Generate a choice from the users input:
input_user = input("\nPlease choose one option:\nrock, paper or scissors:\n").lower()
input_comp = random_num_of_3
print(f"\ncomputer input: {input_comp}\n")

# set nums to rps values
rock_num = 1
scissors_num = 2
paper_num = 3

# check if the user input and the comp input to check who won.

if input_user == 'rock' and input_comp == scissors_num:
    print(f"{rock}\n{input_user} vs scissors\n{scissors}")
    print("You win!")
elif input_user == 'scissors' and input_comp == rock_num:
    print(f"{scissors}\n{input_user} vs rock\n{rock}")
    print("You lose!")
elif input_user == 'rock' and input_comp == rock_num:
    print(f"{rock}\n{input_user} vs rock\n{rock}")
    print("It is a draw!")
elif input_user == 'paper' and input_comp == rock_num:
    print(f"{paper}\n{input_user} vs rock\n{rock}")
    print("You win!")
elif input_user == 'rock' and input_comp == paper_num:
    print(f"{rock}\n{input_user} vs paper\n{paper}")
    print("You lose!")
elif input_user == 'paper' and input_comp == paper_num:
    print(f"{paper}\n{input_user} vs paper\n{paper}")
    print("It is a draw!")
elif input_user == 'scissors' and input_comp == paper_num:
    print(f"{scissors}\n{input_user} vs paper\n{paper}")
    print("You win!")
elif input_user == 'paper' and input_comp == scissors_num:
    print(f"{paper}\n{input_user} vs scissors\n{scissors}")
    print("You lose!")
elif input_user == 'scissors' and input_comp == scissors_num:
    print(f"{scissors}\n{input_user} vs scissors\n{scissors}")
    print("It is a draw!")
else:
    print(f"I am sorry. It seems you misspelled your input: {input_user}.\nPlease try again.")