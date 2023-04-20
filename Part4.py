import sys
import pygame as pg
from InputBox import InputBox
from Rectangle import Rectangle
from Button import Button

BACKGROUND_COLOR = (109, 93, 110)
ACCENT_COLOR = (5, 191, 219)

pg.init()
win_x, win_y = 800*1.67, 800
screen = pg.display.set_mode((win_x, win_y))

font = pg.font.SysFont('Noto Sans', 26)
font_heading = pg.font.SysFont('Montserrat', 40, True)
y_spacing = 120
y_padding = 130

x_spacing = 100
x_padding = 500

rect_image = Rectangle(0, 0, 550, win_y, ACCENT_COLOR)

text_heading = font_heading.render('Tell us more about yourself.', True, 'white', BACKGROUND_COLOR)
text_firstname = font.render('First Name', True, 'white', BACKGROUND_COLOR)
# text_firstname.set_alpha(127)
text_surname = font.render('Last Name', True, 'white', BACKGROUND_COLOR)
text_age = font.render('Age', True, 'white', BACKGROUND_COLOR)

submitted_text = font.render('', True, 'white', BACKGROUND_COLOR)

texts = [
    {'text': text_heading, 'pos': (x_padding + x_spacing*1, y_padding)},
    {'text': text_firstname, 'pos': (x_padding + x_spacing*1, y_padding + y_spacing*1-25)},
    {'text': text_surname, 'pos': (x_padding + x_spacing*1, y_padding + y_spacing*2-25)},
    {'text': text_age, 'pos': (x_padding + x_spacing*1, y_padding + y_spacing*3-25)},
    {'text': submitted_text, 'pos': (x_padding + x_spacing * 1, y_padding + y_spacing * 5 - 25)},

]

input_box_firstname = InputBox(x_padding + x_spacing, y_padding + y_spacing*1, 140, 50)
input_box_surname   = InputBox(x_padding + x_spacing, y_padding + y_spacing*2, 140, 50)
input_box_age       = InputBox(x_padding + x_spacing, y_padding + y_spacing*3, 140, 50)
input_boxes = [input_box_firstname, input_box_surname, input_box_age]


# button_submit = Button(color=(0,0,0), x=x_pgadding + x_spacing, y=y_padding + y_spacing*4, w=140, h=50, font=font, text="Submit")
text_submit = font.render("Submit", True, BACKGROUND_COLOR, ACCENT_COLOR)
text_submit_alt = font.render("Submit", True, ACCENT_COLOR, BACKGROUND_COLOR)
button_submit = Button(x=x_padding + x_spacing, y=y_padding + y_spacing*4-20, w=140, h=50, color=ACCENT_COLOR, text=text_submit)
buttons = [button_submit]


run = True
submittable = False

active_input_box = 0
def submit():
    new_text = f"Hello, {input_box_firstname.text} {input_box_surname.text}, {input_box_age.text}"
    text_output = font.render(new_text, True, 'white', BACKGROUND_COLOR)
    for box in input_boxes:
        box.set_text("")

    return text_output


while run:
    screen.fill(BACKGROUND_COLOR)

    rect_image.draw(screen)
    count = 0
    for box in input_boxes:
        box.update()
        box.draw(screen)

        if box.text.strip():
            count += 1
        if count == len(input_boxes):
            submittable = True
        else:
            submittable = False

    for text in texts:
        text_rect = text['text'].get_rect()
        text_rect.midleft = text['pos']
        screen.blit(text['text'], text_rect)

    for button in buttons:
        button.draw(screen)
        if submittable and button.is_mouse_on():
            button.set_color(BACKGROUND_COLOR)
            button.set_text(text_submit_alt)
            # button.set_text_color()
            if pg.mouse.get_pressed()[0]:
                texts[len(texts)-1]["text"] = submit()
        else:
            button.set_color(ACCENT_COLOR)
            button.set_text(text_submit)

        if active_input_box >= len(input_boxes):
            active_input_box = 0

            if submittable:
                texts[len(texts)-1]["text"] = submit()
        else:
            for (i, box) in enumerate(input_boxes):
                if i is not active_input_box:
                    box.active = False
                else:
                    input_boxes[active_input_box].active = True
                    input_boxes[active_input_box].update()

    for event in pg.event.get():
        for (i, box) in enumerate(input_boxes):
            if i == 2:
                if event.type == pg.KEYDOWN and not event.unicode.isnumeric() and event.key != pg.K_RETURN and event.key != pg.K_BACKSPACE:
                    continue
            command = box.handle_event(event)
            if command == 'on':
                active_input_box = input_boxes.index(box)
            elif command == 'submit':
                active_input_box = input_boxes.index(box) + 1

        if event.type == pg.QUIT:
            pg.quit()
            run = False

    pg.time.delay(1)
    pg.display.update()

