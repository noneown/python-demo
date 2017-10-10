import numpy as np

import image

import matplotlib.pyplot as plt
from PIL import Image


def load_by_image():
    alien = Image.open('images/alien.bmp')
    arr = np.array(alien.getdata(), np.uint8).reshape(alien.size[1], alien.size[0], 3)
    plt.gray()
    plt.imshow(arr)
    plt.colorbar()
    plt.show()


import scipy.misc as mc


def load_by_scipy():
    lena = mc.imread('images/alien.bmp')
    print lena.shape
    plt.gray()
    plt.imshow(lena)
    plt.colorbar()
    plt.show()

load_by_scipy()
