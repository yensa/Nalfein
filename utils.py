# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import pygame

from collections import namedtuple


Point = namedtuple('Point', ['x', 'y'])
Size = namedtuple('Size', ['width', 'height'])


class Color(pygame.Color):
    def __init__(self, rgbavalue):
        if isinstance(rgbavalue, str):
            super(Color, self).__init__(rgbavalue)
        else:
            super(Color, self).__init__(*rgbavalue)
