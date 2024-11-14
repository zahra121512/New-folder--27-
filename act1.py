import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the pen size and color
t.pensize(3)
t.pencolor("blue")

# Draw a square using a for loop
for _ in range(4):
    t.forward(100)
    t.left(90)

# Keep the window open
turtle.done()