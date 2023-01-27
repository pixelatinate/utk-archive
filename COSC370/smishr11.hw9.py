#!/usr/bin/env python3

# Homework 9: Romberg Integration for Heat Capacity
# COSC370
# Swasti Mishra // netid: smishr11
# August 7, 2022

# In this problem, we use Romberg Integration to evaluate integrals. Romberg
# Integration is part Richardson Extrapolation and part trapezoidal rule. In 
# this case, we're approximating the integral for a function from 0 to 1/u.

from romberg import *
from numpy import *
import matplotlib.pyplot as plt

# Defines the integrable function here
def f(x):
  if x == 0: return 0
  else: return (x ** 4 * exp(x)) / ((exp(x) - 1) ** 2)

# Lists that will contain all of g(u)s
u = arange(0, 1.01, 0.05)
print ("    u\t   g(u)")
gu = []

# Performs romberg integration on f and evaluate g(i) here
for i in u:
  if i == 0: g = 0.0;
  else:
    I,nPanels = romberg(f, 0, (1 / i))
    g = i ** 3 * I
  print ('{:6.2f}{:13.6f}'.format(i,g))
  gu.append(g)

# Make graph
plt.title("Problem 6.1.14")
plt.axis([0.0, 1.0, 0.00, 0.35])
plt.xlabel("u")
plt.ylabel("g(u)")
plt.tick_params(direction='inout')
plt.plot(u, gu, 'b-')
plt.savefig("prob6_1_14.png")

# Table written to stdout for verification purposes:
#
#  u      g(u)
# 0.00     0.000000
# 0.05     0.003247
# 0.10     0.025274
# 0.15     0.070997
# 0.20     0.122878
# 0.25     0.167686
# 0.30     0.202568
# 0.35     0.228858
# 0.40     0.248618
# 0.45     0.263608
# 0.50     0.275136
# 0.55     0.284136
# 0.60     0.291265
# 0.65     0.296992
# 0.70     0.301651
# 0.75     0.305487
# 0.80     0.308678
# 0.85     0.311359
# 0.90     0.313631
# 0.95     0.315573
# 1.00     0.317244