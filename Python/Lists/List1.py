import numpy as np

l1 = []
l2 = [4,5,6,8]
l3 = [3,2,1,5]

l1.append(l2)
l1.append(l3)
print("------------------")
print(l1)

arr2 = np.array(l1)
print("------------------")
print(arr2)