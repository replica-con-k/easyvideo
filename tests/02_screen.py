#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import test
test.start('Display init')

import easyvideo.screen

try:
    scr = easyvideo.screen.Screen()
    
except Exception, e:
    test.failed('Cannot init display (%s)' % e)

test.ok()
