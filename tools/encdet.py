#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author ablozhou 周海汉
# ablozhou@gmail.com
# http://blog.csdn.net/ablo_zhou
# 2010.3.14

import chardet
import urllib
import modules.log4py as log4py
import sys
log = log4py.log4py('[encdet]')

def detect(filename, text = '', encoding = None):

    defaultenc = sys.getfilesystemencoding()
    begin = 0
    if not text:
        try:
            text = file(filename,'rb').read(1000)
        except:
            log.tracebk()
            encoding = defaultenc
            return defaultenc

    if text.startswith('\xEF\xBB\xBF'):
        begin = 3
        encoding = 'UTF-8'
    elif text.startswith('\xFF\xFE'):
        begin = 2
        encoding = 'UTF-16'
    if not encoding:
        enc = chardet.detect(text)
        encoding = enc['encoding']
        if encoding == 'GB2312':
            encoding = 'gb18030'
        log.debug('chardet:'+encoding)

#    try:
#        s = unicode(text[begin:], encoding)
#
#    except:
#        encoding = 'gbk'
#        try:
#            s = unicode(text[begin:], encoding, 'replace')
#        except:
#            log.tracebk()
#            encoding = defaultenc
#            return defaultenc

    return encoding,begin

if __name__ == '__main__':
    text=''
    encoding = None
    #filename = '../data/唐诗三百首.txt'
    #filename = '../data/唐诗三百首/唐诗三百首之.卷八、五言绝句.txt'
    filename = '../data/唐诗三百首/唐诗三百首之.卷二、五言乐府.txt'
    filename = '../data/唐诗三百首/唐诗三百首之.卷六、七言律诗.txt'
    enc1 = detect(filename,text,encoding)
    log.debug(filename,enc1)

    def chardetect():

        mydet = {
            'SHIFT_JIS':'http://www.mankan.or.jp/',
            'GB2312':'http://g.cn/',
            'Big5':'http://www.programmer-club.com.tw/',
            'UTF8':'http://zh.wikipedia.org/',
            'ASCII':'http://www.whitehouse.gov'
            }

        for url in mydet.values():
            print url
            rawdata = urllib.urlopen(url).read()
            enc = chardet.detect(rawdata)
            print enc['encoding']


