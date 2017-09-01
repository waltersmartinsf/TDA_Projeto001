
# coding: utf-8

# # Subrotina BFlat

# In[1]:

from astropy.io import fits
import glob
import numpy as np
get_ipython().magic('run Proj_001_bias')


# In[2]:

def BFLAT_mean(): #função para calcular a média das imagens bflats (flat corrigida por bias)
    BFLAT = []
    for fitsName in glob.glob('flat.B.*.fits'):        
        img, hdr = fits.getdata(fitsName,header=True)
        img = np.array(img, dtype='Float64')
        bflat = img - bias() #correção do bias para cada imagem flat
        BFLAT.append(bflat) #junção das imagens flat corrigidas
    BFLAT_mean = np.mean(BFLAT, axis = 0) #média das imagens flat
    BFLAT_mean = np.array(BFLAT_mean, dtype = 'Float64')
    return(BFLAT_mean)


# In[5]:

def bflat(): #função para calcular o bflats
    BFLAT_norm = []
    for fitsName in glob.glob('flat.B.*.fits'):        
        img, hdr = fits.getdata(fitsName, header=True)
#        img = np.array(img, dtype='Float64')
        bflat = img - bias()
        bflat = np.array(bflat, dtype = 'Float64')
        bflat_norm = bflat*(np.linalg.inv(BFLAT_mean())) #normalização de cada imagem flat 
        BFLAT_norm.append(bflat_norm) #junção das imagens flat normalizadas
    bflat_median = np.median(BFLAT_norm, axis = 0) #mediana das imagens flat normalizadas
    return(bflat_median)


# In[7]:

bflat()


# In[ ]:



