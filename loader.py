# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from os import path
from weakref import WeakValueDictionary

import pygame


class Loader(WeakValueDictionary):
    def __init__(self, loader):
        super(Loader, self).__init__()

        self.__load = loader

    def __getitem__(self, key):
        try:
            return super(Loader, self).__getitem__(key)
        except KeyError:
            super(Loader, self).__setitem__(key, self.__load(key))


class ImageLoader(object):
    def __init__(self, path):
        self.__path = path

    def __call__(self, key):
        return pygame.image.load(path.join(self.__path, key)).convert_alpha()
