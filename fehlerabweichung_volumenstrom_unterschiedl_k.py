import numpy as np
import matplotlib.pyplot as plt
 

N = 15
ind = np.arange(N)

#k = 1mm, t = 273.93K

k1 = ([2354.430564,  817.523532,  621.243648,  496.422648, 217.624752, 1445.031324,
  623.684232,  373.578192,  157.809528, 202.234824,  810.67464,   600.474204,
  150.37614,   320.17284,   129.427092])

"""
to convert vdot_norm_m3_per_s to vdot_norm_m3_per_h
b = np.array([0.65400849, 0.2269878 , 0.17246561, 0.1377931 , 0.06045132,
       0.40149967, 0.17303437, 0.10356047, 0.04362473, 0.05607426,
       0.22550074, 0.16711173, 0.04208448, 0.0889369 , 0.03563864])

print (b*3600)
"""

k2 = ([2354.430564,  817.15608,   620.876196,  496.05516,   217.624752, 1445.398812,
  622.923732,  372.817692,  157.049028,  201.867336,  811.802664,  601.602228,
  151.504128,  320.17284,   128.299104])

np.subtract(k1,k2)

f = ([ 0.      ,  0.367452,  0.367452,  0.367488,  0.      , -0.367488,
        0.7605  ,  0.7605  ,  0.7605  ,  0.367488, -1.128024, -1.128024,
       -1.127988,  0.      ,  1.127988])
labels = ('K_1-2', 'K_2-3', 'K_3-4', 'K_4-5', 'K_5-6', 'K_2-10', 'K_10-9', 'K_9-8', 'K_8-7', 'K_5-7', 'K_10-11', 'K_11-12', 'K_12-13', 'K_12-14', 'K_7-13')

plt.xticks(np.arange(15), labels, rotation=45)
ax = plt.subplot(111)
plt.autoscale(tight=True)

rects1 = ax.bar(ind-0.2, k1, width=0.2, color='b', align='center')
rects2 = ax.bar(ind, k2, width=0.2, color='g', align='center')
rects3 = ax.bar(ind+0.2, f, width=0.2, color='m', align='center')

ax.legend( (rects1[0], rects2[0], rects3[0]), ('k = 1mm', 'k = 0.01mm ', 'Fehlerabweichung') )
plt.show()