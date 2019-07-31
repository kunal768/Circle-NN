import matplotlib.pyplot as plt 
import bresenhams as bres 

def plotCircle(x,y,r):
	
	circle_plot = bres.make_circle(x,y,r)
	print(len(circle_plot))
	print(circle_plot)
	# 30 sublists each has a 8 points ..240 points in total 
	for sublist in circle_plot:
		for points in sublist:
			plt.plot(points[0],points[1],'g.')

    
	plt.show()

# plotCircle(3,3,4)
# say i have a circle with center at (2,2) and radius 80
plotCircle(1,1,30)


#
# 1-9 points = r-1 7->5

# n - 10 the radius is approzx the number of points till now
# im  doing hit and trial based stuff here

# radius must be anything ranging from 50 to 1000