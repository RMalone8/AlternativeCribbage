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
    hands = [generateCards(6), generateCards(6)]
    player_points = [0, 0]
    card_was_cut = False
    discard_list = [[-1, -1], [-1, -1]]
    crib = []
    total_pile = []
    player_piles = [[], []]
    new_points = 0
    running_sum = 0
    go_count = 0
    while True:
        WIN.fill((0, 0, 0))
        # set up the screen
        position_info = draw_hand(win=WIN, hand=hands[turn%2], discard_list=discard_list[turn%2])
        position_info.append(draw_game_objs(win=WIN, player_piles=player_piles))

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

        # In-game activity
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                selection = check_click(x, y, pos_info=position_info, num_cards=len(hands[turn%2]))
                # If we've clicked something, let's do what must be done
                if type(selection) == int:
                    # discarding stage
                    if len(crib) != 4:
                        turn += discarding_logic(select=selection, discard_list=discard_list[turn%2], crib=crib, player_hand=hands[turn%2])
                        print(crib)

                    # pegging stage, have to reveal the cut card first tho
                    elif len(hands[0]) != 0 or len(hands[1]) != 0:
                        if not card_was_cut:
                            cut_card = generateCards(1)
                            card_was_cut = True
                        go_count, turn, running_sum, new_points = pegging_logic(selection=selection, player_hands=hands, player_points=player_points, turn=turn, running_sum=running_sum, pile=total_pile, player_piles=player_piles, go_count=go_count)
                    
                    # counting points in our hands
                    else:
                        # we record whoever finished the last pile if it didn't end in 31 (which would've already been recorded then)
                        if sum([card["value"] for card in total_pile]) < 31 and total_pile:
                            player_points[(turn-1)%2] += 1
                        total_pile = []
                        # now we need to count points in order:
                        turn = first_turn
                        player_points[turn%2] += point_check(player_piles[turn%2], cut_card=cut_card)
                        turn += 1
                        player_points[turn%2] += point_check(player_piles[turn%2], cut_card=cut_card)
                        player_points[turn%2] += point_check(crib, cut_card=cut_card, is_crib=True)
                        #card_was_cut = False
            if event.type == pygame.QUIT:
                pygame.quit()
        
        pygame.display.flip()
