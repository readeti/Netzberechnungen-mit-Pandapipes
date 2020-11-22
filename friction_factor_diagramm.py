import matplotlib.pyplot as plt


# Colebrook, k = 1mm, T = 293.15K
# Reynold number from 14_Knotennetz.py
r1 = ([185233.9588537 ,  77170.21162847,  58639.51444397,  46855.21765288,
        34243.09290595, 113697.16302751,  58904.97101151,  44115.71204322,
        24869.9084501 ,  31801.79295587,  76524.04534197,  56679.1143146 ,
        23642.58899177,  37784.22298257,  20384.24474444])


# Friction factor for k = 1mm, bnt. Use "friction_factor_berechnung.py"
bnt1 = ([0.0217, 0.0224, 0.0224, 0.0226, 0.0256, 0.0215, 0.0224, 0.0238, 0.026,
         0.0257, 0.0224, 0.0224, 0.0261, 0.0239, 0.0265])


# Friction factor for k = 1mm, sj. Use "friction_factor_berechnung.py"
sj1 = ([0.0278, 0.0301, 0.0305, 0.031, 0.0358, 0.0283, 0.0305, 0.0328, 0.0366, 
        0.036, 0.0301, 0.0306, 0.0368, 0.0331, 0.0372])


# Colebrook, k = 0.007mm, t = 293.15K
# # Reynold number from 14_Knotennetz.py
r = ([185233.9588537 ,  76830.04180484,  58299.34462035,  46515.04782926,
        34243.09290595, 113980.63788053,  58866.3285119 ,  44067.40891871,
        24805.50428408,  31234.84324982,  76902.8576652 ,  57057.92663783,
        24273.94286383,  37784.22298257,  19752.89087238])


# Friction factor for k = 0.007mm, bnt. Use "friction_factor_berechnung.py"
bnt = ([0.0163, 0.0194, 0.0206, 0.0216, 0.0232, 0.0179, 0.0205, 0.0219, 0.025, 
        0.0237, 0.0194, 0.0207, 0.0251, 0.0226, 0.0264])


# Friction factor for k = 0.007mm, sj. Use "friction_factor_berechnung.py"
sj = ([0.016, 0.019, 0.0202, 0.0212, 0.0228, 0.0175, 0.0201, 0.0215, 0.0246, 
       0.0233, 0.019, 0.0203, 0.0247, 0.0223, 0.026])


# plotting
red_dot, = plt.plot(r1,sj1,'bo', color = 'r')
blue_dot, = plt.plot(r,bnt,'bo')
magenta_dot, = plt.plot(r1,bnt1,'bo', color = 'm')
green_dot, = plt.plot(r,sj,'bo', color = 'g')
plt.legend( (red_dot, magenta_dot, green_dot, blue_dot), 
           ('colebrook,k = 1mm, sj', 'colebrook, k = 1mm, bnt', 
            'colebrook, k = 0.007mm, sj' , 'colebrook, k = 0.007mm, bnt') , 
           loc = 'upper right')

plt.xlabel('Reynoldsnumber')
plt.ylabel('friction factor')
plt.show()
