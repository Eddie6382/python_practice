from vpython import *   #https://youtu.be/NnHr3FdWTos
f = 25
T = 1/f
v0 = 340
t = 0
dt = 0.0002
r = 150
n = 0       #source receive n raflected wave
tt = 0
v = 68
waves = []
reflect_wave = []
scene = canvas(width=800, height=800, background=vector(0.5,0.5,0))
source = sphere(radius = 10, make_trail = True,color = vec(10,0,0))
source.pos = vec(-r,0,0)
obj = sphere(radius = 10, make_trail = True,color = vec(0,0,10))
obj.pos = vec(0,0,0)
obj.v = vec(v,0,0)
count = False
while n<=7:
    rate(1000)
    for wave in reflect_wave:
        wave.radius += v0*dt
        if wave.pos.x - wave.radius < source.pos.x:
            wave.visible = False
            reflect_wave.remove(wave)
            del wave
            count = True
            n += 1
            #reflect_wave.remove(wave)
    for wave in waves:
        wave.radius += v0*dt
        if wave.pos.x + wave.radius > obj.pos.x:
            wave.visible = False
            waves.remove(wave)
            del wave
            wavefront = ring(pos = obj.pos, axis = vec(0,0,1), thickness = 0.5, radius = 0, color = color.red)
            reflect_wave.append(wavefront)
    if tt >= T:
        wavefront = ring(pos = source.pos, axis = vec(0,0,1), thickness = 0.5, radius = 0)
        waves.append(wavefront)
        tt -= T
    if count:
        t += dt
    tt += dt
    obj.pos += obj.v*dt
receive_f = (n-1)/(t-3*dt)
print("f is: ",receive_f, (n-1), t-3*dt)
print("v is: ",v0*(f-receive_f)/(f+receive_f))