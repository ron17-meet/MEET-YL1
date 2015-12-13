from meet import *
import random
import meet
import math
import time
import turtle

colors = ["red", "orange", "yellow", "green", "blue", "violet", "cyan"]

user_cell={"radius":20, "x":0, "y":0, "dx":0, "dy":0, "color":random.choice(colors)} 

cells=[]
user_cell = create_cell(user_cell)
cells.append(user_cell)

colors = ["red", "orange", "yellow", "green", "blue", "violet", "cyan", "grey"]
cells_num=0
for i in range(20):
	ball1 = {"radius":random.randint(0,50), "x":random.randint(-250,250), "y":random.randint(-250,250), "dy":random.uniform(-0.25,0.25), "dx":random.uniform(-0.25,0.25), "color":random.choice(colors)}
	circle1 = create_cell(ball1)
	cells.append(circle1)
	cells_num=cells_num+1

		

def borders(cells):
	for cell in cells:
		width=get_screen_width()
		height=get_screen_height()
		x=cell.xcor()
		y=cell.ycor()


		if (cell.xcor() > width):
			cell.set_dx(-cell.get_dx())
		if (cell.ycor() > height):
			cell.set_dy(-cell.get_dy())
		if (cell.xcor() < -width):
			cell.set_dx(-cell.get_dx())
		if (cell.ycor() < -height):
			cell.set_dy(-cell.get_dy())
def eat(cells):
	for i in cells:
		x=i.xcor()
		y=i.ycor()
		r=i.get_radius()

		for g in cells:
			x2=g.xcor()
			y2=g.ycor()
			r2=g.get_radius()
			if math.sqrt((x-x2)**2+(y-y2)**2)<=(r+r2):
				if r>r2:
					x3=meet.get_random_x()
					y3=meet.get_random_y()
					g.goto(x3, y3)
					i.set_radius(r+(r2/10))
					if g==user_cell:
						meet.write('you lose!', align="center", font=('Ariel',50,'bold'))
						time.sleep(2)
						turtle.bye()

				elif r<r2:
					x3=meet.get_random_x()
					y3=meet.get_random_y()
					i.goto(x3, y3)
					g.set_radius(r2+(r/5))


while(True):
	meet.move_cells(cells)
	x,y = meet.get_user_direction(user_cell)
	user_cell.set_dx(x)
	user_cell.set_dy(y)
	borders(cells)
	eat(cells)
	if ((circle1.xcor()==get_x_mouse())or(circle1.ycor()==get_y_mouse())):
		circle1.goto(300, 300)

meet.mainloop()
