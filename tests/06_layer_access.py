#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import test
test.start('Screen layers access')

import easyvideo.screen
scr = easyvideo.screen.Screen()

try:
    test.ok('Background layer: %s' % type(scr.background.layer))
    
except Exception, e:
    test.failed('Cannot access to background layer (%s)' % e)
