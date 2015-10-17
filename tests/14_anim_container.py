#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import test
test.start('Create animation container')

import easyvideo.animation

try:
    animations = easyvideo.animation.Animations()
except Exception, e:
    test.failed('Cannot create animation container (%s)' % e)

test.ok()
