import pygame as pg
from Rectangle import Rectangle


class Button(Rectangle):
    def __init__(self, color=None, x=0, y=0, w=0, h=0, text=None):
        Rectangle.__init__(self, x, y, w, h, color)
        self.text = text
        if self.text:
            self.text_rect = text.get_rect()
            self.text_rect.center = (x+w//2, y+h//2)

    def is_mouse_on(self):
        mouse_pos = pg.mouse.get_pos()
        if (mouse_pos[0] > self.x) and (mouse_pos[1] > self.y) and (mouse_pos[0] < self.x+self.w) and (mouse_pos[1] < self.y+self.h):
            return True
        else:
            return False

    def set_text(self, text):
        self.text = text

    def draw(self, screen):
        super(Button, self).draw(screen)
        if self.text:
            screen.blit(self.text, self.text_rect)

