import matplotlib.pyplot as plt 
from scripts import bresenhams as bres 

def plotCircle(x,y,r):
	
	circle_plot = bres.make_circle(x,y,r)
	# print(circle_plot)
	# [ [  [],[],[],..8 ] , [ [] , [], [], [] .. 8] ,  ]
	
	for sublist in circle_plot:
		for points in sublist:
			plt.plot(points[0],points[1],'g.')

    
	plt.show()


plotCircle(3,3,4)