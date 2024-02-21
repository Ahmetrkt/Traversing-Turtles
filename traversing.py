#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
#The turtles go to their starting location before they start drawing
#Each turtle is a different shape
#Each turtle is a different color
#Each turtle starts facing the same direction as the previous turtle

import turtle as trtl

# create an empty list of turtles

my_turtles = []
# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  rocket = trtl.Turtle(shape=s)
  my_turtles.append(rocket)
  new_color = turtle_colors.pop()
  print (new_color)
  rocket.fillcolor(new_color)
  rocket.pencolor(new_color)
  rocket.penup()

#  directions variable
startx = 0
starty = 0
directions = 90

# loop for squre
for rocket in my_turtles:
  rocket.goto(startx, starty)
  rocket.setheading(directions)
  rocket.pendown()
  rocket.right(50)    
  rocket.forward(45)
  directions = rocket.heading()
  rocket.penup()

#  make directions
  startx = rocket.xcor()
  starty = rocket.ycor()

wn = trtl.Screen()
wn.mainloop()