from vpython import *

g = 9.8
size, m = 0.05, 0.2
L, k = 0.5, [15, 12, 17]
v = [1, 2, 2.2]
d = [-0.06, 0, -0.1]

scene = canvas(width=400, height=400, center =vec(0.4, 0.2, 0), align = 'left', background=vec(0.5,0.5,0))
floor = box(pos = vec(0.4, 0, 0), length=0.8, height=0.005, width=0.8, color=color.blue)
wall = box(pos= vec(0, 0.05, 0), length = 0.01, height = 0.1, width =0.8)
KP_graph = graph(width = 400, align ='left', xtitle = 'time(s)', ytitle = 'Energy(J)')
kinetic_curve = gcurve(graph = KP_graph, color = color.blue, width =4)
potential_curve = gcurve(graph = KP_graph, color = color.red, width = 4)
avg_KP_graph = graph(width = 400, align ='left', xtitle = 'time(s)', ytitle = 'Average Energy(J)')
avg_K_curve = gcurve(graph = avg_KP_graph, color = color.blue, width =2)
avg_P_curve = gcurve(graph = avg_KP_graph, color = color.red, width =2)

balls = []
for i in range(3):
    ball = sphere(pos = vec(L+d[i], size, (i-1)*3*size), radius = size, color=color.red) 
    ball.v = vec(v[i], 0, 0)
    balls.append(ball)
    
springs =[]
for i in range(3):
    spring = helix(pos = vec(0, size, (i-1)*3*size), radius=0.02, thickness =0.01) 
    spring.axis = balls[i].pos-spring.pos
    spring.k = k[i]
    springs.append(spring)

dt = 0.001
time = 0
avg_K_energy = 0
avg_P_energy = 0
while True:
    rate(1000)
    kinetic_energy = 0
    potential_energy = 0
    for i in range(3):
        springs[i].axis = balls[i].pos - springs[i].pos
        spring_force = -k[i]*(mag(springs[i].axis)-L)*springs[i].axis.norm()  #f = -kx x means deformation of the string
        balls[i].a = spring_force/m
        balls[i].v += balls[i].a*dt
        balls[i].pos += balls[i].v*dt
        kinetic_energy += 0.5*m*(mag(balls[i].v)**2)
        potential_energy += 0.5*k[i]*(mag(springs[i].axis)-L)**2

    time += dt
    kinetic_curve.plot(pos=(time,kinetic_energy))
    potential_curve.plot(pos=(time,potential_energy))
    avg_K_energy += kinetic_energy
    avg_P_energy += potential_energy
    avg_K_curve.plot(pos=(time,avg_K_energy/(time/dt)))
    avg_P_curve.plot(pos=(time,avg_P_energy/(time/dt)))
