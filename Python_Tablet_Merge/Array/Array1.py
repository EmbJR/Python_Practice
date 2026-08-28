import numpy as np
arra = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Array shape:", arra.shape)
print("Array size:", arra.size)
print("Array dimension:", arra.ndim)

file = open('TFile.txt', 'r')
for line in file:
    print(line)
file.close()