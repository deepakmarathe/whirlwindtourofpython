# Matplotlib : matlab style scientific visualization 

#%matplotlib notebook

import matplotlib.pyplot as plt
import numpy as np

# make graphs in the style of R's ggplot
plt.style.use('ggplot')

x = np.linspace(0,10)
y = np.sin(x)
plt.plot(x, y)


