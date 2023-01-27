#!/usr/bin/env python3

# Homework 3: Kiusalaas Set
# COSC370
# Swasti Mishra // netid: smishr11
# July 21, 2022

from numpy import array,zeros
from choleski import *
from gaussElimin import *

# Correct Output: 
# [ 1.66666667  2.66666667  2.66666667]
# See displacement formula in the textbook- unfortunately I can't comment
#   or provide more rationale than that?
k = array([1, 2, 1, 1, 2], float)
W = array([2, 1, 2], float)
a = zeros((3, 3))
a[0, 0] = k[0] + k[1] + k[2] + k[4]
a[0, 1] = -k[2]
a[1, 0] = -k[2]
a[0, 2] = -k[4]
a[2, 0] = -k[4]
a[1, 1] = k[2] + k[3]
a[1, 2] = -k[3]
a[2, 1] = -k[3]
a[2, 2] = k[3] + k[4]
L = choleski(a)
x = choleskiSol(L,W)
print("Displacements are (in units of W/k):\n\n",x)
print("--------------------------------------------")

# Correct Outputs:
# R = 5.0 ohms
# The currents are (in amps):
# [ 2.82926829 1.26829268 4.97560976]
# R = 10.0 ohms
# The currents are (in amps):
# [ 2.66666667 1.33333333 4.88888889]
# R = 20.0 ohms
# The currents are (in amps):
# [ 2.4516129 1.41935484 4.77419355]
# Same comment as above- the numbers in the array correspond 
#   directly to the problem
R = [5.0, 10.0, 20.0]
for r in R:
   a = zeros([3, 3])
   a[0,:] = [50 + r, -r, -30]
   a[1,:] = [-r , 65 + r, -15]
   a[2,:] = [-30, -15, 45]
   b = array([0.0, 0.0, 120.0])
   print("\nR =",r,"ohms")
   print("The currents are (in amps):\n",gaussElimin(a,b))
print("--------------------------------------------")

# Correct Output:
# The loop currents are (in amps):
# [-4.18239492 -2.66455194 -2.71213323 -1.20856463]
a = zeros([4, 4])
a[0,:] = [80, -50, -30, 0]          # The first "bar" of the circuit
a[1,:] = [-50, 100, -10, -25]       # The second row of "bars" on the circuit
a[2,:] = [-30, -10, 65, -20]        # etc
a[3,:] = [0, -25, -20, 100]         # etc
b = array([-120, 0, 0, 0], float)
print("The currents are (in amps):\n",gaussElimin(a,b))

input("Press return to exit")
