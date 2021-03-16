import matplotlib.pyplot as plt
#import scipy.optimize as opt
import numpy as np
import pandas as pd
#DM=372


#LOFREQ=1250
#X=pd.read_csv("output.txt",delim_whitespace=True,header=None)
#X.columns=["a","channels","bins","intensity"]
#A=X[(X["intensity"]>=0.9)]
#bINS=A["bins"]
#channels=A["channels"]

#plt.plot(bINS,channels,"ko")
#************************************************nspace(3000,4096,num=len(bla))
#spectra=pd.read_csv("curve2",delim_whitespace=True)
#spectra.columns=['a','b','c','d']
#A=spectra[(spectra['b'].between(18,60)) & (spectra['c'].between(260,400,inclusive=False))]
#B=spectra[(spectra['b'].between(60,80)) & (spectra['c'].between(390,500,inclusive=False))]
#C=spectra[(spectra['b'].between(80,100)) & (spectra['c'].between(500,600,inclusive=False))]
#combine=pd.concat([A,B,C],ignore_index=True)

#cx=spectra["c"]
#cb=spectra["b"]
#***********************************************#



#plt.plot(cx,cb,"ko")

def dispdelay(DM,LOFREQ,HIFREQ):
    dconst = 4.15e+06
    delay = DM * dconst * (1.0 / LOFREQ**2 - 1.0 / HIFREQ**2) # in ms
    delay2= delay/1000
    return delay


hif=1516.5

bla=np.zeros(96)
fbots = np.zeros(96)
bw = 3
DM= 372
for i in range(len(bla)):
    fbot=hif-i*bw
    fbots[i] = fbot
    print fbot
    a,b,c=DM,fbot,hif
    bla[i] += dispdelay(a,b,c)
    #print bla[i]

y = np.linspace(0,96,num=len(bla))


#bla /= 250/1000000

bla +=0

print bla
bla2=bla-80
plt.plot(bla,y,'w',linewidth=2.0)
plt.plot(bla2,y,'w',linewidth=2.0)    


a,x,y,z=np.loadtxt("dsplot",unpack=True)

#plt.scatter(y/1024,x*3 + 1234.5,color=z)
#plt.gray()


ds = z.reshape(98304/1024,1024)


plt.ylabel("frequency channels")
plt.xlabel("Time bins")


#plt.xlim(50,396.65619307) #plt.ylim(1234.5,1516.5)

plt.imshow(ds,aspect='auto',cmap='gray')
#, extent = [50,396.65619307,1234.5,1516.5])
plt.show()






  
