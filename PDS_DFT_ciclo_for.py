# -*- coding: utf-8 -*-*k
"""
Created on Tue Sep 15 01:42:03 2020
@author: Usuario
"""

import numpy as np

import matplotlib.pyplot as plt



def generador_senoidal (fs, f0, N, a0, p0):
   

    # comienzo de la función
  
    #df=fs/N 
    tt=np.arange(N/fs , step=1/fs)
    #tt=np.arange(start= -10 , stop=10 , step=1/10)
    
    
    signal = a0 * np.sin( 2 * np.pi * f0 * tt + p0 )
     
    return tt, signal
    # fin de la función
    
def twildde_factor ( k , n , N):
    wk = np.cos( 2 * np.pi * k *n / N ) -  np.sin( 2 * np.pi * k * n / N )*1j
    return wk
energia = ()
def DFT ( signal , N  ):
    dft = np.arange(0.0 , N , dtype = 'complex' )
    for k in range (0 , N):
        sum_Wn = 0
        for n in range(0 , N):
            sum_Wn = sum_Wn + twildde_factor(k , n , N) * signal[n]
        dft[k] = sum_Wn
    
    return dft


################ MAIN ####################################################

N  = 100         
fs = 100         
df=fs/N                   

a0 = 1 # Volts
p0 = 0  #radianes. 
f0 = 10     # Hz  .    

tt , signal = generador_senoidal(fs , f0 , N , a0 , p0)
freq1 = np.linspace(0, (N-1)*df, N)


dft = DFT(signal , N)

dftabs = np.abs(dft) # Normalizo para que se cumpla Parserval

dftabs = dftabs**2 / N
dftangle = np.angle(dft)

############## Visualizacion #############################################

#######PARA REPRESENTAR  LA FASE , SI MODULO<0.1 FASE = 0 ########

for i in range(len(dftabs)):
    if dftabs[i] < 0.1:
        dftangle[i] = 0

##############################################################################
        
        
plt.subplot(2, 1, 1)
plt.plot(freq1, dftabs , 'o-')
plt.title('DFT')
plt.ylabel('MODULO')

plt.subplot(2, 1, 2)
plt.plot(freq1, dftangle, '.-')
plt.xlabel('Frecuencia[HZ]')
plt.ylabel('Fase')

plt.show()

