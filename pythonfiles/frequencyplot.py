import numpy as np
import matplotlib.pyplot as plot
from scipy.integrate import odeint
import csv

######intial numbers for prey and predator#####
initial_values=[]

#####parameters of the differential equation set to 1 by default###
a=1
b=1
c=1
d=1
time=10

def ds_dt(s,t=0):
    return [a*s[0] - b*s[0]*s[1],-c*s[1] + d*s[0]*s[1]]

###read initial value and constants from csv file###

f=open('../data.csv')
f.readline()
reader=csv.reader(f,delimiter=',')
for line in reader:
	initial_values.append(float(line[0]))
	initial_values.append(float(line[1]))
	a=float(line[2])
	b=float(line[3])
	c=float(line[4])
	d=float(line[5])
	time=int(line[6])

t=np.linspace(1,time,num=100)

s1=odeint(ds_dt,initial_values,t)
prey=[]
predator=[]
prey=s1[:,0]
predator=s1[:,1]

plot.plot(t,prey,'r--',label='prey')
plot.plot(t,predator,'b--',label='predator')
plot.grid()
plot.legend(loc='best')
plot.xlabel('time')
plot.ylabel('population')
#plot.show()
plot.savefig('../plots/frequencyplot1.jpg')



