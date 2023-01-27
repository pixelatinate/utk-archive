#!/usr/bin/env python3

# Homework 8: Approximation of Derivatives Using FDA, Richardson Extrapolation,
# and Polynomial Interpolation
# COSC370
# Swasti Mishra // netid: smishr11
# August 5, 2022

from numpy import round, array, polyfit, polyder, polyval

# In this problem, we're approximating f'(0.2) using the second-order Central
# FDA method and the Richardson Extrapolation method. The Central FDA will 
# set h to 0.2, and the Richardson Extrapolation method will use our previous
# approximation by halving h. This will give us a closer approximation.

print("Problem 5.1.9\n=============")

# This is an example of a dictionary with key:value pairs,
# e.g., data9[0.1]=0.078348 and data9[0.3]=0.192916
data9 = { 0.0: 0.0, 0.1: 0.078348, 0.2: 0.138910, 0.3: 0.192916, 0.4: 0.244981 }

# We approximate f'(0.2) using two different values of h (=0.2, 0.1)
# Using the central difference FDA, 2hf'(x) = -f(x-h) + f(x+h), with h=0.2
h1 = 0.2
x = 0.2
centralApprox1 = (-data9[x - h1] + data9[x + h1]) / (2 * h1)
print("Central FDA Approximation (h = 0.2): %f" % centralApprox1)

# We now halve the stepsize and set h=0.1 and use the function all
# round(x+h2, decimals=1) so we can ensure the proper key from the data9
# dictionary will be selected.
h2 = h1 / 2.0
centralApprox2 = (-(data9[round(x - h2, decimals = 1)]) + data9[round(x + h2, decimals = 1)]) / (2 * h2)

# Now, we apply Richardson Extrapolation to improve the approximation of
# f'(0.2) using centralApprox1 and centralApprox2
p = 2.0
richardsonExtrap = (((2 ** p) * centralApprox2) - centralApprox1) / ((2 ** p) - 1)
print("Richardson Extrapolation (h2 = h1 / 2, p = 2): %f" % richardsonExtrap)

# In this problem, we're using polynomial interpolation (specifically polyfit,
# polyder, and polyval) to compute f'(x) and f"(x) for a third-degree 
# polynomial. We use polyfit to obtain the coefficients, polyder to compute the
# derivatives, and polyval to evaluate the derivatives. This yields the error
# between our two calculations. 

print("\nProblem 5.1.11\n==============")

# These are the interpolation data points
xData = array([-2.2, -0.3, 0.8, 1.9])
yData = array([15.18, 10.962, 1.92, -2.04])

# Using polyfit and polyder from Numpy, we first compute the coefficients for a
# cubic interpolating polynomial using polyfit
p = polyfit(xData, yData, 3)

# Then, we use those coefficients to construct the first (d1) and second (d2)
# derivative functions via polyder
d1 = polyder(p)
d2 = polyder(d1)

# These are the coeffcients of the actual polynomial, whose derivatives we are
# approximating.
pActual = array([1, -0.3, -8.56, 8.448])

# We then use those coefficients to construct the first (d1Actual) and second
# (d2Acutal) derivative functions via polyder
d1Actual = polyder(pActual)
d2Actual = polyder(d1Actual)

# Now, we evaluate the first derivative of our cubic interpolating polynomial
# at x = 0, and then do the same for the first derivative of the actual
# polynomial whose coefficients are given in pActual.
fd =  polyval(d1, 0)
fdActual = polyval(d1Actual, 0)

print("Interpolated f'(0): %f" % fd)
print("Actual f'(0): %f" % fdActual)
print("Error: %f\n" % (fdActual - fd))

# We then evaluate the second derivative of the cubic interpolating polynomial
# at x = 0, and then do the same for the second derivative of the actual
# polynomial whose coefficients are given in pActual.
sd = polyval(d2, 0)
sdActual = polyval(d2Actual, 0)

print("Interpolated f''(0): %f" % sd)
print("Actual f''(0): %f" % sdActual)
print("Error: %f" % (sdActual - sd))

# Outputs for verification:
#
# Problem 5.1.9
# =============
# Central FDA Approximation (h = 0.2): 0.612452
# Richardson Extrapolation (h2 = h1 / 2, p = 2): 0.559636
#
# Problem 5.1.11
# ==============
# Interpolated f'(0): -8.560000
# Actual f'(0): -8.560000
# Error: -0.000000
#
# Interpolated f''(0): -0.600000
# Actual f''(0): -0.600000
# Error: -0.000000