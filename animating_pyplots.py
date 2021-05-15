import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation


# define acceleration in "return"...
# Caution: use numpy as np


def get_acceleration(position, velocity):
    return -9.8*np.sin(position) - 0.2 * velocity


# some global variables
total_time = 10           # total time of motion
e = 0.001                     # small time interval
mass = 3                    # mass of particle(in Kg)

# Provide initial values
init_x = 1
init_v = -5

# creating lists to store positions, velocities, accelerations and time

pos_list, vel_list, accln_list, force_list = ([]for i in range(4))

# Initialising variables
a = get_acceleration(init_x, init_v)           # acceleration
accln_list.append(a)

whole_x = init_x                               # for positions at times 0.1s, 0.2s, 0.3s ...
pos_list.append(whole_x)

whole_v = init_v                               # for velocities at times 0.1s, 0.2s, 0.3s ...
vel_list.append(whole_v)

half_x = init_x + (init_v * (e / 2))           # for positions at times 0.05 s, 0.15 s, 0.25 s ...
pos_list.append(half_x)

half_v = init_v + (a * (e / 2))                # for velocities at times 0.05 s, 0.15 s, 0.25 s, 0.35 s ...
vel_list.append(half_v)

t = e

while t <= total_time:
    whole_x += half_v * e
    pos_list.append(whole_x)

    a = get_acceleration(half_x, half_v)
    accln_list.append(a)

    whole_v += a * e
    vel_list.append(whole_v)

    half_x += whole_v * e
    pos_list.append(half_x)

    a = get_acceleration(whole_x, whole_v)
    accln_list.append(a)

    half_v += a * e
    vel_list.append(half_v)

    t += e

# Removing last elements of position list and velocity list
# to match the lengths of the arrays
pos_list.pop()
vel_list.pop()

# Creating time_list
time_list = np.linspace(0, total_time + e/2, len(pos_list))

# Creating Force list
for i in accln_list:
    force_list.append(mass*i)

# Further program is for Animation
fig = plt.figure()
ax = plt.subplot(1, 1, 1)

data_skip  = 50
#
def init_func():
    ax.clear()
    plt.xlabel('time')
    plt.ylabel('theta')

def animating_positions(i):
    ax.plot(time_list[i:i+data_skip], pos_list[i:i+data_skip], color='r', label='postions')
    plt.xlim(time_list[0], time_list[-1])
    plt.ylim((-20, 20))

anim = FuncAnimation(fig, animating_positions, frames=np.arange(0, len(time_list), data_skip), init_func=init_func, interval=10)

def animating_velocities(i):
    ax.plot(time_list[i:i+data_skip], vel_list[i:i+data_skip], color='b', label='velocities')
    plt.xlim(time_list[0], time_list[-1])
    plt.ylim((-20, 20))

anim1 = FuncAnimation(fig, animating_velocities, frames=np.arange(0, len(time_list), data_skip), init_func=init_func, interval=10)

def animating_acceln(i):
    ax.plot(time_list[i:i+data_skip], accln_list[i:i+data_skip], color='g', label='acceleration')
    plt.xlim(time_list[0], time_list[-1])
    plt.ylim((-20, 20))

anim3 = FuncAnimation(fig, animating_acceln, frames=np.arange(0, len(time_list), data_skip), init_func=init_func, interval=10)

plt.legend()
plt.show()



