import matplotlib.pyplot as plt


#k = 0.02
r = ([196041.08525172,  81341.6520866 ,  61729.81628176,  49257.98689287,
        36240.9416567 , 120606.36830532,  62302.77569885,  46640.94155379,
        26256.07160185,  33105.69170769,  81358.50167295,  60355.75552734,
        25638.31307078,  39988.67229711,  20957.18334498])

f = ([0.0162,  0.0191, 0.0202, 0.0212, 0.0228, 0.0176, 0.0201, 0.0215, 0.0245, 0.0233, 0.0191, 0.0203, 0.0247, 0.0222, 0.0259])

red_dot, = plt.plot(r,f,'bo', color = 'r')

#plt.legend( (red_dot, magenta_dot, green_dot, blue_dot), ('colebrook, k = 1mm, sj', 'colebrook, k = 1mm, bnt', 'colebrook, k = 0.007mm, sj' , 'colebrook, k = 0.007mm, bnt') , loc = 'upper right')

plt.xlabel('Reynoldsnumber')
plt.ylabel('friction factor')
plt.show()