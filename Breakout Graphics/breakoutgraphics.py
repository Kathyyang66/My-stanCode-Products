"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 4        # Number of rows of bricks
BRICK_COLS = 4        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 1        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.__dy = 0
        self.__dx = 0
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.brick_width = brick_width
        self.brick_height = brick_height

        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.window_width = window_width
        self.window_height = window_height

        self.label = GLabel('Score: ', x=0, y=40)
        self.label.font = '-20'
        self.window.add(self.label)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(window_width-paddle_width)/2, y=window_height-paddle_offset-paddle_height)
        self.paddle_offset = paddle_offset
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball_startpoint_x = window_width/2-ball_radius
        self.ball_startpoint_y = window_height/2-ball_radius
        self.ball.filled = True
        self.window.add(self.ball, x=window_width/2-ball_radius, y=window_height/2-ball_radius)

        self.score = 100
        self.total_score = 0
        self.total_brick = self.brick_rows * self.brick_cols
        self.per_ball_get_score = 100/self.total_brick

        # Initialize our mouse listeners
        self.start = False
        self.ball_action = True
        onmouseclicked(self.action)
        onmousemoved(self.paddle_zone)

        # Draw bricks
        self.color = ''
        for i in range(self.brick_rows):
            for j in range(self.brick_cols):
                if 0 <= j < 2:
                    self.color = 'red'
                elif 2 <= j < 4:
                    self.color = 'orange'
                elif 4 <= j < 6:
                    self.color = 'yellow'
                elif 6 <= j < 8:
                    self.color = 'green'
                else:
                    self.color = 'blue'
                brick = GRect(self.brick_width, self.brick_height)
                brick.filled = True
                brick.fill_color = self.color
                self.window.add(brick, x=i * (brick_width + brick_spacing), y=brick_offset + j * (brick_height + brick_spacing))

    # Default initial velocity for the ball
    def action(self, event):
        """
        :param self.start: while True, allows starting the game without any disturb during the period.
        :param self.ball_action: Detecting ball is moving or not, the ball is not moving so, clicking once to start.
        """
        if self.ball_action:
            self.start = True
            self.set_ball_velocity()
            self.ball_action = False

    def set_ball_velocity(self):
        """
        :param self.__dx: horizontal direction with random giving speed which cannot be changed by user.
        :param self.__dy: vertical direction with fixed initial speed which cannot be changed by user.
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def get_velocity_dx(self):
        return self.__dx

    def get_velocity_dy(self):
        return self.__dy

    def paddle_zone(self, event):
        """
        :param paddle.x: Entire paddle shall be displayed in window, so make window width-paddle width
        :param paddle.y: Paddle shall be limited in specific area, so make it stay in window height-paddle height and offset.
        """
        self.paddle.x = event.x-self.paddle_width/2
        self.paddle.y = self.window_height-self.paddle_offset
        if self.paddle.x < 0:
            self.paddle.x = 0
        elif self.paddle.x+self.paddle_width > self.window_width:
            self.paddle.x = self.window_width-self.paddle_width
        else:
            self.paddle.x = self.paddle.x

    def corner_checker(self):
        for i in range(0, self.ball.width*2, self.ball.width):
            for j in range(0, self.ball.height*2, self.ball.height):
                self.obj = self.window.get_object_at(self.ball.x+i, self.ball.y+j)
                if self.obj is not None:
                    if self.obj is self.paddle:
                        self.__dy = -self.__dy
                        x = self.ball.x
                        self.window.remove(self.ball)
                        self.window.add(self.ball, x=x, y=self.paddle.y-self.ball.height)
                        return True
                    elif self.obj is not self.label:
                        self.window.remove(self.obj)
                        self.total_score += self.per_ball_get_score
                        self.__dy = -self.__dy
                        return True
                self.label.text = 'Score: ' + str(int(self.total_score))
        return False
