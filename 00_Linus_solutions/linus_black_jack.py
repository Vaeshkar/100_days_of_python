############### Blackjack Project #####################

#imports
import random 
from art import logo
from replit import clear


#functions
def score():
  """calculate score of both players"""
  global sum_player, sum_com
  sum_player = sum(player_cards)
  sum_com = sum(com_cards)

def card_index():
  """generate random card index"""
  return random.randint(0, len(cards_in_game) - 1)

def add_card(gamer):
  """add a card to gamers hand"""
  rcard_index = card_index()
  gamer.append(cards_in_game[rcard_index])
  cards_in_game.pop(rcard_index)
  score()

def first_move():
  """first move what is needed for the game, both gamer gets there first cards, second card of com stay hidn till his move"""
  global com_cards_backend
  for n in range(1, 4):
    for card in cards:
      cards_in_game.append(cards[card])
    random.shuffle(cards_in_game)
  #first card
  add_card(player_cards)
  add_card(com_cards)
  #second card
  add_card(player_cards)
  rcard_index = card_index()
  com_cards.append(0)
  com_cards_backend = cards_in_game[rcard_index]
  cards_in_game.pop(rcard_index)
  score()

def turn_player():
  """players move, get ask if he wants more cards till he is over 21 or dont want to"""
  players_turn = True
  while players_turn:
    clear()
    print(logo)
    for n in range(len(player_cards)):
      if sum_player > 21 and player_cards[n] == 11:
        player_cards.pop(n)
        player_cards.insert(n, 1)
        score()
    print(f"     Your cards:{player_cards},      your current score: {sum_player}!")
    print(f" Computer cards:{com_cards}, computers current score: {sum_com}!")
    if sum_player <= 21:
      if input("Type 'y' to get a nother card, type 'n' to pass:  ") == "y":
        add_card(player_cards)
      else:
        print("Computers turn")
        players_turn = False
    if sum_player > 21:
      print("You turn over, computers turn")
      players_turn = False

def turn_com():
  """computer plays automatic till he is over 21 or has a winning hand, or is in the upper 3 scores with a draw"""
  com_turn = True
  com_cards.pop(1)
  com_cards.append(com_cards_backend)
  if sum_player <= 21:
    while com_turn:
      score()
      clear()
      print(logo)
      print(f"     Your cards:{player_cards},      your current score: {sum_player}!")
      print(f" Computer cards:{com_cards}, computers current score: {sum_com}!")
      if (sum_com <= 21 and sum_com >= sum_player) or (sum_com == sum_player and sum_com >18):
        com_turn = False
      if sum_com <= 21 and sum_com <= sum_player:
        add_card(com_cards)
      else:
        com_turn = False
  else:
    com_turn = False

def calc_winner():
  """calculate the end of the game, draw, win or lose"""
  score()
  clear()
  print(logo)
  print(f"     Your cards:{player_cards},      your current score: {sum_player}!")
  print(f" Computer cards:{com_cards}, computers current score: {sum_com}!")
  if sum_com > 21 and sum_player > 21 or sum_player <= 21 and sum_player == sum_com:
    print("Its a draw")
  elif sum_player <= 21 and (sum_player >= sum_com or sum_com > 21):
    print("You win!")
  elif sum_com <= 21 and (sum_com >= sum_player or sum_player > 21):
    print("You lose!")

#code
if input("Do you want to play a Game of Black Jack? Type 'y' for yes an 'n' for no!: ").lower() == "y":
  game_on = True
  while game_on:
    #List of cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards_in_game = []
    player_cards = []
    com_cards = []
    com_cards_backend = 0
    sum_player = 0
    sum_com = 0
    #game
    first_move()
    turn_player()
    turn_com()
    calc_winner()
    if input("Do you want to play a Game of Black Jack? Type 'y' for yes an 'n' for no!: ").lower() != "y":
      game_on = False
    clear()
else:
  print("Okay, have a nice Day :)")