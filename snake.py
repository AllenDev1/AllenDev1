import curses
from random import randint

def main(stdscr):
    # Initialize curses
    curses.curs_set(0)  # Hide cursor
    curses.noecho()     # Don't show key presses
    stdscr.nodelay(1)   # Non-blocking input
    stdscr.timeout(100) # Refresh every 100ms
    
    # Create a window
    win = curses.newwin(20, 60, 0, 0)
    win.keypad(1)
    win.border(0)

    # Initialize snake and food
    snake = [(4, 10), (4, 9), (4, 8)]
    food = (10, 20)
    win.addch(food[0], food[1], '*')

    key = curses.KEY_RIGHT  # Initial direction

    while True:
        new_key = win.getch()
        key = key if new_key == -1 else new_key

        # Determine new head position based on key input
        head = snake[0]
        if key == curses.KEY_UP:
            new_head = (head[0] - 1, head[1])
        elif key == curses.KEY_DOWN:
            new_head = (head[0] + 1, head[1])
        elif key == curses.KEY_LEFT:
            new_head = (head[0], head[1] - 1)
        elif key == curses.KEY_RIGHT:
            new_head = (head[0], head[1] + 1)
        else:
            new_head = head

        # Check for collision with border or self
        if (new_head[0] in [0, 19] or new_head[1] in [0, 59]) or new_head in snake:
            break

        snake.insert(0, new_head)

        # Check if snake has eaten the food
        if new_head == food:
            food = (randint(1, 18), randint(1, 58))
            win.addch(food[0], food[1], '*')
        else:
            tail = snake.pop()
            win.addch(tail[0], tail[1], ' ')

        win.addch(snake[0][0], snake[0][1], 'o')

    # End game
    stdscr.addstr(10, 25, "Game Over! Press any key to exit.")
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)
