import scipy as sp
import matplotlib.pyplot as plt
import matplotlib as mpl
import sys
import numpy as np
import matplotlib.ticker as tck
from numpy import arange,array,ones
from scipy import stats
import statistics as stats
from pylab import *
from scipy.optimize import curve_fit
from scipy import odr

#names are the titles of the arrays in the csv file you upload
table = np.genfromtxt('test_file2.txt',names=['wmax','M','M_err','wmax_err'],skip_header=1)

#for example
x = table['wmax']
y = table['M']
x_err = table['wmax_err']
y_err = table['M_err']

def func(p,x):
    m,c = p #p lists the constants in whatever function you want to use to fit
    return m*x + c

quad_model = odr.Model(func)
data = odr.RealData(x, y, sx=x_err, sy=y_err)
odr = odr.ODR(data, quad_model, beta0=[1.,1.])
    #beta0 is an array of best first-guesses to the fit line. The number of
#elements in the array is equal to the number of parameters in p
out = odr.run()

popt = out.beta
perr = out.sd_beta
print('--------------------------------------')
print('Slope:')
print(str(popt[0])+' +/- '+str(perr[0]))
print('Intercept:')
print(str(popt[1])+' +/- '+str(perr[1]))
#for i in range(len(popt)):
#    print(str(popt[i])+' +- '+str(perr[i]))
print('--------------------------------------')

nstd = 5. # to draw 5-sigma intervals
popt_up = popt + nstd * perr
popt_dw = popt - nstd * perr

    #make the best fit line with the output from the best fit
x_fit = np.linspace(min(x)-2, max(x)+2, 100)
fit = func(popt, x_fit)
