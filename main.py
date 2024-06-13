import random
import math
import numpy as np
from point_counting import point_check, point_check_pegging

deck = [ # Spades
        {"title": "A",
         "suit": "Spades",
         "color": "Black",
         "value": 1,
         "order_value": 1},
         {"title": "2",
         "suit": "Spades",
         "color": "Black",
         "value": 2,
         "order_value": 2},
         {"title": "3",
         "suit": "Spades",
         "color": "Black",
         "value": 3,
         "order_value": 3},
         {"title": "4",
         "suit": "Spades",
         "color": "Black",
         "value": 4,
         "order_value": 4},
         {"title": "5",
         "suit": "Spades",
         "color": "Black",
         "value": 5,
         "order_value": 5},
         {"title": "6",
         "suit": "Spades",
         "color": "Black",
         "value": 6,
         "order_value": 6},
         {"title": "7",
         "suit": "Spades",
         "color": "Black",
         "value": 7,
         "order_value": 7},
         {"title": "8",
         "suit": "Spades",
         "color": "Black",
         "value": 8,
         "order_value": 8},
         {"title": "9",
         "suit": "Spades",
         "color": "Black",
         "value": 9,
         "order_value": 9},
         {"title": "10",
         "suit": "Spades",
         "color": "Black",
         "value": 10,
         "order_value": 10},
         {"title": "J",
         "suit": "Spades",
         "color": "Black",
         "value": 10,
         "order_value": 11},
         {"title": "Q",
         "suit": "Spades",
         "color": "Black",
         "value": 10,
         "order_value": 12},
         {"title": "K",
         "suit": "Spades",
         "color": "Black",
         "value": 10,
         "order_value": 13},

        # Clubs
         {"title": "A",
         "suit": "Clubs",
         "color": "Black",
         "value": 1,
         "order_value": 1},
         {"title": "2",
         "suit": "Clubs",
         "color": "Black",
         "value": 2,
         "order_value": 2},
         {"title": "3",
         "suit": "Clubs",
         "color": "Black",
         "value": 3,
         "order_value": 3},
         {"title": "4",
         "suit": "Clubs",
         "color": "Black",
         "value": 4,
         "order_value": 4},
         {"title": "5",
         "suit": "Clubs",
         "color": "Black",
         "value": 5,
         "order_value": 5},
         {"title": "6",
         "suit": "Clubs",
         "color": "Black",
         "value": 6,
         "order_value": 6},
         {"title": "7",
         "suit": "Clubs",
         "color": "Black",
         "value": 7,
         "order_value": 7},
         {"title": "8",
         "suit": "Clubs",
         "color": "Black",
         "value": 8,
         "order_value": 8},
         {"title": "9",
         "suit": "Clubs",
         "color": "Black",
         "value": 9,
         "order_value": 9},
         {"title": "10",
         "suit": "Clubs",
         "color": "Black",
         "value": 10,
         "order_value": 10},
         {"title": "J",
         "suit": "Clubs",
         "color": "Black",
         "value": 10,
         "order_value": 11},
         {"title": "Q",
         "suit": "Clubs",
         "color": "Black",
         "value": 10,
         "order_value": 12},
         {"title": "K",
         "suit": "Clubs",
         "color": "Black",
         "value": 10,
         "order_value": 13},

         # Diamonds
         {"title": "A",
         "suit": "Diamonds",
         "color": "Red",
         "value": 1,
         "order_value": 1},
         {"title": "2",
         "suit": "Diamonds",
         "color": "Red",
         "value": 2,
         "order_value": 2},
         {"title": "3",
         "suit": "Diamonds",
         "color": "Red",
         "value": 3,
         "order_value": 3},
         {"title": "4",
         "suit": "Diamonds",
         "color": "Red",
         "value": 4,
         "order_value": 4},
         {"title": "5",
         "suit": "Diamonds",
         "color": "Red",
         "value": 5,
         "order_value": 5},
         {"title": "6",
         "suit": "Diamonds",
         "color": "Red",
         "value": 6,
         "order_value": 6},
         {"title": "7",
         "suit": "Diamonds",
         "color": "Red",
         "value": 7,
         "order_value": 7},
         {"title": "8",
         "suit": "Diamonds",
         "color": "Red",
         "value": 8,
         "order_value": 8},
         {"title": "9",
         "suit": "Diamonds",
         "color": "Red",
         "value": 9,
         "order_value": 9},
         {"title": "10",
         "suit": "Diamonds",
         "color": "Red",
         "value": 10,
         "order_value": 10},
         {"title": "J",
         "suit": "Diamonds",
         "color": "Red",
         "value": 10,
         "order_value": 11},
         {"title": "Q",
         "suit": "Diamonds",
         "color": "Red",
         "value": 10,
         "order_value": 12},
         {"title": "K",
         "suit": "Diamonds",
         "color": "Red",
         "value": 10,
         "order_value": 13},

         # Hearts
         {"title": "A",
         "suit": "Hearts",
         "color": "Red",
         "value": 1,
         "order_value": 1},
         {"title": "2",
         "suit": "Hearts",
         "color": "Red",
         "value": 2,
         "order_value": 2},
         {"title": "3",
         "suit": "Hearts",
         "color": "Red",
         "value": 3,
         "order_value": 3},
         {"title": "4",
         "suit": "Hearts",
         "color": "Red",
         "value": 4,
         "order_value": 4},
         {"title": "5",
         "suit": "Hearts",
         "color": "Red",
         "value": 5,
         "order_value": 5},
         {"title": "6",
         "suit": "Hearts",
         "color": "Red",
         "value": 6,
         "order_value": 6},
         {"title": "7",
         "suit": "Hearts",
         "color": "Red",
         "value": 7,
         "order_value": 7},
         {"title": "8",
         "suit": "Hearts",
         "color": "Red",
         "value": 8,
         "order_value": 8},
         {"title": "9",
         "suit": "Hearts",
         "color": "Red",
         "value": 9,
         "order_value": 9},
         {"title": "10",
         "suit": "Hearts",
         "color": "Red",
         "value": 10,
         "order_value": 10},
         {"title": "J",
         "suit": "Hearts",
         "color": "Red",
         "value": 10,
         "order_value": 11},
         {"title": "Q",
         "suit": "Hearts",
         "color": "Red",
         "value": 10,
         "order_value": 12},
         {"title": "K",
         "suit": "Hearts",
         "color": "Red",
         "value": 10,
         "order_value": 13},
         ]


