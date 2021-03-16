import numpy as np
import matplotlib.pyplot as plt



def dispdelay(DM,LOFREQ,HIFREQ):
    dconst = 4.15e+06
    delay = DM * dconst * (1.0 / LOFREQ**2 - 1.0 / HIFREQ**2) # in ms
    return delay

# curves
hif = 1520
bla = 96
for i in range(len(bla)):
    fbot = hif - i * 3
    bla[i] += dispdelay(opts.DM,fbot,hif)
bla /= opts.samptime
bla += 385 # trying to adjust where the curve starts
bla2 = bla - 50 # the curve on the other side of the signal
y = np.linspace(1520,1250,num=len(bla))
plt.plot(bla,y,'k')
plt.plot(bla2,y,'k')

