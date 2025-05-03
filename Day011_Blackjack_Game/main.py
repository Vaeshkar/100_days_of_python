import random
import art

# holding scores
user_score = -1
comp_score = -1

# holding cards and empty hands
user_cards = []
comp_cards = []

# deal a card to the player/computer
def deal_card():
    """
    Deals a random choice card
    - usage: random.choice()
    :return: choice
    """
    # ace = 11 and jack/king/queen = 10
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    choice = random.choice(cards)
    return choice

#print(deal_card())

# check the score
def calculate_score(cards:list):
    """
    Calculates the cards and returns the score
    - Condition: swaps Ace card from 11 to 1 if score > 21
    :param cards:
    :return: score or 0 (Blackjack)
    """
    score = sum(cards)
    black_jack = 21
    ace = 11
    ace_21 = 1

    # check for blackjack
    if score == black_jack and len(cards) == 2:
        return 0
    # check for ace swap with a score over 21
    temp_cards = cards.copy()
    if score > 21 and 11 in temp_cards:
        temp_cards.remove(11)
        temp_cards.append(1)
        score = sum(temp_cards)
        return score
    else:
        return score

#print(calculate_score([12,11]))

# compare cards check who wins
def compare(u_score:int, c_score:int, u_cards:list, c_cards:list):
    """
    Compares the score and cards to check who won the game
    :param u_score:
    :param c_score:
    :param u_cards:
    :param c_cards:
    :return: a String message
    """
    if u_score == c_score:
        if len(u_cards) < len(c_cards):
            return "User wins with a cleaner 21!"
        elif len(c_cards) < len(u_cards):
            return "Computer wins with a cleaner 21!"
        else:
            return "Draw"
    elif c_score == 0:
        return "Computer wins, black jack"
    elif u_score == 0:
        return "User wins, black jack"
    elif u_score > 21:
        return "User bust, Computer wins"
    elif c_score > 21:
        return "Computer bust, User wins"
    elif u_score > c_score:
        return "User wins, Computer lose"
    else:
        return "User lose"

# calculate the score and print it
def display_score(user_cards:list, comp_cards:list):
    """
    Calculates each score and prints it
    :param user_cards:
    :param comp_cards:
    :return: user_score, comp_score
    """
    user_score = calculate_score((user_cards))
    comp_score = calculate_score(comp_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer'S first card: {comp_cards[0]}")
    return user_score, comp_score

def black_jack_game():
    """
    - func: Mains game plays until the user cancels
    - while 1: checks if game_over is True for the user to finish his game
    - while 2: checks if computer_score for Blackjack and <17, so the computer finish his game
    - prints out the final score and the winner
    - Ask if the user wants to continue or stop
    """
    # question: start the game: 'y' or 'n'?
    # needed to control the while loop
    wants_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n")

    # game loop
    while wants_to_play == 'y':
        # black jack logo
        print(art.logo)

        # holding cards and empty hands
        user_cards = []
        comp_cards = []

        #draw two cards for 'user' and 'comp'
        for card in range(2):
            user_cards.append(deal_card())
            comp_cards.append(deal_card())

        # set game_over to False
        game_over = False
        while not game_over:
            # calculate the scores and print them:
            user_score, comp_score = display_score(user_cards, comp_cards)

            # check if the user has a blackjack or a bust
            if user_score == 0 or user_score > 21:
                game_over = True
            else:
                hit_or_pass = input("Type 'y' if you want another card, type 'n' to pass:\n")
                if hit_or_pass == 'y':
                    user_cards.append(deal_card())
                elif hit_or_pass == 'n':
                    game_over = True

        ## Game over print and calculations

        # user stopped playing, the computer needs to finish its turn
        comp_score = calculate_score(comp_cards)
        while comp_score != 0 and comp_score < 17:
            comp_cards.append(deal_card())
            comp_score = calculate_score(comp_cards)

        # final user hand and score
        print(f"User final hand: {user_cards}, final score: {calculate_score(user_cards)}")
        print(f"Computer final hand: {comp_cards}, final score: {calculate_score(comp_cards)}")

        # compare the result of both scores
        ## user_score = calculate_score(user_cards)
        ## comp_score = calculate_score(comp_cards)
        ## result = compare(user_score, comp_score, user_cards, comp_cards)
        print(compare(calculate_score(user_cards), calculate_score(comp_cards), user_cards, comp_cards))

        # check if the user wants to continue
        wants_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n")

    print("Thanks for playing Blackjack with us.") # will never run, he he.

black_jack_game()