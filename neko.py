import pickle

with open('sampleTemp.binaryfile','rb') as k:
	timedepend = pickle.load(k)
	vlas = pickle.load(k)
	resolutionT = pickle.load(k)
	resolutionX = pickle.load(k)
	distanceF = pickle.load(k)
	allFrame = pickle.load(k)

print(allFrame)