#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import pygame

class Layer(object):
    def __init__(self, size):
        self.__layer = pygame.Surface(size).convert_alpha()
        self.clear()

    @property
    def layer(self):
        return self.__layer

    @property
    def area(self):
        return self.layer.get_rect()

    def clear(self):
        self.__layer.fill(pygame.Color(0, 0, 0, 0))
    
    def draw(self, image, position):
        self.__layer.blit(image, position)

    def get_image(self, rect):
        limits = self.__layer.get_rect()
        if limits.contains(rect):
            return self.__layer.subsurface(rect).copy()

        # get_image outside of layer limits
        image = pygame.Surface(rect.size).convert_alpha()
        image.fill(pygame.Color(0, 0, 0, 0))
        visible = limits.clip(rect)
        x = rect.width - visible.width if rect.x < limits.x else 0
        y = rect.height - visible.height if rect.y < limits.y else 0
        image.blit(self.__layer.subsurface(visible), (x, y))
        return image
