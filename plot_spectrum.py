import numpy as np
import matplotlib.pyplot as plt


a,x,y,z=np.loadtxt("dsplot",unpack=True)

ds = z.reshape(98304/1024,1024)

#B=np.loadtxt("just_frequencies",unpack=True)
plt.imshow(ds,aspect='auto',extent=[0,3.9,1234.5,1516.5])

plt.show()



