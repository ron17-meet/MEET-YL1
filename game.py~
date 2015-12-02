from meet import *
import random

cells=[]
colors = ["red", "orange", "yellow", "green", "blue", "violet", "cyan"]
cells_num=0
for i in range(20):
	ball1 = {"radius":random.randint(0,50), "x":random.randint(0,50), "y":random.randint(0,50), "dy":random.uniform(-0.1,0.1), "dx":random.uniform(-0.15,0.15), "color":random.choice(colors)}
	circle1 = create_cell(ball1)
	cells.append(circle1)
	cells_num=cells_num+1

while(True):
	move_cells(cells)

def borders(cells):
	for cell in cells:
		width=get_screen_width
		height=get_screen_height



