#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import pygame

def load(filename):
    return pygame.image.load(filename).convert_alpha()

def horizontal_flip(image):
    return pygame.transform.flip(image, True, False)
