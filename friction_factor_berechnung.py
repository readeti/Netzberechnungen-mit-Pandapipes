import pandapipes as pp
import colebrook

net = pp.create_empty_network(fluid="lgas")



# Colebrook, k = 1mm,  T = 293.15K
# Reynold number. Use "net.res_pipe["reynolds"].values in 14_Knotennetz.py
r = ([185233.9588537 ,  77170.21162847,  58639.51444397,  46855.21765288,
        34243.09290595, 113697.16302751,  58904.97101151,  44115.71204322,
        24869.9084501 ,  31801.79295587,  76524.04534197,  56679.1143146 ,
        23642.58899177,  37784.22298257,  20384.24474444])

k = 1

# diameter for each pipe given in the same order as 14_Knotennetz.py in mm
d = [300, 250, 250, 250, 150, 300, 250, 200, 150, 150, 250, 250, 150,
     200, 150]

# the roughness of the pipe material compared to its inner diameter.
for i in d :     
    relative_roughness = [k/i for i in d]


# calculate friction factor with colebrook.py
for a, b in zip(r,relative_roughness):
    friction_factor = colebrook.sjFriction(a , b)
    print(a, " : ", friction_factor)
    

    
"""
# Colebrook, k = 0.007mm, T = 293.15K
# Reynold number. Use "net.res_pipe["reynolds"].values in 14_Knotennetz.py
r = ([185233.9588537 ,  76830.04180484,  58299.34462035,  46515.04782926,
        34243.09290595, 113980.63788053,  58866.3285119 ,  44067.40891871,
        24805.50428408,  31234.84324982,  76902.8576652 ,  57057.92663783,
        24273.94286383,  37784.22298257,  19752.89087238])


k = 0.007

# diameter for each pipe given in the same order as 14_Knotennetz.py in mm
d = [300, 250, 250, 250, 150, 300, 250, 200, 150, 150, 250, 250, 150,
     200, 150]

# the roughness of the pipe material compared to its inner diameter.
for i in d :     
    relative_roughness = [k/i for i in d]


# calculate friction factor with colebrook.py
for a, b in zip(r,relative_roughness):
    friction_factor = colebrook.sjFriction(a , b)
    print(a, " : ", friction_factor)
    
   

"""


