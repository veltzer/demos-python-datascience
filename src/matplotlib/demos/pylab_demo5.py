"""
Created on Sun Jan 18 00:57:43 2015

@author: liran
"""

import numpy
import matplotlib.pyplot as plt


x = numpy.arange(50)*2*numpy.pi/50
y = numpy.sin(x)

fig, ax = plt.subplots()


plt.plot(x, y, '-o', picker=4)
text = ax.text(0, -0.5, " ", va="bottom", ha="left")


def on_pick(event):
    """ on_pick """
    thisline = event.artist
    _xdata, _ydata = thisline.get_data()
    ind = event.ind
    text.set_text(str(ind))


cid = fig.canvas.mpl_connect('pick_event', on_pick)
plt.show()
