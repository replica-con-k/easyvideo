#!/usr/bin/env pyhthon
# -*- coding: utf-8 -*-
#

import pygame

import layer

DEFAULT_RESOLUTION = (1024, 768)


class Screen(object):
    '''Singleton video representation'''
    class __implementation(object):
        def __init__(self, resolution=DEFAULT_RESOLUTION,
                     caption='EasyVideo'):
            if not pygame.display.get_init():
                pygame.display.init()

            self.__resolution = resolution
            self.__screen = pygame.display.set_mode(self.__resolution)
            self.background = layer.Layer(self.__resolution)
            self.playfield = layer.Layer(self.__resolution)
            self.osd = layer.Layer(self.__resolution)


        @property
        def size(self):
            return self.__resolution


        def set_caption(self, caption):
            if self.__screen is None:
                return
            pygame.display.set_caption(caption)


        def update(self):
            pygame.display.update([
                self.__screen.blit(self.background.layer, (0, 0)),
                self.__screen.blit(self.playfield.layer, (0, 0)),
                self.__screen.blit(self.osd.layer, (0, 0)),
            ])


    __instance = None
    def __init__(self, resolution=DEFAULT_RESOLUTION, caption='EasyVideo'):
        if Screen.__instance is None:
            Screen.__instance = Screen.__implementation(resolution,
                                                        caption)
        self.__dict__['_Sreen__instance'] = Screen.__instance

    def __getattr__(self, attr):
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        return setattr(self.__instance, attr, value)


def get_area():
    return pygame.display.get_surface().get_rect()
