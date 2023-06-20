"""
File: Bouncing_ball
Name:Kathy Yang
-------------------------
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 40
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 50
count = 0
window = GWindow(600, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(falling_ball)


def falling_ball(mouse):
    global count
    vy = 0
    if ball.x == START_X and ball.y == START_Y:
        while True:
            if count < 3:
                vy += GRAVITY
                ball.move(VX, vy)
                if ball.y + SIZE > window.height and vy > 0:
                    vy = -vy*REDUCE
                if ball.x + SIZE > window.width:
                    count += 1
                    ball.x = START_X
                    ball.y = START_Y
                    break
                pause(DELAY)


if __name__ == "__main__":
    main()
