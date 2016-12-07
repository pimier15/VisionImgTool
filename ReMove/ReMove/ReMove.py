import os
import glob
import numpy as np
import csv

a = [(1,2,3678.0),
     (1,2,3),
     (1,2,3)
    ]

anp = np.array(a)
b = anp[0] + anp[1] + anp[2]




with open(r'D:\ztest\test.csv', 'wb') as f:
     wr = csv.writer(f,delimiter=' ')
     wr.writerow(a)

