#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import codecs
import sys

out = codecs.getwriter('utf-8')(sys.stdout)

def conjugate_verb(kind=None, v=None):
    """stuff"""
    verb = {'dict_form'       : None,
            'pres_plain_pos'  : None,
            'pres_polite_pos' : None,
            'pres_plain_neg'  : None,
            'pres_polite_neg' : None,
            'past_plain_pos'  : None,
            'past_polite_pos' : None,
            'past_plain_neg'  : None,
            'past_polite_neg' : None,
            'te_form'         : None,
            }

#    print kind, v

    verb['dict_form'] = v

    if kind == 'irregular':
        if v == u'来る':
            #--------
            # present positive
            verb['pres_plain_pos'] = v
            verb['pres_polite_pos'] = u'来ます'
            #--------
            # present negative
            verb['pres_plain_neg'] = u'来ない'
            verb['pres_polite_neg'] = u'来ません'
            #--------
            # past positive
            verb['past_plain_pos'] = u'来た'
            verb['past_polite_pos'] = u'来ました'
            #--------
            # past negative
            verb['past_plain_neg'] = u'来なかった'
            verb['past_polite_neg'] = u'来ませんでした'
            #--------
            # te_form
            verb['te_form'] = u'来て'
        elif v == u'する':
            #--------
            # present positive
            verb['pres_plain_pos'] = v
            verb['pres_polite_pos'] = u'します'
            #--------
            # present negative
            verb['pres_plain_neg'] = u'しない'
            verb['pres_polite_neg'] = u'しません'
            #--------
            # past positive
            verb['past_plain_pos'] = u'した'
            verb['past_polite_pos'] = u'しました'
            #--------
            # past negative
            verb['past_plain_neg'] = u'しなかった'
            verb['past_polite_neg'] = u'しませんでした'
            #--------
            # te_form
            verb['te_form'] = u'して'
        elif v[-2:] == u'する':
            #--------
            # present positive
            verb['pres_plain_pos'] = v
            verb['pres_polite_pos'] = v[:-2] + u'します'
            #--------
            # present negative
            verb['pres_plain_neg'] = v[:-2] + u'しない'
            verb['pres_polite_neg'] = v[:-2] + u'しません'
            #--------
            # past positive
            verb['past_plain_pos'] = v[:-2] + u'した'
            verb['past_polite_pos'] = v[:-2] + u'しました'
            #--------
            # past negative
            verb['past_plain_neg'] = v[:-2] + u'しなかった'
            verb['past_polite_neg'] = v[:-2] + u'しませんでした'
            #--------
            # te_form
            verb['te_form'] = v[:-2] + u'して'
        elif v[-2:] == u'くる':
            #--------
            # present positive
            verb['pres_plain_pos'] = v
            verb['pres_polite_pos'] = v[:-2] + u'きます'
            #--------
            # present negative
            verb['pres_plain_neg'] = v[:-2] + u'こない'
            verb['pres_polite_neg'] = v[:-2] + u'きません'
            #--------
            # past positive
            verb['past_plain_pos'] = v[:-2] + u'きた'
            verb['past_polite_pos'] = v[:-2] + u'きました'
            #--------
            # past negative
            verb['past_plain_neg'] = v[:-2] + u'こなかった'
            verb['past_polite_neg'] = v[:-2] + u'きませんでした'
            #--------
            # te_form
            verb['te_form'] = v[:-2] + u'きて'
        else:
            pass
            #print 'wrong -irregular'
    #handle RU-verb
    elif kind == 'ru':
        #--------
        # present positive
        verb['pres_plain_pos'] = v
        verb['pres_polite_pos'] = v[:-1] + u'ます'
        #--------
        # present negative
        verb['pres_plain_neg'] = v[:-1] + u'ない'
        verb['pres_polite_neg'] = v[:-1] + u'ません'
        #--------
        # past positive
        verb['past_plain_pos'] = v[:-1] + u'た'
        verb['past_polite_pos'] = v[:-1] + u'ました'
        #--------
        # past negative
        verb['past_plain_neg'] = v[:-1] + u'なかった'
        verb['past_polite_neg'] = v[:-1] + u'ませんでした'
        #--------
        # te_form
        verb['te_form'] = v[:-1] + u'て'

    elif kind == 'u':
        if v[-1] == u'う':
            #--------
            # present positive
            verb['pres_plain_pos'] = v
            verb['pres_polite_pos'] = v[:-1] + u'います'
            #--------
            # present negative
            verb['pres_plain_neg'] = v[:-1] + u'わない'
            verb['pres_polite_neg'] = v[:-1] + u'いません'
            #--------
            # past positive
            verb['past_plain_pos'] = v[:-1] + u'った'
            verb['past_polite_pos'] = v[:-1] + u'いました'
            #--------
            # past negative
            verb['past_plain_neg'] = v[:-1] + u'わなかった'
            verb['past_polite_neg'] = v[:-1] + u'いませんでした'
            #--------
            # te_form
            verb['te_form'] = v[:-1] + u'って'
        elif v[-1] == u'つ':
            #--------
            # present positive
            verb['pres_plain_pos'] = v
            verb['pres_polite_pos'] = v[:-1] + u'ちます'
            #--------
            # present negative
            verb['pres_plain_neg'] = v[:-1] + u'たない'
            verb['pres_polite_neg'] = v[:-1] + u'ちません'
            #--------
            # past positive
            verb['past_plain_pos'] = v[:-1] + u'った'
            verb['past_polite_pos'] = v[:-1] + u'ちました'
            #--------
            # past negative
            verb['past_plain_neg'] = v[:-1] + u'たなかった'
            verb['past_polite_neg'] = v[:-1] + u'ちませんでした'
            #--------
            # te_form
            verb['te_form'] = v[:-1] + u'って'
        elif v[-1] == u'る':
            #--------
            # present positive
            verb['pres_plain_pos'] = v
            verb['pres_polite_pos'] = v[:-1] + u'ります'
            #--------
            # present negative
            verb['pres_plain_neg'] = v[:-1] + u'らない'
            verb['pres_polite_neg'] = v[:-1] + u'りません'
            #--------
            # past positive
            verb['past_plain_pos'] = v[:-1] + u'った'
            verb['past_polite_pos'] = v[:-1] + u'りました'
            #--------
            # past negative
            verb['past_plain_neg'] = v[:-1] + u'らなかった'
            verb['past_polite_neg'] = v[:-1] + u'りませんでした'
            #--------
            # te_form
            verb['te_form'] = v[:-1] + u'って'
        elif v[-1] == u'む':
            #--------
            # present positive
            verb['pres_plain_pos'] = v
            verb['pres_polite_pos'] = v[:-1] + u'みます'
            #--------
            # present negative
            verb['pres_plain_neg'] = v[:-1] + u'まない'
            verb['pres_polite_neg'] = v[:-1] + u'みません'
            #--------
            # past positive
            verb['past_plain_pos'] = v[:-1] + u'んだ'
            verb['past_polite_pos'] = v[:-1] + u'みました'
            #--------
            # past negative
            verb['past_plain_neg'] = v[:-1] + u'まなかった'
            verb['past_polite_neg'] = v[:-1] + u'みませんでした'
            #--------
            # te_form
            verb['te_form'] = v[:-1] + u'んで'
        elif v[-1] == u'ぶ':
            #--------
            # present positive
            verb['pres_plain_pos'] = v
            verb['pres_polite_pos'] = v[:-1] + u'びます'
            #--------
            # present negative
            verb['pres_plain_neg'] = v[:-1] + u'ばない'
            verb['pres_polite_neg'] = v[:-1] + u'びません'
            #--------
            # past positive
            verb['past_plain_pos'] = v[:-1] + u'んだ'
            verb['past_polite_pos'] = v[:-1] + u'びました'
            #--------
            # past negative
            verb['past_plain_neg'] = v[:-1] + u'ばなかった'
            verb['past_polite_neg'] = v[:-1] + u'びませんでした'
            #--------
            # te_form
            verb['te_form'] = v[:-1] + u'んで'
        elif v[-1] == u'ぬ':
            #--------
            # present positive
            verb['pres_plain_pos'] = v
            verb['pres_polite_pos'] = v[:-1] + u'にます'
            #--------
            # present negative
            verb['pres_plain_neg'] = v[:-1] + u'なない'
            verb['pres_polite_neg'] = v[:-1] + u'にません'
            #--------
            # past positive
            verb['past_plain_pos'] = v[:-1] + u'んだ'
            verb['past_polite_pos'] = v[:-1] + u'にました'
            #--------
            # past negative
            verb['past_plain_neg'] = v[:-1] + u'ななかった'
            verb['past_polite_neg'] = v[:-1] + u'にませんでした'
            #--------
            # te_form
            verb['te_form'] = v[:-1] + u'んで'
        elif v[-1] == u'く':
            #--------
            # present positive
            verb['pres_plain_pos'] = v
            verb['pres_polite_pos'] = v[:-1] + u'きます'
            #--------
            # present negative
            verb['pres_plain_neg'] = v[:-1] + u'かない'
            verb['pres_polite_neg'] = v[:-1] + u'きません'
            #--------
            # past positive
            verb['past_plain_pos'] = v[:-1] + u'いた'
            verb['past_polite_pos'] = v[:-1] + u'きました'
            #--------
            # past negative
            verb['past_plain_neg'] = v[:-1] + u'かなかった'
            verb['past_polite_neg'] = v[:-1] + u'きませんでした'
            #--------
            # te_form
            verb['te_form'] = v[:-1] + u'いて'
        elif v[-1] == u'ぐ':
            #--------
            # present positive
            verb['pres_plain_pos'] = v
            verb['pres_polite_pos'] = v[:-1] + u'ぎます'
            #--------
            # present negative
            verb['pres_plain_neg'] = v[:-1] + u'がない'
            verb['pres_polite_neg'] = v[:-1] + u'ぎません'
            #--------
            # past positive
            verb['past_plain_pos'] = v[:-1] + u'いだ'
            verb['past_polite_pos'] = v[:-1] + u'ぎました'
            #--------
            # past negative
            verb['past_plain_neg'] = v[:-1] + u'がなかった'
            verb['past_polite_neg'] = v[:-1] + u'ぎませんでした'
            #--------
            # te_form
            verb['te_form'] = v[:-1] + u'いで'
        elif v[-1] == u'す':
            #--------
            # present positive
            verb['pres_plain_pos'] = v
            verb['pres_polite_pos'] = v[:-1] + u'します'
            #--------
            # present negative
            verb['pres_plain_neg'] = v[:-1] + u'さない'
            verb['pres_polite_neg'] = v[:-1] + u'しません'
            #--------
            # past positive
            verb['past_plain_pos'] = v[:-1] + u'した'
            verb['past_polite_pos'] = v[:-1] + u'しました'
            #--------
            # past negative
            verb['past_plain_neg'] = v[:-1] + u'さなかった'
            verb['past_polite_neg'] = v[:-1] + u'しませんでした'
            #--------
            # te_form
            verb['te_form'] = v[:-1] + u'して'
        else:
            out.write("wrong kind: %s, v:%s\n" % (kind, v))
    else:
        print 'tilt'

    # handle some special cases
    if kind == 'u':
        if v == u'行く':
            verb['te_form'] = v[:-1] + u'って'
            verb['past_plain_pos'] = v[:-1] + u'った'
        elif v == u'ある':
            verb['pres_plain_neg'] = v[:-1] + u'ない'
            verb['past_plain_neg'] = v[:-1] + u'なかった'
        elif v[-2:] == u'いく':
            verb['te_form'] = v[:-1] + u'って'
            verb['past_plain_pos'] = v[:-1] + u'った'
        elif v[-2:] == u'ある':
            verb['pres_plain_neg'] = v[:-2] + u'ない'
            verb['past_plain_neg'] = v[:-2] + u'なかった'

    #    あう， いく


    return verb
