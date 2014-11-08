# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import pygame

from utils import Point, Color
from theme import DefaultTheme
from signal import Signal
from draw import Font
from constants import *


class Widget(object):
    def __init__(self, pos=Point(0, 0), theme=DefaultTheme()):
        self.left, self.top = pos
        self.width = theme.defaultwidth
        self.height = theme.defaultheight

        self.bgcolor = Color(theme.bgcolor)

    @property
    def rect(self):
        return pygame.Rect(self.left, self.top, self.width, self.height)

    def render(self, surf):
        pygame.draw.rect(surf, self.bgcolor, self.rect)


class Button(Widget):
    click = Signal()
    unclick = Signal()

    def __init__(self, text, action, pos=Point(0, 0), theme=DefaultTheme()):
        super(Button, self).__init__(pos, theme)

        self.bgcolor = Color(theme.button.bgcolor)
        self.clicked_bgcolor = Color(theme.button.clicked_bgcolor)

        self.font = Font('button.font', theme)

        self.pressed = False

        self.text = text

        self.click.connect(self._clicked)
        self.unclick.connect(self._unclicked)

        self.click.connect(action)

    def _clicked(self, button):
        if button == constants.LEFTMOUSEBUTTON:
            self.pressed = True

    def _unclicked(self, button):
        if button == constants.LEFTMOUSEBUTTON:
            self.pressed = False

    def render(self, surf):
        if self.pressed:
            pygame.draw.rect(surf, self.clicked_bgcolor, self.rect)
        else:
            pygame.draw.rect(surf, self.bgcolor, self.rect)
        textsize = self.font.size(self.text)
        pos = Point(self.left + (self.rect.width - textsize.width),
            self.top + (self.rect.height - textsize.height))
        self.font.render(self.text, surf, pos)
