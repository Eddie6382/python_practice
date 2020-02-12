from vpython import *
g=9.8                     # g = 9.8 m/s^2
size = 0.25               # ball radius = 0.25 m
theta = pi/4              # initial angle
C_drag = 0.9              # drag cofficient a = -b*v
displacement = [0]*3
highest = [0]*3 
msg = [0]*6
scene1 = canvas(align = 'left', center = vec(0,5,0), width=600, background=vec(0.5,0.5,0))
floor = box(length=30, height=0.01, width = 10, color = color.blue)
ball = sphere(radius = size, color = color.red, make_trail = True, trail_radius = size/3)
vt_graph = graph(width = 300, align ='left', xmin = 0, xmax = 6, ymin = 0, ymax = 25,
                 xtitle = 'time(s)', ytitle = 'speed(m/s)')
funct = gcurve(graph = vt_graph, color = color.blue, width =4)

ball.pos = vec( -15.0, size, 0.0)
ball.v = vec(20*cos(theta), 20*sin(theta), 0)
pre_x = vec(ball.pos.x, ball.pos.y, ball.pos.z)            #vector
pre_y = ball.pos.y                                         #value
number = 1
time = 0
dt = 0.001

while number <= 3:                             
    rate(1000)
    pre_pre_y = pre_y                          #use to check the heightest point of the ball
    pre_y = ball.pos.y
    
    ball.pos += ball.v*dt
    ball.v += vec(0,-g,0)*dt - C_drag*ball.v*dt

    time += dt                                #drawing v-t graph
    funct.plot(pos=(time, mag(ball.v)))
    
    if ball.pos.y <= size and ball.v.y < 0:   # check if ball hits the ground
        ball.v.y = - ball.v.y                 # if so, reverse y component of velocity
        displacement[number-1] = mag(ball.pos-pre_x)
        pre_x = vec(ball.pos.x, ball.pos.y, ball.pos.z)
        number += 1

    if pre_y > ball.pos.y and pre_y > pre_pre_y:   #check if the ball reach the heightest point
        highest[number-1] = pre_y

for i in range(0,3):
    print('The distance in',i+1,'th bounce = %3.4f' % displacement[i])
for j in range(0,3):
    print('The highest point in',j+1,'th bounce = %3.4f' % highest[j])

msg = text(text = 'The distance of entire displacement = %3.4f' % sum(displacement), pos = vec(-10,10,0))
msg = text(text = 'The highest point h = %3.4f' % max(highest), pos = vec(-10,8,0))


