'''
video resource: https://youtu.be/d7P4uhUMT1o
'''

from vpython import *
size, m = 0.02, 0.2  # ball size = 0.02 m, ball mass = 0.2kg
L, k, K = 0.2, 20, 5.0       # spring original length = 0.2m, force constant = 20 N/m
amplitude = 0.03
b1 = 0.05 * m * sqrt(k/m)
b2 = 0.0025 * m * sqrt(k/m)

# =========== delete below in practice 3 ===========
scene = canvas(width=600, height=400, fov=0.03, align='left', center=vec(0.3, 0, 0), background=vec(0.5, 0.5, 0))
wall_left = box(length=0.005, height=0.3, width=0.3, color=color.blue) # left wall
wall_right = box(length=0.005, pos=vector(3*L,0,0), height=0.3, width=0.3, color=color.blue)
ball_1 = sphere(radius=size, color=color.red)
ball_2 = sphere(radius=size, color=color.red)                           # ball
spring_1 = helix(radius=0.015, thickness=0.01)
spring_2 = helix(radius=0.005, thickness=0.004)
spring_3 = helix(radius=0.015, thickness=0.01)
oscillation = graph(width=1000, align='left', xtitle='t', ytitle='x', background=vec(0.5, 0.5, 0))
power = graph(width=1000, align='left', xtitle='t', ytitle='average power', background=vec(0.5,0.5,0))
x = gcurve(color=color.red, graph=oscillation)
avg_p = gdots(color=color.red, graph=power)
# =========== delete above in practice 3 ===========

ball_1.pos = vector(L, 0 , 0)  # ball_1 initial position
ball_2.pos = vector(2*L, 0, 0)
ball_1.v = ball_2.v = vector(0, 0, 0)     # ball_1 initial velocity
ball_1.m = ball_2.m = m
spring_1.pos = vector(0, 0, 0)
spring_2.pos = ball_1.pos
spring_3.pos = vector(3*L,0,0)
sum_p = 0
T = 2*pi/(1*sqrt((k+K)/m))
t, dt = 0, 0.001

while True:
    # =========== delete below in practice 3 ===========
    rate(1000)
    # =========== delete above in practice 3 ===========
    
    spring_1.axis = ball_1.pos - spring_1.pos # spring extended from spring endpoint A to ball
    spring_2.axis = ball_2.pos - spring_2.pos
    spring_3.axis = ball_2.pos - spring_3.pos
    spring_2.pos = ball_1.pos
    spring_1_force = -k * (mag(spring_1.axis) - L) * norm(spring_1.axis) # spring force vector
    spring_2_force = -K * (mag(spring_2.axis) - L) * norm(spring_2.axis)
    spring_3_force = -k * (mag(spring_3.axis) - L) * norm(spring_3.axis)
    res_1_force =  -b1*ball_1.v
    res_2_force = -b2*ball_2.v
    sinu_force = 0.1*sin(1*sqrt((k+K)/m)*t)*vector(1,0,0)
    ball_1.a = (spring_1_force + (-spring_2_force) + res_1_force + sinu_force) / ball_1.m     # ball acceleration = spring force /m - damping
    ball_2.a = (spring_3_force + spring_2_force + res_2_force) / ball_2.m
    ball_1.v += ball_1.a*dt
    ball_2.v += ball_2.a*dt
    ball_1.pos += ball_1.v*dt
    ball_2.pos += ball_2.v*dt
    
    t += dt
    # =========== delete below in practice 3 ===========
    sum_p += dot(sinu_force,ball_1.v)*dt
    if int(t*1000) % int(T*1000) == 0:
        avg_p.plot(pos=(t,sum_p/T))
        sum_p = 0
    x.plot(pos=(t, ball_1.pos.x - L))
    # =========== delete above in practice 3 ===========