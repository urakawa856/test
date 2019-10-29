

import numpy as np
import pandas as pd
import os
# 参照するフォルダを指定
rawTempfolder = './t600sample/'

data=[]
# 0
timedepend=[]

# csvファイルの読み込み
rawTemp = os.listdir(rawTempfolder)
for i in range(len(rawTemp)):
    infile = rawTempfolder + rawTemp[i]
    Temp = pd.read_csv(infile, header = None)
    
    a=[]
    a = Temp
    timedepend.append(a)
print(a)

print(len(timedepend))

print(timedepend[22])

# 実験条件の入力
vlas = 1 # laser velosity = 1.0 mm/s
resolutionT = 0.025 # Temperature resolution = 0.025 K
resolutionX = 0.68 # spatial resolution = 0.68 mrad
distanceF = 250 # focal distance = 250 mm

#timedependおよび各種実験条件の保存
 f = open(hozon.txt,'w')
 f.write(vlas)
 f.close()