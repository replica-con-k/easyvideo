#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

'''Layer handling.'''

import pygame


class Layer(object):
    '''A simple layer. One layer is a surface with alpha channel.'''
    def __init__(self, size):
        self.__layer = pygame.Surface(size).convert_alpha()
        self.clear()

    @property
    def layer(self):
        '''Return the surface.'''
        return self.__layer

    @property
    def area(self):
        '''Return the area of the surface.'''
        return self.layer.get_rect()

    def clear(self):
        '''Clear all pixels.'''
        self.__layer.fill(pygame.Color(0, 0, 0, 0))

    def draw(self, image, position):
        '''Draw image into the layer.'''
        self.__layer.blit(image, position)

    def get_image(self, rect):
        '''Grab area from the layer.'''
        limits = self.__layer.get_rect()
        if limits.contains(rect):
            return self.__layer.subsurface(rect).copy()

        # get_image outside of layer limits
        image = pygame.Surface(rect.size).convert_alpha()
        image.fill(pygame.Color(0, 0, 0, 0))
        visible = limits.clip(rect)
        xofs = rect.width - visible.width if rect.x < limits.x else 0
        yofs = rect.height - visible.height if rect.y < limits.y else 0
        image.blit(self.__layer.subsurface(visible), (xofs, yofs))
        return image
