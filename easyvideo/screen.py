#!/usr/bin/env pyhthon
# -*- coding: utf-8 -*-
#

"""This module is a wrapper of pygame.display() functions."""

import pygame

import easyvideo.layer

DEFAULT_RESOLUTION = (1024, 768)


class Screen(object):
    '''Multi-layered screen handling. This class is a singleton.'''
    class _ScreenImpl(object):
        '''Implementation class.'''
        def __init__(self, resolution=DEFAULT_RESOLUTION,
                     caption='EasyVideo'):
            if not pygame.display.get_init():
                pygame.display.init()

            self.__resolution = resolution
            self.__screen = pygame.display.set_mode(self.__resolution)
            self.set_caption(caption)
            self.background = easyvideo.layer.Layer(self.__resolution)
            self.playfield = easyvideo.layer.Layer(self.__resolution)
            self.osd = easyvideo.layer.Layer(self.__resolution)

        @property
        def size(self):
            '''Return screen size.'''
            return self.__resolution

        def set_caption(self, caption):
            '''Set window caption.'''
            if self.__screen is None:
                return
            pygame.display.set_caption(caption)

        def update(self):
            '''Update layers and the entire screen.'''
            pygame.display.update([
                self.__screen.blit(self.background.layer, (0, 0)),
                self.__screen.blit(self.playfield.layer, (0, 0)),
                self.__screen.blit(self.osd.layer, (0, 0)),
            ])

    __instance = None

    def __init__(self, resolution=DEFAULT_RESOLUTION, caption='EasyVideo'):
        if Screen.__instance is None:
            Screen.__instance = Screen._ScreenImpl(resolution, caption)
        self.__dict__['_Sreen__instance'] = Screen.__instance

    def __getattr__(self, attr):
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        return setattr(self.__instance, attr, value)


def get_area():
    '''Return the screen area'''
    return pygame.display.get_surface().get_rect()
