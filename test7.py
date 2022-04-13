import os

ldir = os.listdir('C:\\A\\')
print(ldir)

fName = "test1.txt"
fName2 = 'test2.txt'
fName3 = 'test10.txt'
fName4 = 'test6.txt'

fPath = "C:\\A\\"


abPath = os.path.join(fPath, fName)
print(abPath)
print(os.path.getmtime(abPath))

acPath = os.path.join(fPath, fName2)
print(acPath)
print(os.path.getmtime(acPath))

adPath = os.path.join(fPath, fName3)
print(adPath)
print(os.path.getmtime(adPath))

aePath = os.path.join(fPath, fName4)
print(aePath)
print(os.path.getmtime(aePath))
