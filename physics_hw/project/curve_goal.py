from vpython import *
#https://youtu.be/rIgQX47xrFg

g = vec(0, -9.8 ,0)           # g = 9.8 m/s^2
size = 0.215 /2             # ball radius = 0.25 m
weight = 0.45           #ball weight
Cd =  0.47              #drag coefficient
Cm = 0.40               #magnus coefficient
Cw = 0.08               #rotational friction coefficient
rpm = 300               #initial rpm
density = 1.293
viscosity = 1.81E-5
v = vec(-16, 7, -26)
omega = rpm/60*2*pi*norm(vec(2,-3,0))                  #initial omega       
SP = size*mag(omega)/mag(v)                  #dimension less angular velocity

class soccer():
    def __init__(self, size, pos, v, rpm ,omega):
        self.o = sphere(radius = size, make_trail = True, trail_radius = 0.05, trail_type="points",
              pos=pos, interval=10, texture='Soccer-ball-Texture1.jpg') 
        self.o.v = v
        self.omega = omega
        self.radius = size
        self.stop = False
        self.rpm = rpm
        self.slab = label(pos= pos + vec(0,2,0), box = True)

class nor_ball():
    def __init__(self, pos, v):
        self.pos = pos
        self.v = v

def drag_torque(Cw, density, omega, radius):
    return -Cw * density/2 * (radius**5) * mag(omega) * omega

def drag_force(Cd, density, velocity, radius):
    return -1/2 * density * Cd * (pi*radius**2) * mag(velocity) * velocity

def magnus_force(Cm, radius, omega, velocity):
    return 4/3*pi*(radius**3) * (Cm*density*cross(omega,velocity))


scene = canvas(width=1000, height=500, center =vec(0,0,0), background=vec(0.5,0.5,0))   # open a window
floor = box(length=90, height=0.01, width=60, color=color.green)                        # the floor
clin = shapes.circle(radius=0.1)
rect = shapes.rectangle(width=0.2, height=0.1)
rectpath_1 = [ vec(-20,0,-20), vec(20,0,-20), 
            vec(20,0,-20+16.5), vec(-20,0,-20+16.5), vec(-20,0,-20) ]
rectpath_2 = [ vec(-40,0,-20), vec(-40,0,-20+45), 
            vec(40,0,-20+45), vec(40,0,-20), vec(-40,0,-20)] 
rectpath_3 = [ vec(-9.14,0,-20), vec(-9.14,0,-20+5.5), 
            vec(9.14,0,-20+5.5), vec(9.14,0,-20)]
rectpath_4 = [ vec(-3.65,0,-20), vec(-3.65,2.5,-20), 
            vec(3.65,2.5,-20), vec(3.65,0,-20)]
rectpath_5 = [ vec(-3.65,0,-22), vec(-3.65,2.5,-21.0), 
            vec(3.65,2.5,-21.0), vec(3.65,0,-22)]
rectpath_6 = [ vec(-3.65,0,-20), vec(-3.65,0,-22), 
            vec(3.65,0,-22), vec(3.65,0,-20)]
rectpath_7 = [ vec(-3.65,2.5,-20), vec(-3.65,2.5,-21.0), 
            vec(3.65,2.5,-21.0), vec(3.65,2.5,-20)]
ar = paths.arc(radius=9.14, angle1=3.8/3*pi, angle2=5.2/3*pi)          

extrusion(path=rectpath_1, shape=rect, color=color.white)
extrusion(path=rectpath_2, shape=rect, color=color.white)
extrusion(path=rectpath_3, shape=rect, color=color.white)
extrusion(path=ar, shape=rect, color=color.white, pos = vec(0, 0, -2.4))
extrusion(path=rectpath_4, shape=clin, color=color.yellow)
extrusion(path=rectpath_5, shape=clin, color=color.yellow)
extrusion(path=rectpath_6, shape=clin, color=color.yellow)
extrusion(path=rectpath_7, shape=clin, color=color.yellow)

peoples = []
for i in range(10):
    people = box(length=2.0, height=0.4, width=0.8, color=color.green, axis=vec(0,1,0), up=vec(0,0,1))
    people.pos = vec(0 + 1.4*i,1.0,-5)
    peoples.append(people)

ball = soccer(size, vec(10, size ,5), v, rpm, omega)
ball_0 = nor_ball(vec(10, size ,5), v)
scene.center = ball.o.pos
dt = 0.001

while True:
    rate(100)
    if ball.o.pos.y >= ball.radius:
        ball.o.pos += ball.o.v*dt
        ball.o.v += ( drag_force(Cd, density, ball.o.v, ball.radius)/weight + magnus_force(Cm, ball.radius, ball.omega, ball.o.v)/weight + g )*dt
        I = 2/3*weight*ball.radius**2
        ball.omega += drag_torque(Cw, density, ball.omega, ball.radius)/I *dt
        ball.o.rotate(angle=mag(ball.omega)*dt, axis=ball.omega, origin=ball.o.pos)
        ball.slab.pos = ball.o.pos + vec(0,2,0)
    else:
        break

    ball_0.pos += ball_0.v*dt
    ball_0.v += ( drag_force(Cd, density, ball_0.v, size)/weight + g )*dt
    ball.slab.text = str('omega: %3.0frpm\nshift: %1.3fm'%(ball.rpm, mag(ball.o.pos - ball_0.pos)))
    scene.center = ball.o.pos
    
