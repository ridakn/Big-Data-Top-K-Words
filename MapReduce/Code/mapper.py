#!/usr/bin/env python
"""The Hadoop Mapper"""

import sys

words = {}

def mapper():

    # Reading and processing words from text file 
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
            
            # Printing <word, 1> for combiner OR reducer 
            print "{0}\t{1}".format(word, 1)
            

if __name__ == "__main__":
    mapper()