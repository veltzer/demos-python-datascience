#!/usr/bin/env python3

"""
TBD
"""

import pylab as py
import scipy as sc
import scipy.stats as scs

x= scs.norm.pdf(sc.r_[-5:5:100j])
py.plot(x)
py.show()
