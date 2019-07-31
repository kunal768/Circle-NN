# bresenhams circle algorithm in python implementation
import time
# from scrupts import draw

def drawCircle(xc,yc,x,y):
	return [[xc+x,yc+y],[xc-x,yc+y],[xc+x,yc-y],[xc-x,yc-y],[xc+y,yc+x],[xc-y,yc+x],[xc+y,yc-x],[xc+y,yc-x]]

def make_circle(xc,yc,r):
	final_list = []
	x = 0
	y = r
	d = 3 - 2*r 
	t = 10
	while t:

		x += 1

		if(d > 0):
			y-=1
			d = d+ 4*(x-y) + 10
		else:
			d = d+ 4*x+6
		final_list.append(drawCircle(xc,yc,x,y))
		t-=1
	return final_list




# heres the script