from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#8fbe0c")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

playing_game = True
while playing_game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect eating food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision to wall
    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
        scoreboard.reset_board()
        snake.reset_snake()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_board()
            snake.reset_snake()

screen.exitonclick()
