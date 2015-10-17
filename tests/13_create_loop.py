#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import test
test.start('Create animation loop')

import easyvideo.animation

frames = easyvideo.animation.FrameSet(
    'data/frame01.png',
    'data/frame02.png',
    'data/frame03.png',
    'data/frame04.png',
    'data/frame05.png',
    'data/frame06.png',
    'data/frame07.png',
    'data/frame08.png')

try:
    animation_loop = frames.animation_loop
except Exception, e:
    test.failed('Cannot create animation loop (%s)' % e)

test.ok()
