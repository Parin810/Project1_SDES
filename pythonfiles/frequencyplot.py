import numpy as np
import matplotlib.pyplot as plot
from scipy.integrate import odeint
import csv

######intial numbers for prey and predator#####
initial_values=[]
a=1
b=1
c=1
d=1
prey=[]
predator=[]
#####parameters of the differential equation set to 1 by default###

def ds_dt(s,t=0):
    return [a*s[0] - b*s[0]*s[1],-c*s[1] + d*s[0]*s[1]]

###read initial value and constants from csv file###
def get_user_values():
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
		t=np.linspace(1,time,num=50)
		return t
	f.close()



def predator_prey_cycles(prey,predator,t):
	fig1=plot.figure(figsize=(8,6)) ###creates an object of plt.figure()
	ax1=fig1.add_subplot(1,1,1) ###creates another object of fig.add_subplot(1,1,1)
	ax1.grid()
	ax1.set_xlabel('time')
	ax1.set_ylabel('population')
	ax1.set_title('Evolution of predator and prey population')
	ax1.plot(t,predator,'b--',label='predator')
	ax1.plot(t,prey,'r--',label='prey')
	ax1.legend(loc='best',fontsize='medium')
	fig1.savefig('../plots/frequencyplot1.jpg')
	
	
	
def phaseplot(prey,predator,t):
	fig2=plot.figure(figsize=(8,6)) ##figure size is 6x8
	ax2=fig2.add_subplot(1,1,1)
	ax2.grid()
	ax2.set_xlabel('predator population')
	ax2.set_ylabel('prey population')
	ax2.plot(predator,prey,'r')
	fig2.savefig('../plots/phaseplot1.jpg')



if __name__=="__main__":
	t=get_user_values()
	s1=odeint(ds_dt,initial_values,t)
	prey=s1[:,0]
	predator=s1[:,1]
	predator_prey_cycles(prey,predator,t)
	phaseplot(prey,predator,t)


