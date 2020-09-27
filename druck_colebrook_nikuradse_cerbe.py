import numpy as np
import matplotlib.pyplot as plt
 

N = 14
ind = np.arange(N)


#druck, k = 1mm, colebrook
c = ([0.03      , 0.02920267, 0.02843769, 0.02763188, 0.02693667,
       0.02583932, 0.02632696, 0.02675017, 0.02728135, 0.02811711,
       0.02651619, 0.02594978, 0.02541469, 0.02510343])

#druck, k = 1mm, nikuradse 
n = ([0.03      , 0.02921187, 0.02846024, 0.02767175, 0.02699407,
       0.02590494, 0.02638857, 0.02680701, 0.02732855, 0.02814549,
       0.02657226, 0.02601814, 0.02548595, 0.0251874 ])

#cerbe
m = [0.030000, 0.02935, 0.0287, 0.02801, 0.02741, 0.02648, 0.0269, 0.02726, 0.02771, 0.02843, 0.02707, 0.02658, 0.02611, 0.02585]
ax = plt.subplot(111)

rects1 = ax.bar(ind-0.2, c, width=0.2, color='b', align='center')
rects2 = ax.bar(ind, n, width=0.2, color='g', align='center')
rects3 = ax.bar(ind+0.2, m, width=0.2, color='r', align='center')
labels = ('K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8', 'K9', 'K10', 'K11', 'K12', 'K13', 'K14')

plt.xticks(np.arange(15), labels, rotation=45)
plt.autoscale(tight=True)


plt.xlabel('Knoten')
plt.ylabel('Druck/bar')
#plt.tilte('Druckwerte')

plt.legend( (rects1[0], rects2[0], rects3[0]), ('Colebrook', 'Nikuradse', 'Cerbe'), bbox_to_anchor=(1.5, 1), loc='upper right' )

plt.show()