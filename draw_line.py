"""
File: draw_line
Name:Kathy Yang
-------------------------
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
window = GWindow()
SIZE = 10
times = 0
start = None


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(start)


def start(mouse):
    global times, start
    if times == 0:
        start = GOval(SIZE, SIZE)
        start.filled = False
        window.add(start, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        times += 1
    else:
        line = GLine(start.x, start.y, mouse.x, mouse.y)
        window.add(line)
        window.remove(start)
        times = times - 1


if __name__ == "__main__":
    main()
