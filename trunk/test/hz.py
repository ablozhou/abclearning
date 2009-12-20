#!/usr/bin/env python
import os,sys
import string
import urllib2
import zipfile
def find_it(x, lines):
	ret = []
	for line in lines:
		if line.find(x)!=-1:
			ret.append(line.split(":")[0].strip())
	return ret
if __name__ == '__main__':
	if len(sys.argv) != 2:
		print "Ni hao! Chu cuo le!"
		sys.exit(1)
	if os.getenv("LANG").upper().find("UTF-8") == -1:
		print "Please use UTF-8 locale!"
		sys.exit(2)
	try:
		f = open('/home/zhouhh/abcl/test/pinyin.zip', 'r+')
	except IOError:
		req = urllib2.Request('http://blogimg.chinaunix.net/blog/upfile2/080906001029.zip')
		resp = urllib2.urlopen(req)
		zfile = resp.read()
		f = open('/home/zhouhh/abcl/test/pinyin.zip', 'w')
		f.write(zfile)
		f.close()
	finally:
		z = zipfile.ZipFile("/home/zhouhh/abcl/test/pinyin.zip", "r")
		bytes = z.read('pinyin.txt')
		lines = bytes.split('\r\n')
		x = sys.argv[1]
		for c in x.decode('utf-8'):
			if c == u'-':
				continue
			if c in string.letters:
				continue
			if c in string.digits:
				continue
			ret = find_it(c.encode('utf-8'), lines)
			if ret:
				print c+" can be read as : "+'/'.join(ret)
		z.close()
