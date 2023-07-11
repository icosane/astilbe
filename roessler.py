import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = 0.15;
p = 0.2;
c = 10.0;
wr = 0.95;
wd = 0.99;
e = 0.11;

def rossler(H, t=0):
    return np.array([(-wd*H[1])-H[2], #xd 0
                    (wd*H[0])+(a*H[1]), #yd 1
                    p+(H[2]*(H[0]-c)), #zd 2 
                    ((-wr*H[4])-H[5])+e*(H[0]-H[3]), #xr 3
                    (wr*H[3])+(a*H[4]), #yr 4 
                    p+(H[5]*(H[3]-c)), #zr 5
                    (((-wr*H[7])-H[8])+e*(H[0]-H[6])), #xa 6
                    ((wr*H[6])+(a*H[7])), #ya 7 
                    p+(H[8]*(H[6]-c))]) #za 8 
                    

T = 10000; T0 = 4000;
t = np.linspace(0, 500, T)
#t = np.arange(0.1, 10000, 0.01)
#T0 = 920000


#H0 = [0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.1, 0.1, 0.1]
H0 = [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 1.05, 1.05, 1.05 ]
#H0 = [0.001, 0.001, 0.001, 0.001, 0.001, 0.001,]
H, infodict = integrate.odeint(rossler, H0, t, full_output=True)

fig, axs = plt.subplots(2)
axs[0].plot(H[T0:,0],H[T0:,3],c='purple') #xd xr
axs[1].plot(H[T0:,3],H[T0:,6],c='purple') #xr,xa
#plt.plot(H[:,3],H[:,6],c='purple') #xr,xa
#plt.plot(H[1000:,0],H[1000:,3],c='purple')
plt.setp(axs[0], xlabel='xd')
plt.setp(axs[0], ylabel='xr')
plt.setp(axs[1], xlabel='xr')
plt.setp(axs[1], ylabel='xa')
plt.show()



