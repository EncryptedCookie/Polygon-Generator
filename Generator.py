import turtle

wn = turtle.Screen()
turtle.setup(550, 600)
pen = turtle.Turtle()


# Draw over the previous text
def draw_over_text():
    pen.penup()
    pen.goto(-275, -280)
    pen.color("#ffffff")
    pen.pensize(50)
    pen.pendown()
    pen.goto(275, -280)


def write_status(string):
    pen.penup()
    pen.color("#000000")
    pen.goto(0, -280)
    pen.write(string, False, align="center", font=("Agency FB", 16, "normal"))


pen.speed(0)
pen.hideturtle()
pen.penup()
pen.goto(0, 260)
pen.write("Regular Polygon Generator and Tessellator", False, align="center", font=("Agency FB", 18, "normal"))
write_status("Drawing grid...")
pen.color('#a9a9a9')
pen.goto(-250, 250)
pen.pendown()
# Construct the border
pen.goto(250, 250)
pen.goto(250, -250)
pen.goto(-250, -250)
pen.goto(-250, 250)

# Draw the horizontal grid lines
pen.right(90)
for x in range(4):
    pen.forward(50)
    pen.left(90)
    pen.forward(500)
    pen.right(90)

    pen.forward(50)
    pen.right(90)
    pen.forward(500)
    pen.left(90)
    if x == 3:
        pen.forward(50)
        pen.left(90)
        pen.forward(500)
        pen.right(90)

# Draw the vertical grid lines
pen.goto(250, 250)
pen.right(90)
for x in range(4):
    pen.forward(50)
    pen.left(90)
    pen.forward(500)
    pen.right(90)

    pen.forward(50)
    pen.right(90)
    pen.forward(500)
    pen.left(90)
    if x == 3:
        pen.forward(50)
        pen.left(90)
        pen.forward(500)
        pen.right(90)

draw_over_text()
pen.color("#000000")
write_status("Please input the desired variables. (0/3)")

# Go to center and show pen
pen.goto(0, 0)
pen.pendown()
pen.left(180)
pen.stamp()

# Ask the user for number of sides and tessellation iterations
sides = turtle.numinput("Number of Sides", "Input the number of sides in the regular polygon as an integer or as the "
                                           "polygon's name: ")
if sides < 3:
    draw_over_text()
    write_status("You can't have a polygon with less than two sides.")

draw_over_text()
write_status("Please input the desired variables. (1/3)")
size = turtle.numinput("Side Lengths  of Polygon", "Input the length (in pixels) of the sides in the regular polygon: ")
draw_over_text()
write_status("Please input the desired variables. (2/3)")
times_to_tessellate = turtle.numinput("Times to Tessellate", "Input the number of times to tessellate the polygon: ")
draw_over_text()
write_status("Please input the desired variables. (3/3)")

if times_to_tessellate == 0:
    draw_over_text()
    write_status("Drawing regular polygon...")
else:
    draw_over_text()
    write_status("Drawing regular polygons...")
# Make the pen better for drawing the polygon
pen.goto(0, 0)
pen.pendown()
pen.showturtle()
pen.color("#ffffff")
pen.stamp()
pen.color("#a9a9a9")
pen.width(1)
pen.left(180)
pen.forward(7)
pen.left(180)
pen.forward(7)
pen.speed(1)
pen.width(3)
pen.color("#000000")

# Draw the regular polygon with n sides
if times_to_tessellate > 0:  # If the polygon will tessellate:
    for t in range(int(times_to_tessellate + 1)):  # Tessellate the polygon the amount of times specified
        for i in range(int(sides)):
            pen.forward(size)
            pen.left(360 / sides)
        pen.left((sides - 2) * 180 / sides)  # Rotate align side of next polygon
else:
    for i in range(sides):
        pen.forward(size)
        pen.left(360 / sides)
pen.stamp()
pen.penup()
pen.hideturtle()
pen.speed(0)
draw_over_text()
write_status("Done. Click anywhere to exit.")

wn.exitonclick()
