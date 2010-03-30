#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unicodedata
import pickle
import os
import sys
import codecs

out = codecs.getwriter('utf-8')(sys.stdout)

from latex_template import *


# up until the first cell to fill with data
WIDTH_1ST=29

def width(string):
    return sum(1+(unicodedata.east_asian_width(unicode(c)) in "WF")
        for c in string)

def pad(array, index, s):
    '''pad'''
    fill=0
    for i in index:
        if width(array[i]) > fill:
            fill=width(array[i])
    for i in index:
        array[i] = array[i] + ' '*((fill+1)-width(array[i]))
    return fill

def make_table(verb,section=True):
    '''make complete table'''
    wc0=pad(verb, [2,4,6,8], u'positive')
    wc1=pad(verb, [3,5,7,9], u'negative')
    wch=pad(verb, [1], u'')
    wcs=width(verb[2])
    s1=verb[1].encode('utf-8')
    s2=verb[2].encode('utf-8')
    s3=verb[3].encode('utf-8')
    s4=verb[4].encode('utf-8')
    s5=verb[5].encode('utf-8')
    s6=verb[6].encode('utf-8')
    s7=verb[7].encode('utf-8')
    s8=verb[8].encode('utf-8')
    s9=verb[9].encode('utf-8')
    tot= WIDTH_1ST + wc0 + wc1

    if section:
        print  s2 + '\n' + '-'*wcs
        print


    print  '+' + '-'*(tot+2) + '+' + '\n' +\
           '| ' + s1 +  ' '*(tot-wch) + '|\n' +\
           '+------------+------------+' + '-'*(wc0+2) + '+' + '-'*(wc1+2) + '+\n' +\
           '| Form                    |' + ' Positive ' + ' '*(wc0 - len('positive')) + '|' +\
           ' Negative ' + ' '*(wc1 - len('positive')) + '|' + '\n' +\
           '+============+============+' + '='*(wc0+2) + '+' + '='*(wc1+2) + '+' + '\n' +\
           '|            | Plain      | ' + s2 + '| ' + s3 + '|' + '\n' +\
           '+ Present    +------------+' + '-'*(wc0+2) + '+' + '-'*(wc1+2) + '+' + '\n' +\
           '|            | Polite     | ' + s4 + '| ' + s5 + '|' + '\n' +\
           '+------------+------------+' + '-'*(wc0+2) + '+' + '-'*(wc1+2) + '+' + '\n' +\
           '|            | Plain      | ' + s6 + '| ' + s7 + '|' + '\n' +\
           '+ Past       +------------+' + '-'*(wc0+2) + '+' + '-'*(wc1+2) + '+' + '\n' +\
           '|            | Polite     | ' + s8 + '| ' + s9 + '|' + '\n' +\
           '+------------+------------+' + '-'*(wc0+2) + '+' + '-'*(wc1+2) + '+' + '\n'
    print

def make_latex_table(verb):
    '''latex table'''

    h=verb_table

    for i in range(1,len(verb)):
        h=h.replace('@'+str(i),verb[i])

    out.write(h)

def make_latex_table_na_adj(verb):
    '''latex table'''

    h=na_table

    for i in range(1,len(verb)):
        h=h.replace('@'+str(i),verb[i])

    h=h.replace('@0',verb[2][:-1])

    out.write(h)

def make_latex_table_i_adj(verb):
    '''latex table'''

    h=i_table

    for i in range(1,len(verb)):
        h=h.replace('@'+str(i)+'-',verb[i])

    out.write(h)

def print_section_header(s,wc0,wc1,wch,wcs):
    '''section header'''
    return s + '\n' + '-'*wcs

def make_latex_section(s):
    '''\section{s}'''
    out.write('\n')
    out.write(r'\section{%s}' % (s))
    out.write('\n')

def make_latex_subsection(s):
    '''\section{s}'''
    out.write('\n')
    out.write(r'\subsection{%s}' % (s))
    out.write('\n')

def latex_list_all():
    '''list'''
    h=r'''
\begin{table}[ht]
  begin{tabular}{ll}
'''
    make_latex_section('List')
    print h
    l=len(list)
    if l%2!=0:
        pad=True
    for i in range(0,l/2):
        print list[i].encode('utf-8'), '&', list[i+1].encode('utf-8'), '\n'
    if pad:
        print '&'

    print r'\end{tabular}'
    print r'\end{table}'

###############################################################

pkl_file = open('data.pkl', 'rb')
list = pickle.load(pkl_file)
pkl_file.close()

out.write(latex_pre)
out.flush()

make_latex_section(u'Verb')

for i,j in zip(['Irregular', 'RU-verbs', 'U-verbs'], ['irregular', 'ru', 'u']):
    make_latex_subsection(i)
    for k in list:
        if k[0]==j:
            make_latex_table(k)
    out.write(ur'\clearpage')
    out.flush()


make_latex_section(u'Adjektiv')

for i,j in zip(['な-adjektiv', 'い-adjektiv'], ['na-adjektiv', 'i-adjektiv']):
    make_latex_subsection(i)
    for k in list:
        if k[0]==j:
            make_latex_table_na_adj(k)
        elif k[0]==j:
            make_latex_table_i_adj(k)
    out.write(ur'\clearpage')
    out.flush()

out.write(latex_post)

# vim: set fileencoding=utf-8 : encoding=utf-8
