#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import test
test.start('Get screen properties')

import easyvideo.screen
scr = easyvideo.screen.Screen()

try:
    test.ok('Screen resolution: %sx%s' % scr.size)
        
except Exception, e:
    test.failed('Cannot get screen size (%s)' % e)
