#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unicodedata
import os
import sys
import codecs
from latex_template import *
from create_jpn_db import JpnDB
from verb_conjugator import *
from adjective_conjugator import *

out = codecs.getwriter('utf-8')(sys.stdout)


#Helper function
def printheader(word):
    '''generate a nice header string'''
    out.write("\n%s\n%s\n" % (word, '-' * len(word)))
#-------------------------------------------------------------------
class JPN:
    '''Super class'''
    def __init__(self):
        self.data=[]
        self.index=0
        self.iv=[]              # irregular verbs
        self.uv=[]              # u verbs
        self.ruv=[]             # ru verbs
        self.ia=[]              # i adj
        self.naa=[]             # na adj

    def add(self,x):
        if x[0]=='irregular':
            tmp=verb(x[0],x)
            self.data.append(tmp)
        elif x[0]=='u':
            tmp=verb(x[0],x)
            self.data.append(tmp)
        elif x[0]=='ru':
            tmp=verb(x[0],x)
            self.data.append(tmp)
        elif x[0]=='na-adjektiv':
            tmp=naa(x[0],x)
            self.data.append(tmp)
        elif x[0]=='i-adjektiv':
            tmp=ia(x[0],x)
            self.data.append(tmp)
        else:
            pass

    def show(self):
        for i in self.data:
            i.show()

    def make_latex(self):
        out.write(latex_pre)

        l0=[u'Verb', u'Adjektiv']
        l1=[u'Irregular',u'RU-verbs', u'U-verbs']
        l2=[u'irregular', u'ru', u'u']
        l3=[u'な-adjektiv', u'い-adjektiv']
        l4=[u'na-adjektiv', u'i-adjektiv']

        dic={}
        dic['Verb']=[l1,l2]
        dic['Adjektiv']=[l3,l4]

        for sec in l0:      # section
            make_latex_section(sec)
            for i,j in zip(dic[sec][0],dic[sec][1]):
#                out.write('\n')
#                out.write(r'\clearpage')
#                out.write('\n')
#                out.write(r'\newpage')
#                out.write('\n')
                make_latex_subsection(i)
                i = 0
                for word in self.data:
                    if word.kind==j:
                        word.gen_table()
                        if i%10 == 0:
                            out.write(ur'\clearpage')
                        i += 1

        # create summary
        out.write('\n')
        out.write(r'\newpage')
        make_latex_section('Summary')
        out.write(summary_pre)
        for i,v in enumerate(self.data):
            #out.write(v.head)
            if i>0 and (i+1)%5==0:
                out.write(r'\\')
                out.write('\n')
            else:
                out.write(' & ')

        out.write('\n')
        out.write(summary_post)

        out.write(latex_post)
#-------------------------------------------------------------------
class Word():                   # base class
    '''word type'''
    def __init__(self,kind,data):
        pass

    def show(self):
        #printheader(self.kind)
        for i in self.data:
            out.write(i)
            out.write('\n')
        out.write('\n')
#-------------------------------------------------------------------
class verb(Word):               # verbs
    '''derived'''
    def __init__(self,kind,data):
        self.kind=kind
        self.data=data
        self.conjugation = conjugate_verb(kind, data[1])
        self.conjugation['title'] = self.conjugation['dict_form']
        self.conjugation['head'] = data[-2] + u' - ' + data[-1]

    def gen_table(self):
        s = verb_table_template.safe_substitute(self.conjugation)
        #s = verb_table_template.substitute(self.conjugation)
        out.write(s)
#-------------------------------------------------------------------
class ia(Word):                 # i adj
    '''derived'''
    def __init__(self,kind,data):
        self.kind=kind
        self.data=data
        self.conjugation= conjugate_adjective(kind, data[1])
        self.conjugation['title'] = self.conjugation['dict_form']
        self.conjugation['head'] = data[-2] + u' - ' + data[-1]

    def gen_table(self):
        s = i_table_template.safe_substitute(self.conjugation)
        out.write(s)
#-------------------------------------------------------------------
class naa(Word):                 # na adj
    '''derived'''
    def __init__(self,kind,data):
        self.kind=kind
        self.data=data
        self.conjugation= conjugate_adjective(kind, data[1])
        self.conjugation['title'] = self.conjugation['dict_form']
        self.conjugation['head'] = data[-2] + u' - ' + data[-1]

    def gen_table(self):
        s = na_table_template.safe_substitute(self.conjugation)
        out.write(s)

#-------------------------------------------------------------------
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

###############################################################

db = JpnDB()

x = JPN()
for i in db.list:
    x.add(i)

x.make_latex()

# vim: set fileencoding=utf-8 expandtab:
