#!/usr/bin/env python
# -*- coding: utf8 -*-
#   Author:        ablozhou
#   E-mail:        ablozhou@gmail.com
#
#   Copyright 2010 ablozhou

class Mutitone():
    '''多音字处理'''
    def __init__(self, mtonefile):
        self.mtonefile = mtonefile
        self.mtones = {}

    def initfile(self):
        lines = open(self.mtonefile, 'r').read().splitlines()
        for line in lines:
            if not line or line[0] == '#':
                continue
            parts = line.split('\t')
            hz = parts[0]
            #phonetics = parts[1].split('/')

            self.mtones[hz] = parts[1]

    def getmtone(self, word , num = None):
        try:
            ph = self.mtones[word]

        except:
            return None:



