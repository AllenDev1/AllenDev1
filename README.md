# Snake game in Python
# Use arrow keys to play

import curses
from random import randint

# Initialize curses
curses.initscr()
win = curses.newwin(20, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

# Initialize snake
snake = [(4, 10), (4, 9), (4, 8)]
food = (10, 20)
win.addch(food[0], food[1], '*')

# Game loop
while True:
    # Move snake
    key = win.getch()
    if key == curses.KEY_UP:
        new_head = (snake[0][0] - 1, snake[0][1])
    elif key == curses.KEY_DOWN:
        new_head = (snake[0][0] + 1, snake[0][1])
    elif key == curses.KEY_LEFT:
        new_head = (snake[0][0], snake[0][1] - 1)
    elif key == curses.KEY_RIGHT:
        new_head = (snake[0][0], snake[0][1] + 1)
    else:
        new_head = (snake[0][0], snake[0][1])

    snake.insert(0, new_head)

    # Check if snake hit border
    if snake[0][0] == 0 or snake[0][0] == 19 or snake[0][1] == 0 or snake[0][1] == 59:
        break

    # Check if snake hit itself
    if snake[0] in snake[1:]:
        break

    # Check if snake ate food
    if snake[0] == food:
        food = (randint(1, 18), randint(1, 58))
        win.addch(food[0], food[1], '*')
    else:
        tail = snake.pop()
        win.addch(tail[0], tail[1], ' ')

    # Update snake on screen
    win.addch(snake[0][0], snake[0][1], 'o')

# End game
curses.nocbreak()
win.keypad(0)
curses.echo()
curses.endwin()
print("Score:", len(snake))
