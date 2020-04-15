import math
import numpy as np

# Semi-major axis between earth and sun
A = 149600000
# Eccentricity of earth
E = 0.0167
l = []

# Calculating the distance between earth and sun
for i in range(365):
    theta = (2 * math.pi * i) / 365.25
    r = A*(1 - E**2)/ (1 - (E * math.cos(theta)))
    l.append(r)

# Calculating the time taken
S = 299792
t = np.divide(l, S)

sunny = np.asarray(list(zip(l, t)))
print(sunny)



d = []
for i in range(1,len(l) - 1):
    d.append(l[i]-l[i-1])
