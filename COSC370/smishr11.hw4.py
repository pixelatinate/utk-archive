#!/usr/bin/env python3

# Homework 3: Kiusalaas Set
# COSC370
# Swasti Mishra // netid: smishr11
# July 21, 2022

from numpy import zeros, array, linalg
from conjGrad import *

# The 9 rows of Ax using the coefficient matrix and v values
def Ax(v):
    Ax = zeros((9)) * 1.0

    Ax[0] = -4 * v[0] + v[1] + v[3]
    Ax[1] = v[0] + -4 * v[1] + v[2] + v[4]
    Ax[2] = v[1] + -4 * v[2] + v[5]
    Ax[3] = v[0] + -4 * v[3] + v[4] + v[6]
    Ax[4] = v[1] + v[3] + -4 * v[4] + v[5] +v[7]
    Ax[5] = v[2] + v[4] + -4 * v[5] + v[8]
    Ax[6] = v[3] + -4 * v[6] + v[7]
    Ax[7] = v[4] + v[6] + -4 * v[7] + v[8]
    Ax[8] = v[5] + v[7] + -4 * v[8]
    
    return Ax

# Uses conjugate gradient method to return direction/iterations
b = array([0, 0, 100, 0, 0, 100, 200, 200, 300]) * (-1.0)
x = zeros((9)) * 1.0
tol = 1e-06
s1, numIter = conjGrad(Ax, x, b, tol)
print("\nThe solution is:\n",s1)
print("\nNumber of iterations =",numIter, "using Tol: ", 1e-06)

print("\n CG Convergence Test")
print("Iterations   Tolerance")

# Creates a loop to call conjGrad with these tolerances and obtain/print the iteration
for tol in [1e-02, 1e-04, 1e-06, 1e-08, 1e-10, 1e-12, 1e-14, 1e-16]:
  x = zeros((9))
  s2, numIter = conjGrad(Ax, x, b, tol)
  print('%6d      %8.1e'%(numIter, tol))

# Finally, prints error between the solutions using the 1.e-06 and 1.e-16 tolerances
print("\nError between vectors obtained with tol=1e-06 and tol=1e-16: ",linalg.norm(s1-s2),"\n")