# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import pygame

from UserList import UserList
from collections import namedtuple


Point = namedtuple('Point', ['x', 'y'])
Size = namedtuple('Size', ['width', 'height'])


class Color(UserList):
    def __init__(self, rgbavalue=(0, 0, 0, 255)):
        if isinstance(rgbavalue, str):
            self._pygameColor = pygame.Color(rgbavalue)
        else:
            self._pygameColor = pygame.Color(*rgbavalue)

        super(Color, self).__init__(self._pygameColor)

    def __repr__(self):
        return repr(self._pygameColor)

    def __str__(self):
        return repr(self)


class RenderQueue(object):
    def __init__(self, objs=[]):
        self._objs = sorted(objs, self.__sort)

    def __sort(self, a, b):
        return a.z_index - b.z_index

    def add(self, o):
        # assert isinstance(o, Widget)
        self._objs.append(o)
        self._objs = sorted(self._objs, self.__sort)

    def __iter__(self):
        for i in self._objs:
            yield i
