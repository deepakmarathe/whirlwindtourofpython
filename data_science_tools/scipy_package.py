# SciPy package for scientific functionality 

# %matplotlib notebook

from matplotlib import pyplot as plt
from scipy import interpolate
import numpy as np

# choose 8 points out of 10 
x = np.linspace(0, 10, 8)
y = np.sin(x)

# create a cubic interpolation function 
func = interpolate.interp1d(x, y, kind='cubic')

# Interpolate on a grid of 1000 points
x_interp = np.linspace(0, 10, 1000)
y_interp = np.sin(x_interp)

# plot the results
plt.figure()
plt.plot(x, y, 'o')
plt.plot(x_interp, y_interp);


