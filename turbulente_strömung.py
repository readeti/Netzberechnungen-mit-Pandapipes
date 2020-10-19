#import pandapipes as pp
import colebrook


#k = 0.007mm
r = 2320

#factor = colebrook.fngFriction(r , 2.3333333333333332e-05) #relative roughness (diameter = 300mm)
#print(factor, sep = ' ')
"""factor1 = colebrook.fngFriction(r , 2.8e-05) #diameter = 250mm
print(factor1)
factor2 = colebrook.fngFriction(r , 3.5000000000000004e-05) #diameter = 200mm
print(factor2)
factor3 = colebrook.fngFriction(r , 4.6666666666666665e-05) #diameter = 150mm
print(factor3)

f = colebrook.eptFriction(r , 2.3333333333333332e-05)
print(f)
f1 = colebrook.eptFriction(r , 2.8e-05) #diameter = 250mm
print(f1)
f2 = colebrook.eptFriction(r , 3.5000000000000004e-05) #diameter = 200mm
print(f2)
f3 = colebrook.eptFriction(r , 4.6666666666666665e-05) #diameter = 150mm
print(f3)
"""
#factor = colebrook.sjFriction(r , 2.3333333333333332e-05) #relative roughness (diameter = 300mm)
#print(r, " : ", factor)
factor = colebrook.sjFriction(r ,  2.8e-05) #diameter = 250mm
print(r, " : ", factor)
    