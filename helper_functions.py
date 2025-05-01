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
        new_card.set_pos(x=i*198 + 3, y=800//2 + 110)
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

def draw_hand(win, hands: list, turn:int, cut_card: Card, crib: list, draw_crib: bool) -> list:
    '''
    Draws the hand of the active player
    '''
    if draw_crib:
        for c in crib:
            c.draw(win)
    else:
        for c in hands[turn]["hand"]:
            c.draw(win)
        for h in hands:
            for c in h["pile"]:
                c.draw(win)

    if cut_card:
        cut_card.draw(win)


    '''
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
    '''

def position_hands(stage: str, hands: list, cut_card: Card):
    if stage == "Discarding":
        for h in hands:
            for i, c in enumerate(h["hand"]):
                c.set_pos(x=i*198 + 3, y=800//2 + 110)
                c.set_scale(2)
    elif stage == "Cutting Card":
        for h in hands:
            for i, c in enumerate(h["hand"]):
                c.set_pos(x=i*120 + 3, y=800//2 + 200)
                c.set_scale(1)
    elif stage == "Pegging":
        for h in hands:
            for i, c in enumerate(h["hand"]):
                c.set_pos(x=i*198 + 3, y=800//2 + 110)
                c.set_scale(2)
        cut_card.set_pos(800, 200)
        cut_card.set_scale(1)

    return hands, cut_card

def draw_buttons(win, buttons: Button) -> None:
    for b in buttons:
        b.draw(win)

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
    
def pegging_logic(select: int, hand_and_pile: list, go_flag: bool, total_pile: list, turn: int):
    new_points = -1
    running_sum = sum([c.get_value() for c in total_pile])

    # Logic for claiming we are done
    if select == -1:
        if check_for_playable_cards(hand=hand_and_pile["hand"], running_sum=running_sum):
            go_flag = False
            return new_points, running_sum, go_flag
        else:
            if not go_flag:
                go_flag = True
            else:
                total_pile.clear()
                running_sum = 0
                new_points = 1
                go_flag = False
            return new_points, running_sum, go_flag
    # If we are trying to play a card, we want to make sure it's legal and then calculate the points
    elif hand_and_pile["hand"][select].get_value() + running_sum > 31:
        return new_points, running_sum, go_flag
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
        go_flag = False

    return new_points, running_sum, go_flag

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
