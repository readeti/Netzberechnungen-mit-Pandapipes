import numpy as np
import matplotlib.pyplot as plt


N = 14
ind = np.arange(N)
# Values of pressure on each junction. Use net.res_junction["p_bar"].values 
# to get the arrays

# same values for p = 1.05bar and p = 1.013bar, k = 1mm
k = ([0.03      , 0.02923972, 0.0284881 , 0.02769964, 0.02702198,
       0.02593287, 0.02641649, 0.02683492, 0.02735644, 0.02817336,
       0.02660018, 0.02604607, 0.02551389, 0.02521535])

# p = 1.013bar, k = 0.01mm
l = ([0.03      , 0.02971716, 0.02943635, 0.02913784, 0.0288778 ,
       0.0284774 , 0.02865446, 0.02881187, 0.02900669, 0.02931546,
       0.02872593, 0.02851496, 0.02830922, 0.02820003])


# values from Cerbe
m = [0.030000, 0.02935, 0.0287, 0.02801, 0.02741, 0.02648, 0.0269, 0.02726,
     0.02771, 0.02843, 0.02707, 0.02658, 0.02611, 0.02585]

# plotting
ax = plt.subplot(111)

rects1 = ax.bar(ind-0.2, k, width=0.2, color='b', align='center')
rects2 = ax.bar(ind, l, width=0.2, color='g', align='center')
rects3 = ax.bar(ind+0.2, m, width=0.2, color='r', align='center')

labels = ('K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8', 'K9', 'K10', 'K11', 
          'K12', 'K13', 'K14')

plt.xticks(np.arange(15), labels, rotation=45)
plt.autoscale(tight=True)


plt.xlabel('Knoten')
plt.ylabel('Druck/bar')


plt.legend( (rects1[0], rects2[0], rects3[0]),
           ('k = 1mm', 'k = 0.01mm', 'Cerbe'),
           bbox_to_anchor=(1.5, 1), loc='upper right' )

plt.show()