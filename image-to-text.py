import math
import numpy
import scipy.misc
from scipy.misc.pilutil import Image


im = Image.\
     open('uploads').\
     convert('L')

im1 = scipy.misc.fromimage(im)

b = im1.max()
a = im1.min()

print(a,b)

c = im1.astype(float)

im2 = 255*(c-a)/(b-a)

im3 = scipy.misc.toimage(im2)

print(im3)

