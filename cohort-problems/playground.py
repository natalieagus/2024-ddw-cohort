import numpy
import itertools 

labels = [0,1]

keys = itertools.product(labels, repeat=3)
for k in keys: 
    print(k)