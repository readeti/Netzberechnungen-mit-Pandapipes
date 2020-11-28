import numpy as np
import matplotlib.pyplot as plt

N = 15
ind = np.arange(N)

# friction factor set as default. T = 273.15K
# calculated array using Darcy Equation. 
# Use "berechnung_darcyequation_default.py" to calculate the values.
ff_darcy = [0.026416933253916797, 0.028291471739288157, 0.02855229193736336, 
  0.028824061349036773, 0.033951055324030574, 0.026639866538837664, 
  0.028558540511912242, 0.0308046024639186, 0.03459766240948081, 
  0.0340714138511781, 0.028338968914380067, 0.028637245762492866, 
  0.03474551832477544, 0.031070976486403206, 0.03513481546691049]

# friction factor set as colebrook. T = 273.15K
# use : "net.res_pipe["lambda"].values" in 14_Knotennetz.py to get the values
ff_colebrook = ([0.02756982, 0.02968767, 0.03006514, 0.0304468 , 0.03517944,
       0.02794735, 0.03005829, 0.03223793, 0.03586593, 0.03532147,
       0.02969815, 0.03011881, 0.03599416, 0.03252755, 0.03639354])


# calculate difference
f_1 =  [a - b for a,b in zip(ff_colebrook, ff_darcy)]


# calculated array from 14_Knotennetz.py
# Use "net.res_pipe["lambda"].values" in 14_Knotennetz.py to get the values 
# below.
ff_default = ([0.02725176, 0.02916463, 0.02941218, 0.02967142, 0.03491798,
       0.02745721, 0.02940814, 0.03170111, 0.03558734, 0.03505237,
       0.02917125, 0.02944784, 0.03570773, 0.0319299 , 0.03612139])

# calculate difference
f_2 =  [c - d for c,d in zip(ff_default, ff_darcy)]


# plotting
ax = plt.subplot(111)

labels = ('K_1-2', 'K_2-3', 'K_3-4', 'K_4-5', 'K_5-6', 'K_2-10', 'K_10-9', 
          'K_9-8', 'K_8-7', 'K_5-7', 'K_10-11', 'K_11-12', 'K_12-13', 
          'K_12-14', 'K_7-13')
plt.xticks(np.arange(15), labels, rotation=45)
plt.autoscale(tight=True)

rects1 = ax.bar(ind-0.2, ff_darcy, width=0.2, color='g', align='center')
rects2 = ax.bar(ind, ff_colebrook, width=0.2, color='r', align='center')
rects3 = ax.bar(ind+0.2, ff_default, width=0.2, color='y', align='center')
rects4 = ax.bar(ind+0.4, f_1, width=0.2, color='b', align='center')
rects5 = ax.bar(ind+0.6, f_2, width=0.2, color='c', align='center')
plt.xlabel('Pipes')
plt.ylabel('Friction factor')

# show legend
ax.legend( (rects1[0], rects2[0], rects3[0], rects4[0], rects5[0]), 
          ('Darcy Equation', 'Colebrook', 'Default', 'Colebrook-Darcy', 
           'Default-Darcy'), 
          bbox_to_anchor=(1.5, 1), loc='upper right' )
plt.show()

