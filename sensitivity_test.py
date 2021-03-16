#!/usr/bin/env python
import math
import matplotlib.pyplot as plt
import numpy as np

#import matplotlib.axes.Axes.legend
#import matplotlib.pyplot.legend
#import matplotlib.axes.Axes.plot

t_sys= 23 #Kelvin
t_sky=14 
G=0.69
t_samp=250
#DDplan2 
#total_bandwidth= 75000000 #MHZ
#channel_bandwidth= 0.024 #MHZ
#observing_f= 0.35 #Ghz
#t_samp= 81.92  #micro seconds
#w_int_seconds=w_int/10**6
#bandwidth= channel_bandwidth*10**6

Aswin=[]
#DM = 786
DM=np.linspace(0,3000,3000)
def sense_curves(x,w_intrinsic_seconds,total_bandwidth,channel_bandwidth,observing_f):
    
    total_sky=t_sys+t_sky    
    sm_list = []
    #max=[]
#    DM = np.linspace(0,3000,3000)
    for dm in range(len(DM)):
        print "****************"
        print "DM: " + str(dm)
        t_chan=8.3*channel_bandwidth*dm*(1/observing_f)**3
        print "t_chan :{}".format(t_chan)
        effects=(x)**2+(t_samp)**2+(t_chan)**2  
        print "effects: ", str(effects)
        w_obs=math.sqrt(effects)
        print "w_obs:{}".format(w_obs)

        w_seconds=w_obs/10**6   #micro seconds to milli seconds
        print "w_milliseconds:{}".format(w_seconds)

        d=w_seconds/w_intrinsic_seconds 
        ds=d/1000
        print "d:{}".format(d) 

        X=total_sky*6  #temp*snr
        #Y=G*w_intrinsic_seconds
       # N=2*100
        #Z=math.sqrt(w_seconds/N)
        B=G*(2*total_bandwidth*w_seconds)**0.5
        smin=d*(X/B)
        #smin=(X/Y)*Z
        print "smin:{}".format(smin)

        #smin=d*t_sys*6/G*(2*total_bandwidth*w_seconds)**(1/2)

        sm_list.append(smin)
    sm_list = np.asarray(sm_list)
    
    #max.append(
    #print max(sm_list)
    print sm_list
    return sm_list 
  
  

#DM = np.linspace(0,3000,3000)

    
fig,ax=plt.subplots() 
#w_int=  1000 #micro seconds
#ax.plot(DM,sense_curves(w_int,1),'g-',label='1ms',linewidth=2)
w_int=  5000 #microseconds
total_bandwidth=576000000 #hz
channel_bandwidth=3 #mhz
observing_f=1.518 #Ghz
ax.plot(DM,sense_curves(w_int,0.005,576000000,3,1.518),'k-',label='DDplan1',linewidth=2)
#w_int=1000 #microseconds
#ax.plot(DM,sense_curves(w_int,0.001,576000000,3,1.518),'k--',label='DDplan1(1ms)',linewidth=2)

#*************************************#
w_int= 5000 #micro seconds
total_bandwidth=768000000 #hz
channel_bandwidth=3 #mhz
observing_f=1.39 #Ghz
ax.plot(DM,sense_curves(w_int,0.005,768000000,3,3.0),'b-',label='DDplan7',linewidth=2)
#w_int=1000 #microseconds
#ax.plot(DM,sense_curves(w_int,0.001,768000000,3,1.39),'b--',label='DDplan7(1ms)',linewidth=2)

#*******************************************#
w_int= 5000 #microseconds
total_bandwidth=288000000 #hz
channel_bandwidth=3 #mhz
observing_f=1.374 #Ghz
ax.plot(DM,sense_curves(w_int,0.005,total_bandwidth,channel_bandwidth,observing_f),'r-',label='DDplan5',linewidth=2)

############################################
w_int= 5000 #microseconds
total_bandwidth=576000000 #hz
channel_bandwidth=3 #mhz
observing_f=6.412 #Ghz

ax.plot(DM,sense_curves(w_int,0.005,total_bandwidth,channel_bandwidth,observing_f),'g-',label='DDplan11',linewidth=2)


plt.xlabel("Dispersion measure ($pc\ cm^{-3}$)")
plt.ylabel("minimum flux density (Jy)")
legend = ax.legend(loc='upper left',fontsize='x-large')
#sense_curves(w_int)
#sense_curves(w_int1)
#sense_curves(w_int2)
plt.show()
