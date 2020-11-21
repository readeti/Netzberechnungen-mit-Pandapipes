import numpy as np
import matplotlib.pyplot as plt
 

N = 15
ind = np.arange(N)

# Use "net.res_pipe["vdot_norm_m3_per_s"].values" in 14_Knotennetz.py 
# p=1.013bar, k=1mm, default, T = 273.15K
a = np.array([0.65400849, 0.22708987, 0.17256768, 0.13789518, 0.06045132,
       0.40139759, 0.17324562, 0.10377172, 0.04383598, 0.05617634,
       0.2251874 , 0.16679839, 0.04177115, 0.0889369 , 0.03595197])

# multiply each element of the array with 3600 to get from s to h.
v1 = a * 3600

# p=1.013bar, k=0.01mm, default, T = 273.15K
b = np.array([0.65400849, 0.2269878 , 0.17246561, 0.1377931 , 0.06045132,
       0.40149967, 0.17303437, 0.10356047, 0.04362473, 0.05607426,
       0.22550074, 0.16711173, 0.04208448, 0.0889369 , 0.03563864])


# multiply each element of the array with 3600 to get from s to h.
v2 = b * 3600


# error deviation
f = np.subtract(v1,v2)
print (f)


# plotting
ax = plt.subplot(111)

labels = ('K_1-2', 'K_2-3', 'K_3-4', 'K_4-5', 'K_5-6', 'K_2-10', 'K_10-9', 'K_9-8', 'K_8-7', 'K_5-7', 'K_10-11', 'K_11-12', 'K_12-13', 'K_12-14', 'K_7-13')
plt.xticks(np.arange(15), labels, rotation=45)
plt.autoscale(tight=True)

rects1 = ax.bar(ind-0.2, v1, width=0.2, color='b', align='center')
rects2 = ax.bar(ind, v2, width=0.2, color='g', align='center')
rects3 = ax.bar(ind+0.2, f, width=0.2, color='m', align='center')

plt.xlabel('Leitungen')
plt.ylabel('Volumenstrom m^3/h')
ax.legend( (rects1[0], rects2[0], rects3[0]), ('k = 1mm', 'k = 0.01mm ', 'Fehlerabweichung'), bbox_to_anchor=(1.5, 1), loc='upper right' )
plt.show()


