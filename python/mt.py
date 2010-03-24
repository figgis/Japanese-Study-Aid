#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unicodedata
import pprint, pickle
import os


# up until the first cell to fill with data
WIDTH_1ST=29
d=u'-' #dash
p=u'+' #plus
b=u'|' #bar
e=u'=' #equal
wc0=0  #width column 0
wc1=0  #width column 1
wch=0  #width column header
wcs=0  #width column section

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
    h=r'''
\begin{table}[ht]
  \resizebox{\textwidth}{!}{%
  \begin{tabular}{|l|l|l|l|}
  \hline
  \multicolumn{4}{|c|}{} \\
  \multicolumn{4}{|c|}{\huge{@2}} \\
  \multicolumn{4}{|c|}{} \\
  \hline
  \multicolumn{4}{|c|}{@1} \\
  \hline
  \multicolumn{2}{|l}{\textbf{Form}} & \textbf{Positive} & \textbf{Negative} \\
  \hline
  Present & Plain   & @2 & @3 \\
          & Polite  & @4 & @5 \\
  \hline
  Past    & Plain   & @6 & @7 \\
          & Polite  & @8 & @9 \\
  \hline
  \end{tabular}}
\end{table}'''

#    s = '\subsubsection{%s}' % (verb[2])
#    print 
#    print s.encode('utf-8')
#    print 

    for i in range(1,len(verb)):
        h=h.replace('@'+str(i),verb[i].encode('utf-8'))

    print h
#    print r'\clearpage'

def make_latex_table_i_adj(verb):
    '''latex table'''
    h=r'''
\begin{table}[ht]
  \resizebox{\textwidth}{!}{%
  \begin{tabular}{|l|l|l|l|}
  \hline
  \multicolumn{4}{|c|}{} \\
  \multicolumn{4}{|c|}{\huge{@2-}} \\
  \multicolumn{4}{|c|}{} \\
  \hline
  \multicolumn{4}{|c|}{@1-} \\
  \hline
  \multicolumn{2}{|l}{\textbf{Form}} & \textbf{Positive} & \textbf{Negative} \\
  \hline
  Present & Plain   & @2- & @3- \\
          & Polite  & @4- & @5- \\
          &         &     & @6- \\
  \hline
  Past    & Plain   & @7- & @8-  \\
          & Polite  & @9- & @10- \\
          &         &     & @11- \\
  \hline
  \end{tabular}}
\end{table}'''

#    s = '\subsubsection{%s}' % (verb[2])
#    print 
#    print s.encode('utf-8')
#    print 


    for i in range(1,len(verb)):
        h=h.replace('@'+str(i)+'-',verb[i].encode('utf-8'))

    print h
#    print r'\clearpage'

def print_section_header(s,wc0,wc1,wch,wcs):
    '''section header'''
    return s + '\n' + '-'*wcs

def make_latex_section(s):
    '''\section{s}'''
    print
    print '\section{%s}' % (s)
    print

def make_latex_subsection(s):
    '''\section{s}'''
    print
    print '\subsection{%s}' % (s)
    print

pkl_file = open('data.pkl', 'rb')
list = pickle.load(pkl_file)
#pprint.pprint(list)
pkl_file.close()

make_latex_section('Verb')

make_latex_subsection('Irregular')
#irregular
for i in list:
    if i[0]==u'irregular':
        make_latex_table(i)
print r'\clearpage'

make_latex_subsection('RU-verbs')
#ru-verbs
for i in list:
    if i[0]==u'ru':
        make_latex_table(i)
print r'\clearpage'

make_latex_subsection('U-verbs')
#u-verbs
for i in list:
    if i[0]==u'u':
        make_latex_table(i)
print r'\clearpage'

#na-adjektiv
make_latex_section('Adjektiv')
make_latex_subsection('な-adjektiv')
for i in list:
    if i[0]==u'na-adjektiv':
        make_latex_table(i)
print r'\clearpage'

#i-adjektiv
make_latex_subsection('い-adjektiv')
for i in list:
    if i[0]==u'i-adjektiv':
        make_latex_table_i_adj(i)
print r'\clearpage'

#print 'Number of items:', len(list)

# vim: set fileencoding=utf-8 : encoding=utf-8

