#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import codecs

out = codecs.getwriter('utf-8')(sys.stdout)

hiragana = "あ い う え お か き くけ こ さしすせそ"

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
        adj['pres_plain_pos'] = a + u'だ'
        adj['pres_polite_pos'] = a + u'です'
        #--------
        # present negative
        adj['pres_plain_neg'] = a  + u'ではない'
        adj['pres_polite_neg'] = a + u'ではありません'
        #--------
        # past positive
        adj['past_plain_pos'] = a + u'だった'
        adj['past_polite_pos'] = a + u'でした'
        #--------
        # past negative
        adj['past_plain_neg'] = a + u'ではなかった'
        adj['past_polite_neg'] = a + u'ではありませんでした'
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
