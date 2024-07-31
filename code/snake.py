
import time
import turtle as t
import random as rd
import pygame
from pygame.locals import*
from pygame import mixer
pygame.init()


# #background music
mixer.init()
mixer.music.load("snake.mp3") 
mixer.music.play(-1) 

t.bgcolor('yellow')

snake = t.Turtle()
snake.shape('square')
snake.speed(0)
snake.penup()
snake.hideturtle()

leaf = t.Turtle()
leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed()

game_started = False
text_turtle = False
text_turtle = t.Turtle()
text_turtle.write('Press SPACE to start', align='center', font=('Arial', 18, 'bold'))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)


def outside_window():
    left_wall = -t.window_width()/2
    right_Wall = t.window_width()/2
    top_wall = t.window_height()/2
    bottom_wall = -t.window_height()/2
    (x,y) = snake.pos()
    outside = x < left_wall or x > right_Wall or y > top_wall or y < bottom_wall
    return outside


def game_over():
    snake.color('black')
    leaf.color('green')
    t.penup()
    t.hideturtle()
    mixer.init()
    mixer.music.load("lost.mp3") 
    mixer.music.play()
    t.write('GAME OVER !', align='center', font=('Arial', 30, 'normal') )
   
    

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width()/2) - 70
    y = (t.window_height()/2) - 70
    score_turtle.setpos(x,y)
    score_turtle.write(str(current_score), align='right', font=('Arial', 40, 'bold'))


def place_leaf():
    leaf.hideturtle()
    leaf.setx(rd.randint(-200,200))
    leaf.sety(rd.randint(-200,200))
    leaf.showturtle()

def start_game():
    global game_started
    if game_started:
        return
    game_started = True
    score = 0
    text_turtle.clear()
    
    snake_speed = 2
    snake_length = 3
    snake.shapesize(1,snake_length,1)
    snake.showturtle()
    display_score(score)
    place_leaf()


    while True:
        snake.forward(snake_speed)
        if snake.distance(leaf) < 20:
            place_leaf()
            snake_length = snake_length + 1  
            mixer.init()
            start=mixer.Sound('bite_sound.wav')
            start.play()
            snake.shapesize(1,snake_length,1)
            snake_speed = snake_speed + 1
            score = score + 10
            display_score(score)
        if outside_window():
           game_over()
           break

def move_up():
    if snake.heading() == 0 or snake.heading() == 180:
        snake.setheading(90)

def move_down():
    if snake.heading() == 0 or snake.heading() == 180:
        snake.setheading(270)

def move_left():
    if snake.heading() == 90 or snake.heading() == 270:
        snake.setheading(180)

def move_right():
    if snake.heading() == 90 or snake.heading() == 270:
        snake.setheading(0)


def pause():
    global pause
    while pause:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
    # time.sleep(5)

def unpaused():
    global pause
    pause=False



            
   

t.onkey(start_game,'space')
t.onkey(move_up,'Up')
t.onkey(move_right,'Right')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.onkeypress(pause, "p")
t.onkeypress(unpaused, "y")
t.listen()
t.mainloop()
