#!/bin/dev python
# coding=utf8

import time
#记忆曲线,5min,30min,12hour,1day,2days,4days,7days,15days
REM_TIME=[300,1800,43200,86400,172800,345600,604800,1296000]

ISOTIMEFORMAT = '%Y-%m-%d %X'

class Memory():
    """
一、 复习点的确定（根据艾宾浩斯记忆曲线制定）：
1． 第一个记忆周期：5分钟
2． 第二个记忆周期：30分钟
3． 第三个记忆周期：12小时
4． 第四个记忆周期：1天
5． 第五个记忆周期：2天
6． 第六个记忆周期：4天
7． 第七个记忆周期：7天
8． 第八个记忆周期：15天

二、背诵方法：
1． 初记单词时需要记忆的内容：
a)单词外观，b） 单词的中文释义，c） 单词的记忆法
2． 每个list的具体背诵过程（每个list按12页，每页10个单词计）：
a) 背完一页（大约5分钟），立即返回该页第一个单词开始复习（大约几十秒）
b) 按上面方法背完1～6页（大约在30分钟），回到第1页开始复习（两三分钟）
c) 按上面同样方法背完7～12页，一个list结束
d) 相当于每个list被分为12个小的单元，每个小的单元自成一个复习系统；每6个小单元组成一个大单元，2个大单元各自成为一个复习系统。背一个list总共需要一小时左右的时间。

3． 复习过程：
a) 复习方法：遮住中文释义，尽力回忆该单词的意思，几遍下来都记不住的单词可以做记号重点记忆。
b) 复习一个list所需的时间为20分钟以内
c) 当天的list最好在中午之前背完，大约12小时之后（最好睡觉前）复习当天所背的list
d) 在其后的1，2，4，7，15天后分别复习当日所背的list

4． 注意事项：
a) 每天连续背诵2个list，并完成复习任务；
b) 复习永远比记新词重要，要反复高频率的复习，复习，再复习；
c) 一天都不能间断，坚持挺过这15天，之后每天都要花大约1小时复习；

5． 时间表（左边序号表示第几天，*号之后表示复习内容）
1. list1-2 *list1-2
2. list3-4 *list1-2 list3-4
3. list5-6 *list3-4 list5-6
4. list7-8 *list1-2 list5-6 list7-8
5. list9-10 *list3-4 list7-8 list9-10
6. list11-12 *list5-6 list9-10 list11-12
7. list13-14 *list7-8 list11-12 list13-14
8. list15-16 *list1-2 list9-10 list13-14 list15-16
9. list17-18 *list3-4 list11-12 list15-16 list17-18
10. list19-20 *list5-6 list13-14 list17-18 list19-20
11. list21-22 *list7-8 list15-16 list19-20 list21-22
12. list23-24 *list9-10 list17-18 list21-22 list23-24
13.*list11-12 list19-20 list23-24
14.*list13-14 list21-22
15.*list1-2 list15-16 list23-24
16.*list3-4 list17-18
17.*list5-6 list19-20
18.*list7-8 list21-22
19.*list9-10 list23-24
20.*list11-12
21.*list13-14
22.*list15-16
23.*list17-18
24.*list19-20
25.*list21-22
26.*list23-24
    """
    def __init__(self,familiar=0, lasttime = None):
        self.familiar = familiar
        self.strange = 0
        self.setlasttime(lasttime)
        
        
    # -5,...,5 共11 等级 
    def addfamiliar(self,count):
        self.familiar += count
            
        if self.familiar > 7:
            self.familiar = 7
            
        if self.familiar < 0:
            self.familiar = 0
            
        return self.familiar
    
    def setlasttime(self,lasttime = None):
        if lasttime == None:
            lasttime = time.time()
        self.lasttime = lasttime
    
    def getlasttime(self):
        return self.lasttime
    
    def strftime(self,ftime = None):
        if ftime == None:
            ftime = self.lasttime
        return time.strftime(ISOTIMEFORMAT,time.localtime(ftime))    
    
    def addstrange(self,count):
        
        self.strange += count
        if self.strange > 7:
            self.strange = 7
        if self.strange < 0:
            self.strange = 0
            
        return self.strange
    
    def needReview(self):
        now = time.time()
        interval = now - self.lasttime
        
        if interval >= REM_TIME[self.familiar]:
            return True
        
        return False

#unit test
if __name__ == '__main__':
    
    mem = Memory()
    mem.addfamiliar(3)
    print mem.familiar
    mem.addstrange(2)
    print mem.strange
    
    print time.localtime(mem.lasttime)
    
    mem.addfamiliar(-4)
    mem.setlasttime(time.time()-400)
    print 'last time=%s' % time.localtime(mem.lasttime)
    
    if(mem.needReview()):
        print 'need review'
    else:
        
        print 'neednot review'
        
    while True:
        t = raw_input('>> ')
        mem.setlasttime()
        if t == 'g':
            mem.setlasttime()
            zt = time.time()
            print mem.strftime()
            print 'zt:',mem.strftime(zt)