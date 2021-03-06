import numpy as np
import matplotlib.pyplot as plt
 

N = 15
ind = np.arange(N)


# Use net.res_pipe["vdot_norm_m^3_per_s "].values in 14_Knotennetz.py
# p=1.013bar, k=1mm, colebrook, T= 273.15K
a = np.array([0.65400849, 0.2270723 , 0.17255011, 0.13787761, 0.06045132,
       0.40141516, 0.17331909, 0.10384519, 0.04390945, 0.05615877,
       0.22513151, 0.1667425 , 0.04171526, 0.0889369 , 0.03600786])

# convert s to h
c = a * 3600


# Use net.res_pipe["vdot_norm_m^3_per_s "].values in 14_Knotennetz.py
# p=1.013bar, k=1mm, default, T= 273.15K
b = np.array([0.65400849, 0.22708987, 0.17256768, 0.13789518, 0.06045132,
       0.40139759, 0.17324562, 0.10377172, 0.04383598, 0.05617634,
       0.2251874 , 0.16679839, 0.04177115, 0.0889369 , 0.03595197])

# convert s to h
d = b * 3600


#Values of volume flow from Cerbe
l = [2206, 765.7, 581.7, 464.7, 204.0, 1354.3, 584.3, 350.2, 148.2, 188.7, 
     760.1, 563.1, 141.1, 300, 120.9] 

# plotting
ax = plt.subplot(111)

labels = ('K_1-2', 'K_2-3', 'K_3-4', 'K_4-5', 'K_5-6', 'K_2-10', 'K_10-9', 
          'K_9-8', 'K_8-7', 'K_5-7', 'K_10-11', 'K_11-12', 'K_12-13', 
          'K_12-14', 'K_7-13')
plt.xticks(np.arange(15), labels, rotation=45)
plt.autoscale(tight=True)

rects1 = ax.bar(ind-0.2, c, width=0.2, color='b', align='center')
rects2 = ax.bar(ind, d, width=0.2, color='g', align='center')
rects3 = ax.bar(ind+0.2, l, width=0.2, color='r', align='center')
plt.xlabel('Pipes')
plt.ylabel('Volumenstrom m^3/h')

ax.legend( (rects1[0], rects2[0], rects3[0]), ('Colebrook', 'Default', 'Cerbe'), 
          bbox_to_anchor=(1.5, 1), loc='upper right' )
plt.show()
