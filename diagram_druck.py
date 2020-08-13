import numpy as np
import matplotlib.pyplot as plt


N = 14
ind = np.arange(N)

#p=1.05bar /1.013bar   k=1mm
k = [0.030000, 0.029240, 0.028488, 0.027700, 0.027022, 0.025933, 0.026416, 0.026835, 0.027356, 0.028173, 0.02660, 0.026046, 0.025514, 0.025215]
#p=1.013bar        k=0.01mm
l = [0.030000, 0.029717, 0.029436, 0.029138, 0.028878, 0.028477, 0.028654, 0.028812, 0.029007, 0.029315, 0.028726, 0.028515, 0.028309, 0.028200]  
#cerbe
m = [0.030000, 0.02935, 0.0287, 0.02801, 0.02741, 0.02648, 0.0269, 0.02726, 0.02771, 0.02843, 0.02707, 0.02658, 0.02611, 0.02585]
ax = plt.subplot(111)

rects1 = ax.bar(ind-0.2, k, width=0.2, color='b', align='center')
rects2 = ax.bar(ind, l, width=0.2, color='g', align='center')
rects3 = ax.bar(ind+0.2, m, width=0.2, color='r', align='center')
labels = ('K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8', 'K9', 'K10', 'K11', 'K12', 'K13', 'K14')

plt.xticks(np.arange(15), labels, rotation=45)
plt.autoscale(tight=True)


plt.xlabel('Knoten')
plt.ylabel('Druck/bar')
#plt.tilte('Druckwerte')

plt.legend( (rects1[0], rects2[0], rects3[0]), ('k = 1mm', 'k = 0.01mm', 'Cerbe'), bbox_to_anchor=(1.5, 1), loc='upper right' )

plt.show()