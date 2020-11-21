import numpy as np
import matplotlib.pyplot as plt


N = 15
ind = np.arange(N)

# Use "net.res_pipe["p_from_bar"].values" in 14_Knotennetz.py, k=1mm
k = ([0.03      , 0.02923972, 0.0284881 , 0.02769964, 0.02702198,
       0.02923972, 0.02817336, 0.02735644, 0.02683492, 0.02702198,
       0.02817336, 0.02660018, 0.02604607, 0.02604607, 0.02641649])

# Use "net.res_pipe["p_to_bar"].values" in 14_Knotennetz.py, k=1mm
l = ([0.02923972, 0.0284881 , 0.02769964, 0.02702198, 0.02593287,
       0.02817336, 0.02735644, 0.02683492, 0.02641649, 0.02641649,
       0.02660018, 0.02604607, 0.02551389, 0.02521535, 0.02551389])

# calculate difference
m =  [a - b for a,b in zip(k, l)]


# plotting
ax = plt.subplot(111)

rects1 = ax.bar(ind-0.2, k, width=0.2, color='b', align='center')
rects2 = ax.bar(ind, l, width=0.2, color='g', align='center')
rects3 = ax.bar(ind+0.2, m, width=0.2, color='r', align='center')
labels = ('K_1-2', 'K_2-3', 'K_3-4', 'K_4-5', 'K_5-6', 'K_2-10', 
          'K_10-9', 'K_9-8', 'K_8-7', 'K_5-7', 'K_10-11', 'K_11-12', 
          'K_12-13', 'K_12-14', 'K_7-13')
plt.xticks(np.arange(15), labels, rotation=45)

plt.autoscale(tight=True)


plt.xlabel('Leitungen')
plt.ylabel('Druck/bar')

ax.legend( (rects1[0], rects2[0], rects3[0]), 
          ('p_from_bar', 'p_to_bar', 'Differenz'), bbox_to_anchor=(1.5, 1), 
          loc='upper right' )

plt.show()
