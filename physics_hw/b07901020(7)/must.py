#videos: https://youtu.be/2OyVkOD5CjE
import numpy as np
from vpython import *
A, N, omega = 0.10, 50, 2*pi/1.0
size, m, k, d = 0.06, 0.1, 10.0, 0.4
scene = canvas(title='Spring Wave', width=800, height=300, background=vec(0.5,0.5,0), center = vec((N-1)*d/2, 0, 0))
c = curve([vector(i*d, 1.0, 0) for i in range(N)], color=color.black)
Unit_K, n = 2 * pi/(N*d), 10
Wavevector = n * Unit_K
phase = Wavevector * arange(N) * d
ball_pos, ball_orig, ball_v, spring_len = np.arange(N)*d + A*np.sin(phase), np.arange(N)*d, np.zeros(N), np.ones(N)*d
t, dt = 0, 0.0003
pre_state = ball_v[7]
while True:
    rate(1000)
    t += dt
    pre_pre_state = pre_state
    pre_state = ball_pos[7]
    spring_len[:-1] = abs(ball_pos[1:]-ball_pos[:-1])
    spring_len[49] = abs(ball_pos[0]+50*d - ball_pos[49])
    ball_v[1:] += ( -k*(spring_len[:-1]-d) + k*(spring_len[1:]-d) )/m*dt              #6
    ball_v[0] += ( -k*(spring_len[49] -d) + k*(spring_len[0] - d) )/m*dt
    ball_pos += ball_v*dt
    ball_disp = ball_pos - ball_orig
    for i in range(N):
        c.modify(i, y = ball_disp[i]*4+1)
    if pre_state > ball_pos[7] and pre_state > pre_pre_state and t > 0.1:
        print('Period: %2.5f s, Angular Frequency: %2.5f theta/s'%(t, 2*pi/t))
        t = 0
    