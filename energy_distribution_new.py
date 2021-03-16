import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import subprocess
import sys

mean_int_on= 0.015384
mean_int_off=0.000357*5




import glob
lists=glob.glob("/u/aswin/sp_test_reatough/individuaal_archives/new/*.ar")


#df=pd.DataFrame()


#df1=pd.DataFrame()
print "ttt"
#def integrated():
   # df1=pd.DataFrame()
    #df=pd.DataFrame()
for i in lists:
 #3trim value
    command=['pdv','-jD','-t',str(i)]
    a=subprocess.Popen(command,stdout=subprocess.PIPE)
    if sys.version_info[0]<3:
       from StringIO import StringIO
    else:
       from io import StringIO
       B=StringIO(a.communicate()[0].decode('utf-8')) 
       
    #command="pdv -jD -t"+" "+str(i)+" "+">>"+" "+ str(i)+".txt"
    #subprocess.check_output(command,shell=True)   #os.commands
       x = pd.read_csv(B,delim_whitespace=True)
       x.columns = ['a', 'b', 'bin', 'energy', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
        #on_pulse = x[x.energy> mean_int_off]
        #off_pulse = x[x.energy<0.001175]
       OFF_MEAN_SUB=x["energy"]-0.004424
        
       on_pulse_total=OFF_MEAN_SUB.iloc[375:420].sum()
       print on_pulse_total
        #total_on_pulse=on_pulse.sum(axis = 1, skipna = True)
       #on_pulse_mean=on_pulse['energy'].mean()
        #mean_on_pulse = on_pulse[['energy']].mean(axis=0)
       #mean=x['energy'].mean()
        #mean_off_pulse = off_pulse[['energy']].mean(axis=0)
    
       #on_pulse_val = on_pulse/on_pulse_mean
    
        #off_pulse_val = mean_off_pulse/0.000357

        #print on_pulse_val 
         
        #data=pd.DataFrame({"off":off_pulse_val})
        #data1=pd.DataFrame({"on":[on_pulse_val]})
        #df=df.append(data)
       # df1=df1.append(data1)
   
     
        #return on_pulse_val


       
#a=integrated()    
#print a
#np.savetxt(r'/u/aswin/sp_test_reatough/individuaal_archives/off_pulse.txt', df.values, fmt='%d')   
#np.savetxt(r'/u/aswin/sp_test_reatough/individuaal_archives/on_pulse.txt', df1.values, fmt='%d')       



     
