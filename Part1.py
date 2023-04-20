import sys
import pygame as pg
from Button import Button

fps = 60
time_constant = 1000 // fps
pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

color_red = (255, 0, 0)
color_purple = (255, 0, 255)
color_gray = (121, 125, 127)
btn = Button(color_red, 20, 20, 100, 100)  # สร้าง Object จากคลาส Button ขึ้นมา
timer = 0

while (run):
    screen.fill((255, 255, 255))
    if btn.is_mouse_on():
        btn.set_color(color_purple)
        if pg.mouse.get_pressed()[0]:
            timer += 1
        else:
            timer = 0

        if timer > 1 * time_constant:
            btn.set_color(color_gray)
    else:
        btn.set_color(color_red)
    btn.draw(screen)

    pg.display.update()
    pg.time.delay(time_constant)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
