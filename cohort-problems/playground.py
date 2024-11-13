import numpy as np 

# 1
# 2
# 3
vector = [[1],[2],[3]]

"""
1 1 1 1
4 4 4 4 
8 8 8 8
"""
array = np.array([[1,1,1,1], [4,4,4,4], [8,8,8,8]]) 


mean_axis0 = array.mean(axis=0) # 1st column mean = (1+4+8) / 3, etc, we end up with 4 means, one for each column 
mean_axis1 = array.mean(axis=1) # 1st row mean = (1+1+1+1) / 4, we end up with 3 means, one for each row 
print("mean_axis0", mean_axis0)
print("mean_axis1", mean_axis1)
