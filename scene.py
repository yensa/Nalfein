# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import pygame

from utils import Point, RenderQueue


class Scene(object):
    """The Scene object represents a scene of the game."""

    init = 0
    end = 1

    nextScene = None

    state = init

    elements = RenderQueue()

    def draw(self, surf):
        """Draws the scene on the screen"""
        for element in self.elements:
            element.draw(surf)

    def dispatch(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.onClick(event.button, event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            self.onUnclick(event.button, event.pos)
        elif event.type == pygame.MOUSEMOTION:
            self.onMouseMotion(event.pos, event.rel, event.buttons)
        elif event.type == pygame.KEYDOWN:
            self.onKeyDown(event.key, event.mod, event.unicode)
        elif event.type == pygame.KEYUP:
            self.onKeyUp(event.key, event.mod)
        elif event.type == pygame.JOYBUTTONDOWN:
            self.onJoyClick(self, event.joy, event.button)
        elif event.type == pygame.JOYBUTTONUP:
            self.onJoyUnclick(self, event.joy, event.button)
        elif event.type == pygame.JOYAXISMOTION:
            self.onJoyMove(event.joy, event.axis, event.value)
        elif event.type == pygame.JOYBALLMOTION:
            self.onJoyBallMove(event.joy, event.ball, event.rel)
        elif event.type == pygame.JOYHATMOTION:
            self.onJoyHatMotion(event.joy, event.hat, event.value)
        elif event.type == pygame.USEREVENT:
            self.onUserEvent(event.code)

    def onKeyDown(self, key, mod, u):
        for element in self.elements:
            if hasattr(element, 'keydown') and element.focus:
                element.keydown(key, mod, u)

    def onKeyUp(self, key, mod):
        for element in self.elements:
            if hasattr(element, 'keyup') and element.focus:
                element.keyup(key, mod)

    def onClick(self, button, pos):
        for element in self.elements:
            element.focus = False
            if element.rect.collidepoint(pos):
                if hasattr(element, 'focus'):
                    element.focus = True
                if hasattr(element, 'click'):
                    element.click(button, Point(*pos))

    def onUnclick(self, button, pos):
        for element in self.elements:
            if hasattr(element, 'unclick'):
                element.unclick(button, Point(*pos))

    def onMouseMotion(self, pos, rel, buttons):
        pass

    def onJoyClick(self, joy, button):
        pass

    def onJoyUnclick(self, joy, button):
        pass

    def onJoyMove(self, joy, axis, value):
        pass

    def onJoyBallMove(self, joy, ball, rel):
        pass

    def onJoyHatMotion(self, joy, hat, value):
        pass

    def onUserEvent(self, code):
        for element in self.elements:
            if hasattr(element, 'userevent'):
                element.userevent(code)
