from vpython import *
g = vec(0, -9.8 ,0)           # g = 9.8 m/s^2
size = 0.215 /2             # ball radius = 0.25 m
weight = 0.45           #ball weight
Cd =  0.47              #drag coefficient
Cm = 0.40               #magnus coefficient
Cw = 0.08               #rotational friction coefficient
rpm = 240               #initial rpm
density = 1.293
viscosity = 1.81E-5
v = vec(18, 9, 0)
omega = rpm/60*2*pi*norm(vec(0,1,0))                  #initial omega       
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

def drag_torque(Cw, density, omega, radius):
    return -Cw * density/2 * (radius**5) * mag(omega) * omega

def drag_force(Cd, density, velocity, radius):
    return -1/2 * density * Cd * (pi*radius**2) * mag(velocity) * velocity

def magnus_force(Cm, radius, omega, velocity):
    return 4/3*pi*(radius**3) * (Cm*density*cross(omega,velocity))


scene = canvas(width=1000, height=500, center =vec(0,0,0), background=vec(0.5,0.5,0))   # open a window
floor = box(length=40, height=0.01, width=30, color=color.blue)                               # the floor
balls = []
for i in range(-2,6):
    rpm = 0 + 250*i
    ball = soccer(size, vec(-20, size ,0), v, rpm, rpm/60*2*pi*norm(vec(0,0,1)))
    balls.append(ball)
stops = [False]*10
scene.center = balls[4].o.pos + vec(0,2,0)
dt = 0.001

while True:
    rate(200)
    for ball in balls:
        if ball.o.pos.y >= ball.radius:
            ball.o.pos += ball.o.v*dt
            ball.o.v += ( drag_force(Cd, density, ball.o.v, ball.radius)/weight + magnus_force(Cm, ball.radius, ball.omega, ball.o.v)/weight + g )*dt
            I = 2/3*weight*ball.radius**2
            ball.omega += drag_torque(Cw, density, ball.omega, ball.radius)/I *dt
            ball.o.rotate(angle=mag(ball.omega)*dt, axis=ball.omega, origin=ball.o.pos)
            ball.slab.pos = ball.o.pos + vec(0,1,0)
            ball.slab.text = str('w:%3.0frpm'%ball.rpm)
        else:
            ball.stop = True
    scene.center = balls[4].o.pos + vec(0,2,0)
    
    for ball in balls:
        if ball.stop == False:
            break
    else:
        break

for ball in balls:
    origin = vec(-20, 0, 0)
    print("ball's rpm: %d, shift: %2.3f"%( ball.rpm, mag(ball.o.pos - balls[3].o.pos) ))




