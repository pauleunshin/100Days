import random
from art import logo
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
player_score = 0
computer_cards = []
computer_score = 0
play_again = True


def starting_hand():
    player_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))


def draw_card(player):
    player.append(random.choice(cards))


def game_state(cards1, cards2, score):
    if cards1[-1] == 11 and score > 21:
        cards1[-1] == 1
        score = sum(cards1)
    print(f"\tYour cards:{cards1}, current score: {score}")
    print(f"\tComputer's first card: {cards2[0]}")


def bust(sum1):
    if sum1 > 21:
        return "N"
    else:
        return "Y"


def compare(sum1, sum2):
    if sum1 == sum2:
        print(f"Your score was {sum1}. \nThe computer's score was {sum2}. You tie!")
    elif sum1 > 21:
        print("You went over 21. You busted!")
    elif sum2 > 21:
        print("The computer busted! You win!")
    elif sum1 > sum2:
        print(f"Your score was {sum1}. \nThe computer's score was {sum2}. You Win!")
    elif sum1 < sum2:
        print(f"Your score was {sum1}. \nThe computer's score was {sum2}. You lose.")


def play_blackjack():
    print(logo)
    starting_hand()
    player_score = sum(player_cards)
    computer_score = sum(computer_cards)
    game_state(player_cards, computer_cards, player_score)
    action = "Y"

    while action == "Y":
        action = input("Would you like to draw another card? (Y or N): ")
        if action == "Y":
            draw_card(player_cards)
            player_score = sum(player_cards)
            game_state(player_cards, computer_cards, player_score)
            action = bust(player_score)
    while computer_score < 17:
        draw_card(computer_cards)
        computer_score = sum(computer_cards)
    computer_score = sum(computer_cards)
    player_score = sum(player_cards)
    compare(player_score, computer_score)


starting = input("Would you like to play blackjack? (Y or N): ")
if starting == "Y":
    play_blackjack()
else:
    print("Good Bye")
    play_again = False

while play_again:
    response = input("Would you like to play again? (Y or N): ")
    if response == "Y":
        player_cards = []
        player_score = 0
        computer_cards = []
        computer_score = 0
        clear()
        play_blackjack()
    elif response == "N":
        print("Goodbye!")
        play_again == False