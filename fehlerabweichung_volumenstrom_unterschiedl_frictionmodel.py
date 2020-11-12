import numpy as np
import matplotlib.pyplot as plt
 

N = 15
ind = np.arange(N)


"""
a = np.array([0.67809223, 0.22707231, 0.17255012, 0.13787762, 0.06045132,
       0.40141515, 0.17331909, 0.10384519, 0.04390945, 0.05615878,
       0.2251315 , 0.16674249, 0.04171525, 0.0889369 , 0.03600788])


print (a * 3600)

b = np.array([0.67809223, 0.22708987, 0.17256768, 0.13789518, 0.06045132,
       0.40139759, 0.17324562, 0.10377172, 0.04383598, 0.05617634,
       0.2251874 , 0.16679839, 0.04177115, 0.0889369 , 0.03595197])

print (b*3600)
"""

#vdot_norm_m^3_per_h  (p=1.013bar    k=1mm) colebrook
c = ([2441.132028,  817.460316,  621.180432,  496.359432,  217.624752, 1445.09454,
  623.948724,  373.842684,  158.07402,   202.171608,  810.4734,    600.272964,
  150.1749,    320.17284,   129.628368])


#vdot_norm_m^3_per_h  (p=1.013bar    k=1mm) nikuradse
n = ([2441.132028,  817.523532,  621.243648,  496.422648,  217.624752, 1445.031324,
           623.684232,  373.578192,  157.809528,  202.234824,  810.67464,   600.474204,
           150.37614,   320.17284,   129.427092])

#np.subtract(c,n)
f = ([ 0.      ,  0.063216,  0.063216,  0.063216,  0.      , -0.063216,
       -0.264492, -0.264492, -0.264492,  0.063216,  0.20124 ,  0.20124 ,
        0.20124 ,  0.      , -0.201276])

labels = ('K_1-2', 'K_2-3', 'K_3-4', 'K_4-5', 'K_5-6', 'K_2-10', 'K_10-9', 'K_9-8', 'K_8-7', 'K_5-7', 'K_10-11', 'K_11-12', 'K_12-13', 'K_12-14', 'K_7-13')

plt.xticks(np.arange(15), labels, rotation=45)
ax = plt.subplot(111)
plt.autoscale(tight=True)

rects1 = ax.bar(ind-0.2, c, width=0.2, color='b', align='center')
rects2 = ax.bar(ind, n, width=0.2, color='g', align='center')
rects3 = ax.bar(ind+0.2, f, width=0.2, color='m', align='center')

plt.xlabel('Leitungen')
plt.ylabel('Volumenstrom m^3/h')

ax.legend( (rects1[0], rects2[0], rects3[0]), ('Colebrook', 'Nikuradse', 'Fehlerabweichung'), bbox_to_anchor=(1.5, 1), loc='upper right'  )
plt.show()
