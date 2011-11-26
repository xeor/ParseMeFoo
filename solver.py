#!/usr/bin/env python

'''
This is a simple python template which you can use to build solutions in parsemefoo in python.
Just change how trySolve() works to make it return the solution for each line..
'''

import sys

def trySolve(line):
    return line

userInput = [ s.strip() for s in sys.stdin.readlines() ]
for line in userInput:
    print trySolve(line)
