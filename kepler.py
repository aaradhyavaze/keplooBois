
import matplotlib.pyplot as plt, numpy as np
x, y = [], []
dt = 1/1000; td = 0.1; theta = 0; r = 1.4; rdd=0; rd=0;k = 1; m = 1; b = 2

#thingamajigis
l = m*r**2*td
fr = lambda : k/(m*r**b) #just for the later traj dont use for eff
u = lambda r : -k/(r**(b-1)) #here integrate
ener = lambda : (rd**2 + r**2*td**2)/2 + u(r)
#u's im keeping b-1 notationabusebutok
#effektiff
veff = lambda r: l**2/(2*m*r**2) + u(r)
lowfor2 = lambda : (l**2/(m*k), -m*k**2/(2*l**2))

fig, (ax1, ax2) = plt.subplots(2)
fig.tight_layout(pad=3);

rs = np.linspace(0.01, 5, 100)
vs = [veff(r) for r in rs]
ax1.set_ylim(-15, 3)
ax1.annotate('r0,Vmin = '+str([round(i, 2) for i in lowfor2()]), lowfor2())
print(lowfor2())
ax1.plot(rs, vs)
ax1.set_xlabel('r'); ax1.set_ylabel('V_eff')
# print(vs)


for i in range(10000):
    lp = m*r**2*td

    rd += rdd*dt/2
    r += rd*dt
    rdd = l**2/(m**2*(r**3)) - fr()
    rd += rdd*dt/2
    td = l/(m*r**2)
    theta += td*dt
    if i%100 == 0:
        x.append(r*np.cos(theta)); y.append(r*np.sin(theta))
ax2.set_title('trajectory')
ax2.axis('equal') #later uncomment cus the blowing up thing wasn't showing up
ax2.plot(x,y)    
plt.show()