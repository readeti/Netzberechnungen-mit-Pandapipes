import math

# Calculate friction factor for example net with 14 junctions. T = 273.15K
# k = 1mm. Friction factor is as colebrook : 
# " pp.pipeflow(net,friction_model="colebrook") ".

# calculated pressure in bar for each junction
# use : "net.res_junction["p_bar"].values" to get the values
p = ([0.03      , 0.02923084, 0.02846588, 0.02766009, 0.0269649 ,
       0.02586758, 0.0263552 , 0.0267784 , 0.02730957, 0.02814531,
       0.02654443, 0.02597804, 0.02544297, 0.02513171])


# calculate pressure difference between two specific juntions according to 
# schema in 14_Knotennetz.py
delta_p = (p[0]-p[1], p[1]-p[2], p[2]-p[3], p[3]-p[4], p[4]-p[5], p[1]-p[9], 
             p[9]-p[8], p[8]-p[7], p[7]-p[6], p[4]-p[6], p[9]-p[10], 
             p[10]-p[11], p[11]-p[12], p[11]-p[13], p[6]-p[12])


#  from bar to Pascal
p_Pa = [i * 100000 for i in delta_p]

# calculated flow in m^3/s for each pipe. 
# use : "net.res_pipe["vdot_norm_m3_per_s"].values" to get the values
Q = ([0.65400849, 0.2270723 , 0.17255011, 0.13787761, 0.06045132,
       0.40141516, 0.17331909, 0.10384519, 0.04390945, 0.05615877,
       0.22513151, 0.1667425 , 0.04171526, 0.0889369 , 0.03600786])

Q_2 = [i ** 2 for i in Q]

# Calculate resistence of each pipe.
R = [x/y for x, y in zip(p_Pa, Q_2)]


# density of lgas
density = 0.7758309108626392

# values of calculated resistence 
R = [179.82493768175848, 1483.5780818807284, 2706.396308679405, 
     3656.9247439161595, 30027.675776303546, 673.6809857934003, 
     2782.136208682081, 4925.618456968256, 21949.754364671393, 
     19332.188475979514, 3158.5387581040113, 2037.149771966579, 
     30748.27045292753, 10699.802479364613, 70357.39120256106]

# diameter for each pipe given in the same order as 14_Knotennetz.py
d = [0.3, 0.25, 0.25, 0.25, 0.15, 0.3, 0.25, 0.2, 0.15, 0.15, 0.25, 0.25, 0.15,
     0.2, 0.15]

# Use Equation of Darcy to calculate friction factor

z = []
for a, b in zip(R,d):
    z.append(a * (b**5) * pow(math.pi,2))


# length of pipes in the same order as 14_Knotennetz.py
l = [26, 80, 144, 192, 106, 96, 148, 80, 76, 68, 170, 108, 106, 172, 240]   

n = [i * 8 * density for i in l]

friction_factor = [x/y for x, y in zip(z, n)]
print(f'Friction factor: \n {friction_factor}')
