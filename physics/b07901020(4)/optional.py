from vpython import *

g = 9.8
size, m = 0.05, 0.5
L, k = 2, 15000
angle = pi/6
omega = 2*pi/86400
latitude = 23.5*pi/180
c = 20     
'''
in order to accelerate the procedure of Foucault pendulum, i add a prameter 'c', which means 
'time magnification factor', it also means that I accelerate the speed of rotation 'c' times
faster.
'''         

scene = canvas(width=500, height=500, center=vec(0, -1, 0), background=vec(0.5, 0.5, 0))
ceiling = box(length=0.8, height=0.005, width=0.8, color=color.blue)
ball = sphere(radius=size, color=color.red, make_trail=True, trail_type="points",
              interval=20, trail_radius = 0.1*size)
spring = cylinder(radius=0.01)   # default pos = vec(0, 0, 0)
ball.v = vec(0.00001, 0, 0)
ball.pos = vec(-sin(angle)*L, -cos(angle)*L, 0)
x_axis = vec(1,0,0)

slab = label(pos=vec(0.4,-1.2,0), box = True)
mlab = label(pos=vec(0.2,-1.2,0), box = True)
hlab = label(pos=vec(0, -1.2,0), box = True)
dlab = label(pos=vec(-0.2, -1.2,0), box = True)
tlab = label(pos=vec(0.1, -1.6,0), box = False, text=str('time magnification factor c: '+str(c)))
plab = label(pos=vec(0.1, -1.4,0), box = True)
rlab = label(pos=vec(0, -2, 0), box = False)

count = 0
dt = 0.001
t = 0
period = 0
ball_v_vec = vec(ball.v.x, 0, ball.v.z)
center = vec(0, -cos(angle)*L, 0)
pre_x = mag(ball.pos-center)
while True:
    rate(2000)
    t += dt
    period += dt
    
    #use two different variables to store distance from ball to center in three different time
    pre_pre_x = pre_x                                              
    pre_x = mag(ball.pos - center)

    spring.axis = ball.pos - spring.pos                                # spring extended from endpoint to ball
    spring_force = - k * (mag(spring.axis) - L) * spring.axis.norm()   # to get spring force vector
    Coriolis_ac = - 2 * cross(vec(0,sin(latitude),-cos(latitude)),ball.v)*omega*c  # Coriolis force, c means 'time magnification factor'
    ball.a = vector(0, - g, 0) + spring_force / m  +  Coriolis_ac            
    ball.v += ball.a*dt                                      
    ball.pos += ball.v*dt
    ball_v_vec = vec(ball.v.x, 0, ball.v.z)

    cos_angle = abs(dot(x_axis,ball_v_vec))/(mag(x_axis)*mag(ball_v_vec))
    if mag(ball.v)>0.5:
        deltaangle = acos(cos_angle)*180/pi                         #claculate the deltaangle
        plab.text = str('deltaangle: %2.3f degree'%deltaangle)
    if pre_x > mag(ball.pos - center) and pre_x > pre_pre_x:
        count += 1
        if count == 2*1000/c:
            rlab.text = str('deltaangle = %2.4f degree after 1000 periods of pendulum'%deltaangle)

    sec = (t*c//1)%60
    mi = (t*c//60)%60
    hr = (t*c)//3600%24
    day = (t*c)//86400
    slab.text = str('%1.0fS'%sec)
    mlab.text = str('%1.0fM'%mi)
    hlab.text = str('%1.0fH'%hr)
    dlab.text = str('%1.0fD'%day)
    
