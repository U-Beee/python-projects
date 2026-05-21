# ============================================================
# SNAKE
# A classic Snake game using Python's built-in turtle library.
# Use the arrow keys to move the snake and eat the red food.
# Each food eaten makes the snake longer. Hitting the wall
# or yourself ends the game.
# ============================================================

import turtle   # The turtle library lets us draw graphics on screen
import random   # We use this to place food in a random position
import time     # We use this to control the speed of the game

# --- SCREEN SETUP ---
# Create the game window
screen = turtle.Screen()
screen.title("Snake Game")           # Title shown at the top of the window
screen.bgcolor("black")              # Background color
screen.setup(width=600, height=600)  # Window size in pixels
screen.tracer(0)                     # Turn off automatic animation (we control it manually)

# --- SNAKE HEAD SETUP ---
# The head is a turtle shape that we move around the screen
head = turtle.Turtle()
head.shape("square")       # Use a square shape for the snake head
head.color("green")        # Green color for the snake
head.penup()               # Don't draw lines when moving
head.goto(0, 0)            # Start at the center of the screen
head.direction = "stop"    # The snake starts not moving

# --- FOOD SETUP ---
# The food is a small red circle the snake needs to eat
food = turtle.Turtle()
food.shape("circle")     # Use a circle shape for the food
food.color("red")        # Red color for the food
food.penup()             # Don't draw lines when moving
food.goto(0, 100)        # Start the food a bit above center

# --- SCORE DISPLAY ---
# This turtle is used only to write text on screen (not a visible shape)
pen = turtle.Turtle()
pen.speed(0)             # Fastest drawing speed
pen.color("white")       # White text color
pen.penup()
pen.hideturtle()         # Hide this turtle so we only see the text
pen.goto(0, 270)         # Position at the top of the screen
pen.write("Score: 0  High Score: 0", align="center", font=("Arial", 18, "bold"))

# --- GAME VARIABLES ---
score = 0           # Current score starts at 0
high_score = 0      # Best score in this session
segments = []       # List to store the extra body squares of the snake
delay = 0.1         # How many seconds to wait between each frame (controls speed)

# --- DIRECTION CONTROL FUNCTIONS ---
# These functions are called when the player presses an arrow key.
# They change the snake's direction (but not backwards, to avoid instant death).

def go_up():
    if head.direction != "down":      # Can't go down if currently going up
        head.direction = "up"

def go_down():
    if head.direction != "up":        # Can't go up if currently going down
        head.direction = "down"

def go_left():
    if head.direction != "right":     # Can't go right if currently going left
        head.direction = "left"

def go_right():
    if head.direction != "left":      # Can't go left if currently going right
        head.direction = "right"

# --- LINK KEYS TO FUNCTIONS ---
# Tell the screen to listen for key presses
screen.listen()
screen.onkeypress(go_up, "Up")        # Up arrow → go_up function
screen.onkeypress(go_down, "Down")    # Down arrow → go_down function
screen.onkeypress(go_left, "Left")    # Left arrow → go_left function
screen.onkeypress(go_right, "Right")  # Right arrow → go_right function

def move():
    # This function moves the snake head one step in its current direction
    if head.direction == "up":
        head.sety(head.ycor() + 20)   # Move up by 20 pixels
    if head.direction == "down":
        head.sety(head.ycor() - 20)   # Move down by 20 pixels
    if head.direction == "left":
        head.setx(head.xcor() - 20)   # Move left by 20 pixels
    if head.direction == "right":
        head.setx(head.xcor() + 20)   # Move right by 20 pixels

def reset_game():
    # This function resets everything when the snake dies
    global score, delay
    time.sleep(1)                      # Brief pause so the player sees what happened
    head.goto(0, 0)                    # Move head back to center
    head.direction = "stop"            # Stop movement

    # Remove all body segments from the screen and clear the list
    for segment in segments:
        segment.goto(1000, 1000)       # Move segment off-screen
    segments.clear()

    score = 0                          # Reset score to zero
    delay = 0.1                        # Reset speed to starting speed

    # Update the score display
    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, high_score),
              align="center", font=("Arial", 18, "bold"))

# --- MAIN GAME LOOP ---
# This while loop runs the game continuously
while True:
    screen.update()   # Refresh the screen to show the latest positions

    # --- WALL COLLISION CHECK ---
    # If the head goes past the edge (±290 pixels), the snake dies
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        reset_game()

    # --- FOOD COLLISION CHECK ---
    # If the head gets close enough to the food (within 20 pixels), eat it
    if head.distance(food) < 20:
        # Move food to a new random location within the walls
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # Add a new body segment at the current tail position
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("light green")
        new_segment.penup()
        segments.append(new_segment)    # Add to our segments list

        # Increase score and update display
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score),
                  align="center", font=("Arial", 18, "bold"))

        # Speed the game up slightly with each food eaten
        delay -= 0.001

    # --- MOVE BODY SEGMENTS ---
    # Each segment moves to where the segment AHEAD of it was.
    # We go backwards through the list so segments don't overwrite each other.
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()    # Get the x position of the segment ahead
        y = segments[i - 1].ycor()    # Get the y position of the segment ahead
        segments[i].goto(x, y)        # Move this segment to that position

    # If there is at least one body segment, it moves to where the head was
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    # Move the head one step
    move()

    # --- SELF COLLISION CHECK ---
    # If the head touches any body segment, the snake dies
    for segment in segments:
        if segment.distance(head) < 20:
            reset_game()

    # Wait a tiny moment before the next frame (controls game speed)
    time.sleep(delay)
