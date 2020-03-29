#videos: https://youtu.be/GQ_ECQEB9S8

from vpython import * 
from diatomic import *

N = 20                                 # 20 molecules
L = ((24.4E-3/(6E23))*N)**(1/3.0)/50   # 2L is the length of the cubic container box, the number is made up
m = 14E-3/6E23                         # average mass of O and C
k, T = 1.38E-23, 298.0                 # some constants to set up the initial speed
initial_v = (3*k*T/m)**0.5             # some constant

scene     = canvas(width = 400, height =400, align = 'left', background = vec(1, 1, 1)) 
container = box(length = 2*L, height = 2*L, width = 2*L, opacity=0.4, color = color.yellow ) 
energies  = graph(width = 600, align = 'left', ymin=0, xtitle='t(s)', ytitle='average energy(J)')

c_avg_com_K = gcurve(color = color.green)
c_avg_v_P   = gcurve(color = color.red)
c_avg_v_K   = gcurve(color = color.purple)
c_avg_r_K   = gcurve(color = color.blue)
com_K, v_K, v_P, r_K = 0, 0, 0, 0

COs=[]

for i in range(N):                     # initialize the 20 CO molecules
    O_pos = vec(random()-0.6, 1.2*(random()-0.5), 1.2*(random()-0.5))*1.3*L       # random() yields a random number between 0 and 1 
    CO = CO_molecule(pos=O_pos, axis = vector(1.0*d, 0, 0))       # generate one CO molecule
    CO.C.v = vector(initial_v*random(), initial_v*random(), initial_v*random())    # set up the initial velocity of C randomly 
    CO.O.v = vector(initial_v*random(), initial_v*random(), initial_v*random())    # set up the initial velocity of O randomly 
    COs.append(CO)                     # store this molecule into list COs
    
times = 0                              # number of loops that has been run
dt    = 5E-16 
t     = 0
while True:
    rate(2000) 
    for CO in COs:
        CO.time_lapse(dt)
        
    for i in range(N-1):               # the first N-1 molecules
        for j in range(i+1,N):         # from i+1 to the last molecules, to avoid double checking
            for atom in (COs[i].C, COs[i].O):
                for other_atom in (COs[j].C, COs[j].O):
                    if mag(atom.pos-other_atom.pos) < 2*size and t > 10E-13:
                        atom.v, other_atom.v = collision(atom, other_atom)          
        ## change this to check and handle the collisions between the atoms of different molecules 
        
    for CO in COs:
        for atom in (CO.O, CO.C):
            if abs(atom.pos.x) > L-size:
                atom.v.x = -atom.v.x
            if abs(atom.pos.y) > L-size:
                atom.v.y = -atom.v.y
            if abs(atom.pos.z) > L-size:
                atom.v.z = -atom.v.z
            ## change this to check and handle the collision of the atoms of all molecules on all 6 walls
    t += dt
    
    for CO in COs:
        com_K += CO.com_K()*dt
        v_K += CO.v_K()*dt
        v_P += CO.v_P()*dt
        r_K += CO.r_K()*dt

    c_avg_com_K.plot(pos=(t,com_K/t))
    c_avg_v_K.plot(pos=(t,v_K/t))
    c_avg_v_P.plot(pos=(t,v_P/t))
    c_avg_r_K.plot(pos=(t,r_K/t))
    
    ## sum com_K, v_K, v_P, and r_K for all molecules, respectively, to get total_com_K, total_v_K, total_v_P, total_r_K at the
    ## current moment
    
    ## calculate avg_com_K to be the time average of total_com_K since the beginning of the simulation, and do the same 
    ## for others.
    
    ## plot avg_com_K, avg_v_K, avg_v_P, and avg_r_K