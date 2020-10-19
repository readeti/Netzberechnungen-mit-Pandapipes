import colebrook

#k = 0.02
r = ([196041.08525172,  81341.6520866 ,  61729.81628176,  49257.98689287,
        36240.9416567 , 120606.36830532,  62302.77569885,  46640.94155379,
        26256.07160185,  33105.69170769,  81358.50167295,  60355.75552734,
        25638.31307078,  39988.67229711,  20957.18334498])

for r in (196041.08525172, 120606.36830532):
    factor = colebrook.sjFriction(r , 6.666666666666667e-05) #relative roughness (diameter = 300mm)
    print(r, " : ", factor)
    
for r in (81341.6520866 ,  61729.81628176,  49257.98689287, 62302.77569885, 81358.50167295,  60355.75552734):
    factor = colebrook.sjFriction(r ,  8e-05) #diameter = 250mm
    print(r, " : ", factor)
    
for r in ( 46640.94155379, 39988.67229711):
    factor = colebrook.sjFriction(r , 0.0001) #diameter = 200mm
    print(r, " : ", factor)
    
for r in (36240.9416567, 26256.07160185,  33105.69170769, 25638.31307078, 20957.18334498):    
    factor = colebrook.sjFriction(r , 0.00013333333333333334) #diameter = 150mm
    print(r, " : ", factor)
    