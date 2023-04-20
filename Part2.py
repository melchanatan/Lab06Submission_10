import pygame as pg
from Rectangle import Rectangle

fps = 60
time_constant = 1000 // fps

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

x_pos, y_pos = 0, 0
rec = Rectangle(x_pos, y_pos, 100, 100)

while run:
    screen.fill((255, 255, 255))

    rec.x = x_pos
    rec.y = y_pos
    rec.draw(screen)
    pg.display.update()
    pg.time.delay(time_constant)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

        if event.type == pg.KEYDOWN and event.key == pg.K_d:  # ปุ่มถูกกดลงและเป็นปุ่ม D
            x_pos += 1
        if event.type == pg.KEYDOWN and event.key == pg.K_a:  # ปุ่มถูกปล่อยและเป็นปุ่ม A
            x_pos -= 1
        if event.type == pg.KEYDOWN and event.key == pg.K_w:  # ปุ่มถูกกดลงและเป็นปุ่ม D
            y_pos -= 1
        if event.type == pg.KEYDOWN and event.key == pg.K_s:  # ปุ่มถูกปล่อยและเป็นปุ่ม A
            y_pos += 1