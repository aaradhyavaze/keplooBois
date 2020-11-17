from vpython import *;import matplotlib.pyplot as plt, numpy as np
#main sync switch
sw = 1
#all the boring ones unity and not mess with them
#v = v + a*dt/2
#r = r + v*dt
#comp acc
#v = v + a*dt/2
#t = t + dt
x, y = [], []
#pos b is neg lol
dt = 1/1000; td = 1; theta = 0; r = 1.4; rdd=0; rd=0;k = 1; m = 1; b = 2
#thingamajigis
l = m*r**2*td
fr = lambda : k/(m*r**b) #just for the later traj dont use for eff
# u = lambda rad : -k/(rad**(b-1)) #here integrate
def u(rad):
    if b == -1 : return k*rad**2/2
    return -k/(rad**(b-1))
ener = lambda : (rd**2 + r**2*td**2)/2 + u(r)
#u's im keeping b-1 notationabusebutok
#effektiff
veff = lambda rad: l**2/(2*m*rad**2) + u(rad)
#veff changes cus l changes. i'll have to keep prod td, r same 
#for ann
# lowfor2 = lambda : (l**2/(m*k), -m*k**2/(2*l**2))


fig, (ax1, ax2) = plt.subplots(2)
fig.tight_layout(pad=3);

rs = np.linspace(0.01, 5, 100)
vs = [veff(rad) for rad in rs]
ax1.set_ylim(-15, 8)
ax1.set_title('U for force = -k/(m*r**' + str(b) + ')' )

#for the lowest point. there's only a few so i can sort.
y1 = min(vs); x1 = rs[vs.index(min(vs))]; #print(x1, y1)


ax1.scatter(x1, y1, c = 'red')
ax1.annotate('r0,Vmin = ' + str([round(i, 2) for i in (x1,y1)]), (x1, y1-2))
ax1.plot(rs, vs)
ax1.set_xlabel('r'); ax1.set_ylabel('V_eff')
# print(vs)

for i in range(50000):
    # lp = m*r**2*td
    #no dive check here
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
#exec after yyy sync damnit
if sw == 1:
    bob = sphere(pos = vec(r*cos(theta),r*sin(theta),0), color = color.yellow, radius = 0.02, make_trail = True, trail_type = "points", trail_radius = 0.009, trail_color = vec(1,1,1))
    origin = simple_sphere(pos = vec(0,0,0), radius = 0.1, color = color.red)
    angmom = label(pos = vec(0, 0, 0.5), text = str(l), height = 8)
    # scene.background = vec(0, 0, 0.1)
    while True:
        rate(1/dt)
        #each iter for a div check
        lp = m*r**2*td
        # if(round(lp, 2) != round(l, 2)):
        #     break
        #end
        rd += rdd*dt/2
        r += rd*dt
        rdd = l**2/(m**2*(r**3)) - fr()
        rd += rdd*dt/2

        # rdd = l**2/(m**2*(r**3)) - k/(m*r**2)
        # rd += rdd*dt
        # r += rd*dt

        td = l/(m*r**2)
        theta += td*dt
        bob.pos = vec(r*cos(theta), r*sin(theta), 0)
        # angmom.text = str(round(lp, 4))
        angmom.text = str(round(lp, 5))