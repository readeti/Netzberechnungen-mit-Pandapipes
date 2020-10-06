import numpy as np
import matplotlib.pyplot as plt
 

N = 15
ind = np.arange(N)



"""
#t_20
a = np.array([0.70225176, 0.24382128, 0.18527723, 0.14804709, 0.06491054,
       0.43102689, 0.186014  , 0.11141532, 0.04705839, 0.06030022,
       0.24182964, 0.17913353, 0.04488359, 0.09549738, 0.03857282])

print (a * 3600)

#t_0
b = np.array([0.65400849, 0.22708987, 0.17256768, 0.13789518, 0.06045132,
       0.40139759, 0.17324562, 0.10377172, 0.04383598, 0.05617634,
       0.2251874 , 0.16679839, 0.04177115, 0.0889369 , 0.03595197])

print (b*3600)
"""


t_20 = ([2528.106336,  877.756608,  666.998028,  532.969524,  233.677944, 1551.696804,
  669.6504,    401.095152,  169.410204,  217.080792,  870.586704,  644.880708,
  161.580924,  343.790568,  138.862152])

t_0 = ([2354.430564,  817.523532,  621.243648,  496.422648, 217.624752, 1445.031324,
  623.684232,  373.578192,  157.809528, 202.234824,  810.67464,   600.474204,
  150.37614,   320.17284,   129.427092])

#np.subtract(t_20,t_0)

f = ([173.675772,  60.233076,  45.75438 ,  36.546876,  16.053192,
       106.66548 ,  45.966168,  27.51696 ,  11.600676,  14.845968,
        59.912064,  44.406504,  11.204784,  23.617728,   9.43506 ])

labels = ('K_1-2', 'K_2-3', 'K_3-4', 'K_4-5', 'K_5-6', 'K_2-10', 'K_10-9', 'K_9-8', 'K_8-7', 'K_5-7', 'K_10-11', 'K_11-12', 'K_12-13', 'K_12-14', 'K_7-13')

plt.xticks(np.arange(15), labels, rotation=45)
ax = plt.subplot(111)
plt.autoscale(tight=True)

rects1 = ax.bar(ind-0.2, t_20, width=0.2, color='b', align='center')
rects2 = ax.bar(ind, t_0, width=0.2, color='g', align='center')
rects3 = ax.bar(ind+0.2, f, width=0.2, color='m', align='center')

ax.legend( (rects1[0], rects2[0], rects3[0]), ('t_20', 't_0', 'Fehlerabweichung') )
plt.show()