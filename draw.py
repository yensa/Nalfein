# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import pygame

# from theme import DefaultTheme
from utils import Size, Color


class Font(object):
    def __init__(self, name, size=22, color=(0, 0, 0, 255)):
        self.name = name
        self.size = size
        self.color = color

        try:
            self.font = pygame.font.SysFont(self.name, self.size)
        except:
            try:
                self.font = pygame.font.Font(self.name, self.size)
            except:
                self.font = pygame.font.SysFont('Arial', self.size)

    def render(self, text):
        return self.font.render(text, True, self.color)

    def get_height(self):
        return self.font.get_height()

    def get_width(self, text):
        return self.font.size(text)[0]

    @property
    def bold(self):
        return self.font.get_bold()

    @bold.setter
    def bold(self, value):
        assert value in [True, False]
        self.font.set_bold(value)

    @property
    def italic(self):
        return self.font.get_italic()

    @italic.setter
    def italic(self, value):
        assert value in [True, False]
        self.font.set_italic(value)

    @property
    def underline(self):
        return self.font.get_underline()

    @underline.setter
    def underline(self, value):
        assert value in [True, False]
        self.font.set_underline(value)
