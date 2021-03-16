from __future__ import division

import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
import math
import subprocess
import sys
#from __future__ import division






import glob
#lists=glob.glob("/u/aswin/sp_test_reatough/individuaal_archives/*.ar")


#df=pd.DataFrame()

i = sys.argv[1]
#df1=pd.DataFrame()
#df1=pd.DataFrame()
#df=pd.DataFrame()
#for i in lists:
command=['pdv','-jFD','-t',str(i)]
a=subprocess.Popen(command,stdout=subprocess.PIPE)
if sys.version_info[0]<3:

   from StringIO import StringIO
else:
   from io import StringIO

B=StringIO(a.communicate()[0].decode('utf-8')) 

x = pd.read_csv(B,delim_whitespace=True)
x.columns = ['a', 'b', 'bin', 'energy', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']


#f=x["bin"]
#t=x["energy"]
#plt.plot(f,t)
#plt.show()


OFF_MEAN_SUB=x["energy"]-0.000321758873611
   #mean subtract
#total_each_pulse=OFF_MEAN_SUB.sum()    #not needed
#on_pulse_total=OFF_MEAN_SUB.iloc[36:41].sum()  #total on pulse energy in each window
  #mean of on pulse energy in each window  

OFF_PULSE=OFF_MEAN_SUB.iloc[0:35].sum()        #total off puls energy 1   
OFF_PULSE2=OFF_MEAN_SUB.iloc[42:77].sum()     #total off pulse energy 2

#A=OFF_MEAN_SUB.iloc[0:128]              #each off pulse value 1
#B=OFF_MEAN_SUB.iloc[137:255]            #each off pulse value 2
#total_off_pulse=pd.concat([A,B],ignore_index=True) # cocat both the sides of off pulse
#X=total_off_pulse.mean()                           #mean of off pulse region
TOTAL_OFF=OFF_PULSE+OFF_PULSE2                    # total off pulse energy
Norm_off_pulse=TOTAL_OFF/0.275588

           # normalized off pulse  enrgy for each window




   #normalized on pulse enrgy for each window
#print on_pulse_total/0.275588
print Norm_off_pulse
#print Norm_off_pulse
#print on_pulse_total/(-0.005987)

#Norm_on_energy=on_pulse_total/0.918925
#print Norm_on_energy
 



    
