# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import pygame

from utils import Point
from theme import DefaultTheme


class Widget(object):
    def __init__(self, pos=Point(0, 0), theme=DefaultTheme()):
        self.left, self.top = pos
        self.width = theme.defaultwidth
        self.height = theme.defaultheight

        self.bgcolor = theme.bgcolor

    @property
    def rect(self):
        return pygame.Rect(self.left, self.top, self.width, self.height)

    def render(self, surf):
        pygame.draw.rect(surf, self.bgcolor, self.rect)
