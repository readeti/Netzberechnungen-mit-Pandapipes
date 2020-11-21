import numpy as np
import matplotlib.pyplot as plt
 

N = 14
ind = np.arange(N)

# Use "net.res_junction["p_bar"].values"
# values of pressure on each junction, k = 1mm, colebrook, T = 273.15K 
c = ([0.03      , 0.02923084, 0.02846588, 0.02766009, 0.0269649 ,
      0.02586758, 0.0263552 , 0.0267784 , 0.02730957, 0.02814531,
      0.02654443, 0.02597804, 0.02544297, 0.02513171])

# Use "net.res_junction["p_bar"].values"
# values of pressure on each junction, k = 1mm, default, T = 273.15K 
n = ([0.03      , 0.02923972, 0.0284881 , 0.02769964, 0.02702198,
      0.02593287, 0.02641649, 0.02683492, 0.02735644, 0.02817336,
      0.02660018, 0.02604607, 0.02551389, 0.02521535])

# values of pressure on each junction from Cerbe
m = [0.030000, 0.02935, 0.0287, 0.02801, 0.02741, 0.02648, 0.0269, 0.02726, 0.02771, 0.02843, 0.02707, 0.02658, 0.02611, 0.02585]

# plotting
ax = plt.subplot(111)

rects1 = ax.bar(ind-0.2, c, width=0.2, color='b', align='center')
rects2 = ax.bar(ind, n, width=0.2, color='g', align='center')
rects3 = ax.bar(ind+0.2, m, width=0.2, color='r', align='center')
labels = ('K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8', 'K9', 'K10', 'K11', 'K12', 'K13', 'K14')

plt.xticks(np.arange(15), labels, rotation=45)
plt.autoscale(tight=True)


plt.xlabel('Knoten')
plt.ylabel('Druck/bar')


plt.legend( (rects1[0], rects2[0], rects3[0]), ('Colebrook', 'Default', 'Cerbe'), bbox_to_anchor=(1.5, 1), loc='upper right' )

plt.show()