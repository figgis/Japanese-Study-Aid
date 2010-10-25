#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unicodedata
import pickle
import sys
import codecs

out = codecs.getwriter('utf-8')(sys.stdout)

class JpnDB:
    '''data-base'''
    def __init__(self,f_name='list.txt'):
        self.list=[]
        self.f_name=f_name

        self.__populate()

    def __populate(self):
        fp=open(self.f_name)
        tmp=[]

        for line in fp:
            if '#' in line: # skip comments
                continue
            if not line.strip(): # empty lines indicates new block/EOB
                self.list.append(tmp)
                tmp=[]
                continue
            tmp.append(unicode(line.strip(),'utf-8'))
        fp.close()

        #remove empty arrays
        while True:
            try:
                self.list.remove([])
            except ValueError:
                break

    def verify(self):
        for i in self.list:
            out.write('%s\t%s\n' % (len(i), i[-1]))

        out.write('\nTotal number of items: %d\n' % len(self.list))

def main():
    x=JpnDB()
    x.verify()


if __name__ == "__main__":
    main()
