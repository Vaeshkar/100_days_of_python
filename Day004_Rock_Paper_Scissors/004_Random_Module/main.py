import random
# random_int = random.randint(1,10)
# print(random_int)

# random_float = random.uniform(1, 10)
# print(random_float)

# random_num_0_to_1 = round(random.random() * 10) # increase it by 10
# print(random_num_0_to_1)

######## heads or tails game ##########
coin_side = input("Let's play a little 'heads' and 'tails' game. Choose! ").lower()
random_num = random.random()
print(random_num)
if (random_num < 0.5 and coin_side == 'tails') or (random_num < 0.5 and coin_side == 'heads'):
    print(f"The coins flips in the air and lands on '{coin_side}'. You lose, sorry.")
elif (random_num >= 0.5 and coin_side == 'tails') or (random_num >= 0.5 and coin_side == 'heads'):
    print(f"The coin flips in the air and lands on '{coin_side}'. You won, nice!")
else:
    print("You have misspelled 'heads' or 'tails, please try again.\n")