import turtle

def draw(radius):
    # Draw a circle with the given radius
    turtle.circle(radius)
    
    # Move the turtle to a new position below the circle
    turtle.penup()
    turtle.setpos(0, -radius)
    turtle.pendown()

# Create a pattern with multiple concentric circles
for i in range(5):
    draw(20 + 20 * i)

turtle.done()