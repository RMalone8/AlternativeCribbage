import random
import math
import numpy as np
import pygame
import pygame.gfxdraw
from helper_functions import *

pygame.init()

WIDTH = 1200
HEIGHT = 800
COLORS = {"Black": (0, 0, 0), "Red": (255, 0, 0)}
FONT = pygame.font.Font('freesansbold.ttf', 32)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Alternative Cribbage")

if __name__ == "__main__":
    first_turn = 0
    turn = first_turn
    deck = reset_deck()
    hands = [generateCards(deck=deck, num_cards=6), generateCards(deck=deck, num_cards=6)]
    player_points = [0, 0]
    reveal_cards = False
    card_was_cut = False
    finished_pegging = False
    crib_counting = False
    discard_list = [[-1, -1], [-1, -1]]
    cut_card = None
    crib = []
    total_pile = []
    player_piles = [[], []]
    new_points = 0
    running_sum = 0
    go_count = 0
    while True:
        WIN.fill((0, 0, 0))
        # set up the screen
        position_info = draw_hand(win=WIN, hand=hands[turn%2], discard_list=discard_list[turn%2], finished_peggging=finished_pegging, reveal_cards=reveal_cards)
        position_info.extend(draw_game_objs(win=WIN, player_piles=player_piles, cut_card=cut_card, finsihed_pegging=finished_pegging))

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

        # In-game activity
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #print(reveal_cards)
                selection = check_click(x, y, pos_info=position_info, num_cards=len(hands[turn%2]), reveal_cards=reveal_cards)
                #print(f"The current turn is: {turn}")
                # If we've clicked something, let's do what must be done
                if type(selection) == int:
                    # discarding stage
                    if len(crib) != 4 and not finished_pegging:
                        #print(position_info)
                        turn_change, reveal_cards = discarding_logic(select=selection, discard_list=discard_list[turn%2], crib=crib, player_hand=hands[turn%2], reveal_cards=reveal_cards)
                        turn += turn_change
                    # cutting the deck
                    elif not card_was_cut and not finished_pegging:
                        if selection == 6:
                            cut_card = generateCards(deck=deck, num_cards=1)[0]
                            # Points if you cut a Jack
                            if cut_card['suit'] == "Jack":
                                player_points[turn%2] += 2
                            card_was_cut = True
                    # pegging stage, have to reveal the cut card first tho
                    elif (len(hands[0]) != 0 or len(hands[1]) != 0) and not finished_pegging:
                        go_count, turn, running_sum, new_points, reveal_cards = pegging_logic(selection=selection, player_hands=hands, player_points=player_points, turn=turn, running_sum=running_sum, pile=total_pile, player_piles=player_piles, go_count=go_count, reveal_cards=reveal_cards)
                    # counting points in our hands
                    else:
                        # setting up point counting
                        if not finished_pegging:
                            # we record whoever finished the last pile if it didn't end in 31 (which would've already been recorded then)
                            if sum([card["value"] for card in total_pile]) < 31 and total_pile:
                                player_points[(turn-1)%2] += 1
                            finished_pegging = True
                            total_pile = []
                            reveal_cards = True
                            # put the piles back in our hands (they get drawn on the screen)
                            hands[0], hands[1] = player_piles[0], player_piles[1]
                            hands[0].append(cut_card)
                            hands[1].append(cut_card)
                            crib.append(cut_card)
                            # set the counting order
                            turn = first_turn
                            #print(f"Player's turn is gonna be {turn}")
                        elif not crib_counting and turn < first_turn + 2:
                            #print(f"We are now here, player's turn is gonna be: {turn}")
                            turn += counting_logic(selection=selection, player_hand=hands[turn%2], player_points=player_points, turn=turn)
                            if turn >= first_turn + 2:
                                crib_counting = True
                                turn = first_turn + 1
                                #print(f"Player {turn%2} has the crib")
                                hands[turn%2] = crib
                        elif crib_counting: # a little convoluted, but this is currently how the point counting will proceed
                                #print(f"The turn right now belongs to: {turn%2}")
                                turn += counting_logic(selection=selection, player_hand=hands[turn%2], player_points=player_points, turn=turn, is_crib=True)
                                if turn != first_turn + 1:
                                    crib_counting = False
                                    hands[0], hands[1] = [], []
                        else:
                            # time to reset it all!
                            first_turn += 1
                            turn = first_turn
                            hands = [generateCards(deck=deck, num_cards=6), generateCards(deck=deck, num_cards=6)]
                            card_was_cut = False
                            finished_pegging = False
                            crib_counting = False
                            discard_list = [[-1, -1], [-1, -1]]
                            cut_card = None
                            crib = []
                            total_pile = []
                            player_piles = [[], []]
                            new_points = 0
                            running_sum = 0
                            go_count = 0
                            reveal_cards = False
            if event.type == pygame.QUIT:
                pygame.quit()
        
        pygame.display.flip()
