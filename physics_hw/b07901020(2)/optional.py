from vpython import *

g = 9.8       # g = 9.8 m/s^2
size = 0.25   # ball radius = 0.25 m
height = 15.0 # ball center initial height = 15 m
C_drag = 0.3

scene = canvas(width=600, height=600,align = 'left', center=vec(0,height/2,0), background=vec(0.5,0.5,0))
floor = box(length=30, height=0.01, width=10, color=color.blue)
vt_graph = graph(width = 600, align ='left', xtitle = 'time(s)', ytitle = 'speed(m/s)')
funct = gcurve(graph = vt_graph, color = color.blue, width =4)
ball = sphere(radius=size, color=color.yellow, make_trail=True)

ball.pos = vec(0, 800, 0)
ball.v = vec(0, 0, 0)     # ball initial velocity
pre_ball_v = 10
dt = 0.001  
time = 0              
while abs(ball.v.mag-pre_ball_v) > 0.00001: # until the ball hit the ground
    rate(5000)            # run 1000 times per real second
    pre_ball_v = mag(ball.v)
    ball.pos += ball.v*dt
    ball.v += vec(0, -g, 0)*dt - C_drag*ball.v*dt

    time += dt                                #drawing v-t graph
    funct.plot(pos=(time, ball.v.mag))
    
print('final speed = %3.4f m' % mag(ball.v))