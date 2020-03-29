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
omega = rpm/60*2*pi*norm(vec(0,0,1))                  #initial omega       
SP = size*mag(omega)/mag(v)                  #dimension less angular velocity


def drag_torque(Cw, density, omega, radius):
    return -Cw * density/2 * (radius**5) * mag(omega) * omega

def drag_force(Cd, density, velocity, radius):
    return -1/2 * density * Cd * (pi*radius**2) * mag(velocity) * velocity

def magnus_force(Cm, radius, omega, velocity):
    return 4/3*pi*(radius**3) * (Cm*density*cross(omega,velocity))


scene = canvas(width=1000, height=300, center =vec(0,14,0), background=vec(0.5,0.5,0))   # open a window
floor = box(length=40, height=0.01, width=10, color=color.blue)                               # the floor
ball = sphere(radius = size, color=color.red, make_trail = True, trail_radius = 0.05, trail_type="points",
              interval=10)         # the ball
ball_1 = sphere(radius = size, color=color.yellow, make_trail = True, trail_radius = 0.05, trail_type="points",
              interval=10)         # the ball
ball_2 = sphere(radius = size, make_trail = True, trail_radius = 0.05, trail_type="points",
              interval=10,texture='Soccer-ball-Texture1.jpg') 

graph_0 = graph(width = 600, align='left', title='v-t graph',xtitle='time', ytitle='v', background=vec(0.5,0.5,0))
graph_1 = graph(width = 600, align='left', title='omega-t graph',xtitle='time', ytitle='omega', background=vec(0.5,0.5,0))
v_0 = gcurve(color=color.red, graph=graph_0)
v_1 = gcurve(color=color.yellow, graph=graph_0)
v_2 = gcurve(color=color.white, graph=graph_0)
omega_2 = gcurve(color=color.purple, graph=graph_1)

ball.pos = vec( -20, size, 0)         # ball center initial position
ball.v = v                            # ball initial velocity
ball_1.pos = ball.pos
ball_1.v = ball.v
ball_2.pos = ball.pos
ball_2.v = ball.v
scene.center = ball_2.pos
slab = label(pos=ball_2.pos + vec(0,1,0), box = True)
stops = [False]*3

dt = 0.001                            # time step
time = 0
while True:         # until the ball hit the ground
    rate(200)                                            
    if ball.pos.y >= size:
        ball.pos += ball.v*dt 
        ball.v += g*dt
    else:
        stops[0] = True
    
    if ball_1.pos.y >= size:
        ball_1.pos += ball_1.v*dt
        ball_1.v += ( drag_force(Cd, density, ball_1.v, size)/weight + g )*dt
    else:
        stops[1] = True

    if ball_2.pos.y >= size:
        ball_2.pos += ball_2.v*dt
        ball_2.v += ( drag_force(Cd, density, ball_1.v, size)/weight + magnus_force(Cm, size, omega, ball_2.v)/weight + g )*dt
        I = 2/3*weight*size**2
        omega += drag_torque(Cw, density, omega, size)/I*dt
        ball_2.rotate(angle=mag(omega)*dt, axis=omega, origin=ball_2.pos)
    else:
        stops[2] = True
    
    for i in stops:
        if i == False:
            break
    else:
        break
    scene.center = ball_2.pos
    time += dt
    if stops[0] == False:
        v_0.plot(pos=(time, mag(ball.v)))
    if stops[1] == False:
        v_1.plot(pos=(time, mag(ball_1.v)))
    if stops[2] == False:
        v_2.plot(pos=(time, mag(ball_2.v)))
        omega_2.plot(pos=(time, mag(omega)))
    slab.pos = ball_2.pos + vec(0,1,0)
    slab.text = str('Shift: %1.4fm'%mag(ball_2.pos - ball_1.pos))

  
print(mag(omega))