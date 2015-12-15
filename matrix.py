#!/usr/bin/env python

from __future__ import unicode_literals

import pygame
import sys


screen = pygame.display.set_mode((320, 240))
background_color = 0, 0, 0
foreground_color = 255, 255, 0


class Matrix(object):
    def __init__(self):
        self.blocks = []

    def take_red_pill(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self._quit()

    def _quit(self):
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    matrix = Matrix()
    matrix.take_red_pill()
