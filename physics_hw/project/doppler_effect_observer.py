from vpython import *
f = 25
T = 1/f
v0 = 340
t = 0
dt = 0.001
r = 150
n = 0       #source receive n raflected wave
tt = 0
ttt = 0
v = 170
prev = 0
now = 0
b={}
oscillation = graph(width=400, xtitle='t', ytitle='f', background=vec(1, 1, 1))
x = gcurve(color=color.red, graph=oscillation)

waves = []
scene = canvas(width=800, height=800, background=vector(0.5,0.5,0))
source = sphere(radius = 10, make_trail = True,color = vec(10,0,0))
source.pos = vec(-r,0,0)
obs = sphere(radius = 10, make_trail = True,color = vec(0,0,10))
obs.pos = vec(0,0,0)
source.v = vec(v,0,0)
count = False
while n <= 1500:
	rate(300)
	if tt >= T:
		wavefront = ring(pos = source.pos, axis = vec(0,0,1), thickness = 0.5, radius = 0)
		waves.append(wavefront)
		tt -= T
	for wave in waves:
		wave.radius += v0*dt
		if abs(wave.pos.x-obs.pos.x)< wave.radius:
				now = t
				b[t] = now-prev
				prev = now
				wave.visible = False
				waves.remove(wave)
				del wave
				n+=1
				
	t += dt
	ttt += dt
	
	tt += dt
	n += 1
	obs.pos += obs.v*dt
for a in b:
    del b[a]
    break
for i in b:
    x.plot(pos = (i,1/b[i]))
