#!/usr/bin/env python

from __future__ import unicode_literals

import pygame
import random
import sys

pygame.init()

screen = pygame.display.set_mode((620, 640))
font = pygame.font.SysFont('monospace', 10, bold=False)
background_color = 0, 0, 0
foreground_color = 255, 255, 0
head_element_color = 255, 255, 200
characters = [chr(i) for i in range(33, 127)]


def _random_coordinates():
    return random.choice(range(0, 620, 10)), random.randint(0, 640)


class _MatrixRainBlock(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def draw(self):
        rendered_text = font.render(random.choice(characters), True, foreground_color)
        screen.blit(rendered_text, (self.x, self.y))

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


class _MatrixRain(object):
    def __init__(self, x, y, length=None):
        self._x = x
        self._y = y
        self._length = length or random.randint(10, 30)
        self._blocks = []
        self._finish = False

    def draw(self):
        if len(self._blocks) < self._length and not self._finish:
            self._blocks.append(_MatrixRainBlock(self._x, self._y + (len(self._blocks) * 12)))
        else:
            self._finish = True
            if not self._blocks:
                return
            self._blocks.pop(0)
        for block in self._blocks:
            block.draw()

    @property
    def finished(self):
        return not self._blocks and self._finish


class Matrix(object):
    def __init__(self):
        self._matrix_lines = [_MatrixRain(*_random_coordinates()) for _ in range(random.randint(1, 10))]
        self._clock = pygame.time.Clock()

    def take_red_pill(self):
        while True:
            screen.fill(background_color)
            for event in pygame.event.get():
                self._handle_event(event)
            self._redraw()

    def _handle_event(self, event):
        if event.type == pygame.QUIT:
            self._quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self._quit()

    def _quit(self):
        pygame.quit()
        sys.exit()

    def _redraw(self):
        if len(self._matrix_lines) < 200:
            self._matrix_lines.append(_MatrixRain(*_random_coordinates()))
        for matrix_line in self._matrix_lines[:]:
            if matrix_line.finished:
                self._matrix_lines.remove(matrix_line)
                continue
            matrix_line.draw()
        self._clock.tick(5)
        pygame.display.flip()

if __name__ == '__main__':
    matrix = Matrix()
    matrix.take_red_pill()
