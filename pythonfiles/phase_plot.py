import csv
import numpy as np
import matplotlib.pyplot as plot
from scipy.integrate import odeint
from frequencyplot import ds_dt as ds
a=1
b=1
c=1
d=1
def ds_dt(s,t=0):
    return [a*s[0] - b*s[0]*s[1],-c*s[1] + d*s[0]*s[1]]


def get_user_values():
	f=open('../data2.csv')
	f.readline()
	reader=csv.reader(f,delimiter=',')
	initial_value_prey=[]
	initial_value_predator=[]
	data=list(reader)
	print data
	print len(data)
	f.close()
	if (len(data)==0):
		print ("No initial values for predator and prey given")
		return
	else:
		for i in range(0,len(data)):
			initial_value_prey.append(int(data[i][0]))
			initial_value_predator.append(int(data[i][1]))
	
	return initial_value_prey,initial_value_predator
	
def multiple_phase_plot(xlabel,ylabel,title):
	prey_init_values=[]
	predator_init_values=[]
	prey_init_values,predator_init_values=get_user_values()
	t=np.linspace(1,10,num=50)
	for i,j in zip(prey_init_values,predator_init_values):
		t0=[i,j]
		s=odeint(ds,t0,t)
		plot.plot(s[:,0],s[:,1],'-',label='t0=(%.f, %.f)' % ( t0[0], t0[1]))
	plot.annotate("stable center point",xy=(c/d,a/b),xytext=(2,2),textcoords='data',arrowprops=dict(arrowstyle='->'))
	plot.xlabel(xlabel)
	plot.ylabel(ylabel)
	plot.title(title)
	plot.legend()
	plot.show()

multiple_phase_plot('prey','predator','Trajectories for different initial values')
