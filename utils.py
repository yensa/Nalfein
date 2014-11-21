# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import pygame

from collections import namedtuple


Point = namedtuple('Point', ['x', 'y'])
Size = namedtuple('Size', ['width', 'height'])


class Color(object):
    def __init__(self, rgbavalue):
        if isinstance(rgbavalue, str):
            self._pygameColor = pygame.Color(rgbavalue)
        else:
            self._pygameColor = pygame.Color(*rgbavalue)

    @property
    def rgba(self):
        return self._pygameColor

    def __repr__(self):
        return repr(self._pygameColor)

    def __str__(self):
        return repr(self)
