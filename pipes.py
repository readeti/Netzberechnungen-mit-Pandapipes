import numpy as np
import matplotlib.pyplot as plt
 

N = 15
ind = np.arange(N)
# p=1.013bar, k=1mm. Use "net.res_pipe["vdot_norm_m3_per_s"].values in 
# 14_Knotennetz.py.
a = np.array([0.65400849, 0.22708987, 0.17256768, 0.13789518, 0.06045132, 
              0.40139759, 0.17324562, 0.10377172, 0.04383598, 0.05617634, 
              0.2251874 , 0.16679839, 0.04177115, 0.0889369 , 0.03595197])

# multiply with 3600 to get from s to h.
k = a * 3600


# p=1.013bar, k=1mm. Use net.res_pipe["mdot_norm_m3_per_s"].values in 
# 14_Knotennetz.py
m = ([2174.57142857,  755.07146308,  573.7857488 ,  458.50003451,
        201.        , 1334.64282263,  576.03990071,  345.03990071,
        145.75418642,  186.7857488 ,  748.74577906,  554.60292192,
        138.88863621,  295.71428571,  119.53993522])



# Volume flow from Cerbe.
l = [2206, 765.7, 581.7, 464.7, 204.0, 1354.3, 584.3, 350.2, 148.2, 188.7, 760.1, 563.1, 141.1, 300, 120.9] 

# plotting
ax = plt.subplot(111)

labels = ('K_1-2', 'K_2-3', 'K_3-4', 'K_4-5', 'K_5-6', 'K_2-10', 'K_10-9', 'K_9-8', 'K_8-7', 'K_5-7', 'K_10-11', 'K_11-12', 'K_12-13', 'K_12-14', 'K_7-13')
plt.xticks(np.arange(15), labels, rotation=45)
plt.autoscale(tight=True)

rects1 = ax.bar(ind-0.2, k, width=0.2, color='b', align='center')
rects2 = ax.bar(ind, l, width=0.2, color='g', align='center')
rects3 = ax.bar(ind+0.2, m, width=0.2, color='r', align='center')


plt.xlabel('Leitungen')
plt.ylabel('Druck/bar')
ax.legend( (rects1[0], rects2[0], rects3[0]), ('vdot_norm_m^3_per_h', 'Volumenstrom(Cerbe)', 'mdot_from_m^3_per_h'), bbox_to_anchor=(1.5, 1), loc='upper right' )

plt.show()