"""
File: Paper woman
Name:Kathy Yang
----------------------
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GArc, GLine
from campy.graphics.gwindow import GWindow

def main():
    """
    Title: Traditional art - Paper woman

    The Ching Ming Festival is a big day to remember our passed families.
    People used to burn paper man or woman to accompany deceased relatives.
    To be a good granddaughter, I designed a drawing for my departed relatives particularly in April.
    PS. I wouldn't say my referring model coming from The Mona Lisa XD
    """
    window = GWindow(width=400, height=600, title='Paper woman')
    window.add(window)
    outside_l = GOval(310, 700, x=50, y=100)
    outside_l.filled = True
    outside_l.fill_color = 'dimgrey'
    window.add(outside_l)
    outside_s = GOval(300, 700, x=50, y=100)#圓心
    outside_s.filled = True
    outside_s.fill_color = 'black'
    window.add(outside_s)
    yarn = GOval(260, 750, x=55, y=120)
    yarn.filled = True
    yarn.fill_color = 'darkgrey'
    window.add(yarn)
    face = GPolygon()
    face.add_vertex((200, 150))
    face.add_vertex((150, 160))
    face.add_vertex((125, 175))
    face.add_vertex((130, 275))
    face.add_vertex((140, 300))
    face.add_vertex((125, 425)) #Y+50 from 375 to 425
    face.add_vertex((200, 450)) #Y+50
    face.add_vertex((250, 400)) #Y+50
    face.add_vertex((280, 250))
    face.add_vertex((250, 175))
    face.add_vertex((225, 160))
    face.filled = True
    face.fill_color = 'wheat'
    window.add(face)
    body = GPolygon()
    body.add_vertex((200, 450))
    body.add_vertex((125, 425))
    body.add_vertex((132, 360))
    body.add_vertex((90, 363))
    body.add_vertex((80, 365))
    body.add_vertex((78, 370))
    body.add_vertex((75, 375))
    body.add_vertex((70, 380))
    body.add_vertex((60, 390))
    body.add_vertex((60, 400))
    body.add_vertex((56, 500))#X50是最左
    body.add_vertex((56, 550))
    body.add_vertex((64, 600))
    body.add_vertex((315, 600)) #X330最右 Y600是底
    body.add_vertex((318, 580))
    body.add_vertex((320, 570))
    body.add_vertex((322, 560))
    body.add_vertex((324, 550))
    body.add_vertex((326, 540))
    body.add_vertex((328, 530))
    body.add_vertex((328, 510))
    body.add_vertex((326, 500))
    body.add_vertex((325, 475))
    body.add_vertex((318, 440))
    body.add_vertex((310, 415))
    body.add_vertex((300, 400))
    body.add_vertex((280, 380))
    body.add_vertex((255, 380))
    body.filled = True
    body.fill_color = 'darkseagreen'
    window.add(body)
    l_eyebrow = GArc(30, 50, 30, 125, x=135, y=195)
    l_eyebrow.filled = False
    window.add(l_eyebrow)
    l_eye = GOval(20, 20, x=140, y=205)
    l_eye.filled = True
    l_eye.fill_color = 'black'
    window.add(l_eye)
    r_eyebrow = GArc(30, 50, 30, 130, x=195, y=195)
    r_eyebrow.filled = False
    window.add(r_eyebrow)
    r_eye = GOval(20, 20, x=200, y=205)
    r_eye.filled = True
    r_eye.fill_color = 'black'
    window.add(r_eye)
    nose = GLine(175, 230, 170, 250)
    window.add(nose)
    mouth = GArc(60, 50, 200, 120, x=155, y=260)
    mouth.filled = False
    window.add(mouth)
    jaw = GArc(140, 140, 180, 130, x=140, y=263)
    jaw.filled = False
    window.add(jaw)
    l_arm = GLine(95, 460, 53, 540)
    window.add(l_arm)
    r_arm = GLine(300, 500, 270, 570)
    window.add(r_arm)
    r_arm_1 = GLine(270, 570, 240, 600)
    window.add(r_arm_1)
    r_arm_2 = GLine(250, 500, 230, 560)
    window.add(r_arm_2)
    r_arm_3 = GLine(230, 560, 190, 600)
    window.add(r_arm_3)

    l_cheek = GOval(13, 13, x=135, y=245)
    l_cheek.filled = True
    l_cheek.fill_color = 'Tomato'
    window.add(l_cheek)

    r_cheek = GOval(16, 16, x=215, y=240)
    r_cheek.filled = True
    r_cheek.fill_color = 'Tomato'
    window.add(r_cheek)


if __name__ == '__main__':
    main()
