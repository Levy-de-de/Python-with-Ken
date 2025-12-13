# draw a ninja
import turtle
ninja = turtle.Turtle()
ninja.speed(999)

for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)

    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()

    ninja.right(2)
turtle.done()

# import turtle

# ninja = turtle.Turtle()
# ninja.speed(10)
# ninja.penup()  # Move this line outside the loop
# ninja.setposition(0, 0)  # Move this line outside the loop
# ninja.pendown()  # Move this line outside the loop

# for i in range(180):
#     ninja.forward(100)
#     ninja.right(30)
#     ninja.forward(20)
#     ninja.left(60)
#     ninja.forward(50)
#     ninja.right(30)
#     ninja.penup()
#     ninja.setposition(0, 0)
#     ninja.pendown()
#     ninja.right(2)

turtle.done()