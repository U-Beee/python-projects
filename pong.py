# ============================================================
# PONG
# A two-player classic arcade game using the turtle library.
# Player 1 (left): W key to move up, S key to move down.
# Player 2 (right): Up/Down arrow keys.
# First player to reach 5 points wins!
# ============================================================

import turtle  # The turtle library is used to draw the game graphics

# --- SCREEN SETUP ---
screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("black")             # Black background like the classic arcade game
screen.setup(width=800, height=600) # Window size in pixels
screen.tracer(0)                    # Manual animation control for smooth movement

# --- LEFT PADDLE (Player 1) ---
left_paddle = turtle.Turtle()
left_paddle.shape("square")         # A square is stretched into a rectangle below
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)  # Make it tall and thin (5x height, 1x width)
left_paddle.penup()                 # Don't draw lines when moving
left_paddle.goto(-350, 0)          # Start on the left side of the screen

# --- RIGHT PADDLE (Player 2) ---
right_paddle = turtle.Turtle()
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)  # Same size as left paddle
right_paddle.penup()
right_paddle.goto(350, 0)          # Start on the right side of the screen

# --- BALL ---
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)                    # Ball starts in the center

# Ball speed: dx is horizontal movement, dy is vertical movement per frame
ball.dx = 0.2   # Move 0.2 pixels right each frame (positive = right)
ball.dy = 0.2   # Move 0.2 pixels up each frame (positive = up)

# --- SCORE DISPLAY ---
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()                   # Only show the text, not the turtle arrow
pen.goto(0, 260)                   # Position the score at the top center
pen.write("Player 1: 0    Player 2: 0", align="center", font=("Arial", 20, "bold"))

# --- SCORE VARIABLES ---
score_left = 0   # Player 1's score
score_right = 0  # Player 2's score
winning_score = 5  # First to this score wins

# --- PADDLE MOVEMENT FUNCTIONS ---
# Each function moves a paddle up or down by 20 pixels.
# We limit movement so paddles don't leave the screen.

def left_paddle_up():
    y = left_paddle.ycor()        # Get current y position
    if y < 250:                   # Only move up if not already at the top
        left_paddle.sety(y + 20) # Move up 20 pixels

def left_paddle_down():
    y = left_paddle.ycor()
    if y > -250:                  # Only move down if not already at the bottom
        left_paddle.sety(y - 20)

def right_paddle_up():
    y = right_paddle.ycor()
    if y < 250:
        right_paddle.sety(y + 20)

def right_paddle_down():
    y = right_paddle.ycor()
    if y > -250:
        right_paddle.sety(y - 20)

# --- LINK KEYS TO FUNCTIONS ---
screen.listen()
screen.onkeypress(left_paddle_up, "w")      # W key → left paddle up
screen.onkeypress(left_paddle_down, "s")    # S key → left paddle down
screen.onkeypress(right_paddle_up, "Up")    # Up arrow → right paddle up
screen.onkeypress(right_paddle_down, "Down") # Down arrow → right paddle down

# --- MAIN GAME LOOP ---
while True:
    screen.update()  # Refresh the screen every frame

    # Move the ball by adding its speed to its current position
    ball.setx(ball.xcor() + ball.dx)  # Move horizontally
    ball.sety(ball.ycor() + ball.dy)  # Move vertically

    # --- TOP AND BOTTOM WALL BOUNCE ---
    # If the ball hits the top or bottom, reverse vertical direction
    if ball.ycor() > 290:
        ball.sety(290)       # Correct position so ball doesn't go out of bounds
        ball.dy *= -1        # Reverse direction (multiply by -1 flips the sign)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1        # Bounce off the bottom wall

    # --- BALL GOES PAST RIGHT SIDE (Player 1 scores) ---
    if ball.xcor() > 390:
        score_left += 1      # Add a point for left player
        # Update the score text on screen
        pen.clear()
        pen.write("Player 1: {}    Player 2: {}".format(score_left, score_right),
                  align="center", font=("Arial", 20, "bold"))
        ball.goto(0, 0)      # Reset ball to center
        ball.dx *= -1        # Send ball in the opposite direction

    # --- BALL GOES PAST LEFT SIDE (Player 2 scores) ---
    if ball.xcor() < -390:
        score_right += 1
        pen.clear()
        pen.write("Player 1: {}    Player 2: {}".format(score_left, score_right),
                  align="center", font=("Arial", 20, "bold"))
        ball.goto(0, 0)
        ball.dx *= -1

    # --- CHECK FOR A WINNER ---
    if score_left >= winning_score:
        pen.clear()
        pen.write("Player 1 Wins!", align="center", font=("Arial", 30, "bold"))
        break  # Stop the game loop

    if score_right >= winning_score:
        pen.clear()
        pen.write("Player 2 Wins!", align="center", font=("Arial", 30, "bold"))
        break  # Stop the game loop

    # --- RIGHT PADDLE COLLISION ---
    # Check if the ball touches the right paddle.
    # We check: ball is near the paddle's x position AND within its y range
    if (ball.xcor() > 340 and ball.xcor() < 360 and
            ball.ycor() < right_paddle.ycor() + 50 and
            ball.ycor() > right_paddle.ycor() - 50):
        ball.setx(340)   # Prevent ball from going inside the paddle
        ball.dx *= -1    # Bounce the ball back to the left

    # --- LEFT PADDLE COLLISION ---
    if (ball.xcor() < -340 and ball.xcor() > -360 and
            ball.ycor() < left_paddle.ycor() + 50 and
            ball.ycor() > left_paddle.ycor() - 50):
        ball.setx(-340)  # Prevent ball from going inside the paddle
        ball.dx *= -1    # Bounce the ball back to the right

# Keep the window open after the game ends so the player can see the result
turtle.done()
