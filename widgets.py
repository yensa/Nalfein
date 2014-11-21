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
        pygame.draw.rect(surf, self.bgcolor.rgba, self.rect)


class Label(Widget):
    def __init__(self, text, pos=Point(0, 0), theme=DefaultTheme()):
        super(Label, self).__init__(pos, theme)

        self.bgcolor = Color(theme.get('label.bgcolor', 'black'))

        self.font = Font('label.font', theme)

        self._text = text

        self.width, self.height = self.font.size(self._text)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, t):
        self._text = t
        self.size = self.font.size(self._text)
        self.rect.width, self.rect.height = self.size.width, self.size.height


class Button(Widget):
    def __init__(self, text, action, pos=Point(0, 0), theme=DefaultTheme()):
        super(Button, self).__init__(pos, theme)

        self.click = Signal()
        self.unclick = Signal()

        self.bgcolor = Color(theme.get('button.bgcolor', 'black'))
        self.clicked_bgcolor = Color(
            theme.get('button.clicked_bgcolor', 'white'))

        self.font = Font('button.font', theme)

        self.pressed = False

        self.text = text

        self.click.connect(self._clicked)
        self.unclick.connect(self._unclicked)

        self.click.connect(action)

    def _clicked(self, button):
        if button == LEFTMOUSEBUTTON:
            self.pressed = True

    def _unclicked(self, button):
        if button == LEFTMOUSEBUTTON:
            self.pressed = False

    def render(self, surf):
        if self.pressed:
            pygame.draw.rect(surf, self.clicked_bgcolor.rgba, self.rect)
        else:
            pygame.draw.rect(surf, self.bgcolor.rgba, self.rect)
        textsize = self.font.size(self.text)
        pos = Point(self.left + (self.rect.width - textsize.width),
            self.top + (self.rect.height - textsize.height))
        self.font.render(self.text, surf, pos)
