
# coding: utf-8

# # Subrotina para BIAS

# In[1]:

from astropy.io import fits
import glob
import numpy as np


# In[2]:

def bias():
    BIAS = []
    i = 1
    for fitsName in glob.glob('bias.B.*.fits'):        
        img, hdr = fits.getdata(fitsName,header=True)
        img = np.array(img, dtype='Float64')
        globals()['bias%s' % i] = img
#        print('bias%s' % i)
        BIAS.append(img)
#        print(img)
        i += 1
    bias_median = np.median(BIAS, axis=0)
    return(bias_median)

