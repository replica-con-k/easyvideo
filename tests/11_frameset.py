#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import test
test.start('Create frameset')

import easyvideo.animation

try:
    frames = easyvideo.animation.FrameSet(
        'data/frame01.png',
        'data/frame02.png',
        'data/frame03.png',
        'data/frame04.png',
        'data/frame05.png',
        'data/frame06.png',
        'data/frame07.png',
        'data/frame08.png')
except Exception, e:
    test.failed('Cannot create frame set (%s)' % e)

test.ok()
