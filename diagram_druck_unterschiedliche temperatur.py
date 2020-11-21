import numpy as np
import matplotlib.pyplot as plt

N = 15
ind = np.arange(N)

# values of p_from_bar from 14_Knotennetz.py for 4 different temperatures
# 293.15K, 288.15K, 281,15K, 273.15K

t_20 = ([0.03      , 0.0291232 , 0.02825569, 0.02734515, 0.02656214,
       0.0291232 , 0.02789261, 0.02694908, 0.02634643, 0.02656214,
       0.02789261, 0.02607566, 0.02543519, 0.02543519, 0.02586229])

t_15 = ([0.03      , 0.02915338, 0.02831591, 0.02743702, 0.02668133,
       0.02915338, 0.02796535, 0.02705465, 0.02647304, 0.02668133,
       0.02796535, 0.0262116 , 0.02559354, 0.02559354, 0.02600595])

t_8 = ([0.03      , 0.0291943 , 0.02839752, 0.02756151, 0.02684282,
       0.0291943 , 0.02806394, 0.02719771, 0.02664459, 0.02684282,
       0.02806394, 0.02639581, 0.02580807, 0.02580807, 0.02620059])

t_0 = ([0.03      , 0.02920267, 0.02843769, 0.02763188, 0.02693667,
       0.02920267, 0.02811711, 0.02728135, 0.02675017, 0.02693667,
       0.02811711, 0.02651619, 0.02594978, 0.02594978, 0.02632696])


# plotting
ax = plt.subplot(111)

rects1 = ax.bar(ind-0.2, t_20, width=0.2, color='b', align='center')
rects2 = ax.bar(ind, t_15, width=0.2, color='g', align='center')
rects3 = ax.bar(ind+0.2, t_8, width=0.2, color='r', align='center')
rects4 = ax.bar(ind+0.4, t_0, width=0.2, color='k', align='center')
labels = ('K_1-2', 'K_2-3', 'K_3-4', 'K_4-5', 'K_5-6', 'K_2-10', 
          'K_10-9', 'K_9-8', 'K_8-7', 'K_5-7', 'K_10-11', 'K_11-12', 
          'K_12-13', 'K_12-14', 'K_7-13')


plt.xticks(np.arange(15), labels, rotation=45)
plt.autoscale(tight=True)


plt.xlabel('Pipes')
plt.ylabel('Druck/bar')


plt.legend( (rects1[0], rects2[0], rects3[0], rects4[0]), 
           ('20 Grad C', '15 Grad C', '8 Grad C', '0 Grad C'), 
           bbox_to_anchor=(1.5, 1), loc='upper right' )

plt.show()