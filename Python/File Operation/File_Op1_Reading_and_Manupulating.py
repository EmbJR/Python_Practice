import numpy as np

#Path = "/storage/emulated/0/Documents/Practices/Git Repo for Python test/Python/TFile.txt"
Path = "TFile.txt"

listitem = []

file = open(Path, 'r')
for line in file:
    
    ln1 = line.strip("\n")
    ln1 = ln1.strip('[')
    ln1 = ln1.strip(']')
    ln2 = ln1.split(',')
    
    #ln2.to
    cnt=0
    for i in ln2:
         ln2[cnt] = int(i)
         cnt+=1
         
    #print(ln2)
    listitem.append(ln2)
file.close()
print(listitem)

print("-------------------------")
arr2 = np.array(listitem)
print(arr2)
