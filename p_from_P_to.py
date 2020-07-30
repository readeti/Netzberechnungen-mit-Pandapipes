import numpy as np
import matplotlib.pyplot as plt




N = 15
ind = np.arange(N)

#p from bar
k = [0.030000, 0.029240, 0.028488, 0.027700, 0.027022, 0.029240, 0.028173, 0.027356, 0.026835, 0.027022, 0.028173, 0.026600, 0.026046, 0.026046, 0.026416]
#p to bar
l = [0.029240, 0.028488, 0.027700, 0.027022, 0.025933, 0.028173, 0.027356, 0.026835, 0.026416, 0.026416, 0.026600, 0.026046, 0.025514, 0.025215, 0.025514] 
#differenz
m = [0.00076, 0.000752, 0.000788, -0.000022, 0.001089, 0.001067, 0.000817, 0.000521, 0.000419, 0.000606, 0.001573, 0.000554, 0.000532, 0.000831, 0.000902]
ax = plt.subplot(111)

rects1 = ax.bar(ind-0.2, k, width=0.2, color='b', align='center')
rects2 = ax.bar(ind, l, width=0.2, color='g', align='center')
rects3 = ax.bar(ind+0.2, m, width=0.2, color='r', align='center')
labels = ('K_1-2', 'K_2-3', 'K_3-4', 'K_4-5', 'K_5-6', 'K_2-10', 'K_10-9', 'K_9-8', 'K_8-7', 'K_5-7', 'K_10-11', 'K_11-12', 'K_12-13', 'K_12-14', 'K_7-13')
plt.xticks(np.arange(15), labels, rotation=45)
ax = plt.subplot(111)
plt.autoscale(tight=True)

#tick_label =  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'] 
#plt.bar(left, height, tick_label = tick_label, 
#       width = 0.8, color = ['red'])
#plt.xlabel('Knoten')
#plt.ylabel('Druck/Pa')
#plt.tilte('Druckwerte')
ax.legend( (rects1[0], rects2[0], rects3[0]), ('k', 'l', 'm') )
plt.show()