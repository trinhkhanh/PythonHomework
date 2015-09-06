__author__ = 'trinhkhanh'

import random

squad = [['q', 'w', 'e'], ['t', 'y', 'u','t1', 'y1', 'u1','y2', 'u2'], ['i', 'o', 'p', 'a', 'i1', 'o2', 'p3', 'a4'],['z', 'x', 'c', 'v', 'z1', 'x1', 'c1', 'v1']]

GK = random.sample(squad[0], 1)# GK: Goalkeeper
DF1 = random.sample(squad[1], 4) # DF: defenders: centre-back, sweeper, full-back, and wing-back
DF2 = random.sample(squad[2], 4)
CF = random.sample(squad[3], 2) #CF: Center forward

print('Doi hinh ra san gom: %s, %s, %s, %s'%(GK,DF1,DF2,CF))
