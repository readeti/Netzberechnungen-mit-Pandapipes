import math

# # Calculate friction factor for example net with 14 junctions. T = 273.15K
# k = 1mm. Friction factor set es default : " pp.pipeflow(net) ".

# calculated pressure in bar for each junction
# use : "net.res_junction["p_bar"].values" to get the values
p = ([0.03      , 0.02923972, 0.0284881 , 0.02769964, 0.02702198,
       0.02593287, 0.02641649, 0.02683492, 0.02735644, 0.02817336,
       0.02660018, 0.02604607, 0.02551389, 0.02521535])


# calculate pressure difference between two specific juntions according to 
# schema in 14_Knotennetz.py
delta_p = (p[0]-p[1], p[1]-p[2], p[2]-p[3], p[3]-p[4], p[4]-p[5], p[1]-p[9], 
             p[9]-p[8], p[8]-p[7], p[7]-p[6], p[4]-p[6], p[9]-p[10], 
             p[10]-p[11], p[11]-p[12], p[11]-p[13], p[6]-p[12])


#  from bar to Pascal
p_Pa = [i * 100000 for i in delta_p]


# calculated flow in m^3/s for each pipe. 
# use : "net.res_pipe["vdot_norm_m3_per_s"].values" to get the values
Q = ([0.65400849, 0.22708987, 0.17256768, 0.13789518, 0.06045132,
       0.40139759, 0.17324562, 0.10377172, 0.04383598, 0.05617634,
       0.2251874 , 0.16679839, 0.04177115, 0.0889369 , 0.03595197])

Q_2 = [i ** 2 for i in Q]

# Calculate resistence of each pipe.
R = [x/y for x, y in zip(p_Pa, Q_2)]


# density of lgas
density = 0.7758309108626392

# values of calculated resistence 
R = [177.748847600873, 1457.4806727998955, 2647.6510406881366,
    3563.8029196887537, 29803.012762667237, 661.8420015101888, 
    2721.7924278613227, 4842.982923551746, 21775.16097098836, 
    19186.691543888526, 3102.3460781172357, 1991.6465999955335, 
    30500.410552653088, 10502.451662658514, 69831.27053556408]


# diameter for each pipe given in the same order as 14_Knotennetz.py
d = [0.3, 0.25, 0.25, 0.25, 0.15, 0.3, 0.25, 0.2, 0.15, 0.15, 0.25, 0.25, 0.15,
     0.2, 0.15]

# Use Equation of Darcy to calculate friction factor

z = []
for a, b in zip(R,d):
    z.append(a * (b**5) * pow(math.pi,2))
""" 
#print(f'k: {k}')   
#k = [4.3127664211778916, 14.29914918582983, 26.085020428939696, 35.24648490918701, 22.50493477565575, 16.156984518229724, 26.81502321253782, 15.556449792313883, 16.450750101292197, 14.488954921577365, 30.44289846483854, 19.634631206132354, 23.045001090408793, 33.79290164515963, 52.73097098139275]
"""
# length of pipes in the same order as 14_Knotennetz.py
l = [26, 80, 144, 192, 106, 96, 148, 80, 76, 68, 170, 108, 106, 172, 240]   

n = [i * 8 * density for i in l]

friction_factor = [x/y for x, y in zip(z, n)]
print(f'Friction factor: \n {friction_factor}')


