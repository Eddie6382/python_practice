'''
video resource: https://youtu.be/d7P4uhUMT1o
'''


from vpython import *
size, m = 0.02, 0.2  # ball size = 0.02 m, ball mass = 0.2kg
L, k = 0.2, 20       # spring original length = 0.2m, force constant = 20 N/m
amplitude = 0.03
b = 0.05 * m * sqrt(k/m)

power = graph(width=1000, align='left', xtitle='omega', ytitle='average power', background=vec(0.5,0.5,0))
avg_p = gdots(color=color.red, graph=power)
class obj:
    pass
    
wall_left, ball, spring = obj(), obj(), obj()


omega = [0.1*i + 0.7*sqrt(k/m) for i in range(1, int(0.5*sqrt(k/m)/0.1))]
p_list = []
for omega_d in omega:
    ball.pos = vector(L, 0 , 0)  # ball initial position
    ball.v = vector(0, 0, 0)     # ball initial velocity
    ball.m = m
    spring.pos = vector(0, 0, 0)
    sum_p = 0
    T = 2*pi/omega_d
    t, dt = 0, 0.001
    pre_avg_p = 0
    while True:
        spring.axis = ball.pos - spring.pos # spring extended from spring endpoint A to ball
        spring_force = -k * (mag(spring.axis) - L) * norm(spring.axis) # spring force vector
        res_force =  -b*ball.v
        sinu_force = 0.1*sin(omega_d*t)*vector(1,0,0)
        ball.a = (spring_force + res_force + sinu_force) / ball.m     # ball acceleration = spring force /m - damping
        ball.v += ball.a*dt
        ball.pos += ball.v*dt
        t += dt
    
        sum_p += dot(sinu_force,ball.v)*dt
        if int(t*1000) % int(T*1000) == 0 :
            if abs(pre_avg_p - sum_p/T) < 1E-9:
                break
            pre_avg_p = sum_p/T
            sum_p = 0
    avg_p.plot(pos=(omega_d,sum_p/T))
    p_list.append((sum_p/T,omega_d))
print(max(p_list)[1])
    

    