'''
This runs the chaos game for an equilateral
triangle, yielding a sierpinski triangle
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

def animate(i):
    if ((i+1)/N*100)%k==0:
        print(str((i+1)/N*100)+"% Complete")
    randv = np.random.randint(0,v)
    pt = frac_point(p,i,vertices,randv)
    p[0].append(pt[0])
    p[1].append(pt[1])
    sc.set_offsets(np.c_[p[0],p[1]])
    return sc

N = 10**5
k = 1
dotSize = 10**4/N

xvertices = [0,0.5,1]
yvertices = [0,sqrt(3)/2,0]
vertices = [xvertices,yvertices]
v = len(xvertices)

fig, ax = plt.subplots()
pt = frac_point(vertices,0,vertices,1)
p = [[pt[0]],[pt[1]]]
sc = ax.scatter(p[0],p[1],marker='.',color='purple',s=dotSize)
plt.xlim(0,1)
plt.ylim(0,1)

ani = FuncAnimation(fig,animate,interval=10,frames=N)
ani.save('chaos_game.mp4',fps=N/10,dpi=80)
