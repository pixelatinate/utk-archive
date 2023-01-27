#!/usr/bin/env python3

# Homework 7: Determine Trajectory and Angle for Orbiting Satellite
# COSC370
# Swasti Mishra // netid: smishr11
# August 4, 2022

from newtonRaphson2 import *
from math import sin, pi
import numpy as np
import matplotlib.pyplot as plt

# The trajectory of a satellite orbiting the earth is given by the equation
#
# R = C/(1+e*sin(theta + alpha)), which can also be written as
# R - C/(1+e*sin(theta + alpha)) = 0 (in order to exploit rootfinding methods).

# Where...
# R is the distance from the Earth to the satellite
# Theta is the angle from R
# C is a constant, the first value in array x
# e is a constant, the second value in array x
# alpha is a constant, the third value stored in array x
# x stores all of our predictions about the satellite's location

# The vector-valued function F(x) whose root defines a system of 3
# trajectory equations (using given data); uses radians for all angles.

# F[j] returns the left-hand-side of [Eqn1] where R and theta are given
# by the jth data pair.
def F(x):
    F = zeros((len(x)), dtype = float64)
    F[0] = 6870 - x[0] / (1 + x[1] * sin((-pi/6) + x[2]))
    F[1] = 6728 - x[0] / (1 + x[1] * sin(x[2]))
    F[2] = 6615 - x[0] / (1 + x[1] * sin((pi/6) + x[2]))
    return F

# Initial guess, list initialized to use Newton-Raphson
x = np.array([6800, 0.5, 0])

# Completes the call to the N-R method to solve for unknowns
x = newtonRaphson2(F, x)

# Prints the solution vector x from N-R
print()
np.set_printoptions(precision = 3)
print('[ C  e  alpha] = ' + np.array_str(x))

# Calculates the minimum trajectory and angle using components of x
minTheta = (pi / 2.0 - x[2]) * 180.0 / pi
minR = x[0] / (1 + x[1])

# Prints minimum trajectory results
print('Minimum trajectory = %.3f km' % minR)
print('Angle at which minimum trajectory occurs = %.3f degrees' % minTheta)
print()

# Creates arrays of points spaced every 0.01 radians around the satellite orbit
# (theta) and their respective trajectories (R)
theta = np.arange(0, 2*pi, 0.01)            # theta and R are arrays now
R = x[0] / (1 + x[1]*np.sin(theta + x[2]))

# Plots orbit and minimum trajectory point
ax = plt.subplot(111, polar = True)
ax.plot(theta, R, color = 'r', linewidth = 2, label = 'Path')
ax.plot(minTheta, minR, 'bo', label = 'Min')
ax.legend(numpoints = 1)
ax.grid(True)
ax.set_title("Satellite path")
plt.show()