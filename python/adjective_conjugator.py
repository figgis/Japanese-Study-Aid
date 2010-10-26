#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import codecs

out = codecs.getwriter('utf-8')(sys.stdout)

def conjugate_adjective(kind, a):
    """stuff"""
    adj = {'dict_form'          : None,
           'pres_plain_pos'     : None,
           'pres_polite_pos'    : None,
           'pres_plain_neg'     : None,
           'pres_polite_neg'    : None,
           'pres_polite_neg_v2' : None,
           'past_plain_pos'     : None,
           'past_polite_pos'    : None,
           'past_plain_neg'     : None,
           'past_polite_neg'    : None,
           'past_polite_neg_v2' : None,
           }

    adj['dict_form'] = a

    if kind == 'na-adjektiv':
        #--------
        # present positive
        adj['pres_plain_pos'] = a[:-1] + u'だ'
        adj['pres_polite_pos'] = a[:-1] + u'です'
        #--------
        # present negative
        adj['pres_plain_neg'] = a[:-1]  + u'ではない'
        adj['pres_polite_neg'] = a[:-1] + u'ではありません'
        #--------
        # past positive
        adj['past_plain_pos'] = a[:-1] + u'だった'
        adj['past_polite_pos'] = a[:-1] + u'でした'
        #--------
        # past negative
        adj['past_plain_neg'] = a[:-1] + u'ではなかった'
        adj['past_polite_neg'] = a[:-1] + u'ではありませんでした'
        #--------

    elif kind == 'i-adjektiv':
        #--------
        # present positive
        adj['pres_plain_pos'] = a
        adj['pres_polite_pos'] = a + u'です'
        #--------
        # present negative
        adj['pres_plain_neg'] = a[:-1] + u'くない'
        adj['pres_polite_neg'] = a[:-1] + u'くないです'
        adj['pres_polite_neg_v2'] = a[:-1] + u'くありません'
        #--------
        # past positive
        adj['past_plain_pos'] = a[:-1] + u'かった'
        adj['past_polite_pos'] = a[:-1] + u'かったです'
        #--------
        # past negative
        adj['past_plain_neg'] = a[:-1] + u'くなかった'
        adj['past_polite_neg'] = a[:-1] + u'くなかったです'
        adj['past_polite_neg_v2'] = a[:-1] + u'くありませんでした'
        #--------

    return adj


#def i_adj(str):
#    '''i-adjectiv'''
#0   a=str
#1   b=a[:-1]
#2   c=b+u'くない'
#3   d=b+u'です'
#4   e=b+u'くないです'
#5   f=b+u'くありません'
#6   g=b+u'かった'
#7   h=b+u'くなかった'
#8   i=b+u'かったです'
#9   j=b+u'くなかったです'
#10  k=b+u'くありませんでした'
#
#
#    s=r"""
#u'%s', u'%s',
#u'%s',u'%s',
#u'%s', 
#u'%s', u'%s',
#u'%s', u'%s', 
#u'%s'],""" % (a,c,d,e,f,g,h,i,j,k)
#
#    return s
#
#def na_adj(str):
#    '''i-adjectiv'''
#0   a=str+u'だ'
#1   b=str+u'ではない'
#2   c=str+u'です'
#3   d=str+u'ではありません'
#4   e=str+u'だった'
#5   f=str+u'ではなかった'
#6   g=str+u'でした'
#7   h=str+u'ではありませんでした'
#
#
#    s=r"""
#u'%s', u'%s',
#u'%s', u'%s',
#u'%s', u'%s',
#u'%s', u'%s'],""" % (a,b,c,d,e,f,g,h)
#
#    return s
##    print s.encode('utf-8')
#
##out.write(i_adj(u'安い'))
#out.write(na_adj(u'有名'))
