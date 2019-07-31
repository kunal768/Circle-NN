import model
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("Xc", type = int , help = "The X coordinate of circles center")
parser.add_argument("Yc", type = int , help = "The Y coordinate of circles center")
parser.add_argument("R", type = int , help = "The radius of the circle")

args = parser.parse_args()

answer = model.prediction_draw(args.Xc,args.Yc,args.R)