def generateCards(num_cards: int) -> list:
    hand = []
    for i in range(num_cards):
        hand.append(deck.pop(random.randint(0,len(deck)-1)))
    return hand

def pegging_prompt(hand: list):
    # This can be the console-based pegging to get the scoring working
    print("Your hand, sire: ")
    for card in hand:
        print(card['suit'] + " " + card['title'])
    played_card = ''
    while played_card == '':
        played_card_text = input("State the card that you wish to play: ")
        if played_card_text == 'go':
            played_card = 'go'
            break
        for card in hand:
            if card["suit"][0] == played_card_text[-1] and card["order_value"] == int(played_card_text[:-1]):
                played_card = card
                hand.remove(card)
        if played_card == '':
            print("You super don't have that card, try again.")

    return played_card

def check_for_playable_cards(hand: list, running_sum: int):
    # Looks to see if the player can possibly go again and forces them to play it.
    answer = ''
    for card in hand:
        if card["value"] + running_sum <= 31:
            print("Bruh you literally have to play a card.")
            while True:
                answer = pegging_prompt(hand)
                if type(answer) != str:
                    if answer["value"] + running_sum <= 31:
                        return answer
                    else:
                        hand.append(answer)
                        print("Bruh that card simply does not work.")
                else:
                    print("Please enter the correct card, this is ridiculous.")
                           
    return 'go'


