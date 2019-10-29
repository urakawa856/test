import pickle

foldername = 'sampleTemp'
filename1 = '{}.binaryfile'.format(foldername)


######################################################################
with open(filename1,'rb') as k:
	timedepend = pickle.load(k)
	vlas = pickle.load(k)
	resolutionT = pickle.load(k)
	resolutionX = pickle.load(k)
	distanceF = pickle.load(k)
	allFrame = pickle.load(k)

print(timedepend[0])
te = []
for i in range(len(timedepend)):
	temp = timedepend[i] - timedepend[0]
	te.append(temp)


print(len(timedepend))
print(te[0])
print(te[5])
print(te[10])
print(te[15])
print(te[20])