"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys
from operator import itemgetter

import first
import thinkstats2
import queue
import nsfg
import math


def Mode(hist):
    """Returns the value with the highest frequency.

    hist: Hist object

    returns: value from Hist
    """
    mode_candidate=(0,0)
    for pair in hist.Items():
        if mode_candidate[1]<pair[1]:
            mode_candidate=pair
    return mode_candidate[0]
    # return 0

def AllModes(hist):
    """Returns value-freq pairs in decreasing order of frequency.

    hist: Hist object

    returns: iterator of value-freq pairs
    """
    items=list(hist.Items())
    items.sort(key=lambda el:-el[1])
    return items

def CohenEffectSize(g1,g2):
    dif=g1.mean()-g2.mean()
    var1= g1.var()
    var2= g2.var()
    n1,n2=len(g1),len(g2)
    pooled_var=(n1*var1+n2*var2)/(n1+n2)
    d=dif/math.sqrt(pooled_var)
    return d

def ex2_4():
    df = nsfg.ReadFemPreg()
    firsts=df[df.birthord==1]
    others=df[df.birthord>1]
    firsts_lb_mean=firsts.totalwgt_lb.mean()
    others_lb_mean=others.totalwgt_lb.mean()
    print (firsts_lb_mean,others_lb_mean)
    print (CohenEffectSize(others.totalwgt_lb,firsts.totalwgt_lb))
    #Not knowing what is statistically significant, .088 is certainly larger than .029
    #The effects between birthorder and wieght are stronger than those between 
    #birthorder and pregnancy duration  


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()
    hist = thinkstats2.Hist(live.prglngth)

    # test Mode    
    mode = Mode(hist)
    print('Mode of preg length', mode)
    assert(mode == 39)

    # test AllModes
    modes = AllModes(hist)
    assert(modes[0][1] == 4693)

    for value, freq in modes[:5]:
        print(value, freq)

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    # main(*sys.argv)
    ex2_4()
