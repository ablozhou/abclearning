#!/bin/env python
#   --*-- coding=utf8 --*--
#
#   Author: ablozhou
#   E-mail: ablozhou@gmail.com
#
#   Copyright 2009 ablozhou
#
#   Distributed under the terms of the GPL (GNU Public License)
#
#   abcl is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# todo: 写文件，log级别常数定义
import datetime

dest = {1:'stdout',2:'stderr',3:'file'}  #stdout

class log4py:
    def __init__(self,filename='log4py.txt',flag=None):
        self.filename = filename
        self.flag=flag
        
    
    def _gettime(self):
        return datetime.datetime.now().isoformat()
    #flag = INFO,DEBUG,WARNING,ERROR,FATAL
    def output(self, *fmt):
        
        print fmt
    
    def debug(self,*fmt):
        #if self.flag>=DEBUG :
        self.output(self._gettime(),'[DEBUG]',*fmt)
             
    def warn(self,*fmt):
    #if self.flag>=WARN :
        self.output(self._gettime(),'[WARN]',*fmt)

    def info(self,*fmt):
        self.output(self._gettime(),'[INFO]',*fmt)
        
    def error(self,*fmt):
        self.output(self._gettime(),'[ERROR]',*fmt)
        
    def fatal(self,*fmt):
        self.output(self._gettime(),'[FATAL',*fmt)
        
#unit test
if __name__ == '__main__':
    log=log4py()
    log.output('INFO','stdout','test')
    log.debug('debug information 调试')