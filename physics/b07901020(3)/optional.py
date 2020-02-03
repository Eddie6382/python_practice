from vpython import *

sizes = [0.06, 0.04]    
ms = [0.2, 0.12]         
L, k = 0.5, 15

scene = canvas(width=400, height=400, center =vec(0, 0, 0), align = 'left', background=vec(0.5,0.5,0))
ball_1 = sphere(pos = vec(-1.1*L/2, 0, 0), radius = sizes[0], color = color.red)
ball_2 = sphere(pos = vec(1.1*L/2, 0, 0), radius = sizes[1], color = color.red)
ball_1.v = vec(0,0,0)
ball_2.v = vec(0,0,0)
spring = helix(pos = ball_1.pos, radius=0.02, thickness =0.01) 
spring.axis = ball_2.pos - ball_1.pos

dt = 0.001
time = 0
pre_ball = ball_2.pos.x
pre_time = 0
while True:
    rate(1000)
    pre_pre_ball = pre_ball
    pre_ball = ball_2.pos.x

    spring.axis = ball_2.pos - ball_1.pos
    string_force_2 = -k*(mag(spring.axis)-L)*spring.axis.norm()
    string_force_1 = - string_force_2
    ball_1.a = string_force_1/ms[0]
    ball_2.a = string_force_2/ms[1]
    ball_1.v += ball_1.a*dt
    ball_2.v += ball_2.a*dt
    ball_1.pos += ball_1.v*dt
    ball_2.pos += ball_2.v*dt
    time += dt
    
    if pre_ball > ball_2.pos.x and pre_ball > pre_pre_ball:
        print('period=%2.5f'%(time-pre_time))
        pre_time = time
