import random
import math
import numpy as np
from itertools import chain, combinations

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

def point_check(hand: list, cut_card: list = [{"title": "Blank", "suit": "Blank", "color": "White", "value": 100, "order_value": 100}], crib: bool = False) -> int:
    total_points = 0
    run_multiplier = 1

    hand_w_cut = hand + cut_card

    print(f"The following hand is:")
    for card in hand_w_cut:
        print(card['suit'] + " " + card['title'])

    # Card face value
    values = [card['value'] for card in hand_w_cut]
    values.sort()

    # Card order value
    order_values = [card['order_value'] for card in hand_w_cut]
    order_values.sort()
    order_values_set = list(sorted(set(order_values)))

    # Getting points for pairs
    pairs = [order_values.count(num) for num in order_values_set]
    total_points += sum([num*(num-1) for num in pairs])

    print(f"Points after pairs: {total_points}")

    # Getting points for runs - rigged in a way to work for all 5-card hands: only keeps track on the highest run in a hand
    ordered_differences = np.array([order_values_set[i+1] - order_values_set[i] for i in range(len(order_values_set)) if i < len(order_values_set) - 1])
    runs = np.split(ordered_differences, np.where(ordered_differences > 1)[0])
    counter = max([sum(run==1) for run in runs]) + 1

    # Checking for double runs, triple runs, double-double runs, etc
    just_added = False
    for i in range(len(ordered_differences)):
        if ordered_differences[i] == 1:
            if order_values.count(order_values_set[i]) > 1 and not just_added:
                run_multiplier *= order_values.count(order_values_set[i])
            elif just_added:
                just_added = False
            if order_values.count(order_values_set[i+1]) > 1:
                run_multiplier *= order_values.count(order_values_set[i+1])
                just_added = True
    total_points += counter*run_multiplier if counter > 2 else 0

    print(f"Points after runs: {total_points}")

    # Getting points for 15s
    s = list(values)
    powerset = chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    total_points += sum([2 for group in powerset if sum(group) == 15])

    print(f"Points after fifteens: {total_points}")

    # Getting points for a flush
    if len(set([card["suit"] for card in hand])) == 1 and hand[0]["suit"] == cut_card[0]["suit"]:
        total_points += 5
    elif len(set([card["suit"] for card in hand])) == 1 and not crib:
        total_points += 4

    print(f"Points after flushes: {total_points}")

    return total_points

def point_check_pegging(pile: list):
    total_points = 0
    run_multiplier = 1

    print(f"The pile so far is:")
    for card in pile:
        print(card['suit'] + " " + card['title'])

    # Card face value
    values = [card['value'] for card in pile]
    values.sort()

    # Card order value
    order_values = [card['order_value'] for card in pile]
    order_values.sort()
    order_values_set = list(sorted(set(order_values)))

    # Getting points for pairs
    pairs = [order_values.count(num) for num in order_values_set]
    total_points += sum([num*(num-1) for num in pairs])

    print(f"Points after pairs: {total_points}")

    # Getting points for runs - rigged in a way to work for all 5-card hands: only keeps track on the highest run in a hand
    ordered_differences = np.array([order_values_set[i+1] - order_values_set[i] for i in range(len(order_values_set)) if i < len(order_values_set) - 1])
    runs = np.split(ordered_differences, np.where(ordered_differences > 1)[0])
    counter = max([sum(run==1) for run in runs]) + 1

    # Checking for double runs, triple runs, double-double runs, etc
    just_added = False
    for i in range(len(ordered_differences)):
        if ordered_differences[i] == 1:
            if order_values.count(order_values_set[i]) > 1 and not just_added:
                run_multiplier *= order_values.count(order_values_set[i])
            elif just_added:
                just_added = False
            if order_values.count(order_values_set[i+1]) > 1:
                run_multiplier *= order_values.count(order_values_set[i+1])
                just_added = True
    total_points += counter*run_multiplier if counter > 2 else 0

    print(f"Points after runs: {total_points}")

    # Getting points for reaching 15 or 31
    if sum([card["value"] for card in pile]) == 15 or sum([card["value"] for card in pile]) == 31:
        total_points += 2

    # Getting points for a flush
    if len(set([card["suit"] for card in pile])) == 1 and len(pile) == 5:
        total_points += 5
    elif len(set([card["suit"] for card in pile])) == 1 and len(pile == 4):
        total_points += 4

    print(f"Points after flushes: {total_points}")

    return total_points


def pegging_prompt(hand: list):
    # This can be the console-based pegging to get the scoring working
    print("Your hand, sire: ")
    for card in hand:
        print(card['suit'] + " " + card['title'])
    played_card = ''
    while played_card == '':
        played_card_text = input("State the card that you wish to play: ")
        for card in hand:
            if card["suit"][0] == played_card_text[-1] and card["order_value"] == int(played_card_text[:-1]):
                played_card = card
                hand.remove(card)
        if played_card == '':
            print("You super don't have that card, try again.")

    return played_card


answer = ''
if __name__ == "__main__":
    player1 = generateCards(4)
    player1_points = 0
    player2 = generateCards(4)
    player2_points = 0
    #cut_card = generateCards(1)
    pile = []

    print("Hello and Welcome! To play a card, state it in the format of the")
    print("number of the card's order followed by the first letter of its suit.")

    player1_turn = True
    while True:
        if player1_turn:
            print("PLAYER 1's TURN")
            answer = pegging_prompt(player1)
        else:
            print("PLAYER 2's TURN")
            answer = pegging_prompt(player2)

        pile.append(answer)
        if len(pile) > 5:
            pile = pile[-5:]

        if len(pile) > 1:
            if player1_turn:
                player1_points += point_check_pegging(pile)
            else:
                player2_points += point_check_pegging(pile)

        player1_turn = not player1_turn

        if answer == "done":
            break