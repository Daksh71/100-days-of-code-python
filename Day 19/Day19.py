# import turtle as t
# import random
# tim = t.Turtle()
# tim.pensize(15)
# tim.speed("fastest")

# def move_forward():
#     tim.forward(10)
# def move_backward():
#     tim.backward(10)
# def turn_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
# def clear_drawing():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()

# screen = t.Screen()
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# tim.pendown()
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="c", fun=clear_drawing)    
# screen.exitonclick()




#######################################################################################################
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_guess = screen.textinput(
    title="Place Your Bet",
    prompt="Which turtle do you think will win the race? Enter a color (e.g., red, blue): "
)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
starting_positions = [-70, -40, -10, 20, 50, 80]

turtles = []
for index in range(6):
    racer = Turtle(shape="turtle")
    racer.penup()
    racer.color(colors[index])
    racer.goto(x=-230, y=starting_positions[index])
    turtles.append(racer)

race_active = False
if user_guess:
    race_active = True

while race_active:
    for racer in turtles:
        distance = random.randint(0, 10)
        racer.forward(distance)

        if racer.xcor() > 230:
            race_active = False
            winning_color = racer.pencolor()

            if winning_color == user_guess:
                print(f"You won! 🎉 The {winning_color} turtle is the champion!")
            else:
                print(f"You lost! 😢 The {winning_color} turtle won the race.")

screen.exitonclick()




