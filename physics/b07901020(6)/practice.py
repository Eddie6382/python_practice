from vpython import *
size, m = 0.02, 0.2  # ball size = 0.02 m, ball mass = 0.2kg
L, k = 0.2, 20       # spring original length = 0.2m, force constant = 20 N/m
amplitude = 0.03
b = 0.05 * m * sqrt(k/m)

# =========== delete below in practice 3 ===========
scene = canvas(width=600, height=400, fov=0.03, align='left', center=vec(0.3, 0, 0), background=vec(0.5, 0.5, 0))
wall_left = box(length=0.005, height=0.3, width=0.3, color=color.blue) # left wall
ball = sphere(radius=size, color=color.red)                            # ball
spring = helix(radius=0.015, thickness=0.01)
oscillation = graph(width=400, align='left', xtitle='t', ytitle='x', background=vec(0.5, 0.5, 0))
power = graph(width=1000, align='left', xtitle='t', ytitle='average power', background=vec(0.5,0.5,0))
x = gcurve(color=color.red, graph=oscillation)
avg_p = gdots(color=color.red, graph=power)
# =========== delete above in practice 3 ===========

ball.pos = vector(L, 0 , 0)  # ball initial position
ball.v = vector(0, 0, 0)               # ball initial velocity
ball.m = m
spring.pos = vector(0, 0, 0)
sum_p = 0
T = 2*pi/(1*sqrt(k/m))
t, dt = 0, 0.001

while True:
    # =========== delete below in practice 3 ===========
    rate(1000)
    # =========== delete above in practice 3 ===========
    
    spring.axis = ball.pos - spring.pos # spring extended from spring endpoint A to ball
    spring_force = -k * (mag(spring.axis) - L) * norm(spring.axis) # spring force vector
    res_force =  -b*ball.v
    sinu_force = 0.1*sin(1*sqrt(k/m)*t)*vector(1,0,0)
    ball.a = (spring_force + res_force + sinu_force) / ball.m     # ball acceleration = spring force /m - damping
    ball.v += ball.a*dt
    ball.pos += ball.v*dt
    t += dt
    
    # =========== delete below in practice 3 ===========
    sum_p += dot(sinu_force,ball.v)*dt
    if int(t*1000) % int(T*1000) == 0:
        avg_p.plot(pos=(t,sum_p/T))
        sum_p = 0
    x.plot(pos=(t, ball.pos.x - L))
    # =========== delete above in practice 3 ===========