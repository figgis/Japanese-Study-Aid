#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import codecs

out = codecs.getwriter('utf-8')(sys.stdout)

def i_adj(str):
    '''i-adjectiv'''
    a=str
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


    s=r"""
u'%s', u'%s',
u'%s',u'%s',
u'%s', 
u'%s', u'%s',
u'%s', u'%s', 
u'%s'],""" % (a,c,d,e,f,g,h,i,j,k)

    return s

def na_adj(str):
    '''i-adjectiv'''
    a=str+u'だ'
    b=str+u'ではない'
    c=str+u'です'
    d=str+u'ではありません'
    e=str+u'だった'
    f=str+u'ではなかった'
    g=str+u'でした'
    h=str+u'ではありませんでした'


    s=r"""
u'%s', u'%s',
u'%s', u'%s',
u'%s', u'%s',
u'%s', u'%s'],""" % (a,b,c,d,e,f,g,h)

    return s
#    print s.encode('utf-8')

#out.write(i_adj(u'安い'))
out.write(na_adj(u'有名'))
