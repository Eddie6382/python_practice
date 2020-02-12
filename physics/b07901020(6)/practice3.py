from vpython import *
size, m = 0.02, 0.2  # ball size = 0.02 m, ball mass = 0.2kg
L, k = 0.2, 20       # spring original length = 0.2m, force constant = 20 N/m
amplitude = 0.03
b = 0.05 * m * sqrt(k/m)

power = graph(width=1000, align='left', xtitle='t', ytitle='average power', background=vec(0.5,0.5,0))
avg_p = gdots(color=color.red, graph=power)
# =========== delete below in practice 3 ===========
class obj:
    pass
    
wall_left, ball, spring = obj(), obj(), obj()
# =========== delete above in practice 3 ===========

ball.pos = vector(L, 0 , 0)  # ball initial position
ball.v = vector(0, 0, 0)               # ball initial velocity
ball.m = m
spring.pos = vector(0, 0, 0)
sum_p = 0
T = 2*pi/(1*sqrt(k/m))
t, dt = 0, 0.001
pre_avg_p = 0

while True:

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
    if int(t*1000) % int(T*1000) == 0 :
        avg_p.plot(pos=(t,sum_p/T))
        if abs(pre_avg_p - sum_p/T) < 5E-10:
            break
        pre_avg_p = sum_p/T
        sum_p = 0
    # =========== delete above in practice 3 ===========
print(sum_p/T)