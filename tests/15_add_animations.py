#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import test
test.start('Add animations to container')

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
    animations.add('animation1', frames.animation)
    
except Exception, e:
    test.failed('Cannot add animation (%s)' % e)

test.ok()
