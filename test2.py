import pygame
import color


class Wall:

    COLOR = color.BLUE

    def __init__(self, rect):
        self.rect = rect

        self.v_left = pygame.math.Vector2()
        self.v_left.from_polar((1, 180))

        self.v_right = pygame.math.Vector2()
        self.v_right.from_polar((1, 0))

        self.v_top = pygame.math.Vector2()
        self.v_top.from_polar((1, -90))

        self.v_bottom = pygame.math.Vector2()
        self.v_bottom.from_polar((1, 90))

    def render(self, surface):
        pygame.draw.rect(surface, Wall.COLOR, self.rect)

    @property
    def right(self):
        return pygame.rect.Rect(self.rect.topright, (1, self.rect.h))

    @property
    def left(self):
        return pygame.rect.Rect(self.rect.topleft, (1, self.rect.h))

    @property
    def top(self):
        return pygame.rect.Rect(self.rect.topleft, (self.rect.w, 1))

    @property
    def bottom(self):
        return pygame.rect.Rect(self.rect.bottomleft, (self.rect.w, 1))