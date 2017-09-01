
# coding: utf-8

# # Subrotina para BIAS

# In[1]:

from astropy.io import fits
import glob
import numpy as np


# In[16]:

#Função que calcula a mediana de todas as imagens de bias
def bias(): 
    BIAS = [] #abre uma variável vazia
    for fitsName in glob.glob('bias.B.*.fits'): #função glob.glob consegue identificar padrões. Todos os meus arquivos com esse padrão de nome serão lidos       
        img, hdr = fits.getdata(fitsName,header=True) 
        img = np.array(img, dtype='Float64') #correção do Float64
        BIAS.append([img]) #junção de todas as iimagens de bias em um array
    bias_median = np.median(BIAS, axis = 0) #cálculo da mediana de todos as imagens bias
    return(bias_median) #retorna a matriz de bias


# In[17]:

bias()


# In[ ]:



