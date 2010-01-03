#!/bin/env python
# coding=utf8
#能将列表封装出迭代器吗？
class Iter():
    def __init__(self):
        self.item = [1,2,3]
        
    def __iter__(self):
        self.i = 0
        return self
    
    def next(self):
        if  self.i < len(self.item):
            it =  self.item[self.i]
            self.i += 1
            return it
        
        else:
            raise StopIteration

t = Iter()
#for i in Iter():
#    print i
    
z = iter(t)
c = next(z)
print c
d = next(z)
print d
e = next(z)
print e
f = z.next()
print f