import numpy as np
import matplotlib.pyplot as plot
from scipy.integrate import odeint
import csv



def plot_square(x,y):
	y_squared=np.square(y)
	return plot.plot(x,y_squared)


def test_plot_square1():
    x, y = [0, 1, 2], [0, 1, 2]
    line, = plot_square(x, y)
    x_plot, y_plot = line.get_xydata().T
    np.testing.assert_array_equal(y_plot, np.square(y))


y=plot_square([0,1,2],[1,5,1])
plot.show(y)
