# from turtle import Turtle, Screen
# import os
# import platform
#
# # Setup the screen
# my_screen = Screen()
# my_screen.setup(width=300, height=300)
# my_screen.bgcolor("white")
#
# # create Turtle
# dennis = Turtle()
# print(dennis)
# dennis.shape("turtle")
# dennis.color("SeaGreen")
#
# # Move
# dennis.forward(100)
#
# # Bring Turtle window to front on macOS when run in PyCharm
# if platform.system() == 'Darwin':
#     os.system(
#         f"osascript -e 'tell application \"System Events\" to set frontmost of the first process whose unix id is {os.getpid()} to true'"
#     )
#
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()


table.add_column("Pokemon Name", ["Pikachu","Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align["Pokemon Name"] = "r"
table.align["Type"] = "l"

print(table)
