import random
import math
import numpy as np
import pygame
import pygame.gfxdraw
from helper_functions import *
from buttons import Button
from cards import Card

pygame.init()

WIDTH = 1200
HEIGHT = 800
COLORS = {"Black": (0, 0, 0), "Red": (255, 0, 0)}
FONT = pygame.font.Font('freesansbold.ttf', 32)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
STAGES = {0: "Discarding", 1: "Cutting Card", 2: "Pegging", 3: "Counting"}

pygame.display.set_caption("Alternative Cribbage")

if __name__ == "__main__":
    first_turn = 0
    turn = first_turn
    deck = reset_deck()
    player_points = [0, 0]
    pegging_points = 0
    cut_card = None
    crib = []
    total_pile = []
    player_piles = [[], []]
    discard_list = []
    new_points = 0
    running_sum = 0
    current_stage = 0
    stage_initialized = False
    go_indicator = 0

    # Button delcarations:
    buttons = initialize_buttons()

    # Hand initialization -> The empty list following the generated hand is the pile for pegging
    hands = initialize_hands(deck=deck)

    while True:
        WIN.fill((0, 0, 0))

        # pile info
        pile_number = FONT.render(f'Current pile is at: {running_sum}', True, (255, 255, 255), (0, 0, 0))
        pile_num_rect = pile_number.get_rect()
        pile_num_rect.center = (300, 60)
        WIN.blit(pile_number, pile_num_rect)
        pile_number = FONT.render(f'The last points made were: {new_points}', True, (255, 255, 255), (0, 0, 0))
        pile_num_rect = pile_number.get_rect()
        pile_num_rect.center = (300, 165)
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

        crib_owner = FONT.render(f'The crib currently belongs to Player {(first_turn+1)%2 + 1}', True, (255, 255, 255), (0, 0, 0))
        crib_owner_rect = crib_owner.get_rect()
        crib_owner_rect.center = (300, 200)
        WIN.blit(crib_owner, crib_owner_rect)

        # Button and Card drawing
        draw_buttons(win=WIN, buttons=buttons)
        draw_hand(win=WIN, hands=hands, turn=turn%2, cut_card=cut_card, crib=crib)

        # Whenever a stage needs to be setup again
        if not stage_initialized:
            stage_initialized = True
            hands, cut_card, crib = position_hands(stage=STAGES[current_stage], hands=hands, cut_card=cut_card, crib=crib)

        # In-game activity
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:

                # check for clicks
                button_select = ''.join([b.check_click(x, y) for b in buttons])

                card_pos_select = [c.check_click(x, y) for c in hands[turn%2]["hand"]]
                if 1 in card_pos_select:
                    card_select = card_pos_select.index(1)
                else:
                    card_select = -1

                # For pegging, selecting a card activates the 'go' button
                if STAGES[current_stage] == "Pegging" and card_select > -1:
                    button_select = "go"
                
                if button_select:
                    if button_select == "go":
                        if STAGES[current_stage] == "Discarding":
                            hands[turn%2]["hand"], discards = discarding_logic(hands[turn%2]["hand"])
                            discard_list.extend(discards)
                            if len(discard_list) == 4:
                                crib = discard_list
                                discard_list = []
                                current_stage += 1
                                stage_initialized = False
                            elif len(discards) == 2:
                                turn += 1

                        elif STAGES[current_stage] == "Cutting Card":
                            cut_card = generate_cards(deck=deck, num_cards=1)[0]
                            cut_card.backside = False
                            if cut_card.get_title() == "Jack":
                                player_points[turn%2] += 2
                            for h in hands:
                                for c in h["hand"]:
                                    c.backside = True
                            
                            current_stage += 1
                            stage_initialized = False
                            
                        elif STAGES[current_stage] == "Pegging":
                            pegging_points, running_sum, go_indicator = pegging_logic(select=card_select, hand_and_pile=hands[turn%2], go_indicator=go_indicator, total_pile=total_pile, turn=turn%2)
                            if pegging_points > -1:
                                for c in hands[turn%2]["hand"]:
                                    c.backside = True
                                player_points[turn%2] += pegging_points
                                turn += 1
                            elif go_indicator == turn%2 + 1:
                                for c in hands[turn%2]["hand"]:
                                    c.backside = True
                                turn += 1

                            # If we are done pegging
                            if len(hands[0]["hand"]) == 0 and len(hands[1]["hand"]) == 0:
                                # if the player did not get 31 and ended the last pile, record a point for them
                                if running_sum != 31:
                                    player_points[(turn - 1)%2] += 1
                                current_stage += 1
                                stage_initialized = False

                        elif STAGES[current_stage] == "Counting":
                            for i in range(len(player_points)):
                                hands[i]["pile"].append(cut_card)
                                player_points[i] += point_check(hand=hands[i]["pile"])
                            crib.append(cut_card)
                            player_points[(first_turn+1)%2] += point_check(hand=crib, is_crib=True)

                            # Reset everything for the next round
                            total_pile = []
                            crib = []
                            deck = reset_deck()
                            hands = initialize_hands(deck=deck)
                            cut_card = None
                            first_turn = (first_turn+1) % 2
                            turn = first_turn
                            current_stage = 0
                            stage_initialized = False

                    elif button_select == "reveal":
                        if STAGES[current_stage] != "Cutting Card":
                            for c in hands[turn%2]["hand"]:
                                c.backside = not c.backside

            if event.type == pygame.QUIT:
                pygame.quit()
        
        pygame.display.flip()
