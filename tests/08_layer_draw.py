#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import test
test.start('Layer drawing')

import easyvideo.screen
scr = easyvideo.screen.Screen()

import random
import pygame

def _randint(max_val):
    return random.randint(0, max_val)

for circle in range(100):
    try:
        pygame.draw.circle(scr.background.layer,
                           (_randint(255), _randint(255), _randint(255), 255),
                           (_randint(1024), _randint(768)),
                           _randint(10))
    except Exception, e:
        test.failed('Cannot draw into layer (%s)' % e)
            
    scr.update()

test.ok()
