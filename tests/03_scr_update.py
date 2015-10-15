#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import test
test.start('Screen update')

import easyvideo.screen
scr = easyvideo.screen.Screen()

try:
    scr.update()
    
except Exception, e:
    test.failed('Cannot perform update() (%s)' % e)

test.ok()
