import numpy as np
import matplotlib.pyplot as plt
 

N = 14
ind = np.arange(N)


# Use net.res_junction["p_bar"].values
# Values of pressure on each junction at T = 293.13K
t_20 = ([0.03      , 0.0291232 , 0.02825569, 0.02734515, 0.02656214,
       0.0253027 , 0.02586229, 0.02634643, 0.02694908, 0.02789261,
       0.02607566, 0.02543519, 0.02481815, 0.02447446])

# Values of pressure on each junction at T = 273.13K
t_0 = ([0.03      , 0.02923972, 0.0284881 , 0.02769964, 0.02702198,
       0.02593287, 0.02641649, 0.02683492, 0.02735644, 0.02817336,
       0.02660018, 0.02604607, 0.02551389, 0.02521535])


# error deviation
f =  [a - b for a,b in zip(t_20,t_0)]

# plotting
ax = plt.subplot(111)

rects1 = ax.bar(ind-0.2, t_20, width=0.2, color='b', align='center')
rects2 = ax.bar(ind, t_0, width=0.2, color='g', align='center')
rects3 = ax.bar(ind+0.2, f, width=0.2, color='r', align='center')

labels = ('K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8', 'K9', 'K10', 
          'K11', 'K12', 'K13', 'K14')

plt.xticks(np.arange(15), labels, rotation=45)
plt.autoscale(tight=True)


plt.xlabel('Knoten')
plt.ylabel('Druck/bar')

plt.legend( (rects1[0], rects2[0], rects3[0]), 
           ('t_20', 't_0', 'Fehlerabweichung'), 
           bbox_to_anchor=(1.5, 1), loc='upper right' )

plt.show()