#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import sys
import logging
logging.basicConfig(level=logging.INFO)

ENABLE_QUIT = True
_test_name = 'unknown'

def start(test_name):
    global _test_name
    logging.info('[START] test: %s' % test_name)
    _test_name = test_name
    

def _end(self, message=None, quit=False, code=0):
    logging.info('[ END ] test: %s%s' % (
        _test_name,
        (' (%s)' % message if message is not None else '')))
    if quit:
        sys.exit(code)

def ok(message=None):
    _end(message)

def failed(message, fail_code=-1):
    _end(message, ENABLE_QUIT, fail_code)

if __name__ == '__main__':    
    logging.info('[ INF ] Run all tests...')

    import glob

    python_files = set(glob.glob('*.py'))
    excludes = set(glob.glob('_*.py') + ['test.py'])
    test_programs = python_files - excludes
        
    for program in list(test_programs):
        execfile(program)
        
    logging.info('[ INF ] Bye.')
