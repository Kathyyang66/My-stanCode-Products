"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.


Breakout Project - Make a colorful bricks and movable paddle to conquer the game!
Speed and direction of ball are random giving, you have to lucky enough to finish the game!
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    """
    When lives>0, player may click and start the game. When brick is being punching,
    the ball will check four corners of brick to make sure which brick shall be removed.
    """
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    while True:
        pause(FRAME_RATE)
        if graphics.score <= graphics.total_score:
            break
        elif graphics.start:
            graphics.start = False
            pause(FRAME_RATE)
            dx = graphics.get_velocity_dx()
            dy = graphics.get_velocity_dy()
            while True:
                pause(FRAME_RATE)
                if graphics.score <= graphics.total_score:
                    break
                elif lives > 0:
                    graphics.ball.move(dx, dy)
                    #確認有沒有掉到板子底下=死掉
                    if graphics.ball.y+graphics.ball.height >= graphics.window_height:
                        lives -= 1
                        graphics.window.add(graphics.ball, x=graphics.ball_startpoint_x, y=graphics.ball_startpoint_y)
                        graphics.ball_action = True
                        break
                    #確認撞到邊界反彈
                    if graphics.ball.y <= 0:
                        dy = -dy
                    if graphics.ball.x+graphics.ball.width >= graphics.window_width \
                            or graphics.ball.x < 0:
                        dx = -dx
                    if graphics.corner_checker():
                        dy = graphics.get_velocity_dy()


if __name__ == '__main__':
    main()
