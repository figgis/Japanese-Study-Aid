#!/usr/bin/env python
# -*- coding: UTF-8 -*-


a=u'安い'
b=a[:-1]
c=b+u'くない'
d=b+u'です'
e=b+u'くないです'
f=b+u'くありません'
g=b+u'かった'
h=b+u'くなかった'
i=b+u'かったです'
j=b+u'くなかったです'
k=b+u'くありませんでした'


s=r"""u'%s', u'%s',
 u'%s',u'%s',
 u'%s', 
 u'%s', u'%s',
 u'%s', u'%s', 
 u'%s'],""" % (a,c,d,e,f,g,h,i,j,k)

print s.encode('utf-8')