answer = ''
if __name__ == "__main__":
    turn = 0
    player_hands = [generateCards(4), generateCards(4)]
    player_points = [0, 0]
    #cut_card = generateCards(1)
    pile = []
    previous_run_points = 0
    new_points = 0
    running_sum = 0

    print("Hello and Welcome! To play a card, state it in the format of the")
    print("number of the card's order followed by the first letter of its suit.")

    while len(player_hands[0]) != 0 or len(player_hands[1]) != 0:
        # Logic to prompt for playing a card, checks to see if the card played can even be played.
        # Will also reward the player that played the last card the points and the other starts the pile
        while True:
            print(f"PLAYER {turn%2 + 1}'s TURN {turn%2 + 1} {turn%2 + 1} {turn%2 + 1} {turn%2 + 1}\n")
            answer = pegging_prompt(player_hands[turn%2])
            if type(answer) == str:
                answer = check_for_playable_cards(player_hands[turn%2], running_sum)
            # Giving the other player a chance to play more cards...
                
            if answer == 'go':
                turn += 1
                print(f"PLAYER {turn%2 + 1}'s ADDITIONAL PLAYS {turn%2 + 1} {turn%2 + 1} {turn%2 + 1} {turn%2 + 1}\n")
                answer = pegging_prompt(player_hands[turn%2])
                if type(answer) == str:
                    answer = check_for_playable_cards(player_hands[turn%2], running_sum)
                if type(answer) != str:  
                    while answer["value"] + running_sum > 31:
                        print("No sir, try again")
                        player_hands[turn%2].append(answer)
                        answer = pegging_prompt(player_hands[turn%2])
                        if type(answer) == str:
                            answer = check_for_playable_cards(player_hands[turn%2], running_sum)
                            if answer == 'go':
                                break
        
            # Did they BOTH say go? If so, let's reset
            if answer == 'go':
                player_points[turn%2] += 1
                pile.clear()
                previous_run_points = 0
                new_points = 0
                running_sum = 0
                turn += 1

            # Do not execute if we are resetting
            if type(answer) != str:
                if running_sum + answer["value"] < 32:
                    running_sum += answer["value"]
                    pile.append(answer)
                    if len(pile) > 5:
                        pile = pile[-5:]
                    break
                else:
                    print("Try a different card, or type 'go' to concede.")
                    # Then give them their card back
                    player_hands[turn%2].append(answer)
                
        if len(pile) > 1:
            new_points, previous_run_points = point_check_pegging(pile, previous_run_points)
            player_points[turn%2] += new_points

        print(f"PILE SUM IS THUS: {running_sum}\n" )
        print(f"Player 1 has {player_points[0]} points.")
        print(f"Player 2 has {player_points[1]} points.")
        turn += 1

    turn += 1
    if running_sum == 31:
        player_points[turn%2] += 2
    else:
        player_points[turn%2] += 1
    print(f"Pegging Over!! Player 1 scored {player_points[0]} and Player 2 scored {player_points[1]}... What a game!")


# pile = [{"title": "7",
#          "suit": "Hearts",
#          "color": "Red",
#          "value": 7,
#          "order_value": 7},
#         {"title": "7",
#          "suit": "Diamonds",
#          "color": "Red",
#          "value": 7,
#          "order_value": 7},
#          {"title": "6",
#          "suit": "Hearts",
#          "color": "Red",
#          "value": 6,
#          "order_value": 6},
#         {"title": "7",
#          "suit": "Diamonds",
#          "color": "Red",
#          "value": 7,
#          "order_value": 7},
#          {"title": "5",
#          "suit": "Hearts",
#          "color": "Red",
#          "value": 5,
#          "order_value": 5},
#          ]

# print(point_check_pegging(pile=pile, previous_run_points=00))