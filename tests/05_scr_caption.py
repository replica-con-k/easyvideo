#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import test
test.start('Change screen caption')

import easyvideo.screen
scr = easyvideo.screen.Screen()

try:
    scr.set_caption('Another caption')    
except Exception, e:
    test.failed('Cannot change screen caption (%s)' % e)
    
test.ok()
