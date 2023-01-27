#!/usr/bin/env python3

# Homework 2: LU Decomposition Methods
# COSC370
# Swasti Mishra // netid: smishr11
# July 19, 2022

from numpy import zeros, ones, array, float64, inf
from numpy import linalg
from LUdecomp import *

# 'linalg.norm' is renamed to just 'norm'.
norm = linalg.norm  

TOL = 0.000001                      # Set tolerance to 1.E-6 per lab directions
err = 0
n = 0
while err < TOL:
  n += 1
  a = zeros((n,n),dtype=float64)
  b = zeros((n),dtype=float64)
  soln = ones((n), dtype=float64)   # The correct solution is all 1's

  # The loops below define matrix 'a' and vector 'b':
  for i in range(n):
    for j in range(n):
      a[i,j] = 1/( i + j + 1 )      # Stores the coefficient matrix
      b[i] = b[i] + a[ i, j ]       # Adds up rows of the matrix 

  # Calls the appropriate functions from the LUdecomp.py module to
  #     solve the equations Ax = b with the b-vector being overridden
  #     by the solution vector x.
  a = LUdecomp(a)                   # Do the decomposition on matrix a...
  b = LUsolve(a,b)                  # ...And then solve for x

  # The solution is stored in 'b'
  print("\n", n, " equations. ", "The solution is:\n", b)
  err = norm(b-soln, ord=inf)
  print("Error (inf-norm of difference)): ", err)

print("^^^(Greater than TOL = ", TOL, ")^^^\n")
print("********************************************\n")
print("Max number of equations while error remains less than ", TOL, " is: ", n-1, "\n") 
print("********************************************")