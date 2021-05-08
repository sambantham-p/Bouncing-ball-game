import turtle
import winsound

#winsound.PlaySound("StarWars3.wav", winsound.SND_ASYNC)
##game="y"
wn=turtle.Screen()
wn.title("Ping Pong")
wn.setup(width=1000,height=600)
select=0
select=wn.numinput("Select", "Enter 1 to play single player\nEnter 2 to play 2 player : ", 0, minval=0, maxval=2)
select=int(select)

if select==2:
    game="y"
    while game=="y" or game=="Y":
        wn.bgcolor("blue")
        wn.tracer(0)
        name1=wn.textinput("Player 1","Name of player 1 : ")
        name2=wn.textinput("Player 2","Name of player 2 : ")
        name1=name1.upper()
        name2=name2.upper()
        flag=int(wn.textinput("score","Enter the maximum number of round you want to play : "))

#paddle

        paddle1=turtle.Turtle()
        paddle1.speed(0)
        paddle1.shape("square")
        paddle1.color("red")
        paddle1.shapesize(stretch_wid=5,stretch_len=1)
        paddle1.penup()
        paddle1.goto(-450,0)

        paddle2=turtle.Turtle()
        paddle2.speed(0)
        paddle2.shape("square")
        paddle2.color("red")
        paddle2.shapesize(stretch_wid=5,stretch_len=1)
        paddle2.penup()
        paddle2.goto(450,0)

#score
        player_1=0
        player_2=0
        score=turtle.Turtle()
        score.speed(0)
        score.penup()
        score.hideturtle()
        score.goto(0,360)
        score.write("{} = 0   {} = 0".format(name1,name2),align="center",font=("ariel",26,"bold"))

#ball

        ball=turtle.Turtle()
        ball.speed(0)
        ball.color("white")
        ball.shape("circle")
        ball.penup()
        ball.goto(0,0)
        ball.x=-0.5
        ball.y=0.5

#movement

        def paddle1_down():
            y=paddle1.ycor()
            if y!=-350:
                y-=25
                paddle1.sety(y)
        def paddle1_up():
            y=paddle1.ycor()
            if y!=350:
                y+=25
                paddle1.sety(y)

        def paddle2_down():
            y=paddle2.ycor()
            if y!=-350:
                y-=25
                paddle2.sety(y)
        def paddle2_up():
            y=paddle2.ycor()
            if y!=350:
                y+=25
                paddle2.sety(y)

#keybord

        wn.listen()
        wn.onkeypress(paddle1_up,"w")
        wn.onkeypress(paddle1_down,"s")
        wn.onkeypress(paddle2_up,"Up")
        wn.onkeypress(paddle2_down,"Down")

#main fxn
    
        while player_1!=flag and player_2!=flag:
            wn.update()
    
            ball.setx(ball.xcor()+ball.x)
            ball.sety(ball.ycor()+ball.y)

            if ball.ycor()>390:
            
                wn.update()
                ball.sety(390)
                ball.y*=-1
            
            if ball.ycor()<-390:
                wn.update()
                ball.sety(-390)
                ball.y*=-1
            
            if ball.xcor()>490:
                wn.update()
                player_1+=1
                score.clear()
                score.write("{} = {}   {} = {}".format(name1,player_1,name2,player_2),align="center",font=("ariel",26,"bold"))
                ball.goto(0,0)
                ball.x*=-1
            
            if ball.xcor()<-490:
                wn.update()
                player_2+=1
                score.clear()
                score.write("{} = {}   {} = {}".format(name1,player_1,name2,player_2),align="center",font=("ariel",26,"bold"))
                ball.goto(0,0)
                ball.x*=-1

            
            if ball.xcor()<-425 and ball.xcor()>-435 and ball.ycor()<paddle1.ycor()+50 and ball.ycor()>paddle1.ycor()-50:
            
                ball.setx(-425)
                ball.x*=-1
            
            if ball.xcor()>425 and ball.xcor()<435 and ball.ycor()<paddle2.ycor()+50 and ball.ycor()>paddle2.ycor()-50:
            
                ball.setx(425)
                ball.x*=-1
            wn.update()
        wn.clear()
        wn.bgcolor("orange")
        score.goto(0,0)
        if player_1==flag:
            winsound.PlaySound("StarWars3.wav", winsound.SND_ASYNC)
            score.write("{} Wins".format(name1),align="center",font=("ariel",56,"bold","italic"))
        else:
            winsound.PlaySound("StarWars3.wav", winsound.SND_ASYNC)
            score.write("Winner\n{}".format(name2),align="center",font=("ariel",56,"bold","italic"))
        game=wn.textinput("Game","Enter Y/y to play again or N/n to exit : ")
        score.clear()
        wn.reset()
    score.write("Thank you!",align="center",font=("ariel",60,"bold"))

####Single player game

elif select==1:
    score=0
    
    wn.bgcolor("blue")
    wn.tracer(0)
    
#paddle
    paddle=turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("red")
    paddle.shapesize(stretch_wid=1,stretch_len=5)
    paddle.penup()
    paddle.goto(0,-360)
    
#ball
    ball=turtle.Turtle()
    ball.speed(0)
    ball.color("white")
    ball.shape("circle")
    ball.penup()
    ball.goto(0,0)
    ball.x=-0.5
    ball.y=0.5

#movement
    def paddle_left():
        x=paddle.xcor()
        x-=25
        paddle.setx(x)
    def paddle_right():
        x=paddle.xcor()
        x+=25
        paddle.setx(x)

#key
    wn.listen()
    wn.onkeypress(paddle_left,"Left")
    wn.onkeypress(paddle_right,"Right")
    

#score
    pen=turtle.Turtle()
    pen.speed(0)
    pen.penup()
    pen.hideturtle()
    pen.goto(0,360)
    pen.write("score : {}".format(score),align="center",font=("ariel",26,"bold"))


    while True:
        wn.update()
        ball.setx(ball.xcor()+ball.x)
        ball.sety(ball.ycor()+ball.y)
        wn.update()

        if ball.ycor()>390:
            wn.update()
            ball.sety(390)
            ball.y*=-1

        if ball.xcor()>490:
            wn.update()
            ball.setx(490)
            ball.x*=-1

        if ball.xcor()<-490:
            wn.update()
            ball.setx(-490)
            ball.x*=-1
        
        if ball.ycor()<-330 and ball.ycor()>-345 and ball.xcor()<paddle.xcor()+50 and ball.xcor()>paddle.xcor()-50:
            wn.update()
            score+=1
            pen.clear()
            pen.write("score : {}".format(score),align="center",font=("ariel",26,"bold"))
            ball.sety(-325)
            ball.y*=-1

        if ball.ycor()<-390:
            wn.update()
            score=0;
            pen.clear()
            pen.write("score : {}".format(score),align="center",font=("ariel",26,"bold"))
            ball.goto(0,0)
            ball.x*=-1
            ball.y*=-1
        wn.update()
