#!/bin/dev python
# coding=utf8

from memory import *
import codecs
import string
import modules.log4py as log4py

log = log4py.log4py('[Char]')

class Char: #字，词
    def __init__(self,char):
        self.mem = Memory()
        self.char=char
        self.freq=1
        self.phonetic='' #拼音 phonetic symbols
        self.stroknum=1 #笔画 number of strokes
        
    def getphonetic(self):
        p = phonetic(self.phonetic.encode('utf8'))
        return p.getphonetic()

    def getaphonetic(self):
        p = phonetic(self.phonetic.encode('utf8'))
        return p.getaphonetic()

       
    def display(self,*format, **format2):
    
        #print self.char,phonetic
        self.mem.addfamiliar(1)
        self.mem.setlasttime()
        #phonetic = codecs.encode(self.char,'utf8')+codecs.encode(self.phonetic,'utf8'),time.strftime(ISOTIMEFORMAT,time.localtime(self.mem.lasttime))
        phonetic = self.char + self.phonetic
        print phonetic.encode('utf8')
        
        return phonetic
    
    def addfamiliar(n):
        self.mem.addfamiliar(n)
    

class phonetic():
    def __init__(self, phonetic):
        self.phonetic = self.proc_phonetic(phonetic)
    #TODO 重载如何进行？
#    def getphonetic(self,phonetic):
#        p = phonetic.strip();
#            space = [' ', '\n', '\t']
#            for c in p:
#                if c == u'-' or c in space:
#            	continue
#                if c in string.letters:
#            	continue
#                if c in string.digits:
#            	continue
#                ret = find_it(c.encode('utf-8'), lines)
#                if ret:
#            	result.append(c+':'+'/'.join(ret))

    #多音字显示全部拼音
    def getphonetic(self):
        return self.phonetic
    #多音字只显示一个拼音
    def getaphonetic(self):
        return self.phonetic.split('/')[0]    
    #兼容多音字处理                    
    def proc_phonetic(self,phonetic):
        phonetics = phonetic.split('/')
        ps = []
        for ph in phonetics:
            p = self.proc_singleph(ph)
            ps.append(p)
            
        return string.join(ps,'/')
    
    def proc_singleph(self,phonetic,tone = None):
        
        if tone == None:
            tone = string.join(phonetic[-1:],'')
            phonetic = string.join(phonetic[:-1],'')
            
        if tone not in ('1234'):
            return phonetic
        
        ph_a = ['ā', 'á', 'ǎ', 'à']
        ph_o = ['ō', 'ó', 'ǒ', 'ò']
        ph_e = ['ē', 'é', 'ě', 'è']
        ph_i = ['ī', 'í', 'ǐ', 'ì']
        ph_u = ['ū', 'ú', 'ǔ', 'ù']
        ph_v = ['ǖ', 'ǘ', 'ǚ', 'ǜ']
        #ph_A = ['Ā', 'Á', 'Ǎ', 'À']
        #ph_O = ['Ō', 'Ó', 'Ǒ', 'Ò']
        #ph_E = ['Ē', 'É', 'Ě', 'È']
        if 'iu' in phonetic:
            return string.replace(phonetic,'u',ph_u[int(tone)-1],maxsplit=1)
        if 'ui' in phonetic:
            return string.replace(phonetic,'i',ph_i[int(tone)-1],maxsplit=1)
        if 'a' in phonetic:
            return string.replace(phonetic,'a',ph_a[int(tone)-1],maxsplit=1)
        if 'o' in phonetic:
            log.debug(phonetic)
            return string.replace(phonetic,'o',ph_o[int(tone)-1],maxsplit=1)
        if 'e' in phonetic:
            return string.replace(phonetic,'e',ph_e[int(tone)-1],maxsplit=1)
        if 'i' in phonetic :
            return string.replace(phonetic,'i',ph_i[int(tone)-1],maxsplit=1)
        if 'u' in phonetic:
            return string.replace(phonetic,'u',ph_u[int(tone)-1],maxsplit=1)
        if 'v' in phonetic:
            return string.replace(phonetic,'v',ph_v[int(tone)-1],maxsplit=1)
    
        return phonetic    
        
#TODO 如何继承系统dict类型？        
class CharDict(dict):
    
    def __init__(self):
        #self.dict={}
        pass
        
    def addchar(self, char):
        self[char.char] = char

if __name__ == '__main__':
    a = phonetic('lv3')
    
    #b = a.getphonetic('lv3')
    print a.phonetic
    
    c = phonetic('lv3/lv4')
    print c.phonetic
    
    s = Char('中')
    s.phonetic='zhong1/zhong4'
    
    t = s.char+s.getphonetic()
    print t