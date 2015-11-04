#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import test
test.start('Add horizontal-flipped animation to container')

import easyvideo.animation
animations = easyvideo.animation.Animations()
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
    animations.add('animation1', frames.horizontal_flip.animation)
    
except Exception, e:
    test.failed('Cannot add flipped animation (%s)' % e)

test.ok()
