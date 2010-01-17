#!/bin/env python
# coding=utf8
#import sys
#sys.path.append('/home/zhouhh/abclearning')

import unittest
import sys
print sys.path
import modules.group
#no module named modules?

gs = modules.group.Groups(2,2)
gs.open('./data/freq_part.txt')
class testgroup(unittest.TestCase):
    
    def testwalk(self):
        gs.walk()
        
if __name__ == '__main__':
    unittest.main()