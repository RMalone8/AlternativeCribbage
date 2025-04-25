import pygame

class Button:
    def __init__(self, color, x, y, label:str, height=100, width=100, enabled=False):
        self.color = color
        self.x = x
        self.y = y
        self.label = label
        self.height = height
        self.width = width
        self.enabled = enabled
        self.show_label = False

    def draw(self, win):
        if self.enabled:
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def check_click(self, mouse_x, mouse_y) -> bool:
        if self.x < mouse_x < self.x + self.width and self.y < mouse_y < self.y + self.height and self.enabled:
            return self.label
        return ""
