import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#define universal variables
a = 10
w1 = 40
w2 = 35
w3 = 35 
b = 8/3
K = 5
def dH_dt(H, t=0):
        return np.array([a*(H[1]-H[0]), #H[0]-X1
                     w1*H[0]-H[1]-H[0]*H[2], #H[1]-Y1
                     (-b*H[2]+H[0]*H[1]), #H[2]-Z1
                         
                     a*(H[4]-H[3])+K*(H[0]-H[3]),#H[3]-X2
                     w2*H[3]-H[4]-H[3]*H[5],#H[4]-Y2
                     (-b*H[5]+H[3]*H[4]),#H[5]-Z2
                    
                     a*(H[7]-H[6])+K*(H[0]-H[6]),#H[6]-X3
                     w3*H[6]-H[7]-H[6]*H[8],#H[7]-Y3
                     (-b*H[8]+H[6]*H[7])])#H[8]-Z3
t = np.linspace(0, 400, 40000)
H0 = [0.001, 0.001, 0.001, 0.002, 0.002, 0.002, 1.05, 1.05, 1.05 ]
H, infodict = integrate.odeint(dH_dt, H0, t, full_output=True)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(H[3500:,0], H[3500:,1], H[3500:,2])
#ax.plot(H[3500:,3], H[3500:,4], H[3500:,5])
#ax.plot(H[3500:,6], H[3500:,7], H[3500:,8])
#plt.plot(H[3500:,4], H[3500:,7])
plt.show()
