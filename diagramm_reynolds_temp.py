import numpy as np
import matplotlib.pyplot as plt

N = 15
ind = np.arange(N)

#values of reynolds from 14_Knotennetz.py. Use net.res_pipe["reynolds"].values

# friction factor set as default, T = 293.15K
t_20 = ([185233.9588537 ,  77175.70725153,  58645.01006703,  46860.71327594,
        34243.09290595, 113692.58334163,  58878.21724542,  44082.26983561,
        24825.31883995,  31810.95232763,  76545.303485  ,  56700.37245763,
        23678.01923016,  37784.22298257,  20348.81450605])

# friction factor set as default, T = 288.15K
t_15 = ([187825.8800785 ,  78257.20764469,  59467.2161729 ,  47518.02537879,
        34722.24586394, 115282.11107709,  59702.9781244 ,  44700.21969068,
        25174.18561444,  32258.74760486,  77613.87714482,  57491.26216439,
        24005.17008631,  38312.92587332,  20637.71745304])

# friction factor set as default, T = 281.15K
t_8 = ([191571.57363722,  79820.13115988,  60655.42268959,  48467.93668839,
        35414.68980522, 117579.20216806,  60894.87635797,  45593.2471452 ,
        25678.3506511 ,  32905.87883777,  79158.11353727,  58634.20588469,
        24477.94276219,  39076.97649084,  21055.22984453])

# friction factor set as default, T = 273.15K
t_0 = ([196041.08525172,  81678.76017948,  62066.92437464,  49595.09498574,
        36240.9416567 , 120325.44489459,  62343.52550464,  46691.87881103,
        26323.98794483,  33667.53852915,  80980.64377429,  59977.89762867,
        25008.54990635,  39988.67229711,  21586.94650941])

# plotting
ax = plt.subplot(111)

rects1 = ax.bar(ind-0.2, t_20, width=0.2, color='b', align='center')
rects2 = ax.bar(ind, t_15, width=0.2, color='g', align='center')
rects3 = ax.bar(ind+0.2, t_8, width=0.2, color='r', align='center')
rects4 = ax.bar(ind+0.4, t_0, width=0.2, color='k', align='center')
labels = ('K_1-2', 'K_2-3', 'K_3-4', 'K_4-5', 'K_5-6', 'K_2-10', 'K_10-9', 
          'K_9-8', 'K_8-7', 'K_5-7', 'K_10-11', 'K_11-12', 'K_12-13', 
          'K_12-14', 'K_7-13')


plt.xticks(np.arange(15), labels, rotation=45)
plt.autoscale(tight=True)


plt.xlabel('Pipes')
plt.ylabel('Reynoldszahl')


plt.legend( (rects1[0], rects2[0], rects3[0], rects4[0]), 
           ('20 Grad C', '15 Grad C', '8 Grad C', '0 Grad C'),
           bbox_to_anchor=(1.5, 1), loc='upper right' )

plt.show()