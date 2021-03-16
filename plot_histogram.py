import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import Rectangle

y=np.loadtxt("on_pulse",unpack=True)
x=np.loadtxt("off_pulse",unpack=True)

plt.hist(x,histtype='stepfilled',alpha=0.3,normed=True,bins=20)
plt.hist(y,histtype='stepfilled',alpha=0.3,normed=True,bins=20)

plt.xlabel("$\mathrm{E}$/$\hat{E}$")
plt.ylabel("Counts")

labels= ["Off pulse","On pulse"]
plt.legend(labels)
#plt.legend(handles, labels)
plt.show()

