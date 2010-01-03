#!/usr/bin/python3.0
# -*- coding:utf-8 -*-

# by: Tony
# from: <a href="http://tonychen123.blog.ubuntu.org.cn" target="_blank">Loving Ubuntu</a>

style_dic = {0:'Normal', 1:'Bold', 4:'Underline',
                        5:'Blink', 7:'Inverse'}

list_sdic = list(style_dic.keys())

for style in list_sdic:
        #print('-'*60)
        #print('Mode: %-12s Code: \\033[%s;Foreground;Background\n' %(style_dic[style], style))
#        for fore in range(30,37):
        fore = 30
        #for back in range(40,47):
        back = 41
        print('\033[0;30;41m asfd' )
                #print('\033[0m ')
        print('\033[0m')
