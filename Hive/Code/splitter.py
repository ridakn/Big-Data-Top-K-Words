#!/usr/bin/env python
"""Splitter"""

import sys

for line in sys.stdin:
    words = line.split()
    for word in words:
        word = word.strip(',')
        word = word.strip('.')
        word = word.strip('!')
        word = word.strip(';')
        word = word.strip('"')
        word = word.strip(':')
        word = word.strip('(')
        word = word.strip(')')

        print (word)
            
