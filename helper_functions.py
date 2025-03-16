import random
import pygame
from point_counting import point_check, point_check_pegging

def generateCards(deck: list, num_cards: int) -> list:
    hand = []
    for i in range(num_cards):
        hand.append(deck.pop(random.randint(0,len(deck)-1)))
    return hand

def check_for_playable_cards(hand: list, running_sum: int) -> bool:
    # Looks to see if the player can possibly go again and forces them to play it.
    for card in hand:
        if card["value"] + running_sum <= 31:
            print("Bruh you literally have to play a card.")
            return True                      
    return False

def draw_hand(win, hand: list, discard_list: list, finished_peggging: bool, reveal_cards: bool) -> list:
    '''
    Draws the hand of the active player, returns the position of the cards
    '''
    #print(hand)
    i = 0
    pos_info = []
    # setting up the hand pre-pegging
    if not finished_peggging:
        for card in hand:
            # cards being displayed if they are revealed, otherwise you only see their backs.
            # for the sprites that are being used, to keep proper proportions: height = 1.38411 * width
            pos_dict = {"x": i*198 + 3, "y": 800//2 + 110, "width": 200, "height": 280}
            if reveal_cards:
                pos_info.append(pos_dict)
                card_sprite = pygame.image.load(f"Assets/Cards/Modern/{(card['suit'][0]).lower()}{card['order_value']}.png").convert_alpha()
            else:
                card_sprite = pygame.image.load(f"Assets/Backs/Card-Back-04.png").convert_alpha()
            card_sprite = pygame.transform.scale(card_sprite, (pos_dict['width'], pos_dict['height']))
            if i in discard_list:
                highlighted_sprite = pygame.Surface(card_sprite.get_size()).convert_alpha()
                highlighted_sprite.fill((255,255,160))
                card_sprite.blit(highlighted_sprite, (0,0), special_flags=pygame.BLEND_RGBA_MULT)
            card_rect = card_sprite.get_rect()
            card_rect.topleft = (pos_dict['x'], pos_dict['y'])
            win.blit(card_sprite, card_rect)
            i += 1
    else: # setting up the hand post-pegging
        for card in hand:
            # cards being displayed
            pos_dict = {"x": i*198 + 3, "y": 230, "width": 200, "height": 280}
            pos_info.append(pos_dict)
            card_sprite = pygame.image.load(f"Assets/Cards/Modern/{(card['suit'][0]).lower()}{card['order_value']}.png").convert_alpha()
            card_sprite = pygame.transform.scale(card_sprite, (pos_dict['width'], pos_dict['height']))
            card_rect = card_sprite.get_rect()
            card_rect.topleft = (pos_dict['x'], pos_dict['y'])
            win.blit(card_sprite, card_rect)
            i += 1
    return pos_info

def draw_game_objs(win, player_piles: list, cut_card: dict, finsihed_pegging: bool) -> list:
    '''
    Drawing game objects (buttons, graphics) and 
    returning the positions of the interactable ones
    '''
    pos_info = []
    # setting up the screen pre-pegging
    if not finsihed_pegging:
        # The 'go' button
        pos_dict = {"x": 80, "y": 800//2 - 160, "width": 120, "height": 60}
        pos_info.append(pos_dict)
        pygame.draw.rect(win, (173, 216, 230), (pos_dict['x'], pos_dict['y'], pos_dict['width'], pos_dict['height']))
        # The 'reveal' button
        pos_dict = {"x": 400, "y": 800//2 - 160, "width": 120, "height": 60}
        pos_info.append(pos_dict)
        pygame.draw.rect(win, (255, 71, 76), (pos_dict['x'], pos_dict['y'], pos_dict['width'], pos_dict['height']))
        # each player's pegging pile
        i = 0
        for pile in player_piles:
            for card in pile:
                pile_card_sprite = pygame.image.load(f"Assets/Cards/Modern/{(card['suit'][0]).lower()}{card['order_value']}.png").convert_alpha()
                pile_card_sprite = pygame.transform.scale(pile_card_sprite, (100, 140))
                pile_card_sprite = pygame.transform.rotate(pile_card_sprite, card['rotation'])
                pile_card_rect = pile_card_sprite.get_rect()
                pile_card_rect.topleft = (1000, 150*i + 100)
                win.blit(pile_card_sprite, pile_card_rect)
            i += 1
        # drawing the cut card if we've cut it
        if cut_card is not None:
            cut_card_sprite = pygame.image.load(f"Assets/Cards/Modern/{(cut_card['suit'][0]).lower()}{cut_card['order_value']}.png").convert_alpha()
            cut_card_sprite = pygame.transform.scale(cut_card_sprite, (150, 210))
            cut_card_rect = cut_card_sprite.get_rect()
            cut_card_rect.topleft = (800, 200)
            win.blit(cut_card_sprite, cut_card_rect)
    else: # setting up the screen post-pegging
        # The 'go' button
        pos_dict = {"x": 400, "y": 600, "width": 120, "height": 60}
        pos_info.append(pos_dict)
        pygame.draw.rect(win, (173, 216, 230), (pos_dict['x'], pos_dict['y'], pos_dict['width'], pos_dict['height']))
    return pos_info

def check_click(x: float, y: float, pos_info: list, num_cards: int, reveal_cards: bool) -> int: # encoding for which button
    # right now, I will only allocate enocding for 0-3 being the cards and then 4 will be 'go'
    i = 0
    if reveal_cards:
        for card in range(num_cards):
            if is_in_bounds(x, y, pos_info[i]):
                return i
            i += 1
    # checking for 'go'
    if is_in_bounds(x, y, pos_info[i]):
        return 6
    i += 1
    # checking for 'reveal'
    if is_in_bounds(x,y, pos_info[i]):
        return 7
    return None

def is_in_bounds(x: float, y: float, positions: list) -> bool:
    '''
    Checking if inputted coordinates are within a particular bounds
    '''
    if x >= positions['x'] and x <= positions['width'] + positions['x'] and y >= positions['y'] and y <= positions['height'] + positions['y']:
        return True
    return False

def discarding_logic(select: int, discard_list: list, crib: list, player_hand: list, reveal_cards: bool) -> int:
    '''
    Logic for selecting two of the cards in hands to be discarded
    Returns an int to either increment the turn or stay where we are
    '''
    #print(f"Select is {select}")
    if select < 6:
        # deselecting
        if select in discard_list:
            discard_list[discard_list.index(select)] = -1
        # selecting if there's a slot to select a card
        elif min(discard_list) == -1:
            discard_list[discard_list.index(min(discard_list))] = select
        return 0, reveal_cards
    elif select == 6 and min(discard_list) > -1:
        discard_list.sort(reverse=True)
        for discard in discard_list:
            #print(f"discarding: {discard}")
            crib.append(player_hand.pop(discard))
        discard_list[0], discard_list[1] = -1, -1
        reveal_cards = False
        return 1, reveal_cards # add one to the turn
    elif select == 7: # change where the cards are revealed
        #print("BANG")
        reveal_cards = not reveal_cards
    return 0, reveal_cards # do not change the turn, still figuring out what to discard

def pegging_logic(selection: int, player_hands: list, player_points: list, turn: int, running_sum: int, pile: list, player_piles: list, go_count: int, reveal_cards: bool):
    new_points = 0
    # If we are trying to play a card, we want to make sure it's legal and then calculate the points
    if selection < len(player_hands[turn%2]) and player_hands[turn%2][selection]['value'] + running_sum < 32:
        selected_card = player_hands[turn%2].pop(selection)
        pile.append(selected_card)
        # adding a new field so the cards can rotate on their piles
        selected_card['rotation'] = random.randint(-7, 7)
        player_piles[turn%2].append(selected_card)
        running_sum += selected_card['value']
        new_points = point_check_pegging(pile=pile)
        player_points[turn%2] += new_points
        turn += 1
        go_count = 0
        reveal_cards = False
    elif selection == 6 and not check_for_playable_cards(player_hands[turn%2], running_sum) or running_sum == 31:
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
            running_sum = 0
        turn += 1
        reveal_cards = False
    elif selected_card == 7: # reveal the cards if need be
        reveal_cards = not reveal_cards
    return go_count, turn, running_sum, new_points, reveal_cards #pile, player_piles, player_hands, new_points

def counting_logic(selection: int, player_hand: list, player_points: list, turn: int, is_crib: bool = False) -> int:
    '''
    Returns an int to either increment the turn or stay where we are
    '''
    if selection == 6:
        player_points[turn%2] += point_check(player_hand, is_crib=is_crib)
        return 1
    return 0

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
