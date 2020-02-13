from vpython import*
class metronome:
    def __init__(self,f,theta,length,pos):
        self.rod = cylinder(pos = pos + vector(sin(theta), -cos(theta), 0)*1/4*length, 
                            axis = vector(-sin(theta), cos(theta), 0)*length, radius = length/35)
        self.shell = box(pos = pos + vector(0,0.04,-0.03), length=0.06, height=0.16, width=0.04, color=color.red)
        self.glass = box(pos = pos + vector(0,0.08,-0.01), length=0.04, height=0.07, width=0.001, color=vector(0.5,0.5,0.5))
        self.balance = box(pos = pos + vector(sin(theta), -cos(theta), 0)*1/5*length, axis = vector(-sin(theta), cos(theta), 0), size = vector(0.02, 0.03, 0.01))
        self.bearing = cylinder(pos = pos, axis = vector(0,0,-0.02), radius = 0.002, color = color.black)
        self.pos = pos
if __name__ == '__main__':
    f = 2
    theta = -pi/6
    length = 0.15
    a1 = metronome(f,theta,length,vector(0,0,0))
    dt = 0.001
    t = 0
    while t<=1:
        rate(200)
        a1.rod.rotate(angle = f*2*pi*dt, axis=vector(0,0,1), origin=a1.pos)
        a1.balance.rotate(angle = f*2*pi*dt, axis=vector(0,0,1), origin=a1.pos)
        t += dt
        
