#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import pygame


class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class Group(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)
