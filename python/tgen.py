#!/usr/bin/env python
# coding=UTF-8

# generate sphinx tables

h='''
+------------+---------+-----------+---------------------+
| Form                 | Positive  | Negative            |
+============+=========+===========+=====================+
|            | Plain   |  する     | しない              |
+ Present    +---------+-----------+---------------------+
|            | Polite  |  します   | しません            |
+------------+---------+-----------+---------------------+
|            | Plain   |  した     | しなかた            |
+ Past       +---------+-----------+---------------------+
|            | Polite  |  しました | しませんでした      |
+------------+---------+-----------+---------------------+
'''

head=['dictionary form', 
      'present plain pos',
      'present polite pos',
      'present plain neg',
      'present polite neg',
      'past plain pos',
      'past polite pos',
      'past plain neg',
      'past polite neg']


f=open('list.txt')
verb=[]
tmp=[]

for line in f:
    if '#' in line: # skip comments
        continue
    if not line.strip(): # empty lines indicates new block/EOB
        verb.append(tmp)
        tmp=[]
        continue
    tmp.append(unicode(line.strip(),'utf-8'))
f.close()

#remove empty arrays
while True:
    try:
        verb.remove([])
    except ValueError:
        break


print len(verb)
for i in verb:
    for j in i:
        print j
    print

