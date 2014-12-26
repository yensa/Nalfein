# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import pygame

from utils import Point, Color, RenderQueue
# from theme import DefaultTheme
from signal import Signal
from draw import Font
from constants import *


class Widget(object):
    def __init__(self, pos=(0, 0), size=(100, 100)):
        self.pos = pos
        self.size = list(size)

        self._bgcolor = (80, 80, 80, 0)

        self.transparent = True

        self.z_index = 0

        self._focus = False

        self.queue = RenderQueue()

    @property
    def focus(self):
        return self._focus

    @focus.setter
    def focus(self, value):
        if hasattr(self, 'elements'):
            for element in self.elements:
                element.focus = value
        self._focus = value

    def resize(self, newsize):
        self.size = list(newsize)

    def move(self, value):
        self.pos = (self.pos[0] + value[0], self.pos[1] + value[1])
        for r in self.queue:
            r.move(value)

    def move_to(self, point):
        dx = point[0] - self.pos[0]
        dy = point[1] - self.pos[1]
        self.pos = point
        for r in self.queue:
            r.move((dx, dy))

    @property
    def bgcolor(self):
        return self._bgcolor

    @bgcolor.setter
    def bgcolor(self, value):
        if len(value) == 4:
            self.transparent = (value[3] == 0)
        self._bgcolor = value

    @property
    def alpha(self):
        return self.bgcolor[-1]

    @alpha.setter
    def alpha(self, value):
        assert value >= 0 and value < 256
        self.transparent = (value == 0)
        self.bgcolor = tuple(list(self.bgcolor[:2]) + [value])

    @property
    def width(self):
        return self.size[0]

    @width.setter
    def width(self, nwidth):
        self.size[0] = nwidth

    @property
    def height(self):
        return self.size[1]

    @height.setter
    def height(self, nheight):
        self.size[1] = nheight

    @property
    def rect(self):
        return pygame.Rect(self.pos, self.size)

    def draw(self, surf):
        if not self.transparent:
            pygame.draw.rect(surf, self.bgcolor, self.rect)
        for r in self.queue:
            r.draw(surf)


class Label(Widget):
    def __init__(self, text, font, pos=(0, 0), size=(100, 40)):
        super(Label, self).__init__(pos, size)

        self.font = font
        self.text = text

    def get_font_width(self, text=None):
        if text is None:
            text = self.text
        return self.font.get_width(text)

    def draw(self, surf):
        surf.blit(self.font.render(self.text), self.pos)


class Rect(Widget):
    def __init__(self, pos, size, bgcolor):
        super(Rect, self).__init__(pos, size)

        self.bgcolor = bgcolor

    def draw(self, surf):
        pygame.draw.rect(surf, self.bgcolor, self.rect)


class LineEdit(Widget):
    def __init__(self, pos=(0, 0), size=(100, 40)):
        super(LineEdit, self).__init__(pos, size)

        self.keydown = Signal()

        self.font = Font('Arial')

        self.bgcolor = (80, 80, 80, 255)
        self.blinktime = 700

        self.hmargin = 2
        self.vmargin = 2

        self.label = Label('', self.font)
        self.label.resize((self.width - 2 * self.hmargin,
            self.height - 2 * self.vmargin))
        self.label.move_to(self.pos)
        self.label.move((self.hmargin, self.vmargin))

        self.queue.add(self.label)

        self.keydown.connect(self.on_keyDown)

    def on_keyDown(self, key, mod, u):
        if key == pygame.K_BACKSPACE:
            self.remove()
        else:
            self.add(u)

    def add(self, letter):
        if self.label.get_font_width(self.label.text + letter) <= \
            self.width - 2 * self.hmargin:
            self.label.text += letter

    def remove(self):
        self.label.text = self.label.text[:-1]

    def draw(self, surf):
        super(LineEdit, self).draw(surf)

        if ((pygame.time.get_ticks() / self.blinktime % 2 == 0) or
            (not self.focus)):
            x = self.label.pos[0] + self.label.get_font_width()
            y1 = self.label.pos[1]
            y2 = y1 + self.label.height - self.vmargin
            pygame.draw.line(surf, (0, 0, 0, 255), (x, y1), (x, y2))


class Button(Widget):
    def __init__(self, text, action, pos=(0, 0), size=(100, 40)):
        super(Button, self).__init__(pos, size)

        self.click = Signal()
        self.unclick = Signal()

        self.font = Font('Arial')

        self.bgcolor = (110, 110, 110, 255)

        self.hmargin = 5
        self.vmargin = 5

        self.pressed = False

        self.label = Label(text, self.font)
        self.label.resize((self.width - 2 * self.hmargin,
            self.height - 2 * self.vmargin))
        self.label.move_to(self.pos)
        self.label.move((self.hmargin, self.vmargin))

        self.queue.add(self.label)

        self.click.connect(self._clicked)
        self.unclick.connect(self._unclicked)

        self.click.connect(action)

    def _clicked(self, button, pos):
        if button == LEFTMOUSEBUTTON:
            self.pressed = True

    def _unclicked(self, button, pos):
        if button == LEFTMOUSEBUTTON:
            self.pressed = False


class Window(Widget):
    def __init__(self, title, pos=(0, 0), size=(200, 160)):
        super(Window, self).__init__(pos, size)

        self.font = Font('Arial', size=18)

        self.bgcolor = (80, 80, 80, 255)

        self.top = Rect(self.pos, (self.width, 20), (120, 120, 120, 255))

        self.l_title = Label(title, self.font)
        self.l_title.z_index = 100
        self.l_title.move_to((self.pos[0] + 5, self.pos[1]))

        self.queue.add(self.top)
        self.queue.add(self.l_title)
