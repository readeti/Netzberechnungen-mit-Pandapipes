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


# plotting
ax = plt.subplot(111)

labels = ('K_1-2', 'K_2-3', 'K_3-4', 'K_4-5', 'K_5-6', 'K_2-10', 'K_10-9', 
          'K_9-8', 'K_8-7', 'K_5-7', 'K_10-11', 'K_11-12', 'K_12-13', 
          'K_12-14', 'K_7-13')
plt.xticks(np.arange(15), labels, rotation=45)
plt.autoscale(tight=True)

rects1 = ax.bar(ind, ff_darcy, width=0.2, color='g', align='center')
rects2 = ax.bar(ind+0.2, ff_colebrook, width=0.2, color='r', align='center')
plt.xlabel('Pipes')
plt.ylabel('Friction factor')

# show legend
ax.legend( (rects1[0], rects2[0]), ('Darcy Equation', 'Colebrook'), bbox_to_anchor=(1.5, 1), loc='upper right' )
plt.show()
