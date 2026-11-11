import math
import turtle
screen = turtle.Screen()
screen.title("Heart Made of Words")
screen.bgcolor("black")
screen.setup(width=800, height=800)
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.penup()
def heart_a(k):
    return 15 * math.sin(k) ** 3


def heart_b(k):
    return (
        12 * math.cos(k)
        - 5 * math.cos(2 * k)
        - 2 * math.cos(3 * k)
        - math.cos(4 * k)
    )
t.color("#F3003D") 

for i in range(60):
    k = (2 * math.pi / 60) * i
    x = heart_a(k) * 18
    y = heart_b(k) * 18

    t.goto(x, y - 50)
    t.write("i really", align="center", font=("Arial", 12, "bold"))
t.color("#FF99BB")
for i in range(40):
    k = (2 * math.pi / 40) * i
    x = heart_a(k) * 11
    y = heart_b(k) * 11

    t.goto(x, y - 50)
    t.write("LOVE", align="center", font=("Arial", 9, "bold"))
t.goto(0, -50)
t.color("DARK red")
t.write("YOU", align="center", font=("Arial", 28, "bold"))
turtle.ontimer(0,100)
t.clear()
t.goto(0, -50)
t.color("DARK red")
t.write("Accept or Reject", align="center", font=("Arial", 28, "bold"))

screen.exitonclick()