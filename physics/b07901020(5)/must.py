from vpython import*
G = 6.673E-11
mass = {'earth': 5.97E24, 'moon': 7.36E22, 'sun':1.99E30}
radius = {'earth': 6.371E6*10, 'moon': 1.317E6*10, 'sun':6.95E8*10} #10 times larger for better view 
earth_orbit = {'r': 1.495E11, 'v': 2.9783E4}
moon_orbit = {'r': 3.844E8, 'v': 1.022E3}
theta = 5.145*pi/180.0
scene = canvas(width=800, height=800, background=vector(0.5,0.5,0))
scene.lights = []
sun = sphere(pos=vector(0,0,0), radius=radius['sun'], m=mass['sun'], color = color.orange, emissive=True)
local_light(pos=vector(0,0,0))
sun.v = vector(0,0,0)
earth = sphere( m = mass['earth'], radius = radius['earth'], texture = {'file':textures.earth})
moon = sphere(m = mass['moon'], radius = radius['moon'], color = color.white)
earth.pos = vector(earth_orbit['r'], 0, 0) + (mass['moon']/(mass['earth']+mass['moon']))*moon_orbit['r']*vector(cos(theta),-sin(theta),0)
earth.v = vector(0, 0, -earth_orbit['v']) + (mass['moon']/mass['earth'])*vector(0, 0, -moon_orbit['v'])
nor_orbit = arrow(pos=earth.pos, axis=20E6*10*vector(sin(theta),cos(theta),0), shaftwidth=2E6*10)
moon.pos = vector(earth_orbit['r'], 0, 0) + -(mass['earth']/(mass['earth']+mass['moon']))*moon_orbit['r']*vector(cos(theta),-sin(theta),0)
moon.v = vector(0, 0, -earth_orbit['v']) + -vector(0, 0, -moon_orbit['v'])
scene.center = earth.pos
ylab = label(pos=earth.pos, box = True)
orbit = graph(width = 400, align ='left', xtitle = 'year', ytitle = 'diff_angle(degree)')
distance = gcurve(graph = orbit, color = color.blue, width =4)

def G_force(m1,m2):
    return -G*m1.m*m2.m/mag2(m1.pos-m2.pos)*norm(m1.pos-m2.pos)

dt=60*30  #30 min hr as dt
time = 0
pre_orbit = nor_orbit.axis
pre = time
while True:
    rate(4000)
    time += dt
    moon.a = (G_force(moon,earth) + G_force(moon,sun))/moon.m
    moon.v += moon.a*dt
    moon.pos += moon.v*dt
    earth.a = (G_force(earth,moon) + G_force(earth,sun))/earth.m
    earth.v += earth.a*dt
    earth.pos += earth.v*dt
    omega = cross(moon.pos-earth.pos, moon.v-earth.v)
    nor_orbit.pos = earth.pos
    nor_orbit.axis =  20E6*10*norm(omega)
    scene.center = earth.pos
    year = time/(86400*365)
    ylab.text = str('%2.2f Year'%year)
    ylab.pos = earth.pos
    dif_angle = (diff_angle(nor_orbit.axis, 20E6*10*vector(sin(theta),cos(theta),0)))*180/pi
    distance.plot(pos=(year,dif_angle))
    if dif_angle < 0.7 and abs(time-pre) > 86400*365 :
        print('presession period = ',(time-pre)/(365*86400))
        pre = time
        
