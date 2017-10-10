import matplotlib.pyplot as plt
import random

import numpy as np

from numpy import ones, convolve, linspace, sin
from numpy.random.mtrand import randn
from scipy import signal

SAMPLE_SIZE = 100

def average_random():
    random.seed()

    rand_vars = [random.random() for val in range(SAMPLE_SIZE)]

    x = range(SAMPLE_SIZE)
    y = []
    tempy = 0
    for i in x:
        tempy += random.normalvariate(0.2, 1.2)
        y.append(tempy)

    plt.plot(x, y)
    plt.xlabel('number')
    plt.ylabel('count')

    plt.show()

def get_average(interval, windwo_size):
    window = ones(windwo_size)/float(windwo_size)
    return convolve(interval, window, 'same')

def moving_average():
    t = linspace(-4, 4, 100)

    y = sin(t) + randn(len(t))*0.1

    plt.plot(t, y, 'k.')

    y_av = get_average(y, 10)

    plt.plot(t, y_av, 'r.')
    plt.xlabel('number')
    plt.ylabel('count')
    plt.grid(True)
    plt.show()

def middle_filter():
    x = linspace(0, 1, 101)
    x[3::10] = x[3::10] + 0.1
    x[1::10] = x[1::10] - 0.1
    plt.plot(x)
    plt.plot(signal.medfilt(x, 3))
    plt.plot(signal.medfilt(x, 5))
    plt.legend(['origin', 'length3', 'length5'])
    plt.show()

import tushare as ts
import lxml.html
def finance():
    print ts.get_today_all()

def sort_list():
    a = [1, 3, 4, 5]
    b = [2, 4, 5, 9]
    a.extend(b)
    print list(set(a))
sort_list()


