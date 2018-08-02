import pandas as pd
import numpy as np 
##Media
collection = [1525, 257, 378, 9543, 7854, 152]
print('/** Media **/')
result = np.mean(collection)
print(result)
##Moda
print('/** Moda **/')
collection_mo = [9, 5, 9, 4, 3, 6, 7, 1, 2, 3, 9, 1, 2]
print(np.bincount(collection_mo).argmax())
##Mediana
print('/** Mediana **/')
collection_me = [9, 5, 9, 4, 3, 6, 7, 1, 2, 3, 9, 1, 2]
print(np.median(collection_me))

print('/** Percentiles **/')
print(np.percentile(collection_me, 75))

