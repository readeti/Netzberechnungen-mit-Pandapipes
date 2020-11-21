import numpy as np
import matplotlib.pyplot as plt
 

N = 14
ind = np.arange(N)

# values from "druck_colebrook_default_cerbe.py"
# pressure, k = 1mm, colebrook
c = ([0.03      , 0.02923084, 0.02846588, 0.02766009, 0.0269649 ,
      0.02586758, 0.0263552 , 0.0267784 , 0.02730957, 0.02814531,
      0.02654443, 0.02597804, 0.02544297, 0.02513171])

# pressure, k = 1mm, default
n = ([0.03      , 0.02923972, 0.0284881 , 0.02769964, 0.02702198,
      0.02593287, 0.02641649, 0.02683492, 0.02735644, 0.02817336,
      0.02660018, 0.02604607, 0.02551389, 0.02521535])

# error deviation
f =  [a - b for a,b in zip(c,n)]

# plotting        
ax = plt.subplot(111)

rects1 = ax.bar(ind-0.2, c, width=0.2, color='b', align='center')
rects2 = ax.bar(ind, n, width=0.2, color='g', align='center')
rects3 = ax.bar(ind+0.2, f, width=0.2, color='r', align='center')

labels = ('K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8', 'K9', 'K10', 'K11', 'K12', 'K13', 'K14')

plt.xticks(np.arange(15), labels, rotation=45)
plt.autoscale(tight=True)


plt.xlabel('Knoten')
plt.ylabel('Druck/bar')


plt.legend( (rects1[0], rects2[0], rects3[0]), ('Colebrook', 'Default', 'Fehlerabweichung'), bbox_to_anchor=(1.5, 1), loc='upper right' )

plt.show()