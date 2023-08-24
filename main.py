from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_game_on = True
while is_game_on:
     screen.update()
     time.sleep(0.06)
     snake.move()

     if snake.segments[0].distance(food) < 15:
          food.refresh()
          scoreboard.increase_score()
          snake.extend()
     
     if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -300 or snake.segments[0].ycor() > 300 or snake.segments[0].ycor() < -280:
          is_game_on = False
          scoreboard.game_over()

     for segment in snake.segments[1:]:
          if snake.segments[0].distance(segment) < 2:
               is_game_on = False
               scoreboard.game_over()

screen.exitonclick()