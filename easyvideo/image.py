#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

'''Wrappers and tools for image manipulation.'''

import pygame


def load(filename):
    '''Load image with alpha channel (if it's possible).'''
    image = pygame.image.load(filename)
    return image if not pygame.display.get_init() else image.convert_alpha()


def horizontal_flip(image):
    '''Perform horizontal flip to given image.'''
    return pygame.transform.flip(image, True, False)
