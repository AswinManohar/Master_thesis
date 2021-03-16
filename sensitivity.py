#!/usr/bin/env python


import math
import matplotlib.pyplot as plt
import numpy as np

#import matplotlib.axes.Axes.legend
#import matplotlib.pyplot.legend
#import matplotlib.axes.Axes.plot



total_bandwidth= 288*10**6
channel_bandwidth=3 #MHZ
observing_f= 1.374 #Ghz
t_samp= 250  #micro seconds
w_int=  1000 #micro seconds
w_int1= 500000 #micro seconds
w_int2= 100000 #micro seconds
t_sys= 21 #Kelvin
G= 0.690 

#w_int_seconds=w_int/10**6
#bandwidth= channel_bandwidth*10**6

aswin=[]

def sense_curves(x):
    
    
    sm_list = []
    #max=[]
    DM = np.linspace(0,3000,3000)
    for i in range(len(DM)):

        t_chan=8.3*channel_bandwidth*(1/observing_f)**3*i
        effects=(x)**2+(t_samp)**2+(t_chan)**2  
        w_obs=math.sqrt(effects)
        w_seconds=w_obs/10**6 #seconds
        w_intrinsic_seconds=0.001 #seconds

        d=w_seconds/w_intrinsic_seconds

        smin=d*t_sys*6/G*(2*total_bandwidth*w_seconds)**(1/2)

        sm_list.append(smin)
    sm_list = np.asarray(sm_list)
    print t_chan
    print w_obs
    print w_seconds
    print w_intrinsic_seconds
    print d
    
    #max.append(
    print max(sm_list)
    print sm_list
    return sm_list 
  
  

DM = np.linspace(0,3000,3000)

    
fig,ax=plt.subplots() 
ax.plot(DM,sense_curves(w_int),'k--',label='DDplan1')
#ax.plot(DM,sense_curves(w_int1),'k:',label='50ms') 
#ax.plot(DM,sense_curves(w_int2),'k',label='wint=100ms')
ax.set_yscale('log')

plt.xlabel("Dispersion measure")
plt.ylabel("minimum flux density (jy)")
legend = ax.legend(loc='upper left', shadow=True, fontsize='x-large')
#sense_curves(w_int)
#sense_curves(w_int1)
#sense_curves(w_int2)
plt.show()

