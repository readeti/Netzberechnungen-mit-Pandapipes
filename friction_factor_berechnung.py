# -*- coding: utf-8 -*-

import pandapipes as pp
import colebrook

net = pp.create_empty_network(fluid="lgas")
#class Fluid(name = "methane",fluid_type = "gas"):
 #   fluid = Fluid(name = "methane",fluid_type = "gas")
  #  Fluid.add_property('methane_density', pp.FluidPropertyConstant(0.657), overwrite=True, warn_on_duplicates=True)



  

           

#for r in (196041.08525172  ,  81685.07713518,  62073.24133033,  49601.41194144,
 #         36240.9416567 , 120320.18076485,  62317.09980153,  46658.84668214,
  #        26279.94510632,  33678.06678865,  81000.75252169,  59998.00637608,
   #       25042.06448536,  39988.67229711,  21553.4319304): 
 
  #  factor = colebrook.sjFriction(r , 1)
        
   # print(factor)
    #print(factor,sep = ",")
   # print(r, " : ", factor)

#k = 1mm

#for r in (196041.08525172, 120320.18076485):
 #   factor = colebrook.bntFriction(r , 0.0033333333333333335) #relative roughness (diameter = 300mm)
  #  print(r, " : ", factor)
    
#for r in (81685.07713518,  62073.24133033,  49601.41194144, 62317.09980153, 81000.75252169,  59998.00637608):
 #   factor = colebrook.bntFriction(r ,  0.004) #diameter = 250mm
  #  print(r, " : ", factor)
    
#for r in (46658.84668214, 39988.67229711):
 #   factor = colebrook.bntFriction(r , 0.005) #diameter = 200mm
  #  print(r, " : ", factor)
    
#for r in (36240.9416567, 26279.94510632,  33678.06678865, 25042.06448536, 21553.4319304):    
 #   factor = colebrook.bntFriction(r , 0.006666666666666667) #diameter = 150mm
  #  print(r, " : ", factor)
    




# wenn colebrook, k = 1mm
r = ([185233.9588537 ,  77170.21162847,  58639.51444397,  46855.21765288,
        34243.09290595, 113697.16302751,  58904.97101151,  44115.71204322,
        24869.9084501 ,  31801.79295587,  76524.04534197,  56679.1143146 ,
        23642.58899177,  37784.22298257,  20384.24474444])

#k = 1mm
for r in (185233.9588537, 113697.16302751 ):
    factor = colebrook.sjFriction(r , 0.0033333333333333335) #relative roughness (diameter = 300mm)
    print(r, " : ", factor)
    
for r in (77170.21162847,  58639.51444397,  46855.21765288, 58904.97101151, 76524.04534197,  56679.1143146 ):
    factor = colebrook.sjFriction(r ,  0.004) #diameter = 250mm
    print(r, " : ", factor)
    
for r in ( 44115.71204322,  37784.22298257):
    factor = colebrook.sjFriction(r , 0.005) #diameter = 200mm
    print(r, " : ", factor)
    
for r in (34243.09290595, 24869.9084501 ,  31801.79295587, 23642.58899177, 20384.24474444):    
    factor = colebrook.sjFriction(r , 0.006666666666666667) #diameter = 150mm
    print(r, " : ", factor) 
    
    
"""
    #t = 20 grad c
r = ([185233.9588537 ,  76830.04180484,  58299.34462035,  46515.04782926,
        34243.09290595, 113980.63788053,  58866.3285119 ,  44067.40891871,
        24805.50428408,  31234.84324982,  76902.8576652 ,  57057.92663783,
        24273.94286383,  37784.22298257,  19752.89087238])

#k = 0.007mm
for r in (185233.9588537, 113980.637881 ):
    factor = colebrook.sjFriction(r , 2.3333333333333332e-05) #relative roughness (diameter = 300mm)
    print(r, " : ", factor)
    
for r in (76830.04180484,  58299.34462035,  46515.04782926,  58866.3285119, 76902.8576652 ,  57057.92663783, ):
    factor = colebrook.sjFriction(r ,  2.8e-05) #diameter = 250mm
    print(r, " : ", factor)
    
for r in ( 44067.40891871, 37784.22298257):
    factor = colebrook.sjFriction(r , 3.5000000000000004e-05) #diameter = 200mm
    print(r, " : ", factor)
    
for r in (34243.09290595, 24805.50428408,  31234.84324982,  24273.94286383, 19752.89087238):    
    factor = colebrook.sjFriction(r , 4.6666666666666665e-05) #diameter = 150mm
    print(r, " : ", factor)
    
    """
    





