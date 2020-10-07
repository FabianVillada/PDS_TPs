# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 08:59:45 2020

@author: Usuario
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
    

def generador_senoidal (fs, f0, N, a0, p0):
   
    tt=np.arange(N/fs , step=1/fs)
    signal = a0 * np.sin( 2 * np.pi * f0 * tt + p0 )
     
    return tt, signal   

N  = 1000         
fs = 1000        
df=fs/N                   

a0 = 1 # Volts
p0 = np.pi/4  #radianes. 

fd = [0, 0.5]

for i in range(len(fd)):

    f0 = fs/4  + fd[i]   

    tt , signal = generador_senoidal(fs , f0 , N , a0 , p0)

   
    fft1 = fft(signal) # no hace falta pasar N
    fftabs = np.abs(fft1)/(N-N/2)
    fftangle = np.angle(fft1)
    
    freq = np.arange(0 , fs , df)     
    plt.figure(i+1)
    # plt.plot (freq , fftabs , 'o-' )
    plt.stem( freq , fftabs, use_line_collection = True) 
    # plt.xlim(200,300)
    plt.xlabel('fercuencia') 
    plt.ylabel('modulo')
    plt.title ('espectro normalizado a N/2 con frecuencia de desintonia'+str(fd[i]))
    plt.grid()
    plt.show()
    
    fftabs = np.abs(fft1)/N
    plt.figure(i+3)
    # plt.plot (freq , fftabs , 'o-' )
    plt.stem( freq , fftabs, use_line_collection = True) 
    # plt.xlim(200,300)
    plt.xlabel('fercuencia') 
    plt.ylabel('modulo')
    plt.title ('espectro normalizado a N con frecuencia de desintonia'+str(fd[i]))
    plt.grid()
    plt.show()
    
    fftabs = np.abs(fft1)
    plt.figure(i+5)
    # plt.plot (freq , fftabs , 'o-' )
    plt.stem( freq , fftabs, use_line_collection = True) 
    # plt.xlim(200,300)
    plt.xlabel('fercuencia') 
    plt.ylabel('modulo')
    plt.title ('espectro sin normalizacion con frecuencia de desintonia'+str(fd[i]))
    plt.grid()
    plt.show()  
    
    