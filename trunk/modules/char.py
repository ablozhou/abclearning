#!/bin/dev python
# coding=utf8

from memory import *
import codecs
import string
import modules.log4py as log4py

log = log4py.log4py('[Char]')


Chinese = 1

Japanese = 3

Korean=5
Vietnamese = 6
English = 8

#sublang
Mandarin = 11
Cantonese = 12
JapaneseOn = 31
JapaneseKun = 32

Hangul = 51
Korean_roman = 52

Us_en = 81
Eng_en = 82

class Phonetic():
    def __init__(self,phonetic,sublang = Mandarin, language = Chinese ):
        self.language = language
        self.sublang = sublang
        self.setphonetic(phonetic,sublang,language)

    def setphonetic(self,phonetic,sublang = Mandarin, language = Chinese):
        if self.sublang == Mandarin:
            self.phonetic = self.proc_phonetic(phonetic)
        else:
            self.phonetic = phonetic
    #定位多音字的词，读音，第几个字的读音,避免重复，如“数数"
    def setmulphone(self,word,phonetic,num):
        pass

    #todo 处理多音字
    def getaphonetic(self,word = None,num = None):
        p = phonetic.split('/')
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

#class gloss():
#    def __init__(self,language):
#        self.language = language
#        self.gloss = gloss
#        #self.sublang = sublang
#Lang={Chinese:'Chinese'
class Language():
    def __init__(self,language):
        self.language = language
        self.phonetic={} #读音 phonetic symbols，languae:phonetic
        self.gloss=[] #释义 language:gloss
    #增加解释
    def addgloss(self,gloss):
        self.gloss.append(gloss)

    def getlangname(self,language):
        if language == English:
            return 'en'
        return ''

    def getgloss(self):
        if len(self.gloss) > 0:
            return 'en:'+''.join(self.gloss)
        return ''

    #增加拼音
    def addphonetic(self,phonetic,sublang = Mandarin, language = Chinese):
        try:
            po = self.phonetic[sublang]
        except KeyError:
            po = Phonetic(phonetic,sublang,language)
            self.phonetic[po.sublang] = po

        plist = po.getphonetic().split('/')

        new_plist = phonetic.split('/')
        if len(plist) < len(new_plist):
            po.setphonetic(phonetic,sublang,language)


#    def getphone_sublang(self,sublang = Mandarin):
#        try:
#            p =  self.phonetic[sublang]
#            return p.getphonetic()
#        except KeyError:
#            return None

    def getphonetic(self,sublang = Mandarin):
        try:
            p =  self.phonetic[sublang]
            return p.getphonetic()
        except KeyError:
            return None

    def getphonetics(self):
        return self.phonetics

class Char: #字，词
    def __init__(self,char):
        self.mem = Memory()
        self.char=char #字型

        self.languages = {} #语言列表 chinese,korea,japanese,veitnamese
        self.freq=-1
        self.strokenum=-1 #笔画 number of strokes
        self.virant=[] #变体，如繁简异体字
        self.consult={} #检索方法:检索码
        self.radical='' #偏旁部首
        self.strokes='' #横竖撇捺弯对应12345

    def addlang(self,lang):
        self.languages[lang.language]=lang


    def getlang(self,langstr):
        try:
            return self.languages[langstr]
        except KeyError:
            return None

    def addphonetic(self,phonetic, sublang = Mandarin, language = Chinese):
        try:
            lang = self.languages[language]
        except KeyError:
            lang = Language(language)
            self.languages[language]=lang

        lang.addphonetic(phonetic,sublang,language)

    def getphonetic(self,sublang = Mandarin, language = Chinese):
        try:
            l = self.languages[language]
            return l.getphonetic(sublang)
        except KeyError:#TypeError:
            return None

    def getphonetics(self):
        p = ''
        for l in ((Mandarin,Chinese),(Cantonese,Chinese),
            (JapaneseOn,Japanese),(JapaneseKun,Japanese),
                (Hangul,Korean),(Korean_roman,Korean),(Vietnamese,Vietnamese)):
            s = self.getphonetic(*l)
            if s != None:
                if len(p) > 0:
                    p += ','
                p += s
        log.debug(p.encode('utf8'))
        return p
    #解释
    def addgloss(self,gloss,language):
        try:
            lang = self.languages[language]
        except KeyError:
            lang = Language(language)
            self.languages[language]=lang

        lang.addgloss(gloss)

    def getgloss(self,lang = None):
        if lang != None:
            #print 'lang not None:'+str(lang)
            try:
                l = self.languages[lang]
                return l.getgloss()
            except KeyError:
                return ''

        else :
            #print 'lang is None'
            g = ''
            for l in (Chinese,Japanese,Korean,Vietnamese,English):
                s = self.getgloss(l)
                if s != '':
                    g += s + '\t'
            return g

    def display(self,*format, **format2):

        #print self.char,phonetic
        self.mem.addfamiliar(1)
        self.mem.setlasttime()
        #phonetic = codecs.encode(self.char,'utf8')+codecs.encode(self.phonetic,'utf8'),time.strftime(ISOTIMEFORMAT,time.localtime(self.mem.lasttime))
        phonetic = self.char + '\t' + self.phonetic + '\t' + self.english
        print phonetic.encode('utf8')

        return phonetic

    def addfamiliar(n):
        self.mem.addfamiliar(n)



#TODO 如何继承系统dict类型？
class CharDict(dict):

    def __init__(self):
        #self.dict={}
        pass

    def addchar(self, char):
        self[char.char] = char

if __name__ == '__main__':
    a = Phonetic('lv3/lv4/lü4/lÜ4'.decode('utf8'))

    #b = a.getphonetic('lv3')
    print a.phonetic.encode('utf8')

    c = Language(Chinese)
    c.addphonetic('lv3/lv4/lü4/lÜ4'.decode('utf8'))
    print c.getphonetic(Mandarin).encode('utf8')

    s = Char('中')
    l = Language(Chinese)
    s.addlang(l)
    #l.addphonetic('qiu1/zhong4')
    l.addphonetic('kuáng 10.11')
    le = Language(English)
    le.addgloss('media,center 中'.decode('utf8'))
    s.addlang(le)
    #s.addgloss('media,center 中'.decode('utf8'),English)
    print l.getphonetic().encode('utf8')
    #s.phonetic['Mandarin']=Phonetic('Mandarin','zhong1/zhong4')
    p = s.getphonetic()
    t = s.char
    g = s.getgloss()
    print g.encode('utf8')
    print t
    print p.encode('utf8')
    #for l in p.items:
    #    print l.encode('utf8')
