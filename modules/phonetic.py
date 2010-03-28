#!/usr/bin/env python
# -*- coding: utf8 -*-
#   Author:        ablozhou
#   E-mail:        ablozhou@gmail.com
#
#   Copyright 2010 ablozhou
import codecs
import string
import modules.log4py as log4py

log = log4py.log4py('[phonetic]')


Chinese = 1

#sublang
Mandarin = 11
Cantonese = 12

class Phonetic():
    ''' Process phonetic symbols of Chiese characters
    or other languages.
    '''
    def __init__(self,phonetic,sublang = Mandarin, language = Chinese, complete = False ):
        self.language = language
        self.sublang = sublang
        self.complete = complete
        self.setphonetic(phonetic,sublang,language, complete)

    def setphonetic(self,phonetic,sublang = Mandarin, language = Chinese, complete = False):
        if self.sublang == Mandarin:
            if complete == False:
                self.phonetic = self.proc_phonetic(phonetic)
            else:
                self.phonetic = phonetic
        else:
            self.phonetic = phonetic
    #定位多音字的词，读音，第几个字的读音,避免重复，如“数数"
    def setmulphone(self,word,phonetic,num):
        pass

    #处理多音字，轻声字
    #word:多音字的词
    #num:遇到叠字指出第几个字的读音
    def getaphonetic(self,word = None,num = None,filename = None):
        p = self.phonetic.split('/')
        if len(p) == 1 or word == None:
            return p[0]

        ph = common.mtone.getaphonetic(word,num)
        if ph != None:
            return ph
        else:
            return p[0]

    def getphonetic(self):
        return self.phonetic
    #兼容多音字处理
    def proc_phonetic(self,phonetic):
        phonetics = phonetic.split('/')
        ps = []
        for ph in phonetics:
            p = self.proc_singleph(ph)
            ps.append(p)

        return string.join(ps,'/')

    def proc_singleph(self,phonetic,tone = None):
        log.debug('proc_singleph:'+phonetic.decode('utf8'))
        if tone == None:
            try:
                tone = int(phonetic[-1:])
            except ValueError:
                return phonetic
            phonetic = ''.join(phonetic[:-1])
            #print 'py:'+ phonetic
            #phonetic = phonetic.decode('utf8')
        #5 neutral tone
        if tone not in range(1,5):
            print 'tone:'+str(tone)
            return phonetic

        a = ['ā', 'á', 'ǎ', 'à']
        o = ['ō', 'ó', 'ǒ', 'ò']
        e = ['ē', 'é', 'ě', 'è']
        i = ['ī',  'í', 'ǐ', 'ì']
        u = ['ū', 'ú', 'ǔ', 'ù']
        v = ['ǖ', 'ǘ', 'ǚ', 'ǜ']
        vb = ['ǖ', 'ǘ', 'ǚ', 'ǜ'] #Ü
        vs = ['ǖ', 'ǘ', 'ǚ', 'ǜ'] #ü
        A = ['Ā', 'Á', 'Ǎ', 'À']
        O = ['Ō', 'Ó', 'Ǒ', 'Ò']
        E = ['Ē', 'É', 'Ě', 'È']

        if 'iu' in phonetic:
            return phonetic.replace('u',u[tone-1].decode('utf8'),1)
        if 'ui' in phonetic:
            return phonetic.replace('i',i[tone-1].decode('utf8'),1)
        if 'a' in phonetic:
            return phonetic.replace('a',a[tone-1].decode('utf8'),1)
        if 'o' in phonetic:
            #log.debug(phonetic)
            return phonetic.replace('o',o[tone-1].decode('utf8'),1)
        if 'e' in phonetic:
            return phonetic.replace('e',e[tone-1].decode('utf8'),1)
        if 'i' in phonetic :
            return phonetic.replace('i',i[tone-1].decode('utf8'),1)
        if 'u' in phonetic:
            return phonetic.replace('u',u[tone-1].decode('utf8'),1)
        if 'v' in phonetic:
            return phonetic.replace('v',v[tone-1].decode('utf8'),1)
        if 'Ü'.decode('utf8') in phonetic:
            return phonetic.replace('Ü'.decode('utf8'),vb[tone-1].decode('utf8'),1)
        if 'ü'.decode('utf8') in phonetic:
            return phonetic.replace('ü'.decode('utf8'),vs[tone-1].decode('utf8'),1)

        #log.debug(phonetic.encode('utf8'))
        return phonetic

