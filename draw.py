# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import pygame

from theme import DefaultTheme
from utils import Size, Color


class Font(object):
    def __init__(self, name, theme=DefaultTheme()):
        def attr(attrname, default=None):
            return theme.get(name + '-' + attrname, default)

        try:
            self._font = pygame.font.Font(attr('name'), attr('size'))
        except IOError:
            self._font = pygame.font.SysFont(attr('name'), attr('size'))

        self.color = Color(attr('color', 'white'))
        self.antialias = attr('antialias', True)

        self._font.set_bold(attr('bold', False))
        self._font.set_italic(attr('italic', False))
        self._font.set_underline(attr('underline', False))

    @property
    def bold(self):
        return self._font.get_bold()

    @bold.setter
    def bold(self, state):
        self._font.set_bold(state)

    @property
    def italic(self):
        return self._font.get_italic()

    @italic.setter
    def italic(self, state):
        self._font.set_italic(state)

    @property
    def underline(self):
        return self._font.get_underline()

    @underline.setter
    def underline(self, state):
        self._font.set_underline(state)

    def size(self, text):
        return Size(*self._font.size(text))

    def render(self, text, surf, pos):
        todraw = self._font.render(text, self.antialias, self.color)
        surf.blit(todraw, pos)
