import colebrook

#k = 0.02mm
r = ([196041.08525172,  81341.6520866 ,  61729.81628176,  49257.98689287,
        36240.9416567 , 120606.36830532,  62302.77569885,  46640.94155379,
        26256.07160185,  33105.69170769,  81358.50167295,  60355.75552734,
        25638.31307078,  39988.67229711,  20957.18334498])


k = 0.02

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

