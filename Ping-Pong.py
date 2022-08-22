import turtle
import winsound

#window
wnd = turtle.Screen()
wnd.title("Pong")
wnd.bgcolor("blue")
wnd.setup(width = 800, height = 600)
wnd.tracer(0)

#Left Paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid = 5, stretch_len = 1)
left_paddle.penup()
left_paddle.goto(-350,0)

#Right Paddle 
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid = 5, stretch_len = 1)
right_paddle.penup()
right_paddle.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)

#Ball movement
ball.dx = 0.1
ball.dy = -0.1

#Score 
score_left = 0
score_right = 0

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align = "center", font = ("Courier", 18, "bold"))


#Up and Down Function
def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)

def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)

#Keybinds
wnd.listen()
wnd.onkeypress(left_paddle_up, "w")
wnd.onkeypress(left_paddle_down, "s")
wnd.onkeypress(right_paddle_up, "Up")
wnd.onkeypress(right_paddle_down, "Down")



#Main game loop
while True:
    wnd.update()

    #Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking Top and Bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    #Border Checking Left and Right and Count Scores
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_left += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_left, score_right), align = "center", font = ("Courier", 18, "bold"))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_right += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_left, score_right), align = "center", font = ("Courier", 18, "bold"))
    
    #Paddle Bounce
    if (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < left_paddle.ycor() + 40 and ball.ycor() > left_paddle.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < right_paddle.ycor() + 40 and ball.ycor() > right_paddle.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

