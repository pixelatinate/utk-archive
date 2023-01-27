#!/usr/bin/env python3

# Homework 6: Curve Fitting Thermal Efficiencies
# COSC370
# Swasti Mishra // netid: smishr11
# August 1, 2022


# In this problem, we are using the least squares curve-fitting approach
# (i.e. polyFit.py) to predict the thermal efficiency of a steam engine.

# We plug an "m" value (the degree of the polynomial) into polyFit and
# get the coefficient, standard deviation, and prediction. 

# If the standard deviation is less than infinity and the projection for
# the year 2000 is less than 100 but greater than zero, it passes our
# human smell test (so to speak) and is a valid projection. If it doesn't,
# we're probably using the wrong degree and our projection is not viable.

from numpy import array,zeros
from polyFit import *
import pylab

def evalPoly(c, x): # c stores coefficients for polynomial
    m = len(c) - 1  # (copied from polyFit module)
    p = c[m]
    for j in range(m):
        p = p * x + c[ m - j - 1 ]
    return p

xData = array([1718, 1767, 1774, 1775, 1792, 1816, 1828, 1834, 1878, 1906])
yData = array([0.5, 0.8, 1.4, 2.7, 4.5, 7.5, 12.0, 17.0, 17.2, 23.0])

minsdev = float("inf")
minpoly = 0
n = len(xData)
print('Degree  Stdev   2000P')
for m in range(1, 6):                 # Tries m = 1, 2, 3, 4, 5 (degree of polynomial)
    ys = zeros((n), dtype = 'float')  # Initializes y-coords for curve

    coeff = polyFit(xData, yData, m)    # Gets coefficients for nth polynomial
    stdev = stdDev(coeff, xData, yData) # Gets stdev of the error in the fit
    proj  = evalPoly(coeff, 2000)       # Evaluates the polynomial at year 2000

    # Year 2000 projections
    if (stdev < minsdev) and proj < 100 and proj > 0 :
        print('{:3d}\t{:5.3f}\t{:5.3f}\t{:s}'.format(m,stdev,proj,'viable'))
        ys = evalPoly(coeff, xData)     # Gets y-coords of polynomial

		# Plots the data using matplotlib
        pylab.figure()
        pylab.xlabel("x")
        pylab.ylabel("Thermal Efficiency")
        my_title = 'Fit with poly degree = ' + str(m) + '; green dot is 2000 projection'
        pylab.title(my_title)
        pylab.xlim(1710, 2015)
        pylab.plot(2000, proj, 'go')			  # Plots Year 2000 projection as a green dot
        pylab.plot(xData, yData, 'ro')            # Plots the original data arrays as red dots
        pylab.plot(xData, ys, 'b-')				  # Plots polynomial curve in blue
        pylab.grid()
        fname = 'degree' + str(m) + 'fit.png'     # Saves figure to file rather than display
        pylab.savefig(fname)
    else :
        print('{:3d}\t{:5.3f}\t{:5.3f}\t{:s}'.format(m,stdev,proj,'not viable'))
