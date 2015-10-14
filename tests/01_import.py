#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import test

test.start('Import')

try:
    import easyvideo.screen
except ImportError:
    test.failed('Cannot import library!')

test.ok()
