import math
import matplotlib.pyplot as plt
import numpy as np

#import matplotlib.axes.Axes.legend
#import matplotlib.pyplot.legend
#import matplotlib.axes.Axes.plot



tot_bandwidth= 288000000 #Mhz
#tot_bandwidth= #Mhz
channel_bandwidth= 3 #MHZ
observing_f= 1.34#Ghz
t_samp= 250 #micro seconds
w_int=  1000  #micro seconds
w_int1= 5000  #micro seconds
w_int2= 50000 #micro seconds
t_sys= 44 #Kelvin
t_rec= 21 #Kelvin
G= 0.69


DM=0
DM1=70
DM2=200
DM3=500
#w_int_seconds=w_int/10**6
#bandwidth= channel_bandwidth*10**6

aswin=[]

def sense_curves(x,DM,w_intrinsic_seconds):


    sm_list = []
    #max=[]
    scat = np.linspace(0,40,40)
    for i in range(len(scat)):

        t_sct=i*1000 #ms to micro seconds
        print t_sct
        t_chan=8.3*channel_bandwidth*DM*(1/observing_f)**3 #calculating t_channel in microseconds
        effects=(x)**2+(t_samp)**2+(t_chan)**2+(t_sct)**2  
        w_obs=math.sqrt(effects)                            #observed width
        w_seconds=w_obs/10**3 #second  #micro seconds to milli seconds
        print w_obs
        print w_seconds 
        #w_intrinsic_seconds=0.001 #seconds                  #micro seconds to seconds
        
        #d=w_seconds/w_intrinsic_seconds                     #observed_width/intrinsic width

        #smin=d*t_sys*6/G*(2*total_bandwidth*w_seconds)**(1/2)
        total_sky=t_sys+t_rec
        X=total_sky*6   #temp*snr
        Y=G*w_intrinsic_seconds
        N=2*tot_bandwidth
        Z=math.sqrt(w_seconds/N)
        smin=(X/Y)*Z
        #Y= G*(2*total_bandwidth*w_seconds)**(1/2)            #gain*n_pol*total_bandwidth*w_seconds
        #SMIN=X/Y                                             
        #smin=d*SMIN                                          # SMIN*observed_width/intrinsic width


        sm_list.append(smin)
    sm_list = np.asarray(sm_list)
    print t_chan
    print w_obs
    print w_seconds
    print w_intrinsic_seconds
    #print d

    #max.append(
    print max(sm_list)
    print sm_list
    return sm_list


sct = np.linspace(0,40,40)


fig,ax=plt.subplots()
A=5
#B=0.005

ax.plot(sct,sense_curves(w_int,DM,A),'k--',label='$DM=70 pc cm^-3$')
ax.plot(sct,sense_curves(w_int,DM2,A),'k:',label='$DM=200 pc cm^-3$') 
ax.plot(sct,sense_curves(w_int,DM3,A),'k:',label='$DM=500 pc cm ^-3$') 
#ax.plot(DM,sense_curves(w_int2),'k',label='wint=100ms')
#ax.set_yscale('log')
plt.xlabel("scattering time")
plt.ylabel("minimum flux density (jy)")
legend = ax.legend(loc='upper left', shadow=True, fontsize='x-large')
plt.show()

