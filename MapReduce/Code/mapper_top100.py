#!/usr/bin/env python
"""The Hadoop Mapper for Top 100 words"""

import sys

words = {}
 
# Reading and processing words from output directory
for line in sys.stdin:
    line = line.split("\t")
    current_word, count = line
    print '%s\t%s'% ( current_word, count)

