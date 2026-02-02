import sys as system

Name = "SampleName"
Number = "SampleNmber"
HomeData = dict({1:"NameSample"})

HomeData[2] = "Name2"

print(HomeData[1])

for key, values in HomeData.items():
     print(key, ":",  values)
 
 