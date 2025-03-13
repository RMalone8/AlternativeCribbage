import random
import math
import numpy as np
from point_counting import point_check, point_check_pegging
import pygame
import pygame.gfxdraw

pygame.init()

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

def pegging_play_card(card: dict, previous_run_points: int) -> list:
    '''
    Returns two fields:
    Firstis the number of points acquired,
    Second is the previous run points, important for calculating the points for runs in pegging
    '''

    

def check_for_playable_cards(hand: list, running_sum: int) -> bool:
    # Looks to see if the player can possibly go again and forces them to play it.
    for card in hand:
        if card["value"] + running_sum <= 31:
            print("Bruh you literally have to play a card.")
            return True                      
    return False

def draw_hand_pegging(hand: list) -> list:
    i = 0
    pos_info = []
    for card in hand:
        # card background
        pos_dict = {"x": i*200 + 80, "y": HEIGHT//2 - 80, "width": 120, "height": 450}
        pos_info.append(pos_dict)
        pygame.draw.rect(WIN, (255, 255, 255), (pos_dict['x'], pos_dict['y'], pos_dict['width'], pos_dict['height']))
        # symbols on card to identify which is which
        for val in range(card['order_value']):
            if card['suit'] == "Spades" or card['suit'] == "Diamonds":
                pygame.draw.rect(WIN, COLORS[card['color']], (i*200 + 100, HEIGHT//2 - 60 + val*30, 40, 20))
            else:
                pygame.draw.circle(WIN, COLORS[card['color']], (i*200 + 100, HEIGHT//2 - 60 + val*35), 17)
                pygame.gfxdraw.aacircle(WIN, i*200 + 100, HEIGHT//2 - 60 + val*35, 16, COLORS[card['color']])
        i += 1
    return pos_info

def draw_game_buttons() -> list:
    pos_info = []
    pos_dict = {"x": 80, "y": HEIGHT//2 - 160, "width": 120, "height": 60}
    pos_info.append(pos_dict)
    pygame.draw.rect(WIN, (173, 216, 230), (pos_dict['x'], pos_dict['y'], pos_dict['width'], pos_dict['height']))
    return pos_dict

def check_click(x: float, y: float, pos_info: list, num_cards: int) -> int: # encoding for which button
    # right now, I will only allocate enocding for 0-3 being the cards and then 4 will be 'go'
    i = 0
    for card in range(num_cards):
        if is_in_bounds(x, y, pos_info[i]):
            return i
        i += 1
    # checking for 'go' and beyond... (Will probably eventually have to be i = 6 to make room for the discard stage)
    if is_in_bounds(x, y, pos_info[i]):
        return 4
    return None

def is_in_bounds(x: float, y: float, positions: list) -> bool:
    '''
    Checking if inputted coordinates are within a particular bounds
    '''
    if x >= positions['x'] and x <= positions['width'] + positions['x'] and y >= positions['y'] and y <= positions['height'] + positions['y']:
        return True
    return False

def pegging_logic(select: int, hands: list, t: int, r_sum: int, prp: int, stack: list, g_count: int):
    go_count = g_count
    turn = t
    previous_run_points = prp
    running_sum = r_sum
    selection = select
    pile = stack
    player_hands = hands
    # If we are trying to play a card, we want to make sure it's legal and then calculate the points
    if selection < len(player_hands[turn%2]) and player_hands[turn%2][selection]['value'] + running_sum < 32:
        pile.append(player_hands[turn%2][selection])
        running_sum += player_hands[turn%2][selection]['value']
        player_hands[turn%2].remove(player_hands[turn%2][selection])
        new_points, previous_run_points = point_check_pegging(pile=pile, previous_run_points=previous_run_points)
        player_points[turn%2] += new_points
        turn += 1
        go_count = 0
    if selection == 4 and not check_for_playable_cards(player_hands[turn%2], running_sum) or running_sum == 31:
        go_count += 1
        # override if pile == 31
        if running_sum == 31:
            go_count = 31
            turn -= 1
        # If both players cannot go, the player to go most recently gets the point and we reset the pile
        if go_count > 1:
            go_count = 0
            pile.clear()
            player_points[turn%2] += 1
            previous_run_points = 0
            running_sum = 0
        turn += 1
    return go_count, turn, previous_run_points, running_sum, pile, player_hands

WIDTH = 1200
HEIGHT = 800
COLORS = {"Black": (0, 0, 0), "Red": (255, 0, 0)}
FONT = pygame.font.Font('freesansbold.ttf', 32)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Alternative Cribbage")

if __name__ == "__main__":
    turn = 0
    player_hands = [generateCards(4), generateCards(4)]
    player_points = [0, 0]
    #cut_card = generateCards(1)
    pile = []
    previous_run_points = 0
    new_points = 0
    running_sum = 0
    go_count = 0
    while True:
        WIN.fill((0, 0, 0))
        # set up the screen
        position_info = draw_hand_pegging(player_hands[turn%2])
        position_info.append(draw_game_buttons())

        # pile info
        pile_number = FONT.render(f'Current pile is at: {running_sum}', True, (255, 255, 255), (0, 0, 0))
        pile_num_rect = pile_number.get_rect()
        pile_num_rect.center = (300, 60)
        WIN.blit(pile_number, pile_num_rect)

        # player info
        player_name = FONT.render(f'Player {turn%2 + 1}\'s Turn', True, (255, 255, 255), (0, 0, 0))
        p_name_rect = player_name.get_rect()
        p_name_rect.center = (300, 25)
        WIN.blit(player_name, p_name_rect)

        player1_points = FONT.render(f'Player 1\'s Points: {player_points[0]}', True, (255, 255, 255), (0, 0, 0))
        p1_points_rect = player1_points.get_rect()
        p1_points_rect.center = (300, 95)
        WIN.blit(player1_points, p1_points_rect)
        player2_points = FONT.render(f'Player 2\'s Points: {player_points[1]}', True, (255, 255, 255), (0, 0, 0))
        p2_points_rect = player2_points.get_rect()
        p2_points_rect.center = (300, 130)
        WIN.blit(player2_points, p2_points_rect)

        # In-game activity
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                selection = check_click(x, y, pos_info=position_info, num_cards=len(player_hands[turn%2]))
                # If we've clicked something, let's do what must be done
                if type(selection) == int:
                    if len(player_hands[0]) != 0 and len(player_hands[1]) != 0:
                        go_count, turn, previous_run_points, running_sum, pile, player_hands = pegging_logic(select=selection, hands=player_hands, t=turn, r_sum=running_sum, prp=previous_run_points, stack=pile, g_count=go_count)
                    '''
                    # If we are trying to play a card, we want to make sure it's legal and then calculate the points
                    if selection < len(player_hands[turn%2]) and player_hands[turn%2][selection]['value'] + running_sum < 32:
                        pile.append(player_hands[turn%2][selection])
                        running_sum += player_hands[turn%2][selection]['value']
                        player_hands[turn%2].remove(player_hands[turn%2][selection])
                        new_points, previous_run_points = point_check_pegging(pile=pile, previous_run_points=previous_run_points)
                        player_points[turn%2] += new_points
                        turn += 1
                        go_count = 0
                    if selection == 4 and not check_for_playable_cards(player_hands[turn%2], running_sum) or running_sum == 31:
                        go_count += 1
                        # override if pile == 31
                        if running_sum == 31:
                            go_count = 31
                            turn -= 1
                        # If both players cannot go, the player to go most recently gets the point and we reset the pile
                        if go_count > 1:
                            go_count = 0
                            pile.clear()
                            player_points[turn%2] += 1
                            previous_run_points = 0
                            running_sum = 0
                        turn += 1
            '''
            if event.type == pygame.QUIT:
                pygame.quit()
        
        pygame.display.flip()

    pygame.quit()
    '''
    print("Hello and Welcome! To play a card, state it in the format of the")
    print("number of the card's order followed by the first letter of its suit.")

    while len(player_hands[0]) != 0 or len(player_hands[1]) != 0:
        # Logic to prompt for playing a card, checks to see if the card played can even be played.
        # Will also reward the player that played the last card the points and the other starts the pile
        while True:
            print(f"----- PLAYER {turn%2 + 1}'s TURN -----\n")
            print(f"PILE SUM IS THUS: {running_sum}\n" )
            print(f"Player 1 has {player_points[0]} points.")
            print(f"Player 2 has {player_points[1]} points.")
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
        
            # Did they BOTH say go? If so, let's reset the pile
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

        turn += 1

    # last check for how the pile ended
    turn += 1
    if running_sum == 31:
        player_points[turn%2] += 2
    else:
        player_points[turn%2] += 1
    print(f"Pegging Over!! Player 1 scored {player_points[0]} and Player 2 scored {player_points[1]}... What a game!")
'''

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
#          "order_value": 5},4
#          ]

# print(point_check_pegging(pile=pile, previous_run_points=00))
