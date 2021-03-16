import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import subprocess
import sys

C=np.arange(63)
A="Candidate.pam"

for i in range(len(C)):
 #3trim value
        command=['pdv','-t','-n',str(i),str(A)]
        a=subprocess.Popen(command,stdout=subprocess.PIPE)
        if sys.version_info[0]<3:
           from StringIO import StringIO
        else:
           from io import StringIO
        B=StringIO(a.communicate()[0].decode('utf-8'))
        X=pd.read_csv(B,delim_whitespace=True)
        X.columns=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
        
        c=X['c'].values #bin values
        d=X['d'].values #intensity values
        
        max_d=max(d)
        max_c=c[d.argmax()]
        print i,max_c,max_d


        


