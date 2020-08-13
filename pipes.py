import numpy as np
import matplotlib.pyplot as plt
 

N = 15
ind = np.arange(N)
#vdot_norm_m^3_per_h  (p=1.013bar    k=1mm)
array1 = ([2354.43055236,  817.52353523,  621.24365276,  496.42264003,
        217.62473966, 1445.03132746,  623.68424591,  373.57820182,
        157.80953669,  202.23482565,  810.67465295,  600.47421144,
        150.37613581,  320.17285793,  129.42710091])
#mdot_from_m^3_per_h  (p=1.013bar    k=1mm)
array2 = ([2174.57142857,  755.07146308,  573.7857488 ,  458.50003451,
        201.        , 1334.64282263,  576.03990071,  345.03990071,
        145.75418642,  186.7857488 ,  748.74577906,  554.60292192,
        138.88863621,  295.71428571,  119.53993522])

k = array1
m = array2

#cerbe Volumenstrom
l = [2206, 765.7, 581.7, 464.7, 204.0, 1354.3, 584.3, 350.2, 148.2, 188.7, 760.1, 563.1, 141.1, 300, 120.9] 


labels = ('K_1-2', 'K_2-3', 'K_3-4', 'K_4-5', 'K_5-6', 'K_2-10', 'K_10-9', 'K_9-8', 'K_8-7', 'K_5-7', 'K_10-11', 'K_11-12', 'K_12-13', 'K_12-14', 'K_7-13')
plt.xticks(np.arange(15), labels, rotation=45)
ax = plt.subplot(111)
plt.autoscale(tight=True)

rects1 = ax.bar(ind-0.2, k, width=0.2, color='b', align='center')
rects2 = ax.bar(ind, l, width=0.2, color='g', align='center')
rects3 = ax.bar(ind+0.2, m, width=0.2, color='r', align='center')



ax.legend( (rects1[0], rects2[0], rects3[0]), ('vdot_norm_m^3_per_h', 'Volumenstrom(Cerbe)', 'mdot_from_m^3_per_h') )
plt.show()