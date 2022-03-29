import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm 

x = np.linspace(0,10)
y = np.linspace(0,10)
f = lambda x,y: x**2 + y**2
z = f(x,y)

heat_source = 10

k_values = {
    'Copper' : 400,
    'Bronze' : 50,
    'Stainless Steel' : 12,
    'Mercury' : 8,
    'Concrete' : 1,
    'Plastic' : 0.15
}
max_value = 0
for i in range(len(k_values)):
    for k in k_values[i]:
        delta_T = heat_source/k
        if delta_T > max_value:
            max_value = delta_T
            print(i)