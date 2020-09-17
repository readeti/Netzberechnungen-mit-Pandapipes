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


for r in (196041.08525172, 120320.18076485):
    factor = colebrook.bntFriction(r , 0.0033333333333333335) #relative roughness (diameter = 300mm)
    print(r, " : ", factor)
    
for r in (81685.07713518,  62073.24133033,  49601.41194144, 62317.09980153, 81000.75252169,  59998.00637608):
    factor = colebrook.bntFriction(r ,  0.004) #diameter = 250mm
    print(r, " : ", factor)
    
for r in (46658.84668214, 39988.67229711):
    factor = colebrook.bntFriction(r , 0.005) #diameter = 200mm
    print(r, " : ", factor)
    
for r in (36240.9416567, 26279.94510632,  33678.06678865, 25042.06448536, 21553.4319304):    
    factor = colebrook.bntFriction(r , 0.006666666666666667) #diameter = 150mm
    print(r, " : ", factor)
    





