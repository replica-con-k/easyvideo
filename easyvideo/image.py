#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

'''Wrappers and tools for image manipulation.'''

import pygame


def load(filename):
    '''Load image with alpha channel.'''
    return pygame.image.load(filename).convert_alpha()


def horizontal_flip(image):
    '''Perform horizontal flip to given image.'''
    return pygame.transform.flip(image, True, False)
