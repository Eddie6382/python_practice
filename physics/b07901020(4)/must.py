from vpython import*

N = int(input('How many balls to be lifted?[1-4]'))
NN, size = 5, 1
m = [4,4,4,4,4]
angle = pi/6
k, L = 15000, 16
g = 9.8
balls_reference, balls, balls_stick = [0]*5, [0]*5, [0]*5
scene = canvas(width=500, height=500, center=vec(0, 0, 0), background=vec(0.5, 0.5, 0))
ceiling = box(length=18, height=0.4, width=1, pos=vec(0,8,0), color=color.blue)
for i in range(NN):
    balls_reference[i] = sphere(pos=vec(-4+2*i,8,0), radius=0.4)
    balls_stick[i] = cylinder(radius=0.2, pos=vec(-4+2*i,8,0), axis=vec(0,-L,0))
    balls[i] = sphere(pos=vec(-4+2*i,-8,0), radius=size, color=color.black)
    balls[i].v = vec(0,0,0)
for i in range(N):
    balls_stick[i].axis = vec(-sin(angle),-cos(angle),0)*L
    balls[i].pos = balls_stick[i].pos + balls_stick[i].axis

def af_col_v(m1, m2, v1, v2, x1, x2):          # function after collision velocity
    v1_prime = v1 + 2*(m2/(m1+m2))*(x1-x2) * dot (v2-v1, x1-x2) / dot (x1-x2, x1-x2)
    v2_prime = v2 + 2*(m1/(m1+m2))*(x2-x1) * dot (v1-v2, x2-x1) / dot (x2-x1, x2-x1)
    return (v1_prime, v2_prime)

dt = 0.0005
time = 0
while True:
    rate = (2000)
    for i in range(NN):
        balls_stick[i].axis = balls[i].pos - balls_stick[i].pos
        spring_force = -k * (mag(balls_stick[i].axis) - L) * balls_stick[i].axis.norm()
        balls[i].a = vector(0,-g,0) + spring_force / m[i]
        balls[i].v += balls[i].a*dt
        balls[i].pos += balls[i].v*dt
    for i in range(NN-1):
        if (mag(balls[i].pos-balls[i+1].pos)) <= 2*size and dot(balls[i].pos-balls[i+1].pos, balls[i].v-balls[i+1].v) <= 0:
            balls[i].v, balls[i+1].v = af_col_v (m[i], m[i+1], balls[i].v, balls[i+1].v, balls[i].pos, balls[i+1].pos)