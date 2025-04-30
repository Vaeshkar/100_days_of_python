print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first_junction = input("We've landed on an Island.\nDo you want to do 'left' or 'right'?\n")
if first_junction == "left" or first_junction == "Left":
    print("Nice, you've arrived at a laguna!")
    second_junction = input("Would you like to take a 'swim' or 'wait'?\n")
    if second_junction == 'wait' or second_junction == 'Wait':
        print("After waiting for a while you discover three doors behind some bushes.")
        third_junction = input("Which door do you want to enter: Red, Blue or Yellow?\n")
        if third_junction == 'Red' or third_junction == 'red':
            print("You walked in and fell into a burning pit of fire.\n**Game over**")
        elif third_junction == 'Blue' or third_junction == 'blue':
            print("Locked behind the Blue door where beasts.\n**Game over**")
        elif third_junction == 'Yellow' or third_junction == 'yellow':
            print("Can you believe it!?! Behind this door is a treasure.\n_|_|_| You win! |_|_|_")
        else:
            print("Your choice wasn't a door and you've been eaten by a panther.\n**Game over**")
    elif second_junction == 'swim' or second_junction == 'Swim':
        print("Attacked by trout.\n**Game over**")
elif first_junction == 'right' or first_junction == 'Right':
    print("You've fallen into a hole. \n**Game Over**")
