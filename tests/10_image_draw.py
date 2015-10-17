#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import test
test.start('Image draw')

import easyvideo.screen
import easyvideo.image

scr = easyvideo.screen.Screen()
img = easyvideo.image.load('data/sample_image.jpg')
try:
    scr.background.draw(img, (0, 0))
    scr.update()
except Exception, e:
    test.failed('Cannot draw image (%s)' % e)

test.ok()
