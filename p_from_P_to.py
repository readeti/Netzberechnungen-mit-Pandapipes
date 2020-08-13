import numpy as np
import matplotlib.pyplot as plt




N = 15
ind = np.arange(N)
#p_from_bar k=1mm
array1 = ([0.03      , 0.02923972, 0.0284881 , 0.02769964, 0.02702198,
       0.02923972, 0.02817336, 0.02735644, 0.02683492, 0.02702198,
       0.02817336, 0.02660018, 0.02604607, 0.02604607, 0.02641649])
#p_to_bar k=1mm
array2 = ([0.02923972, 0.0284881 , 0.02769964, 0.02702198, 0.02593287,
       0.02817336, 0.02735644, 0.02683492, 0.02641649, 0.02641649,
       0.02660018, 0.02604607, 0.02551389, 0.02521535, 0.02551389])
#differenz
array3 = ([0.00076028, 0.00075162, 0.00078846, 0.00067766, 0.00108911,
       0.00106636, 0.00081691, 0.00052153, 0.00041843, 0.00060548,
       0.00157318, 0.00055411, 0.00053218, 0.00083072, 0.0009026 ])


k = array1
l = array2
m = array3

ax = plt.subplot(111)

rects1 = ax.bar(ind-0.2, k, width=0.2, color='b', align='center')
rects2 = ax.bar(ind, l, width=0.2, color='g', align='center')
rects3 = ax.bar(ind+0.2, m, width=0.2, color='r', align='center')
labels = ('K_1-2', 'K_2-3', 'K_3-4', 'K_4-5', 'K_5-6', 'K_2-10', 'K_10-9', 'K_9-8', 'K_8-7', 'K_5-7', 'K_10-11', 'K_11-12', 'K_12-13', 'K_12-14', 'K_7-13')
plt.xticks(np.arange(15), labels, rotation=45)
ax = plt.subplot(111)
plt.autoscale(tight=True)


plt.xlabel('Knoten')
plt.ylabel('Druck/bar')

ax.legend( (rects1[0], rects2[0], rects3[0]), ('p_from_bar', 'p_to_bar', 'Differenz'), bbox_to_anchor=(1.5, 1), loc='upper right' )

plt.show()
