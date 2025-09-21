import numpy as np
import random
import os
import time
import msvcrt

# grid size
ROWS, COLS = 10, 10

# symbols
EMPTY = "⬜"
SNAKE = "🟩"
FOOD = "🍎"

# initialize grid
def create_grid():
    return np.full((ROWS, COLS), EMPTY)

# place snake and food on grid
def update_grid(snake, food):
    grid = create_grid()
    for r, c in snake:
        grid[r, c] = SNAKE
    grid[food] = FOOD
    return grid

# print grid
def print_grid(grid):
    os.system("cls" if os.name == "nt" else "clear")  # clear screen
    for row in grid:
        print(" ".join(row))
    print("\n")

# move snake
def move_snake(snake, direction, food):
    head = snake[0]
    if direction == "UP":
        new_head = (head[0]-1, head[1])
    elif direction == "DOWN":
        new_head = (head[0]+1, head[1])
    elif direction == "LEFT":
        new_head = (head[0], head[1]-1)
    elif direction == "RIGHT":
        new_head = (head[0], head[1]+1)
    else:
        return snake, food, False

    # check collision with wall
    if new_head[0] < 0 or new_head[0] >= ROWS or new_head[1] < 0 or new_head[1] >= COLS:
        return snake, food, True  # game over

    # check collision with itself
    if new_head in snake:
        return snake, food, True  # game over

    # add new head
    snake.insert(0, new_head)

    # check food
    if new_head == food:
        while True:
            new_food = (random.randint(0, ROWS-1), random.randint(0, COLS-1))
            if new_food not in snake:
                food = new_food
                break
    else:
        snake.pop()  # remove tail if no food

    return snake, food, False

# initialize game
snake = [(ROWS // 2, COLS // 2)]
food = (random.randint(0, ROWS-1), random.randint(0, COLS-1))
while food == snake[0]:
    food = (random.randint(0, ROWS-1), random.randint(0, COLS-1))

direction = "RIGHT"
game_over = False

print("use W/A/S/D to move the snake. Press any key to start.")
msvcrt.getch()  # wait for first key press

# game loop
while not game_over:
    grid = update_grid(snake, food)
    print_grid(grid)
    print(f"Score: {len(snake)-1}")

    # read key if pressed
    if msvcrt.kbhit():
        key = msvcrt.getch().decode("utf-8").upper()
        if key == "W" and direction != "DOWN":
            direction = "UP"
        elif key == "S" and direction != "UP":
            direction = "DOWN"
        elif key == "A" and direction != "RIGHT":
            direction = "LEFT"
        elif key == "D" and direction != "LEFT":
            direction = "RIGHT"

    # move snake
    snake, food, game_over = move_snake(snake, direction, food)

    time.sleep(0.5)  #snake will move after every 0.7 seconds.

print("Game over! Final score:", len(snake)-1)




