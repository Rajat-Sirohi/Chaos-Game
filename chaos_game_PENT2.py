'''
This runs the chaos game for a pentagon
where the current vertex cannot be 1
or 3 places, respectively away from
the two previously chosen vertices.
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math import sqrt

def frac_point(p1,i1,p2,i2,r=0.5):
    x1 = p1[0][i1]
    y1 = p1[1][i1]
    x2 = p2[0][i2]
    y2 = p2[1][i2]

    xp = x1*(1-r) + x2*r
    yp = y1*(1-r) + y2*r
    return xp,yp

randv = -1
temp1 = -1
temp2 = -1
def animate(i):
    global randv,temp1,temp2
    if ((i+1)/N*100)%k==0:
        print(str((i+1)/N*100)+"% Complete")
    
    if i != 0:
        randv = np.random.randint(0,v)
        while abs(randv-temp1)==1 or abs(randv-temp2)==4:
            randv = np.random.randint(0,v)
        temp2 = temp1
        temp1 = randv
        
        pt = frac_point(p,i-1,vertices,randv)
        p[0].append(pt[0])
        p[1].append(pt[1])
        sc.set_offsets(np.c_[p[0],p[1]])

    return sc

N = 10**5
k = 1
dotSize = 10**4/N

xvertices = [.2,0,.5,1,.8]
yvertices = [0,.7,1,.7,0]
vertices = [xvertices,yvertices]
v = len(xvertices)

fig, ax = plt.subplots()
p = [[np.random.random()],[np.random.random()]]
sc = ax.scatter(p[0],p[1],marker='.',color='purple',s=dotSize)
plt.xlim(0,1)
plt.ylim(0,1)

ani = FuncAnimation(fig,animate,interval=10,frames=N)
ani.save('chaos_game_PENT2.mp4',fps=N/10)
