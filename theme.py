# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import json


class Theme(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @classmethod
    def load(self, name):
        try:
            f = open(name)
        except IOError:
            # TODO: Add trace log here
            # switching to default theme
            return DefaultTheme()

        return Theme(**json.load(f))

    def __getitem__(self, name):
        return self.__dict__[name]


class DefaultTheme(Theme):
    def __init__(self):
        theme = {
            'bgcolor': (80, 80, 80),
            'defaultwidth': 100,
            'defaultheight': 100,
            'titlefont-name': 'Arial',
            'titlefont-size': 64,
            'titlefont-color': (255, 255, 255),
            'titlefont-antialias': True,
            'titlefont-bold': True,
            'titlefont-underline': False,
            'titlefont-italic': False
            }

        super(DefaultTheme, self).__init__(**theme)
