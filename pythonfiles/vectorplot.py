import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from frequencyplot import ds_dt as ds

a=1
b=1
c=1
d=1

def get_user_values():
	f=open('../data.csv')
	f.readline()
	reader=csv.reader(f,delimiter=',')
	initial_values=[]
	for line in reader:
		initial_values.append(float(line[0]))
		initial_values.append(float(line[1]))
		a=float(line[2])
		b=float(line[3])
		c=float(line[4])
		d=float(line[5])
		time=int(line[6])
		t=np.linspace(1,time,num=50)
		return intial_values
	f.close()

def vector_tragectories_plot():
	print (c/d,a/b)
	fig= plt.figure()
	ax=fig.add_subplot(1,1,1)
	x=np.linspace(0.4,2,num=20)
	y=np.linspace(0.4,2,num=20)
	x1,y1=np.meshgrid(x,y)
	DX1,DY1=ds([x1,y1])
	M=np.hypot(DX1,DY1)
	M[ M == 0] = 1.                                 # Avoid zero division errors
	DX1 /= M                                        # Normalize each arrows
	DY1 /= M
	ax.quiver(x1,y1,DX1,DY1,M,pivot='mid')
	ax.grid()
	ax.annotate("stable center point",xy=(c/d,a/b),xytext=(2,2),textcoords='data',arrowprops=dict(arrowstyle='->'))
	ax.set_xlabel('prey population')
	ax.set_ylabel('predator population')
	plt.show()

get_user_values()
vector_tragectories_plot()
