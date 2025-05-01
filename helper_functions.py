import random
import pygame
from point_counting import point_check, point_check_pegging
from cards import Card
from buttons import Button

def generate_cards(deck: list, num_cards: int) -> list:
    hand = []
    for i in range(num_cards):
        new_card_info = deck.pop(random.randint(0,len(deck)-1))
        new_card = Card(card_info=new_card_info)
        new_card.set_pos(x=3000, y=3000)
        new_card.set_scale(2)
        hand.append(new_card)
    return hand

def check_for_playable_cards(hand: list, running_sum: int) -> bool:
    # Looks to see if the player can possibly go again and forces them to play it.
    for card in hand:
        if card.get_value() + running_sum <= 31:
            print("Bruh you literally have to play a card.")
            return True                      
    return False

def initialize_buttons() -> list:
    buttons = []
    # 'go' button
    buttons.append(Button(color=(173,216, 230), x=80, y=800//2 - 160, label="go", height=60, width=120, enabled=True))
    # reveal button
    buttons.append(Button(color=(173,13,230), x=400, y=800//2 - 160, label="reveal", height=60, width=120, enabled=True))
    return buttons

def initialize_hands(deck) -> list:
    return [{"hand": generate_cards(deck=deck, num_cards=6), "pile": []}, {"hand": generate_cards(deck=deck, num_cards=6), "pile": []}]

def draw_hand(win, hands: list, turn:int, cut_card: Card, crib: list) -> None:
    '''
    Draws the hand of the active player
    '''
    for c in hands[turn]["hand"]:
        c.draw(win)
    for h in hands:
        for c in h["pile"]:
            c.draw(win)
    for c in crib:
        c.draw(win)
    if cut_card:
        cut_card.draw(win)

def position_hands(stage: str, hands: list, cut_card: Card, crib: list):
    if stage == "Discarding":
        for h in hands:
            for i, c in enumerate(h["hand"]):
                c.set_pos(x=i*198 + 3, y=800//2 + 110)
                c.set_scale(2)
    elif stage == "Cutting Card":
        for h in hands:
            for i, c in enumerate(h["hand"]):
                c.disenable()
                c.backside = True
                c.set_pos(x=i*120 + 3, y=800//2 + 200)
                c.set_scale(1)
        for c in crib:
            c.disenable()
            c.set_pos(x=540, y=10)
            c.set_scale(1)
            c.set_rotation(random.randint(-7, 7))
            c.backside = True
    elif stage == "Pegging":
        for h in hands:
            for i, c in enumerate(h["hand"]):
                c.set_pos(x=i*198 + 3, y=800//2 + 110)
                c.set_scale(2)
        cut_card.set_pos(800, 200)
        cut_card.set_scale(1)
    elif stage == "Counting":
        for i, h in enumerate(hands):
            for j, c in enumerate(h["pile"]):
                c.set_pos(x=i*600 + (j%2)*200 + 10, y=(j//2)*240 + 310)
                c.set_scale(1.5)
        for z, c in enumerate(crib):
            c.set_pos(x=z*150 + 600, y=10)
            c.set_scale(1)
            c.backside = False
            c.highlighted = False

        cut_card.set_pos(410, 310)
        cut_card.set_scale(1.5)
        
    return hands, cut_card, crib

def draw_buttons(win, buttons: Button) -> None:
    for b in buttons:
        b.draw(win)

def discarding_logic(hand: list):
    '''
    Returns the hand if two cards are selected to be discarded. Also
    returns the two cards to be added to the crib
    '''
    discard_list = []
    discard_idxs = []

    for idx, c in enumerate(hand):
        if c.highlighted and not c.backside:
            discard_list.append(c)
            discard_idxs.append(idx)

    if len(discard_list) == 2:
        hand = [c for idx, c in enumerate(hand) if idx not in discard_idxs]
    else:
        discard_list = []

    return hand, discard_list
    
def pegging_logic(select: int, hand_and_pile: list, go_indicator: bool, total_pile: list, turn: int):
    new_points = -1
    running_sum = sum([c.get_value() for c in total_pile])

    # Logic for claiming we are done
    if select == -1:
        if check_for_playable_cards(hand=hand_and_pile["hand"], running_sum=running_sum):
            go_indicator = 0
            return new_points, running_sum, go_indicator
        else:
            if not go_indicator:
                go_indicator = turn + 1
            else:
                total_pile.clear()
                running_sum = 0
                new_points = 1
                go_indicator = 0
            return new_points, running_sum, go_indicator
    # If we are trying to play a card, we want to make sure it's legal and then calculate the points
    elif hand_and_pile["hand"][select].get_value() + running_sum > 31:
        return new_points, running_sum, go_indicator
    else: # playable card is placed down
        selected_card = hand_and_pile["hand"].pop(select)
        selected_card.set_rotation(random.randint(-7, 7))
        selected_card.set_pos(1000, 150*turn + 100)
        selected_card.set_scale(1)
        total_pile.append(selected_card)
        hand_and_pile["pile"].append(selected_card)
        running_sum += selected_card.get_value()
        new_points = point_check_pegging(pile=total_pile, running_sum=running_sum)
        if running_sum == 31:
            total_pile.clear()
            running_sum = 0
        go_indicator = 0

    return new_points, running_sum, go_indicator

def reset_deck() -> list:
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
    return deck
