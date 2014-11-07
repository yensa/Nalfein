# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import pygame
from pygame.locals import *

from scene import Scene


class Game(object):
    """This object represents the game in itself"""

    running = False

    def __init__(self, scene, scrSize=(640, 480)):
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.display.set_mode(scrSize)
        self.currentScene = scene()

    def run(self):
        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                else:
                    self.currentScene.dispatch(event)

            self.clock.tick(60)

            self.updateScene()

        pygame.quit()
        exit()

    def updateScene(self):
        surf = pygame.display.get_surface()
        surf.fill((0, 0, 0))
        pygame.display.update(self.currentScene.draw(surf))
        if self.currentScene.state == Scene.end:
            if self.currentScene.nextScene is None:
                self.running = False
            else:
                self.currentScene = self.currentScene.nextScene()
