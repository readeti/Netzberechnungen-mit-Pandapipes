import numpy as np
import matplotlib.pyplot as plt
 

N = 15
ind = np.arange(N)

#vdot m^3/h (p=1.013bar    k=1mm)
k = [2354.42, 817.524, 621.2448, 496.422, 217.6236, 1445.0328, 623.6856, 373.5792, 157.8096, 202.2336, 810.6732, 600.4728, 150.3756, 320.1732, 129.4272]
#cerbe Volumenstrom
l = [2206, 765.7, 581.7, 464.7, 204.0, 1354.3, 584.3, 350.2, 148.2, 188.7, 760.1, 563.1, 141.1, 300, 120.9] 
#mdot to m^3/h  (p=1.013bar    k=1mm)
m = [1514.28456, 765.089, 581.3978, 464.58, 203.667, 1352.353679, 583.682, 349.61, 147.6868, 189.2627, 758.679, 561.960, 140, 299.638, 121.127]

labels = ('K_1-2', 'K_2-3', 'K_3-4', 'K_4-5', 'K_5-6', 'K_2-10', 'K_10-9', 'K_9-8', 'K_8-7', 'K_5-7', 'K_10-11', 'K_11-12', 'K_12-13', 'K_12-14', 'K_7-13')
plt.xticks(np.arange(15), labels, rotation=45)
ax = plt.subplot(111)
plt.autoscale(tight=True)

rects1 = ax.bar(ind-0.2, k, width=0.2, color='b', align='center')
rects2 = ax.bar(ind, l, width=0.2, color='g', align='center')
rects3 = ax.bar(ind+0.2, m, width=0.2, color='r', align='center')



ax.legend( (rects1[0], rects2[0], rects3[0]), ('vdot_m^3/h', 'Volumenstrom(Cerbe)', 'mdot_to_m^3/h ') )
plt.show()