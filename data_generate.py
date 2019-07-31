import pandas as pd
import random
from scripts import bresenhams as bres

################ pre-processing part #####################


Xc = []
Yc = []
Radius = []

g = globals()

for i in range(1,81):
	g['X{0}'.format(i)] = []
	g['Y{0}'.format(i)] = []


for i in range(2000):
	
	x = (random.randint(1,15))
	y = (random.randint(1,15))
	r = (random.randint(20,45))
	Xc.append(x)
	Yc.append(y)
	Radius.append(r)
	circle_plot = bres.make_circle(x,y,r)

	count = 1
	for sublist in circle_plot:
		for sub_sublist in sublist:
			g['X{0}'.format(count)].append(sub_sublist[0])
			g['Y{0}'.format(count)].append(sub_sublist[1])
			count+=1



data = {"xc" : Xc,"yc":Yc,"radius":Radius}

for i in range(1,81):
	data["x"+str(i)] = g['X{0}'.format(i)]
	data["y"+str(i)] = g['Y{0}'.format(i)]

df = pd.DataFrame.from_dict(data)

df.to_csv('data/data_new.csv')