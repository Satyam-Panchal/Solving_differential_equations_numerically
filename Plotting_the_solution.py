import numpy as np
import matplotlib.pyplot as plt
from tabulate import  tabulate

# define acceleration in "return"...
# Caution: use numpy as np


def get_acceleration(position, velocity):
    return np.sin(position) + np.cos(velocity)


# some global variables
total_time = 5              # total time of motion
e = 0.0001                     # small time interval
mass = 3                    # mass of particle(in Kg)

# Provide initial values
init_x = 0
init_v = 0

# creating lists to store positions, velocities, accelerations and force (with respect to time)

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

# creating table
empty_array = np.empty((len(time_list), 0), float)

empty_array = np.append(empty_array, np.array([time_list]).transpose(), axis=1)
empty_array = np.append(empty_array, np.array([pos_list]).transpose(), axis=1)
empty_array = np.append(empty_array, np.array([vel_list]).transpose(), axis=1)
empty_array = np.append(empty_array, np.array([accln_list]).transpose(), axis=1)

print(tabulate(empty_array))

# Creating Force list
for i in accln_list:
    force_list.append(mass*i)

# Plotting

plt.plot(time_list, pos_list, 'r', label='position')
plt.plot(time_list, vel_list, 'b--', label='velocity')
plt.plot(time_list, accln_list, 'c--', label='acceleration')
# plt.plot(np.linspace(0, total_time + e/2, len(force_list)), force_list, 'k--', label='Force')          # uncomment to plot force vs t graph

# Editing Graphs
plt.title('Position, Velocity and Acceleration of a particle in force field')
plt.legend()

plt.show()





