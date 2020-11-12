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

# t = 0 grad c, colebrook k = 1mm
#array([196041.08525172,  81678.75648363,  62066.92067878,  49595.09128989,
 #       36240.9416567 , 120325.44797447,  62343.52462785,  46691.87771504,
  #      26323.98648351,  33667.5323694 ,  80980.64834693,  59977.90220132,
   #     25008.55752742,  39988.67229711,  21586.93888834])

for r in (196041.08525172, 120325.44797447):
    factor = colebrook.bntFriction(r , 0.0033333333333333335) #relative roughness (diameter = 300mm)
    print(r, " : ", factor)
    
for r in (81678.75648363,  62066.92067878,  49595.09128989, 62343.52462785, 80980.64834693, 59977.90220132):
    factor = colebrook.bntFriction(r ,  0.004) #diameter = 250mm
    print(r, " : ", factor)
    
for r in (46691.87771504, 39988.67229711):
    factor = colebrook.bntFriction(r , 0.005) #diameter = 200mm
    print(r, " : ", factor)
    
for r in ( 36240.9416567, 26323.98648351, 33667.5323694, 25008.55752742, 21586.93888834):    
    factor = colebrook.bntFriction(r , 0.006666666666666667) #diameter = 150mm
    print(r, " : ", factor)
    
    





