import pygame

class Card:
    def __init__(self, card_info, x, y, scale, rotation=0):
        self.card_info = card_info
        self.x = x
        self.y = y
        self.scale = scale
        self.backside = True
        self.highlighted = False

    def draw(self, win):
        # display the side that's showing
        if self.backside:
            card_sprite = pygame.image.load(f"Assets/Backs/Card-Back-04.png").convert_alpha()
        else:
            card_sprite = pygame.image.load(f"Assets/Cards/Modern/{(self.card_info['suit'][0]).lower()}{self.card_info['order_value']}.png").convert_alpha() 
        card_sprite = pygame.transform.scale(card_sprite, (100*self.scale, 140*self.scale))
        card_sprite = pygame.transform.rotate(card_sprite, self.card_info['rotation'])
        
        # if it's highlighted
        if self.highlighted and not self.backside:
            highlighted_sprite = pygame.Surface(card_sprite.get_size()).convert_alpha()
            highlighted_sprite.fill((255,255,160))
            card_sprite.blit(highlighted_sprite, (0,0), special_flags=pygame.BLEND_RGBA_MULT)

        # position the sprite and draw it to the screen!
        card_rect = card_sprite.get_rect()
        card_rect.topleft = (self.x, self.y)
        win.blit(card_sprite, card_rect)

    def check_click(self, mouse_x, mouse_y) -> bool:
        if self.x < mouse_x < self.x + self.scale*100 and self.y < mouse_y < self.y + self.scale*140:
            if not self.backside:
                self.highlighted =  not self.highlighted
            return True
        return False
