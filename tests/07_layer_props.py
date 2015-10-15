#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import test
test.start('Layer property access')

import easyvideo.screen
scr = easyvideo.screen.Screen()

try:
    test.ok('Background layer size: %s' % scr.background.area)
    
except Exception, e:
    test.failed('Cannot get layer size (%s)' % e)
