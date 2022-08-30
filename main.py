# This is a snake game
# 21/09/20

import turtle
import time
import random

delay = 0.1 # So we can see it as no delay it goes off the screen too quickly

score = 0
high_score = 0

# set up the screen
window = turtle.Screen()
window.title("Snake Game by Mark and Joshua")
window.bgcolor("green")
window.setup(width=600, height=600)

# for animations
window.tracer(0) # Turns off screen updates

# snake head
head = turtle.Turtle()
head.speed(0) # animation speed rather than the speed of the object
head.shape("square")
head.color("black")
head.penup() # turtle module is for making lines. pen up means it does not draw anything
head.goto(0,0) # starts at centre of screen
head.direction = "stop"

# Snake Food
food = turtle.Turtle()
food.speed(0) # animation speed rather than the speed of the object
food.shape("circle")
food.color("red")
food.penup() # turtle module is for making lines. pen up means it does not draw anything
food.goto(0,100) # starts at centre of screen
food.direction = "stop"

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
        # move head up by 20 pixels if up key is pushed

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
        # move head down by 20 pixels if down key is pushed

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
        # move head right by 20 pixels if right key is pushed

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
        # move head right by 20 pixels if right key is pushed

# Keyboard bindings
window.listen()
window.onkeypress(go_up, "Up") # For future reference, special keys always require a capital letter, whereas individual keys such as w,a,s,d is all lower case
window.onkeypress(go_down, "Down")
window.onkeypress(go_right, "Right")
window.onkeypress(go_left, "Left")

# Main game loop
while True:
    window.update()

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000) # Move off the screen

        # Clear the segments list
        segments.clear()

        # reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Food collision logic
    if head.distance(food) < 20: # Each turtle size is 20 so if the distance is less than 20 they have collided
        # Move food to random spot on the screen
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        # -290 and 290 because with the screen being 600x600 and centre being 0 it means the each border is between -300 and 300 for both x and y
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0) # animation speed
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

   # Move the end segment first in reverse order
    for index in range(len(segments)-1, 0, -1): # gets length of segments (but starts at 0 not 1 so need to do -1 for index position). 2nd 0 is saying when to stop. and -1 is saying to decrease by 1
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
        # this loop does it in reverse. so it puts a segment at position 9 for instance, then 8, then 7 etc. until 0

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)  # Move off the screen
                # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

# keeps open
window.mainloop()