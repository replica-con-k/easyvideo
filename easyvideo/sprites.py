#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

'''Simple pygame.sprite wrapper module.'''

import pygame


class Sprite(pygame.sprite.Sprite):
    '''Wrapper for Sprite() class.'''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def collide(self, targets):
        return pygame.sprite.spritecollideany(self, targets)
        
class Group(pygame.sprite.Group):
    '''Wrapper for Group() class.'''
    def __init__(self):
        pygame.sprite.Group.__init__(self)
