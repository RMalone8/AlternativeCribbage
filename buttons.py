import pygame

class Button:
    def __init__(self, color, x, y, height=100, width=100):
        self.color = color
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def check_click(self, mouse_x, mouse_y) -> bool:
        if self.x < mouse_x < self.x + self.width and self.y < mouse_y < self.y + self.height:
            return True
        return False

    