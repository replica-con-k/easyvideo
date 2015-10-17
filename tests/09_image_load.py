#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import test
test.start('Image load')

import easyvideo.image

try:
    img = easyvideo.image.load('data/sample_image.jpg')
except Exception, e:
    test.failed('Cannot load image (%s)' % e)

test.ok()
