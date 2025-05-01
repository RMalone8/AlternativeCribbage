import pygame

class Card:
    def __init__(self, card_info, x=0, y=0, scale=1, rotation=0):
        self.card_info = card_info
        self.x = x
        self.y = y
        self.scale = scale
        self.rotation = rotation
        self.backside = True
        self.highlighted = False
        self.enable_highlight = True

    def get_value(self) -> int:
        return self.card_info['value']
    
    def get_ordered_val(self) -> int:
        return self.card_info['order_value']
    
    def get_suit(self) -> str:
        return self.card_info['suit']

    def get_color(self) -> str:
        return self.card_info['color']
    
    def get_title(self) -> str:
        return self.card_info['title']

    def set_pos(self, x, y) -> None:
        self.x = x
        self.y = y

    def set_scale(self, scale) -> None:
        self.scale = scale

    def set_rotation(self, rotation) -> None:
        self.rotation = rotation

    def disenable(self) -> None:
        self.enable_highlight = False

    def enable(self) -> None:
        self.enable_highlight = True

    def draw(self, win):
        # display the side that's showing
        if self.backside:
            card_sprite = pygame.image.load(f"Assets/Backs/Card-Back-04.png").convert_alpha()
        else:
            card_sprite = pygame.image.load(f"Assets/Cards/Modern/{(self.card_info['suit'][0]).lower()}{self.card_info['order_value']}.png").convert_alpha() 
        card_sprite = pygame.transform.scale(card_sprite, (100*self.scale, 140*self.scale))
        card_sprite = pygame.transform.rotate(card_sprite, self.rotation)
        
        # if it's highlighted
        if self.highlighted and not self.backside:
            highlighted_sprite = pygame.Surface(card_sprite.get_size()).convert_alpha()
            highlighted_sprite.fill((255,255,160))
            card_sprite.blit(highlighted_sprite, (0,0), special_flags=pygame.BLEND_RGBA_MULT)

        # position the sprite and draw it to the screen!
        card_rect = card_sprite.get_rect()
        card_rect.topleft = (self.x, self.y)
        win.blit(card_sprite, card_rect)

    def check_click(self, mouse_x, mouse_y) -> int:
        if self.x < mouse_x < self.x + self.scale*100 and self.y < mouse_y < self.y + self.scale*140:
            if self.enable_highlight:
                self.highlighted =  not self.highlighted
            if not self.backside:
                return 1
        return 0
